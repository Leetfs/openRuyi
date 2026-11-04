import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;
import org.apache.maven.artifact.Artifact;
import org.apache.maven.artifact.DefaultArtifact;
import org.apache.maven.artifact.handler.DefaultArtifactHandler;
import org.apache.maven.model.Build;
import org.apache.maven.model.Model;
import org.apache.maven.plugin.logging.SystemStreamLog;
import org.apache.maven.plugins.shade.DefaultShader;
import org.apache.maven.plugins.shade.ShadeRequest;
import org.apache.maven.plugins.shade.filter.MinijarFilter;
import org.apache.maven.plugins.shade.filter.SimpleFilter;
import org.apache.maven.plugins.shade.relocation.Relocator;
import org.apache.maven.plugins.shade.relocation.SimpleRelocator;
import org.apache.maven.project.MavenProject;

class BootstrapShade {
    private static Artifact artifact(File file, String name) {
        DefaultArtifactHandler handler = new DefaultArtifactHandler("jar");
        handler.setAddedToClasspath(true);
        Artifact artifact = new DefaultArtifact("org.openruyi.bootstrap", name, "1", "compile", "jar", null, handler);
        artifact.setFile(file);
        return artifact;
    }

    public static void main(String[] args) throws Exception {
        File input = new File(args[0]);
        File output = new File(args[1]);
        Model model = new Model();
        model.setGroupId("org.vafer");
        model.setArtifactId("jdependency");
        model.setVersion("2.10");
        Build build = new Build();
        build.setOutputDirectory("target/classes");
        model.setBuild(build);
        MavenProject project = new MavenProject(model);
        project.setArtifact(artifact(input, "jdependency"));
        Set<Artifact> dependencies = new LinkedHashSet<>();
        Set<File> jars = new LinkedHashSet<>();
        jars.add(input);
        for (String arg : Arrays.copyOfRange(args, 2, args.length)) {
            File file = new File(arg);
            jars.add(file);
            dependencies.add(artifact(file, file.getName()));
        }
        project.setArtifacts(dependencies);
        SimpleFilter signatures = new SimpleFilter(jars, Collections.emptySet(),
                new LinkedHashSet<>(Arrays.asList("META-INF/*.SF", "META-INF/*.DSA", "META-INF/*.RSA")));
        ShadeRequest request = new ShadeRequest();
        request.setJars(jars);
        request.setUberJar(output);
        request.setFilters(Arrays.asList(signatures, new MinijarFilter(project, new SystemStreamLog())));
        List<Relocator> relocators = new ArrayList<>();
        relocators.add(new SimpleRelocator("org.apache.commons", "org.vafer.jdeb.shaded.commons", null, null));
        relocators.add(new SimpleRelocator("org.ow2.asm", "org.vafer.jdeb.shaded.ow2.asm", null, null));
        relocators.add(new SimpleRelocator("org.objectweb.asm", "org.vafer.jdeb.shaded.objectweb.asm", null, null));
        request.setRelocators(relocators);
        request.setResourceTransformers(Collections.emptyList());
        new DefaultShader().shade(request);
    }
}
