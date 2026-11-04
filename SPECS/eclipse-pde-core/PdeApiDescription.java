// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import java.nio.file.Path;
import javax.xml.parsers.DocumentBuilderFactory;
import org.eclipse.pde.api.tools.internal.tasks.ApiFileGenerationTask;
import org.w3c.dom.Element;

class PdeApiDescription {
    public static void main(String[] args) throws Exception {
        Path root = Path.of(args[0]).toAbsolutePath();
        var task = new ApiFileGenerationTask();
        task.setProjectName("org.openruyi.api.fixture");
        task.setProject(root.toString());
        task.setTarget(root.resolve("target").toString());
        task.setBinary(root.resolve("bin").toString());
        task.execute();
        var xml = DocumentBuilderFactory.newInstance().newDocumentBuilder()
                .parse(root.resolve("target/.api_description").toFile());
        Element pkg = (Element) xml.getElementsByTagName("package").item(0);
        Element type = (Element) pkg.getElementsByTagName("type").item(0);
        if (!"org.openruyi.fixture".equals(pkg.getAttribute("name"))
                || !"ApiSample".equals(type.getAttribute("name"))
                || !"2".equals(type.getAttribute("restrictions"))) {
            throw new AssertionError("The generated descriptor lost the @noextend restriction");
        }
        System.out.println("The Ant task wrote the @noextend restriction for org.openruyi.fixture.ApiSample");
    }
}
