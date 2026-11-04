// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import org.junit.Test;
import org.junit.platform.engine.discovery.DiscoverySelectors;
import org.junit.platform.launcher.EngineFilter;
import org.junit.platform.launcher.core.LauncherDiscoveryRequestBuilder;
import org.junit.platform.launcher.core.LauncherFactory;
import org.junit.platform.launcher.listeners.SummaryGeneratingListener;

public class VintageExecution {
    public static class LegacyTests {
        @Test public void passing() { org.junit.Assert.assertEquals(4, 2 + 2); }
        @Test public void failing() { org.junit.Assert.fail("expected JUnit 4 failure"); }
    }

    public static void main(String[] args) {
        var request = LauncherDiscoveryRequestBuilder.request()
            .filters(EngineFilter.includeEngines("junit-vintage"))
            .selectors(DiscoverySelectors.selectClass(LegacyTests.class)).build();
        var summary = new SummaryGeneratingListener();
        LauncherFactory.create().execute(request, summary);
        var result = summary.getSummary();
        if (result.getTestsSucceededCount() != 1 || result.getTestsFailedCount() != 1
                || !"expected JUnit 4 failure".equals(result.getFailures().get(0).getException().getMessage())) {
            throw new AssertionError("Vintage did not report the two JUnit 4 outcomes");
        }
    }
}
