import java.net.URI;
import org.eclipse.core.net.proxy.IProxyData;
import org.eclipse.core.net.proxy.IProxyService;
import org.osgi.framework.BundleContext;

public class ProxyCheck {
    public static void verify(BundleContext context) throws Exception {
        var reference = context.getServiceReference(IProxyService.class);
        if (reference == null) throw new AssertionError("Proxy service not registered");
        try {
            var proxy = context.getService(reference);
            proxy.setSystemProxiesEnabled(false);
            proxy.setProxiesEnabled(true);
            var http = proxy.getProxyData(IProxyData.HTTP_PROXY_TYPE);
            http.setHost("proxy.example.invalid");
            http.setPort(3128);
            proxy.setProxyData(new IProxyData[] {http});
            proxy.setNonProxiedHosts(new String[] {"internal.example.invalid"});
            var route = proxy.select(URI.create("http://outside.example.invalid/"));
            if (route.length != 1 || !http.getHost().equals(route[0].getHost()) || route[0].getPort() != 3128) {
                throw new AssertionError("Incorrect HTTP proxy route");
            }
            if (proxy.select(URI.create("http://internal.example.invalid/")).length != 0) {
                throw new AssertionError("Proxy bypass ignored");
            }
            System.out.println("Eclipse registered the proxy service and applied its HTTP route and bypass");
        } finally {
            context.ungetService(reference);
        }
    }
}
