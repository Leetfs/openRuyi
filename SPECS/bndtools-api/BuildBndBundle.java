// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import aQute.bnd.component.DSAnnotations;
import aQute.bnd.osgi.Analyzer;
import aQute.bnd.osgi.Jar;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.jar.Manifest;

class BuildBndBundle {
    public static void main(String[] args) throws Exception {
        String name=args[0];
        try (Analyzer analyzer=new Analyzer()) {
            analyzer.setProperties(Path.of("cnf/includes/bndtools.bnd").toFile());
            analyzer.setJar(new Jar(name,Path.of(args[1]).toFile()));
            for (String file : Files.readAllLines(Path.of(args[3]))) analyzer.addClasspath(new File(file));
            analyzer.setProperty("Bundle-SymbolicName",name);
            analyzer.setProperty("Bundle-Version","7.2.1.202601121903");
            analyzer.setProperty("Bundle-License","(Apache-2.0 OR EPL-2.0)");
            if (name.equals("bndtools.api")) {
                analyzer.setProperty("Export-Package","org.bndtools.*");
                analyzer.setProperty("Import-Package","$" + "{eclipse.importpackage},*");
            } else {
                analyzer.setProperty("Export-Package","org.bndtools.versioncontrol.ignores.manager.api");
                analyzer.setProperty("Private-Package","org.bndtools.versioncontrol.ignores.manager");
                analyzer.setProperty("Bundle-ActivationPolicy","lazy");
                analyzer.setProperty("-dsannotations","*");
                analyzer.addBasicPlugin(new DSAnnotations());
            }
            Manifest manifest=analyzer.calcManifest();
            if (!analyzer.isOk()) throw new IllegalStateException(analyzer.getErrors().toString());
            analyzer.getJar().setManifest(manifest);
            analyzer.getJar().write(Path.of(args[2]).toFile());
        }
    }
}
