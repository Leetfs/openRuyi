// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import org.eclipse.tycho.test.util.HttpServer;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TemporaryFolder;
import static org.junit.Assert.*;
public class TychoServerCompatibility {
    @Rule public TemporaryFolder folder = new TemporaryFolder();
    @Rule public HttpServer server = new HttpServer();
    @Test public void servesAndRecordsRepositoryRequests() throws Exception {
        Path repo = folder.newFolder().toPath();
        Files.writeString(repo.resolve("content.xml"), "p2 repository metadata");
        String url = server.addServlet("repository", repo.toFile());
        HttpClient client = HttpClient.newHttpClient();
        var ok = client.send(HttpRequest.newBuilder(URI.create(url + "/content.xml")).build(), HttpResponse.BodyHandlers.ofString());
        assertEquals(200, ok.statusCode());
        assertEquals("p2 repository metadata", ok.body());
        var missing = client.send(HttpRequest.newBuilder(URI.create(url + "/absent")).build(), HttpResponse.BodyHandlers.ofString());
        assertEquals(404, missing.statusCode());
        assertEquals(List.of("/repository/content.xml", "/repository/absent"), server.getAccessedUrls("repository"));
        server.clearAccessedUrls("repository");
        assertTrue(server.getAccessedUrls("repository").isEmpty());
        System.out.println("Tycho HTTP fixture returned 200/404 and recorded both request paths");
    }
}
