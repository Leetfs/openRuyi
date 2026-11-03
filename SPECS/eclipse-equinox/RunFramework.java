// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import java.net.URL;
import java.net.URLClassLoader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.ServiceLoader;
import org.osgi.framework.Bundle;
import org.osgi.framework.Constants;
import org.osgi.framework.launch.FrameworkFactory;
import org.osgi.framework.wiring.BundleWiring;

/** Run a test entry point against the resolved classes of an installed Eclipse bundle. */
class RunFramework {
    public static void main(String[] args) throws Exception {
        Path state=Path.of(args[0]).toAbsolutePath();
        var framework=ServiceLoader.load(FrameworkFactory.class).findFirst().orElseThrow()
            .newFramework(Map.of(Constants.FRAMEWORK_STORAGE,state.resolve("framework").toString(),
                "osgi.instance.area",state.resolve("workspace").toUri().toString()));
        framework.start();
        var previous=Thread.currentThread().getContextClassLoader();
        try {
            var context=framework.getBundleContext();
            List<Bundle> start=new ArrayList<>();
            Bundle target=null;
            for (String line : Files.readAllLines(Path.of(args[1]))) {
                if (line.isBlank()) continue;
                String[] fields=line.split(" ",2);
                Bundle bundle=context.installBundle(Path.of(fields[1]).toAbsolutePath().toUri().toString());
                switch (fields[0]) {
                    case "start" -> start.add(bundle);
                    case "install" -> { }
                    default -> throw new IllegalArgumentException("Unknown bundle action: "+fields[0]);
                }
                if (args[2].equals(bundle.getSymbolicName())) target=bundle;
            }
            if (target==null) throw new IllegalArgumentException("Missing test host "+args[2]);
            for (Bundle bundle:start) bundle.start();
            List<URL> urls=new ArrayList<>();
            for (String line : Files.readAllLines(Path.of(args[3]))) {
                if (!line.isBlank()) urls.add(Path.of(line).toAbsolutePath().toUri().toURL());
            }
            var wiring=target.adapt(BundleWiring.class);
            if (wiring==null) throw new IllegalStateException("Unresolved test host "+args[2]);
            try (var loader=new URLClassLoader(urls.toArray(URL[]::new),wiring.getClassLoader())) {
                Thread.currentThread().setContextClassLoader(loader);
                var main=loader.loadClass(args[4]).getDeclaredMethod("main",String[].class);
                main.setAccessible(true);
                main.invoke(null,(Object)Arrays.copyOfRange(args,5,args.length));
            }
        } finally {
            Thread.currentThread().setContextClassLoader(previous);
            framework.stop();
            framework.waitForStop(20000);
        }
    }
}
