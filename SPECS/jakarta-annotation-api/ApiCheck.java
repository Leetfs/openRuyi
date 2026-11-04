package check;

import jakarta.annotation.*;
import jakarta.annotation.security.RolesAllowed;
import jakarta.annotation.sql.DataSourceDefinition;

public class ApiCheck {
    @RolesAllowed("reader")
    @DataSourceDefinition(name="jdbc/example", className="example.Driver")
    static class Example {
        @PostConstruct void start() {}
        @PreDestroy void stop() {}
    }
    public static void main(String[] args) throws Exception {
        if (!Example.class.getDeclaredMethod("start").isAnnotationPresent(PostConstruct.class)
                || !Example.class.getDeclaredMethod("stop").isAnnotationPresent(PreDestroy.class)
                || !"reader".equals(Example.class.getAnnotation(RolesAllowed.class).value()[0]))
            throw new AssertionError("Lifecycle and role annotations");
        var ds = Example.class.getAnnotation(DataSourceDefinition.class);
        if (!"jdbc/example".equals(ds.name()) || !"example.Driver".equals(ds.className()) || !ds.transactional())
            throw new AssertionError("Data source defaults");
    }
}
