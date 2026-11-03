import aQute.bnd.osgi.Analyzer;
import java.io.File;
class WrapBundle {
    public static void main(String[] args) throws Exception {
        try (Analyzer analyzer = new Analyzer()) {
            analyzer.setJar(new File(args[0]));
            analyzer.mergeManifest(analyzer.getJar().getManifest());
            analyzer.setProperty("Bundle-SymbolicName", args[2]);
            analyzer.setProperty("Bundle-Version", args[3]);
            analyzer.setProperty("Export-Package", args[4]);
            analyzer.setProperty("Import-Package", args[5]);
            analyzer.setProperty("Multi-Release", "true");
            analyzer.setProperty("-noextraheaders", "true");
            analyzer.setProperty("-reproducible", "true");
            String[] paths = args[6].split(File.pathSeparator);
            File[] files = new File[paths.length];
            for (int i = 0; i < paths.length; i++) files[i] = new File(paths[i]);
            analyzer.setClasspath(files);
            analyzer.getJar().setManifest(analyzer.calcManifest());
            if (!analyzer.isOk()) throw new IllegalStateException(String.join("\n", analyzer.getErrors()));
            analyzer.getJar().write(new File(args[1]));
        }
    }
}
