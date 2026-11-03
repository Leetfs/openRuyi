// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import aQute.bnd.build.Workspace;
import aQute.bnd.version.Version;
import aQute.bnd.service.RepositoryPlugin;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Map;
class CheckEmbeddedPlugins {
    public static void main(String[] args) throws Exception {
        Path directory = Path.of(args[0]);
        Files.createDirectories(directory.resolve("cnf"));
        Files.writeString(directory.resolve("cnf/build.bnd"), "");
        try (Workspace workspace = new Workspace(directory.toFile())) {
            for (String name : new String[]{"biz.aQute.launcher", "biz.aQute.remote.launcher",
                    "biz.aQute.tester", "biz.aQute.tester.junit-platform", "biz.aQute.junit"}) {
                File found = null;
                for (RepositoryPlugin repository : workspace.getRepositories()) {
                    if (repository.versions(name).contains(new Version("7.2.3"))) {
                        found = repository.get(name, new Version("7.2.3"), Map.of());
                        break;
                    }
                }
                if (found == null || !found.isFile()) throw new AssertionError("Missing embedded bundle " + name);
                System.out.println(name + " -> " + found.getName());
            }

            Path projectPath = directory.resolve("sample");
            Files.createDirectories(projectPath);
            Files.writeString(projectPath.resolve("bnd.bnd"), "Bundle-SymbolicName: org.openruyi.sample\n");
            var project = workspace.getProject("sample");
            try (var launcher = project.getProjectLauncher()) {
                if (!launcher.getClass().getName().equals("aQute.launcher.plugin.ProjectLauncherImpl"))
                    throw new AssertionError(launcher.getClass());
            }
            var tester = project.getProjectTester();
            if (!tester.getClass().getName().equals("aQute.tester.plugin.ProjectTesterImpl"))
                throw new AssertionError(tester.getClass());
            project.setProperty("-tester", "biz.aQute.tester.junit-platform");
            var platform = project.getProjectTester();
            if (!platform.getClass().getName().equals("aQute.tester.junit.platform.plugin.ProjectTesterImpl"))
                throw new AssertionError(platform.getClass());
            System.out.println("Native default launcher, JUnit 4 tester and JUnit Platform tester constructed");
            if (!workspace.isOk()) throw new AssertionError(workspace.getErrors());
        }
    }
}
