// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import org.junit.Test;
import org.junit.runner.RunWith;
import org.powermock.api.mockito.PowerMockito;
import org.powermock.core.classloader.annotations.PrepareForTest;
import org.powermock.modules.junit4.PowerMockRunner;
import static org.junit.Assert.assertEquals;
@RunWith(PowerMockRunner.class)
@PrepareForTest(StaticServiceTest.Service.class)
public class StaticServiceTest {
    static final class Service { static String read() { return "original"; } }
    @Test public void staticCall() {
        PowerMockito.mockStatic(Service.class);
        PowerMockito.when(Service.read()).thenReturn("mocked");
        assertEquals("mocked", Service.read());
        PowerMockito.verifyStatic(Service.class);
        Service.read();
    }
}
