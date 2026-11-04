// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import com.sun.net.httpserver.HttpServer;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.atomic.AtomicReference;
import org.apache.maven.search.api.MAVEN;
import org.apache.maven.search.api.SearchRequest;
import org.apache.maven.search.api.request.Paging;
import org.apache.maven.search.api.request.Query;
import org.apache.maven.search.api.transport.Java11HttpClientTransport;
import org.apache.maven.search.backend.smo.SmoSearchBackendFactory;

class SearchCoordinates {
    public static void main(String[] args) throws Exception {
        String sha1 = "0123456789abcdef0123456789abcdef01234567";
        var query = new AtomicReference<String>();
        var agent = new AtomicReference<String>();
        var response = new AtomicReference<String>();
        var server = HttpServer.create(new InetSocketAddress("127.0.0.1", 0), 0);
        server.createContext("/solrsearch/select", exchange -> {
            try (exchange) {
                query.set(exchange.getRequestURI().getQuery());
                agent.set(exchange.getRequestHeaders().getFirst("User-Agent"));
                byte[] body = response.get().getBytes(StandardCharsets.UTF_8);
                exchange.getResponseHeaders().set("Content-Type", "application/json");
                exchange.sendResponseHeaders(200, body.length);
                exchange.getResponseBody().write(body);
            }
        });
        server.start();
        try {
            String endpoint = "http://127.0.0.1:" + server.getAddress().getPort() + "/solrsearch/select";
            var backend = SmoSearchBackendFactory.create("test-smo", "test-central", endpoint, new Java11HttpClientTransport());
            var request = new SearchRequest(new Paging(2), Query.query("1:" + sha1));
            response.set("{\"response\":{\"numFound\":1,\"docs\":[{\"id\":\"fixture\",\"g\":\"org.openruyi\",\"a\":\"fixture\",\"v\":\"1.2.3\",\"p\":\"jar\"}]}}");
            var hits = backend.search(request);
            if (hits.getTotalHits() != 1 || hits.getPage().size() != 1) throw new AssertionError("Missing coordinate");
            var item = hits.getPage().get(0);
            if (!"org.openruyi".equals(item.getValue(MAVEN.GROUP_ID)) || !"fixture".equals(item.getValue(MAVEN.ARTIFACT_ID))
                    || !"1.2.3".equals(item.getValue(MAVEN.VERSION)) || !"jar".equals(item.getValue(MAVEN.PACKAGING))) {
                throw new AssertionError(item);
            }
            if (!query.get().contains("1:" + sha1) || !query.get().contains("rows=2")
                    || !agent.get().contains("Apache-Maven-Search-SMO/7.1.6")) throw new AssertionError(query + " " + agent);
            response.set("{\"response\":{\"numFound\":0,\"docs\":[]}}");
            var empty = backend.search(request);
            if (empty.getTotalHits() != 0 || !empty.getPage().isEmpty()) throw new AssertionError("Unexpected coordinate");
        } finally {
            server.stop(0);
        }
    }
}
