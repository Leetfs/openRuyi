import java.io.ByteArrayInputStream;
import java.net.URL;
import java.net.URLClassLoader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Map;
import java.util.ServiceLoader;
import org.eclipse.core.filesystem.EFS;
import org.eclipse.core.resources.IResource;
import org.eclipse.core.resources.ResourcesPlugin;
import org.eclipse.core.runtime.NullProgressMonitor;
import org.osgi.framework.Bundle;
import org.osgi.framework.BundleActivator;
import org.osgi.framework.BundleContext;
import org.osgi.framework.Constants;
import org.osgi.framework.FrameworkEvent;
import org.osgi.framework.launch.FrameworkFactory;

public class ResourcesProbe implements BundleActivator {
    public void start(BundleContext context) throws Exception {
        var monitor = new NullProgressMonitor();
        var project = ResourcesPlugin.getWorkspace().getRoot().getProject("source-check");
        project.create(monitor);
        project.open(monitor);
        try {
            var file = project.getFile("example.txt");
            byte[] sample = "platform\n".getBytes(StandardCharsets.UTF_8);
            file.create(new ByteArrayInputStream(sample), IResource.NONE, monitor);
            try (var input = file.getContents()) {
                if (!java.util.Arrays.equals(input.readAllBytes(), sample)) throw new AssertionError("Workspace contents");
            }
            var location = Path.of(file.getLocationURI());
            if (!java.util.Arrays.equals(Files.readAllBytes(location), sample)) throw new AssertionError("File contents");
            var link = location.resolveSibling("example-link");
            Files.createSymbolicLink(link, location.getFileName());
            var info = EFS.getLocalFileSystem().getStore(link.toUri()).fetchInfo();
            if (!info.getAttribute(EFS.ATTRIBUTE_SYMLINK)) throw new AssertionError("Symbolic link attributes");
            if (!Files.readString(Path.of("/proc/self/maps")).contains("libunixfile_1_0_0.so")) {
                throw new AssertionError("The Unix filesystem native library was not loaded");
            }
        } finally {
            project.delete(true, true, monitor);
        }
    }

    public void stop(BundleContext context) {}
}

class ResourcesFramework {
    public static void main(String[] args) throws Exception {
        Path base = Path.of(args[0]).toAbsolutePath();
        Files.createDirectories(base.resolve("workspace"));
        var framework = ServiceLoader.load(FrameworkFactory.class).findFirst().orElseThrow()
                .newFramework(Map.of(Constants.FRAMEWORK_STORAGE, base.resolve("framework").toString(),
                        "osgi.instance.area", base.resolve("workspace").toUri().toString()));
        framework.start();
        ClassLoader previous = Thread.currentThread().getContextClassLoader();
        try {
            var context = framework.getBundleContext();
            var bundles = new ArrayList<Bundle>();
            for (int i = 2; i < args.length; i++) {
                bundles.add(context.installBundle(Path.of(args[i]).toUri().toString()));
            }
            for (Bundle bundle : bundles) bundle.start();
            if (!"-".equals(args[1])) {
                URL tests = Path.of(args[1]).toUri().toURL();
                try (var loader = new URLClassLoader(new URL[]{tests}, previous) {
                    @Override
                    protected Class<?> findClass(String name) throws ClassNotFoundException {
                        if (name.startsWith("org.eclipse.") && !name.contains(".tests.")) {
                            for (Bundle bundle : bundles) {
                                try { return bundle.loadClass(name); }
                                catch (ClassNotFoundException ignored) { continue; }
                            }
                        }
                        return super.findClass(name);
                    }
                }) {
                    Thread.currentThread().setContextClassLoader(loader);
                    RunJupiter.main(new String[]{"org.eclipse.core.internal.expressions.tests.CountExpressionTest", "org.eclipse.core.internal.expressions.tests.ExpressionInfoTests"});
                }
            }
        } finally {
            Thread.currentThread().setContextClassLoader(previous);
            framework.stop();
            if (framework.waitForStop(30000).getType() != FrameworkEvent.STOPPED) {
                throw new AssertionError("Framework did not stop");
            }
        }
    }
}
