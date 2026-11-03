import aQute.bnd.header.Parameters;
import aQute.bnd.osgi.Analyzer;
import java.io.File;
import java.io.Reader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Properties;

class BndManifest {
    public static void main(String[] args) throws Exception {
        Path module = Path.of(args[0]);
        String name = module.getFileName().toString();
        Properties original = new Properties();
        try (Reader reader = Files.newBufferedReader(module.resolve("bnd.bnd"))) {
            original.load(reader);
        }
        Properties imports = new Properties();
        try (Reader reader = Files.newBufferedReader(Path.of(args[5]))) {
            imports.load(reader);
        }
        List<String> classpath = Files.readAllLines(Path.of(args[4]));
        try (Analyzer analyzer = new Analyzer()) {
            analyzer.setJar(new File(args[1]));
            analyzer.setClasspath(classpath.stream().map(File::new).toArray(File[]::new));
            analyzer.setProperty("Bundle-SymbolicName", name);
            analyzer.setProperty("Bundle-Name", name);
            analyzer.setProperty("Bundle-Version", args[3]);
            analyzer.setProperty("Bundle-Vendor", "Bndtools https://bndtools.org/");
            analyzer.setProperty("Bundle-License", "(Apache-2.0 OR EPL-2.0)");
            analyzer.setProperty("Automatic-Module-Name", name);
            analyzer.setProperty("-noimportjava", "true");
            analyzer.setProperty("-reproducible", "true");
            analyzer.setProperty("-noextraheaders", "true");
            for (String key : List.of("Bundle-Description", "Export-Package", "-exportcontents",
                    "Import-Package", "Provide-Capability", "Require-Capability")) {
                String value = original.getProperty(key);
                if (value != null) analyzer.setProperty(key, value);
            }
            var manifest = analyzer.calcManifest();
            var headers = manifest.getMainAttributes();
            String contract = imports.getProperty(name);
            if (contract == null || !new Parameters(contract).keySet()
                    .equals(new Parameters(headers.getValue("Import-Package")).keySet())) {
                throw new IllegalStateException("Compiled imports differ from the release contract for " + name);
            }
            // Preserve the original provider ranges even when compiling against aggregate API jars.
            headers.putValue("Import-Package", contract);
            var exports = new Parameters(headers.getValue("Export-Package"));
            exports.values().forEach(attributes -> attributes.putIfAbsent("version", args[3]));
            headers.putValue("Export-Package", exports.toString());
            analyzer.getJar().setManifest(manifest);
            if (!analyzer.isOk()) throw new IllegalStateException(String.join("\n", analyzer.getErrors()));
            analyzer.getJar().write(new File(args[2]));
        }
    }
}
