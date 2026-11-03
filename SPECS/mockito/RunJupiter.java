import java.io.PrintWriter;
import java.util.Arrays;
import org.junit.platform.engine.DiscoverySelector;
import org.junit.platform.engine.discovery.DiscoverySelectors;
import org.junit.platform.launcher.Launcher;
import org.junit.platform.launcher.core.LauncherDiscoveryRequestBuilder;
import org.junit.platform.launcher.core.LauncherFactory;
import org.junit.platform.launcher.listeners.SummaryGeneratingListener;
import org.junit.platform.launcher.listeners.TestExecutionSummary;

public class RunJupiter {
    public static void main(String[] classes) {
        DiscoverySelector[] selectors = Arrays.stream(classes)
                .map(DiscoverySelectors::selectClass)
                .toArray(DiscoverySelector[]::new);
        SummaryGeneratingListener listener = new SummaryGeneratingListener();
        Launcher launcher = LauncherFactory.create();
        launcher.registerTestExecutionListeners(listener);
        launcher.execute(LauncherDiscoveryRequestBuilder.request().selectors(selectors).build());
        TestExecutionSummary summary = listener.getSummary();
        PrintWriter output = new PrintWriter(System.out, true);
        summary.printTo(output);
        summary.printFailuresTo(output);
        if (summary.getTestsSucceededCount() == 0 || summary.getTotalFailureCount() != 0) {
            System.exit(1);
        }
    }
}
