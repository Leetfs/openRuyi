import java.io.PrintWriter;
import java.util.Arrays;
import org.junit.platform.engine.DiscoverySelector;
import org.junit.platform.engine.discovery.DiscoverySelectors;
import org.junit.platform.launcher.Launcher;
import org.junit.platform.launcher.core.LauncherDiscoveryRequestBuilder;
import org.junit.platform.launcher.core.LauncherFactory;
import org.junit.platform.launcher.listeners.SummaryGeneratingListener;
class RunJupiter {
    public static void main(String[] args) {
        DiscoverySelector[] selectors = Arrays.stream(args).map(DiscoverySelectors::selectClass)
                .toArray(DiscoverySelector[]::new);
        var request = LauncherDiscoveryRequestBuilder.request().selectors(selectors).build();
        var listener = new SummaryGeneratingListener();
        Launcher launcher = LauncherFactory.create();
        launcher.registerTestExecutionListeners(listener);
        launcher.execute(request);
        var summary = listener.getSummary();
        var output = new PrintWriter(System.out, true);
        summary.printTo(output);
        summary.printFailuresTo(output);
        if (summary.getTestsSucceededCount() == 0 || summary.getTotalFailureCount() != 0) {
            throw new AssertionError("JUnit Jupiter tests failed");
        }
    }
}
