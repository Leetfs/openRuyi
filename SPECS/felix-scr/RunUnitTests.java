import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

class RunUnitTests {
    public static void main(String[] args) throws Exception {
        Class<?>[] tests = new Class<?>[args.length - 1];
        for (int i = 1; i < args.length; i++) tests[i - 1] = Class.forName(args[i]);
        Result result = new JUnitCore().run(tests);
        try (var report = new PrintWriter(Files.newBufferedWriter(Path.of(args[0])))) {
            for (Failure failure : result.getFailures()) {
                report.println(failure.getTestHeader());
                failure.getException().printStackTrace(report);
            }
            report.println("SCR JUnit: " + result.getRunCount() + " tests, " + result.getFailureCount() + " failures");
        }
        if (!result.wasSuccessful() || result.getRunCount() == 0) System.exit(1);
    }
}
