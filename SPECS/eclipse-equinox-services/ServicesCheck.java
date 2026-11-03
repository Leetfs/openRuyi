import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.ServiceLoader;
import org.osgi.framework.Bundle;
import org.osgi.framework.Constants;
import org.osgi.framework.FrameworkEvent;
import org.osgi.framework.launch.Framework;
import org.osgi.framework.launch.FrameworkFactory;

class ServicesCheck {
    public static void main(String[] args) throws Exception {
        Path state = Path.of(args[0]).toAbsolutePath();
        Framework framework = ServiceLoader.load(FrameworkFactory.class).findFirst().orElseThrow()
                .newFramework(Map.of(Constants.FRAMEWORK_STORAGE, state.resolve("framework").toString(),
                        "osgi.instance.area", state.resolve("instance").toUri().toString()));
        framework.start();
        try {
            var context = framework.getBundleContext();
            List<Bundle> order = new ArrayList<>();
            Map<String, Bundle> bundles = new HashMap<>();
            for (int i = 2; i < args.length; i++) {
                Bundle bundle = context.installBundle(Path.of(args[i]).toUri().toString());
                order.add(bundle);
                bundles.put(bundle.getSymbolicName(), bundle);
            }
            for (Bundle bundle : order) {
                bundle.start();
            }

            Bundle registry = bundles.get("org.eclipse.equinox.registry");
            Class<?> registryApi = registry.loadClass("org.eclipse.core.runtime.IExtensionRegistry");
            var registryContext = registry.getBundleContext();
            var installed = registryContext.getService(registryContext.getServiceReference(registryApi.getName()));
            Object point = registryApi.getMethod("getExtensionPoint", String.class)
                    .invoke(installed, "org.eclipse.core.runtime.applications");
            if (point == null) throw new AssertionError("Application extension point is absent");

            Bundle prefs = bundles.get("org.eclipse.equinox.preferences");
            var prefsContext = prefs.getBundleContext();
            Class<?> serviceApi = prefs.loadClass("org.osgi.service.prefs.PreferencesService");
            Object service = prefsContext.getService(prefsContext.getServiceReference(serviceApi.getName()));
            Object node = serviceApi.getMethod("getSystemPreferences").invoke(service);
            Class<?> api = prefs.loadClass("org.osgi.service.prefs.Preferences");
            api.getMethod("put", String.class, String.class).invoke(node, "package-test", "saved");
            api.getMethod("flush").invoke(node);
            if (!"saved".equals(api.getMethod("get", String.class, String.class).invoke(node, "package-test", null))) {
                throw new AssertionError("OSGi preference did not round-trip");
            }

            Class<?> encoding = bundles.get("org.eclipse.equinox.security")
                    .loadClass("org.eclipse.equinox.security.storage.EncodingUtils");
            String key = "node/key";
            Object encoded = encoding.getMethod("encodeSlashes", String.class).invoke(null, key);
            if (key.equals(encoded) || !key.equals(encoding.getMethod("decodeSlashes", String.class).invoke(null, encoded))) {
                throw new AssertionError("Secure storage key did not round-trip");
            }

            if (!args[1].equals("-")) {
                Bundle tests = context.installBundle(Path.of(args[1]).toUri().toString());
                tests.start();
                runTests(tests);
            }
        } finally {
            framework.stop();
            if (framework.waitForStop(30000).getType() != FrameworkEvent.STOPPED) {
                throw new AssertionError("Framework did not stop");
            }
        }
    }
    private static void runTests(Bundle bundle) throws Exception {
        String[] names = {
            "org.eclipse.equinox.preferences.tests.PreferenceMetadataTest",
            "org.eclipse.equinox.preferences.tests.OsgiPreferenceMetadataStoreTest",
            "org.eclipse.equinox.internal.security.tests.storage.Base64Test",
            "org.eclipse.equinox.internal.security.tests.storage.DetectPBECiphersTest"
        };
        Class<?>[] classes = new Class<?>[names.length];
        for (int i = 0; i < names.length; i++) {
            classes[i] = bundle.loadClass(names[i]);
        }
        Class<?> runner = bundle.loadClass("org.junit.runner.JUnitCore");
        Object result = runner.getMethod("runClasses", Class[].class).invoke(null, (Object) classes);
        Class<?> type = result.getClass();
        List<?> failures = (List<?>) type.getMethod("getFailures").invoke(result);
        int count = (Integer) type.getMethod("getRunCount").invoke(result);
        System.out.println("Equinox JUnit: " + count + " tests, " + failures.size() + " failures");
        if (count == 0 || !failures.isEmpty()) throw new AssertionError(failures);
    }
}
