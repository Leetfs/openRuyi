import java.nio.file.Path;
import java.util.HashMap;
import java.util.Map;
import java.util.ServiceLoader;
import org.osgi.framework.Bundle;
import org.osgi.framework.BundleContext;
import org.osgi.framework.Constants;
import org.osgi.framework.FrameworkEvent;
import org.osgi.framework.launch.Framework;
import org.osgi.framework.launch.FrameworkFactory;

public class FrameworkCheck {
    public static void main(String[] args) throws Exception {
        Map<String, String> config = new HashMap<>();
        config.put(Constants.FRAMEWORK_STORAGE, args[1]);
        FrameworkFactory factory = ServiceLoader.load(FrameworkFactory.class).iterator().next();
        Framework framework = factory.newFramework(config);
        framework.start();
        try {
            BundleContext context = framework.getBundleContext();
            Bundle common = context.installBundle(Path.of(args[0]).toUri().toString());
            common.start();
            Object path = common.loadClass("org.eclipse.core.runtime.Path")
                    .getConstructor(String.class).newInstance("/eclipse/test");
            if (common.getState() != Bundle.ACTIVE || !path.toString().equals("/eclipse/test")) {
                throw new AssertionError("Equinox Common did not start or load its classes");
            }
        } finally {
            framework.stop();
            if (framework.waitForStop(30000).getType() != FrameworkEvent.STOPPED) {
                throw new AssertionError("Equinox framework did not stop");
            }
        }
    }
}
