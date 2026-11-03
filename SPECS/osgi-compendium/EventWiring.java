// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0
import java.nio.file.Path;
import java.util.HashMap;
import java.util.Map;
import java.util.ServiceLoader;
import org.osgi.framework.Constants;
import org.osgi.framework.Filter;
import org.osgi.framework.FrameworkUtil;
import org.osgi.framework.launch.FrameworkFactory;

class EventWiring {
    public static void main(String[] args) throws Exception {
        var fw = ServiceLoader.load(FrameworkFactory.class).findFirst().orElseThrow().newFramework(
            Map.of(Constants.FRAMEWORK_STORAGE, Path.of(args[0]).toAbsolutePath().toString()));
        fw.start();
        try {
            var api = fw.getBundleContext().installBundle(Path.of(args[1]).toUri().toString());
            api.start();
            var eventType = api.loadClass("org.osgi.service.event.Event");
            var properties = new HashMap<String, Object>();
            properties.put("count", 3);
            var event = eventType.getConstructor(String.class, Map.class).newInstance("eclipse/target/changed", properties);
            properties.put("count", 9);
            if (!eventType.getMethod("getTopic").invoke(event).equals("eclipse/target/changed")
                    || !eventType.getMethod("getProperty", String.class).invoke(event, "count").equals(3)
                    || !(Boolean)eventType.getMethod("matches", Filter.class).invoke(event, FrameworkUtil.createFilter("(count=3)")))
                throw new AssertionError("Event did not preserve the topic and copied properties");
            api.loadClass("org.osgi.service.event.EventAdmin");
            api.loadClass("org.osgi.service.event.EventHandler");
        } finally {
            fw.stop(); fw.waitForStop(10000);
        }
    }
}
