#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
repo=/usr/share/maven-repository
bootstrap=/usr/share/java/javapackages-bootstrap
mkdir -p target/{rng/src,rng/classes,rhino/src,rhino/classes,test-classes,launcher}
# Compile the RNG implementation used by the decimal conversion assertions.
for archive in "$1" "$2" "$3"; do
    unzip -qo "$archive" -d target/rng/src
done
find target/rng/src -name '*.java' ! -name module-info.java | sort > target/rng/sources
javac --release 8 -proc:none -encoding UTF-8 -d target/rng/classes @target/rng/sources
# Compile Rhino and its JSR-223 provider to exercise the original JavaScript inputs.
for archive in "$4" "$5"; do
    unzip -qo "$archive" -d target/rhino/src
done
find target/rhino/src -name '*.java' ! -name module-info.java | sort > target/rhino/sources
javac --release 11 -proc:none -encoding UTF-8 -d target/rhino/classes @target/rhino/sources
python3 - <<'RESOURCES'
from pathlib import Path
import shutil
source = Path("target/rhino/src")
destination = Path("target/rhino/classes")
for path in source.rglob("*"):
    relative = path.relative_to(source)
    if path.is_file() and path.suffix != ".java" and relative.as_posix() != "META-INF/MANIFEST.MF":
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)
RESOURCES
mkdir -p target/rhino/classes/META-INF/services
printf '%s\n' org.mozilla.javascript.engine.RhinoScriptEngineFactory > target/rhino/classes/META-INF/services/javax.script.ScriptEngineFactory
cp="$PWD/target/commons-text.jar:$PWD/target/rng/classes:$PWD/target/rhino/classes"
for artifact in org/apache/commons/commons-lang3/3.20.0/commons-lang3-3.20.0 commons-io/commons-io/2.21.0/commons-io-2.21.0 org/mockito/mockito-core/4.11.0/mockito-core-4.11.0 org/mockito/mockito-junit-jupiter/4.11.0/mockito-junit-jupiter-4.11.0; do
    cp="$cp:$repo/$artifact.jar"
done
for group in org/junit/jupiter org/junit/platform; do
    jars=$(find "$repo/$group" -name '*-5.12.2.jar' -o -name '*-1.12.2.jar' | paste -sd:)
    cp="$cp:$jars"
done
cp="$cp:$bootstrap/*"
# Both excluded files contain JMH benchmarks. All JUnit test classes are compiled.
find src/test/java -name '*.java' ! -name DoubleFormatPerformance.java ! -name LongestCommonSubsequencePerformance.java | sort > target/test-sources
javac --release 11 -proc:none -encoding ISO-8859-1 -g -cp "$cp" -d target/test-classes @target/test-sources
cp -r src/test/resources/. target/test-classes/
# The upstream test dependency selects Mockito's inline mock maker for final classes.
mkdir -p target/test-classes/mockito-extensions
printf '%s\n' mock-maker-inline > target/test-classes/mockito-extensions/org.mockito.plugins.MockMaker
tests=$(sed -n '/Test[.]java$/{s|src/test/java/||;s|[.]java$||;s|/|.|g;p;}' target/test-sources)
javac -proc:none -cp "$cp" -d target/launcher /usr/libexec/eclipse-equinox/RunJupiter.java
# Give the local HTTPS lookup fixture a certificate trusted only during that test.
jdk_bin=$(dirname "$(readlink -f /usr/bin/javac)")
"$jdk_bin/keytool" -genkeypair -alias localhost -keyalg RSA -keysize 2048 -validity 2 -dname CN=localhost -ext SAN=dns:localhost -storetype PKCS12 -keystore target/test-keystore.p12 -storepass changeit -keypass changeit -noprompt
java -cp "target/launcher:target/test-classes:$cp" RunJupiter $tests
