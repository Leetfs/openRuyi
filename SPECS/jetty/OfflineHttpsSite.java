// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import com.sun.net.httpserver.HttpsConfigurator;
import com.sun.net.httpserver.HttpsServer;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.nio.file.Path;
import java.security.KeyStore;
import java.util.Set;
import javax.net.ssl.KeyManagerFactory;
import javax.net.ssl.SSLContext;

final class OfflineHttpsSite implements AutoCloseable {
    private final HttpsServer server;

    OfflineHttpsSite(Path keystore) throws Exception {
        char[] password = "jetty-test".toCharArray();
        var keys = KeyStore.getInstance(keystore.toFile(), password);
        var manager = KeyManagerFactory.getInstance(KeyManagerFactory.getDefaultAlgorithm());
        manager.init(keys, password);
        var tls = SSLContext.getInstance("TLS");
        tls.init(manager.getKeyManagers(), null, null);
        server = HttpsServer.create(new InetSocketAddress(InetAddress.getLoopbackAddress(), 0), 0);
        server.setHttpsConfigurator(new HttpsConfigurator(tls));
        server.createContext("/", exchange -> {
            try (exchange) {
                String path = exchange.getRequestURI().getPath();
                if (!Set.of("/", "/blog/", "/favicon.ico").contains(path)) {
                    exchange.sendResponseHeaders(404, -1);
                    return;
                }
                byte[] content = ("webtide.com " + path).getBytes(StandardCharsets.UTF_8);
                exchange.getResponseHeaders().set("Last-Modified", "Mon, 01 Jan 2024 00:00:00 GMT");
                exchange.getResponseHeaders().set("Content-Length", Integer.toString(content.length));
                if (exchange.getRequestMethod().equals("HEAD")) {
                    exchange.sendResponseHeaders(200, -1);
                } else {
                    exchange.sendResponseHeaders(200, content.length);
                    exchange.getResponseBody().write(content);
                }
            }
        });
        server.start();
        System.setProperty("jetty.test.site", "https://localhost:" + server.getAddress().getPort() + "/");
    }

    public void close() {
        server.stop(0);
    }
}
