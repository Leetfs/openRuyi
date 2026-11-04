// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import aQute.bnd.osgi.Analyzer;
import aQute.bnd.osgi.Jar;
import java.io.File;
import java.nio.file.Path;

class BuildPlatformBundle {
    public static void main(String[] args) throws Exception {
        try (var bnd = new Analyzer()) {
            bnd.setJar(new Jar(args[0], Path.of(args[1]).toFile()));
            for (String dependency : args[3].split(File.pathSeparator)) bnd.addClasspath(new File(dependency));
            bnd.setProperty("Bundle-SymbolicName", args[0]);
            bnd.setProperty("Bundle-Name", args[4]);
            bnd.setProperty("Bundle-Version", args[5]);
            bnd.setProperty("Import-Package", "org.apiguardian.api;resolution:=optional;version=\"[1.1,2)\",org.junit.platform.commons.logging;status=INTERNAL,org.opentest4j;version=\"[1.3,2)\",kotlin.*;resolution:=optional,*");
            bnd.setProperty("-noclassforname", "true");
            bnd.setProperty("-noextraheaders", "true");
            bnd.setProperty("-removeheaders", "Private-Package");
            bnd.setProperty("-export-apiguardian", "*;version=" + args[5]);
            if (args[0].equals("junit-platform-commons")) bnd.setProperty("Multi-Release", "true");
            var manifest = bnd.calcManifest();
            if (!bnd.isOk()) throw new IllegalStateException(bnd.getErrors().toString());
            bnd.getJar().setManifest(manifest);
            bnd.getJar().write(Path.of(args[2]).toFile());
        }
    }
}
