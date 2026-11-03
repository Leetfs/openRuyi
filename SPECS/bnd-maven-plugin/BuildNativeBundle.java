// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import aQute.bnd.osgi.Builder;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
class BuildNativeBundle {
    public static void main(String[] args) throws Exception {
        try (Builder builder = new Builder()) {
            File instructions = new File(args[0]);
            builder.setBase(instructions.getParentFile());
            builder.setProperty("workspace", args[1]);
            builder.setProperty("project", instructions.getParentFile().getAbsolutePath());
            java.util.Properties versions = new java.util.Properties();
            try (var input = java.nio.file.Files.newBufferedReader(Path.of(args[1], "cnf/ext/junit.bnd"))) {
                versions.load(input);
            }
            for (String key : versions.stringPropertyNames()) builder.setProperty(key, versions.getProperty(key));
            builder.setProperty("p", args[2]);
            builder.setProperty("base.version", "7.2.3");
            if (instructions.getName().equals("launcher.bnd")) {
                builder.setProperties(new File(instructions.getParentFile(), "bnd.bnd"));
            }
            builder.setProperties(instructions);
            builder.setProperty("Bundle-SymbolicName", args[2]);
            builder.setProperty("Bundle-Version", "7.2.3");
            builder.setProperty("-noextraheaders", "true");
            File[] classpath = Arrays.stream(Files.readString(Path.of(args[3])).trim().split(File.pathSeparator))
                .filter(p -> !p.isEmpty()).map(File::new).filter(File::exists).toArray(File[]::new);
            builder.setClasspath(classpath);
            var jar = builder.build();
            if (!builder.isOk()) throw new IllegalStateException(String.join("\n", builder.getErrors()));
            jar.write(new File(args[4]));
            System.out.println(args[2] + " resources=" + jar.getResources().size());
            for (String warning : builder.getWarnings()) System.out.println("WARNING " + warning);
        }
    }
}
