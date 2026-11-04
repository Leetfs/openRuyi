// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import java.nio.file.Path;
import java.util.concurrent.TimeUnit;
import org.eclipse.jdi.Bootstrap;

public class EclipseVmCheck {
    public static void main(String[] args) throws Exception {
        if (args.length == 0) {
            System.out.println("JDT resumed the debuggee");
            return;
        }
        var manager = Bootstrap.virtualMachineManager();
        var connector = manager.attachingConnectors().stream()
            .filter(c -> c.transport().name().equals("dt_socket")).findFirst().orElseThrow();
        var child = new ProcessBuilder(Path.of(System.getProperty("java.home"), "bin", "java").toString(),
            "-agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=127.0.0.1:0",
            "-cp", args[0], EclipseVmCheck.class.getName()).redirectErrorStream(true).start();
        try {
            var output = child.inputReader();
            var line = output.readLine();
            String prefix = "Listening for transport dt_socket at address: ";
            if (line == null || !line.startsWith(prefix)) throw new AssertionError(line);
            var parameters = connector.defaultArguments();
            parameters.get("hostname").setValue("127.0.0.1");
            parameters.get("port").setValue(line.substring(prefix.length()));
            parameters.get("timeout").setValue("10000");
            var vm = connector.attach(parameters);
            if (!vm.version().equals(System.getProperty("java.version"))) throw new AssertionError(vm.version());
            vm.resume();
            if (!child.waitFor(20, TimeUnit.SECONDS) || child.exitValue() != 0
                    || output.lines().noneMatch("JDT resumed the debuggee"::equals)) {
                throw new AssertionError("The Eclipse JDI client did not resume the target");
            }
        } finally {
            child.destroyForcibly();
        }
    }
}
