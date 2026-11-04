package check;

import jakarta.inject.*;
import java.lang.annotation.*;
import java.lang.reflect.Constructor;

public class ApiCheck {
    @Qualifier @Retention(RetentionPolicy.RUNTIME) @interface Flavor {}
    @Singleton static class Example {
        @Inject Example(@Named("item") Provider<String> value) {}
    }
    public static void main(String[] args) throws Exception {
        Constructor<?> constructor = Example.class.getDeclaredConstructor(Provider.class);
        if (!constructor.isAnnotationPresent(Inject.class)
                || !"item".equals(constructor.getParameters()[0].getAnnotation(Named.class).value())
                || !Named.class.isAnnotationPresent(Qualifier.class)
                || !Singleton.class.isAnnotationPresent(Scope.class)
                || !Example.class.isAnnotationPresent(Singleton.class)
                || !Flavor.class.isAnnotationPresent(Qualifier.class)) throw new AssertionError("Injection metadata");
        Provider<String> provider = () -> "item";
        if (!"item".equals(provider.get())) throw new AssertionError("Provider");
    }
}
