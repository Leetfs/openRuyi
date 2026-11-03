import java.io.InputStream;
import java.io.OutputStream;
import java.nio.file.Path;
import java.util.Hashtable;
import java.util.Map;
import java.util.ServiceLoader;
import org.osgi.framework.Constants;
import org.osgi.framework.FrameworkEvent;
import org.osgi.framework.launch.FrameworkFactory;

class GogoCheck {
    public static class Commands {
        public String greet(String name) { return "hello " + name; }
    }
    public static void main(String[] args) throws Exception {
        var framework = ServiceLoader.load(FrameworkFactory.class).findFirst().orElseThrow()
                .newFramework(Map.of(Constants.FRAMEWORK_STORAGE, args[1]));
        framework.start();
        try {
            var bundle = framework.getBundleContext().installBundle(Path.of(args[0]).toUri().toString());
            bundle.start();
            var context = bundle.getBundleContext();
            var properties = new Hashtable<String, Object>();
            properties.put("osgi.command.scope", "packaging");
            properties.put("osgi.command.function", new String[]{"greet"});
            context.registerService(Commands.class.getName(), new Commands(), properties);
            Class<?> api = bundle.loadClass("org.apache.felix.service.command.CommandProcessor");
            var processor = context.getService(context.getServiceReference(api.getName()));
            Object session = api.getMethod("createSession", InputStream.class, OutputStream.class, OutputStream.class)
                    .invoke(processor, System.in, System.out, System.err);
            Class<?> sessionApi = bundle.loadClass("org.apache.felix.service.command.CommandSession");
            try {
                Object result = sessionApi.getMethod("execute", CharSequence.class).invoke(session, "packaging:greet Eclipse");
                if (!"hello Eclipse".equals(result)) throw new AssertionError("Unexpected response: " + result);
            } finally {
                sessionApi.getMethod("close").invoke(session);
            }
        } finally {
            framework.stop();
            if (framework.waitForStop(30000).getType() != FrameworkEvent.STOPPED) throw new AssertionError();
        }
    }
}
