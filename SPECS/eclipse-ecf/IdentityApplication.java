package org.eclipse.ecf.tests.core.identity;
import java.util.ArrayList;
import java.util.List;
import org.eclipse.equinox.app.IApplication;
import org.eclipse.equinox.app.IApplicationContext;
import org.junit.runner.JUnitCore;
import org.junit.runner.notification.Failure;

public class IdentityApplication implements IApplication {
    @Override
    public Object start(IApplicationContext context) throws ClassNotFoundException {
        String[] names = (String[]) context.getArguments().get(IApplicationContext.APPLICATION_ARGS);
        List<Class<?>> tests = new ArrayList<>();
        for (String name : names) tests.add(Class.forName(getClass().getPackageName() + "." + name));
        var result = new JUnitCore().run(tests.toArray(Class<?>[]::new));
        for (Failure failure : result.getFailures()) System.err.println(failure.getTrace());
        System.out.printf("ECF identity suite ran %d tests with %d failures%n", result.getRunCount(), result.getFailureCount());
        return result.wasSuccessful() && result.getRunCount() != 0 ? EXIT_OK : Integer.valueOf(1);
    }

    @Override
    public void stop() {}
}
