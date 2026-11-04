#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
root=$PWD; b=/usr/share/java/javapackages-bootstrap
work="$root/build/platform-tests"; mkdir -p "$work/tests"
cp="$root/build/bundles/junit-vintage-engine.jar:$root/build/bundles/junit-jupiter-engine.jar:$root/build/bundles/junit-jupiter-api.jar"
cp="$cp:$root/build/bundles/junit-platform-launcher.jar:$root/build/bundles/junit-platform-engine.jar:$root/build/bundles/junit-platform-commons.jar"
java --module-path "$cp:$b/apiguardian-api.jar:$b/opentest4j.jar:$b/junit.jar:$b/hamcrest-core.jar" --add-modules org.junit.platform.launcher,org.junit.jupiter.engine,org.junit.vintage.engine --validate-modules
mockito=/usr/share/maven-repository/org/mockito
cp="$cp:$mockito/mockito-junit-jupiter/4.11.0/mockito-junit-jupiter-4.11.0.jar:$mockito/mockito-core/4.11.0/mockito-core-4.11.0.jar:$b/*"
sourcepath=$(find "$root" -path '*/src/testFixtures/java' -type d | sort | paste -sd:)
classes=(
    org.junit.platform.commons.util.{ExceptionUtilsTests,PreconditionsTests,StringUtilsTests}
    org.junit.platform.engine.{TestTagTests,UniqueIdTests}
    org.junit.platform.engine.discovery.{ClassSelectorTests,ClasspathRootSelectorTests,DiscoverySelectorsTests,MethodSelectorTests,PackageSelectorTests}
    org.junit.platform.launcher.{MethodFilterTests,TagFilterTests,TestIdentifierTests}
    org.junit.platform.launcher.core.HierarchicalOutputDirectoryProviderTests org.junit.platform.launcher.listeners.OutputDirTests
    org.junit.platform.launcher.tagexpression.{ParserErrorTests,ParserTests,TagExpressionsTests,TokenTests,TokenizerTests}
)
cd platform-tests
for name in "${classes[@]}"; do echo "src/test/java/${name//.//}.java"; done > "$work/test-sources"
javac --release 17 -g -proc:none -encoding UTF-8 -cp "$cp" -sourcepath "src/test/java:$sourcepath" \
    -d "$work/tests" /usr/libexec/eclipse-equinox/RunJupiter.java @"$work/test-sources"
for dir in "$PWD/src/test/resources" "$root"/{platform-tests,junit-platform-commons,junit-platform-engine,junit-platform-launcher,junit-jupiter-api}/src/testFixtures/resources; do
    if test -d "$dir"; then cp="$dir:$cp"; fi
done
java -cp "$work/tests:$cp" RunJupiter "${classes[@]}"
javac --release 17 -proc:none -encoding UTF-8 -cp "$cp" -d "$work/tests" "$1"
java -cp "$work/tests:$cp" VintageExecution
