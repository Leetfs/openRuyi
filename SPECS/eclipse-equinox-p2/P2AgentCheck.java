import java.net.URI;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.ServiceLoader;
import org.osgi.framework.Bundle;
import org.osgi.framework.Constants;
import org.osgi.framework.FrameworkEvent;
import org.osgi.framework.launch.FrameworkFactory;
import org.osgi.util.tracker.ServiceTracker;

class P2AgentCheck {
    public static void main(String[] args) throws Exception {
        Path state = Path.of(args[0]).toAbsolutePath();
        var framework = ServiceLoader.load(FrameworkFactory.class).findFirst().orElseThrow()
                .newFramework(Map.of(Constants.FRAMEWORK_STORAGE, state.resolve("framework").toString(),
                        "osgi.instance.area", state.resolve("workspace").toUri().toString()));
        framework.start();
        try {
            List<Bundle> order = new ArrayList<>();
            Map<String, Bundle> bundles = new HashMap<>();
            for (int i = 1; i < args.length; i++) {
                var bundle = framework.getBundleContext().installBundle(Path.of(args[i]).toUri().toString());
                order.add(bundle); bundles.put(bundle.getSymbolicName(), bundle);
            }
            for (Bundle bundle : order) { bundle.start(); System.out.println("Active: " + bundle.getSymbolicName()); }
            Bundle runtime = bundles.get("org.eclipse.core.runtime");
            Class<?> platform = runtime.loadClass("org.eclipse.core.runtime.Platform");
            Object manager = platform.getMethod("getContentTypeManager").invoke(null);
            Object content = runtime.loadClass("org.eclipse.core.runtime.content.IContentTypeManager")
                    .getMethod("findContentTypeFor", String.class).invoke(manager, "feature.xml");
            String type = (String) runtime.loadClass("org.eclipse.core.runtime.content.IContentType")
                    .getMethod("getId").invoke(content);
            if (!"org.eclipse.core.runtime.xml".equals(type)) throw new AssertionError(type);
            Bundle core = bundles.get("org.eclipse.equinox.p2.core");
            Class<?> provider = core.loadClass("org.eclipse.equinox.p2.core.IProvisioningAgentProvider");
            var tracker = new ServiceTracker<Object, Object>(core.getBundleContext(), provider.getName(), null);
            tracker.open();
            try {
                Object service = tracker.waitForService(15000);
                if (service == null) throw new AssertionError("No p2 agent provider");
                Class<?> api = core.loadClass("org.eclipse.equinox.p2.core.IProvisioningAgent");
                Object agent = provider.getMethod("createAgent", URI.class).invoke(service, state.resolve("agent").toUri());
                Object marker = new Object(); String key = "org.openruyi.test.service";
                try {
                    api.getMethod("registerService", String.class, Object.class).invoke(agent, key, marker);
                    if (marker != api.getMethod("getService", String.class).invoke(agent, key)) throw new AssertionError();
                    api.getMethod("unregisterService", String.class, Object.class).invoke(agent, key, marker);
                    if (api.getMethod("getService", String.class).invoke(agent, key) != null) throw new AssertionError();
                } finally { api.getMethod("stop").invoke(agent); }
            } finally { tracker.close(); }
            System.out.println("Native RPMs identified the XML file type and created, exercised and stopped a p2 provisioning agent");
        } finally {
            framework.stop();
            if (framework.waitForStop(30000).getType() != FrameworkEvent.STOPPED) throw new AssertionError();
        }
    }
}
