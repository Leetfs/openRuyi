import java.nio.file.Path;
import java.util.Map;
import java.util.ServiceLoader;
import java.util.function.Supplier;
import org.osgi.framework.Bundle;
import org.osgi.framework.Constants;
import org.osgi.framework.FrameworkEvent;
import org.osgi.framework.launch.FrameworkFactory;
import org.osgi.util.tracker.ServiceTracker;

class ScrCheck {
    public static void main(String[] args) throws Exception {
        var framework = ServiceLoader.load(FrameworkFactory.class).findFirst().orElseThrow()
                .newFramework(Map.of(Constants.FRAMEWORK_STORAGE, args[0]));
        framework.start();
        try {
            var context = framework.getBundleContext();
            for (int i = 1; i < args.length - 1; i++) {
                context.installBundle(Path.of(args[i]).toUri().toString()).start();
            }
            var filter = context.createFilter("(&(objectClass=java.util.function.Supplier)(component.name=packaging.echo))");
            var service = new ServiceTracker<Object, Object>(context, filter, null);
            service.open();
            try {
                Bundle client = context.installBundle(Path.of(args[args.length - 1]).toUri().toString());
                client.start();
                Object active = service.waitForService(15000);
                if (!(active instanceof Supplier<?> supplier) || !"active".equals(supplier.get())) {
                    throw new AssertionError("SCR did not activate the component");
                }
                client.stop();
                if (service.getService() != null) throw new AssertionError("SCR did not unregister the service");
            } finally { service.close(); }
        } finally {
            framework.stop();
            if (framework.waitForStop(30000).getType() != FrameworkEvent.STOPPED) throw new AssertionError();
        }
    }
}
