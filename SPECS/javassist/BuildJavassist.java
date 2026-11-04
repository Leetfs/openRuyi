// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import aQute.bnd.osgi.Analyzer;
import aQute.bnd.osgi.Jar;
import java.nio.file.Path;
import java.util.jar.Manifest;

class BuildJavassist {
    public static void main(String[] args) throws Exception {
        try (var bnd = new Analyzer()) {
            bnd.setJar(new Jar("javassist", Path.of(args[0]).toFile()));
            bnd.setProperty("Bundle-SymbolicName", "javassist");
            bnd.setProperty("Bundle-Name", "Javassist");
            bnd.setProperty("Bundle-Version", "3.27.0.GA");
            bnd.setProperty("Import-Package", "!com.sun.jdi.*");
            bnd.setProperty("Export-Package", "!com.sun.jdi.*,javassist.*;version=\"3.27.0.GA\"");
            bnd.setProperty("Main-Class", "javassist.CtClass");
            bnd.setProperty("Specification-Title", "Javassist");
            bnd.setProperty("Specification-Version", "3.27.0-GA");
            bnd.setProperty("Specification-Vendor", "Shigeru Chiba, www.javassist.org");
            Manifest manifest = bnd.calcManifest();
            if (!bnd.isOk()) throw new IllegalStateException(bnd.getErrors().toString());
            bnd.getJar().setManifest(manifest);
            bnd.getJar().write(Path.of(args[1]).toFile());
        }
    }
}
