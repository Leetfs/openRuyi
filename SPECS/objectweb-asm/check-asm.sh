#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
root=$PWD
bootstrap=/usr/share/java/javapackages-bootstrap
repo=/usr/share/maven-repository/org/junit
tests=$root/build/tests
compiler=$root/build/test-compiler
mkdir -p "$tests" "$compiler" build/compiler-sources
# ASMifierTest recompiles each regenerated class with Janino and compares the bytecode.
unzip -oq "$1" -d build/compiler-sources
unzip -oq "$2" -d build/compiler-sources
find build/compiler-sources -name '*.java' ! -name module-info.java | sort > build/compiler-sources.list
javac --release 8 -proc:none -nowarn -cp "$bootstrap/ant.jar:$bootstrap/ant-launcher.jar" -d "$compiler" @build/compiler-sources.list
cp build/compiler-sources/org.codehaus.commons.compiler.properties "$compiler/"
cp="$tests:$compiler"
for jar in "$root"/build/bundles/*.jar "$repo"/platform/*/1.12.2/*.jar "$repo"/jupiter/*/5.12.2/*.jar; do cp="$cp:$jar"; done
for n in junit-jupiter-params opentest4j apiguardian-api junit univocity-parsers hamcrest-core; do cp="$cp:$bootstrap/$n.jar"; done
modules='asm-test asm asm-tree asm-analysis asm-commons asm-util'
find asm-test/src/main/java -name '*.java' > build/test-sources.list
cp -a asm-test/src/main/resources/. "$tests/"
for n in $modules; do
    find "$n/src/test/java" -name '*.java' >> build/test-sources.list
    if test -d "$n/src/test/resources"; then cp -a "$n/src/test/resources/." "$tests/"; fi
done
javac --release 17 -g -proc:none -encoding UTF-8 -cp "$cp" -d "$tests" @build/test-sources.list /usr/libexec/eclipse-equinox/RunJupiter.java
for n in $modules; do
    (
        cd "$n"
        mapfile -t selectors < <(find src/test/java -name '*Test.java' | sed 's|^src/test/java/||;s|/|.|g;s|[.]java$||' | sort)
        java -ea -cp "$cp" RunJupiter "${selectors[@]}"
    )
done
