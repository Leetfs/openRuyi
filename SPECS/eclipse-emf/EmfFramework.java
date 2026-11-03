import java.nio.file.*;
import java.util.*;
import org.osgi.framework.*;
import org.osgi.framework.launch.FrameworkFactory;
class EmfFramework {
    public static void main(String[] args) throws Exception {
        Path base = Path.of("build/runtime").toAbsolutePath();
        Files.createDirectories(base.resolve("workspace"));
        var framework = ServiceLoader.load(FrameworkFactory.class).findFirst().orElseThrow()
            .newFramework(Map.of(Constants.FRAMEWORK_STORAGE, base.resolve("framework").toString(),
                                 "osgi.instance.area", base.resolve("workspace").toUri().toString()));
        framework.start();
        try {
            var context = framework.getBundleContext();
            var bundles = new ArrayList<Bundle>();
            for (String arg : args) bundles.add(context.installBundle(Path.of(arg).toUri().toString()));
            for (var bundle : bundles) bundle.start();
            var probe = bundles.get(bundles.size()-1);
            var tests = new ArrayList<Class<?>>();
            for (String name : Files.readAllLines(Path.of("build/test-classes"))) tests.add(probe.loadClass(name));
            var capabilities = probe.adapt(org.osgi.framework.wiring.BundleRevision.class)
                .getDeclaredCapabilities("org.eclipse.emf.ecore.generated_package");
            boolean declared = false;
            for (var capability : capabilities) {
                var attributes = capability.getAttributes();
                if ("http:///org.eclipse.emf.test.models/provide-capability".equals(attributes.get("uri")))
                    declared = probe.getEntry((String)attributes.get("genModel")) != null;
            }
            if (!declared) throw new AssertionError("Original GenModel capability or resource missing");
            boolean hasPde = Arrays.stream(context.getBundles()).anyMatch(b -> "org.eclipse.pde.core".equals(b.getSymbolicName()));
            Thread.currentThread().setContextClassLoader(probe.adapt(org.osgi.framework.wiring.BundleWiring.class).getClassLoader());
            probe.loadClass("EmfJUnit").getMethod("run", List.class, boolean.class).invoke(null, tests, hasPde);
        } finally {
            framework.stop();
            if (framework.waitForStop(30000).getType() != FrameworkEvent.STOPPED) throw new AssertionError("Equinox stop");
        }
    }
}
