import java.nio.file.Path;
import java.util.HashMap;
import java.util.Map;
import java.util.ServiceLoader;
import org.osgi.framework.Constants;
import org.osgi.framework.launch.FrameworkFactory;
import org.osgi.framework.namespace.PackageNamespace;
import org.osgi.framework.wiring.BundleWiring;

class RepositoryWiring {
    public static void main(String[] args) throws Exception {
        var factory = ServiceLoader.load(FrameworkFactory.class).findFirst().orElseThrow();
        var framework = factory.newFramework(Map.of(Constants.FRAMEWORK_STORAGE, Path.of(args[0]).toAbsolutePath().toString()));
        framework.start();
        try {
            var context = framework.getBundleContext();
            var function = context.installBundle(Path.of(args[1]).toUri().toString());
            var promise = context.installBundle(Path.of(args[2]).toUri().toString());
            var repository = context.installBundle(Path.of(args[3]).toUri().toString());
            function.start(); promise.start(); repository.start();
            var wires = new HashMap<String, Long>();
            for (var wire : repository.adapt(BundleWiring.class).getRequiredWires(PackageNamespace.PACKAGE_NAMESPACE)) {
                var pkg = (String) wire.getCapability().getAttributes().get(PackageNamespace.PACKAGE_NAMESPACE);
                wires.put(pkg, wire.getProviderWiring().getBundle().getBundleId());
            }
            if (!Long.valueOf(0).equals(wires.get("org.osgi.resource"))
                    || !Long.valueOf(promise.getBundleId()).equals(wires.get("org.osgi.util.promise"))) {
                throw new AssertionError(wires);
            }
            var api = repository.loadClass("org.osgi.service.repository.Repository");
            var expression = repository.loadClass("org.osgi.service.repository.RequirementExpression");
            var result = api.getMethod("findProviders", expression).getReturnType();
            if (result != promise.loadClass("org.osgi.util.promise.Promise")) throw new AssertionError(result);
            System.out.println("Repository.findProviders resolves against the installed Resource and Promise APIs");
        } finally {
            framework.stop(); framework.waitForStop(10000);
        }
    }
}
