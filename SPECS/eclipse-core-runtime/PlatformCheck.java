import java.net.URL;
import java.net.URLClassLoader;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.ServiceLoader;
import org.osgi.framework.Bundle;
import org.osgi.framework.Constants;
import org.osgi.framework.FrameworkEvent;
import org.osgi.framework.launch.FrameworkFactory;
import org.osgi.util.tracker.ServiceTracker;

class PlatformCheck {
    public static void main(String[] args) throws Exception {
        Path state = Path.of(args[0]).toAbsolutePath();
        var framework = ServiceLoader.load(FrameworkFactory.class).findFirst().orElseThrow()
                .newFramework(Map.of(Constants.FRAMEWORK_STORAGE, state.resolve("framework").toString(),
                        "osgi.instance.area", state.resolve("workspace").toUri().toString()));
        framework.start();
        ClassLoader previous = Thread.currentThread().getContextClassLoader();
        try {
            var context = framework.getBundleContext();
            List<Bundle> installed = new ArrayList<>();
            for (int i = 2; i < args.length; i++) {
                installed.add(context.installBundle(Path.of(args[i]).toUri().toString()));
            }
            for (Bundle bundle : installed) bundle.start();
            Bundle network = installed.stream().filter(b -> "org.eclipse.core.net".equals(b.getSymbolicName()))
                    .findFirst().orElseThrow();
            var testDirectory = Path.of(args[1]).toUri().toURL();
            try (var tests = new URLClassLoader(new URL[] {testDirectory},
                    network.adapt(org.osgi.framework.wiring.BundleWiring.class).getClassLoader())) {
                tests.loadClass("ProxyCheck").getMethod("verify", org.osgi.framework.BundleContext.class)
                        .invoke(null, network.getBundleContext());
            }
            Bundle runtime = installed.stream().filter(b -> "org.eclipse.core.runtime".equals(b.getSymbolicName()))
                    .findFirst().orElseThrow();
            String managerName = "org.eclipse.core.runtime.content.IContentTypeManager";
            var manager = new ServiceTracker<Object, Object>(runtime.getBundleContext(), managerName, null);
            manager.open();
            try {
                if (manager.waitForService(15000) == null) throw new AssertionError("Missing content type service");
                Class<?> platform = runtime.loadClass("org.eclipse.core.runtime.Platform");
                Object service = platform.getMethod("getContentTypeManager").invoke(null);
                Object type = runtime.loadClass(managerName).getMethod("findContentTypeFor", String.class)
                        .invoke(service, "project.xml");
                if (type == null || !"org.eclipse.core.runtime.xml".equals(runtime
                        .loadClass("org.eclipse.core.runtime.content.IContentType").getMethod("getId").invoke(type))) {
                    throw new AssertionError("Platform did not recognize its XML content type");
                }
            } finally { manager.close(); }

            if (!"-".equals(args[1])) {
                URL tests = Path.of(args[1]).toUri().toURL();
                try (var loader = new URLClassLoader(new URL[]{tests}, previous) {
                    @Override protected Class<?> findClass(String name) throws ClassNotFoundException {
                        if (name.startsWith("org.eclipse.")) {
                            for (Bundle bundle : installed) {
                                try { return bundle.loadClass(name); }
                                catch (ClassNotFoundException unavailable) { continue; }
                            }
                        }
                        return super.findClass(name);
                    }
                }) {
                    Thread.currentThread().setContextClassLoader(loader);
                    RunJupiter.main(new String[]{
                            "org.eclipse.core.internal.contenttype.tests.XMLRootHandlerTest",
                            "org.eclipse.core.internal.contenttype.tests.UserContentTypeTest",
                            "org.eclipse.core.tests.internal.runtime.CollectionTrustManagerTest",
                            "org.eclipse.core.tests.internal.runtime.KeyStoreUtilTest"});
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
