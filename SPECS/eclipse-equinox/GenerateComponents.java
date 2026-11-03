import aQute.bnd.component.DSAnnotations;
import aQute.bnd.osgi.Analyzer;
import aQute.bnd.osgi.Resource;
import java.io.File;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

class GenerateComponents {
    public static void main(String[] args) throws Exception {
        Path output = Path.of(args[0]).toAbsolutePath();
        List<File> classpath = new ArrayList<>();
        for (String element : args[1].split(File.pathSeparator)) {
            classpath.add(new File(element));
        }
        try (Analyzer analyzer = new Analyzer()) {
            analyzer.setJar(output.toFile());
            analyzer.setClasspath(classpath.toArray(new File[0]));
            analyzer.setProperty("-dsannotations", "*");
            analyzer.addBasicPlugin(new DSAnnotations());
            analyzer.analyze();
            if (!analyzer.isOk()) {
                throw new IllegalStateException(String.join("\n", analyzer.getErrors()));
            }
            for (Map.Entry<String, Resource> entry : analyzer.getJar().getResources().entrySet()) {
                String name = entry.getKey();
                if (!name.startsWith("OSGI-INF/") || !name.endsWith(".xml")) {
                    continue;
                }
                Path file = output.resolve(name);
                if (!Files.exists(file)) {
                    Files.createDirectories(file.getParent());
                    try (OutputStream stream = Files.newOutputStream(file)) {
                        entry.getValue().write(stream);
                    }
                }
            }
        }
    }
}
