#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
repo=/usr/share/maven-repository
bootstrap=/usr/share/java/javapackages-bootstrap
ecj=$repo/org/eclipse/jdt/ecj/3.32.0/ecj-3.32.0.jar
fixtures=$PWD/target/fixtures
mkdir -p "$fixtures" target/test-classes
# ECJ needs the historical java.util.Random API when compiling Commons Lang 2.0.
python3 - "$JAVA_HOME/lib/ct.sym" "$fixtures/java8-apis.jar" <<'PY'
from pathlib import PurePosixPath
from sys import argv
from zipfile import ZipFile

with ZipFile(argv[1]) as source, ZipFile(argv[2], "w") as output:
    names = set()
    for entry in source.namelist():
        path = PurePosixPath(entry)
        if len(path.parts) < 3 or "8" not in path.parts[0] or path.suffix != ".sig":
            continue
        name = PurePosixPath(*path.parts[2:]).with_suffix(".class").as_posix()
        if name not in names:
            output.writestr(name, source.read(entry))
            names.add(name)
    assert "java/util/Random.class" in names
PY
for coordinate in commons-lang-2.0 wsdl4j-1.5.3; do
    src="$fixtures/$coordinate"
    mkdir -p "$src/classes"
    find "$src/src" -name '*.java' | sort > "$src/files"
    java -jar "$ecj" -source 1.3 -target 1.1 -inlineJSR -g -nowarn -bootclasspath "$fixtures/java8-apis.jar" -d "$src/classes" @"$src/files"
    if test "$coordinate" = commons-lang-2.0; then
        # BCELifier compares the javap instruction offsets for these two classes with javac output.
        find "$src/src" \( -name Fraction.java -o -name NestableDelegate.java \) | sort > "$src/javap-fixtures"
        javac --release 8 -encoding ISO-8859-1 -g -proc:none -cp "$src/classes" -d "$src/classes" @"$src/javap-fixtures"
    fi
    jar cf "$fixtures/$coordinate.jar" -C "$src/classes" .
done
cp="$PWD/target/test-classes:$PWD/target/classes:$ecj:$fixtures/commons-lang-2.0.jar:$fixtures/wsdl4j-1.5.3.jar:$fixtures/javaee-api.jar"
for path in org/junit/platform org/junit/jupiter org/apache/commons/commons-lang3 org/apache/commons/commons-exec net/java/dev/jna commons-io; do
    jars=$(find "$repo/$path" -name '*.jar' ! -name '*-sources.jar' -printf '%p:')
    cp="$cp:$jars"
done
for n in junit-jupiter-params junit-platform-reporting mockito-core byte-buddy byte-buddy-agent objenesis apiguardian-api opentest4j junit hamcrest-core asm asm-commons asm-tree; do
    cp="$cp:$bootstrap/$n.jar"
done
# The upstream build excludes its JMH benchmark from the unit test suite.
find src/test/java -name '*.java' ! -name '*Benchmark*' | sort > target/test-units
grep -v 'ConstantPoolModuleAccessTest.java$' target/test-units > target/java8-tests
javac --release 8 -g -proc:none -encoding UTF-8 -cp "$cp" -d target/test-classes @target/java8-tests
javac --release 25 -g -proc:none -encoding UTF-8 -cp "$cp" -d target/test-classes src/test/java/org/apache/bcel/classfile/ConstantPoolModuleAccessTest.java
cp -r src/test/resources/. target/test-classes/
tests=$(sed 's|src/test/java/||;s|[.]java$||;s|/|.|g' target/test-units)
java -Xmx1024m -Dbasedir="$PWD" -cp "$cp" /usr/libexec/eclipse-equinox/RunJupiter.java $tests
