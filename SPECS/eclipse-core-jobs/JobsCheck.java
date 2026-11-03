import java.lang.reflect.Proxy;
import java.nio.file.Path;
import java.util.Map;
import java.util.ServiceLoader;
import java.util.concurrent.atomic.AtomicBoolean;
import org.osgi.framework.Bundle;
import org.osgi.framework.Constants;
import org.osgi.framework.FrameworkEvent;
import org.osgi.framework.launch.Framework;
import org.osgi.framework.launch.FrameworkFactory;

class JobsCheck {
    public static void main(String[] args) throws Exception {
        Framework framework = ServiceLoader.load(FrameworkFactory.class).iterator().next()
                .newFramework(Map.of(Constants.FRAMEWORK_STORAGE, args[2]));
        framework.start();
        try {
            var context = framework.getBundleContext();
            context.installBundle(Path.of(args[0]).toUri().toString()).start();
            Bundle jobs = context.installBundle(Path.of(args[1]).toUri().toString());
            jobs.start();
            Class<?> type = jobs.loadClass("org.eclipse.core.runtime.jobs.Job");
            Class<?> runnable = jobs.loadClass("org.eclipse.core.runtime.ICoreRunnable");
            Class<?> monitor = jobs.loadClass("org.eclipse.core.runtime.IProgressMonitor");
            AtomicBoolean ran = new AtomicBoolean();
            Object action = Proxy.newProxyInstance(runnable.getClassLoader(), new Class<?>[]{runnable},
                    (proxy, method, arguments) -> {
                        if (method.getName().equals("run")) ran.set(true);
                        return null;
                    });
            Object job = type.getMethod("create", String.class, runnable).invoke(null, "openRuyi test", action);
            type.getMethod("schedule").invoke(job);
            boolean joined = (Boolean) type.getMethod("join", long.class, monitor).invoke(job, 30000L, null);
            if (!joined || !ran.get()) throw new AssertionError("Scheduled job did not complete");
        } finally {
            framework.stop();
            if (framework.waitForStop(30000).getType() != FrameworkEvent.STOPPED) {
                throw new AssertionError("Framework did not stop");
            }
        }
    }
}
