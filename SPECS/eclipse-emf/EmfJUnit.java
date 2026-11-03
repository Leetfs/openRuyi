import java.util.List;
import org.junit.runner.Description;
import org.junit.runner.JUnitCore;
import org.junit.runner.Request;
import org.junit.runner.manipulation.Filter;
public class EmfJUnit {
    public static void run(List<Class<?>> tests, boolean hasPde) throws Exception {
        Request request = Request.classes(tests.toArray(Class<?>[]::new));
        if (!hasPde) {
            String type = "org.eclipse.emf.test.core.ecore.EcoreTest";
            String method = "testProvideCapabilityRegistration";
            Class.forName(type).getMethod(method);
            request = request.filterWith(new Filter() {
                public boolean shouldRun(Description test) {
                    return !type.equals(test.getClassName()) || !method.equals(test.getMethodName());
                }
                public String describe() { return "PDE target registry is unavailable during SDK bootstrap"; }
            });
            System.out.println("PDE target model unavailable: deferred " + type + "." + method);
        }
        var result = new JUnitCore().run(request);
        for (var failure : result.getFailures()) failure.getException().printStackTrace();
        System.out.println("EMF framework JUnit tests=" + result.getRunCount() + ", ignored=" + result.getIgnoreCount()
                           + ", failed=" + result.getFailureCount());
        if (!result.wasSuccessful() || result.getRunCount() != (hasPde ? 52 : 51)) throw new AssertionError("EMF JUnit");
    }
}
