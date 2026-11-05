// SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
// SPDX-License-Identifier: MulanPSL-2.0

import java.lang.reflect.Modifier;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import junit.framework.TestCase;
import org.junit.Test;
import org.junit.internal.TextListener;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;

class RunJUnit {
    public static void main(String[] args) throws Exception {
        List<Class<?>> tests = new ArrayList<>();
        for (String name : args) {
            Class<?> candidate = Class.forName(name, false, RunJUnit.class.getClassLoader());
            if (Modifier.isAbstract(candidate.getModifiers())) {
                continue;
            }
            if (TestCase.class.isAssignableFrom(candidate)
                    || Arrays.stream(candidate.getMethods()).anyMatch(method -> method.isAnnotationPresent(Test.class))) {
                tests.add(candidate);
            }
        }
        JUnitCore runner = new JUnitCore();
        runner.addListener(new TextListener(System.out));
        Result result = runner.run(tests.toArray(new Class<?>[0]));
        if (result.getRunCount() == 0 || !result.wasSuccessful()) {
            throw new AssertionError("Upstream JUnit tests failed");
        }
    }
}
