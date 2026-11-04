#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
fixture=$PWD/build/api-fixture
mkdir -p "$fixture"/{META-INF,src/org/openruyi/fixture,bin,target} build/api-state
cat > "$fixture/.project" <<'EOF'
<projectDescription><name>org.openruyi.api.fixture</name><projects/><buildSpec/><natures><nature>org.eclipse.jdt.core.javanature</nature><nature>org.eclipse.pde.PluginNature</nature><nature>org.eclipse.pde.api.tools.apiAnalysisNature</nature></natures></projectDescription>
EOF
cat > "$fixture/.classpath" <<'EOF'
<classpath><classpathentry kind="src" path="src"/><classpathentry kind="output" path="bin"/></classpath>
EOF
cat > "$fixture/META-INF/MANIFEST.MF" <<'EOF'
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-SymbolicName: org.openruyi.api.fixture
Bundle-Version: 1.0.0
Export-Package: org.openruyi.fixture
EOF
cat > "$fixture/src/org/openruyi/fixture/ApiSample.java" <<'EOF'
package org.openruyi.fixture;
/** Sample public API.
 * @noextend This fixture may not be subclassed.
 */
public class ApiSample { public int value() { return 42; } }
EOF
javac --release 17 -d "$fixture/bin" "$fixture/src/org/openruyi/fixture/ApiSample.java"
api=$PWD/build/bundles/org.eclipse.pde.api.tools.jar
ant=$PWD/build/classpath/apitooling-ant.jar
unzip -p "$api" lib/apitooling-ant.jar > "$ant"
ant_runtime=/usr/share/java/javapackages-bootstrap/ant.jar
cp="$ant:$api:$ant_runtime:build/bundles/org.eclipse.pde.core.jar:$(cat build/compiler-classpath)"
javac --release 17 -proc:none -cp "$cp" -d build/tests "$1"
printf '%s\n' "$PWD/build/tests" "$ant" "$ant_runtime" > build/api-test-path
java -cp "$2" /usr/libexec/eclipse-equinox/RunFramework.java "$PWD/build/api-state" build/test-bundles org.eclipse.pde.api.tools build/api-test-path PdeApiDescription "$fixture"
