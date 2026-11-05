#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
version=$1
root=$PWD
repo=/usr/share/maven-repository
bootstrap=/usr/share/java/javapackages-bootstrap
cp=$(cat target/production-classpath)
for group in org/junit/jupiter org/junit/platform; do
    jars=$(find "$repo/$group" -name '*-5.12.2.jar' -o -name '*-1.12.2.jar' | paste -sd:)
    cp="$cp:$jars"
done
cp="$cp:$repo/org/codehaus/plexus/plexus-testing/2.1.0/plexus-testing-2.1.0.jar"
for artifact in org.eclipse.sisu.inject org.eclipse.sisu.plexus javax.inject guice guava aopalliance javax.annotation-api slf4j-simple plexus-classworlds plexus-container-default plexus-component-annotations apiguardian-api opentest4j failureaccess junit-jupiter-params hamcrest-core xmlunit-core xmlunit-matchers asm asm-commons; do
    cp="$cp:$bootstrap/$artifact.jar"
done
# Assemble the upstream document archive used by the XDoc schema validation tests.
documents=doxia-test-docs/target/classes
mkdir -p "$documents/META-INF/maven/org.apache.maven.doxia/doxia-test-docs"
cp -r doxia-test-docs/src/main/resources/. "$documents/"
cp doxia-test-docs/pom.xml "$documents/META-INF/maven/org.apache.maven.doxia/doxia-test-docs/"
printf 'groupId=org.apache.maven.doxia\nartifactId=doxia-test-docs\nversion=%s\n' "$version" > "$documents/META-INF/maven/org.apache.maven.doxia/doxia-test-docs/pom.properties"
jar cf "target/doxia-test-docs-$version.jar" -C "$documents" .
cp="$cp:$root/target/doxia-test-docs-$version.jar"
mkdir -p target/launcher
javac -cp "$cp" -d target/launcher /usr/libexec/eclipse-equinox/RunJupiter.java
cp="$root/target/launcher:$cp"
for module in doxia-core doxia-modules/doxia-module-apt doxia-modules/doxia-module-fml doxia-modules/doxia-module-xdoc doxia-modules/doxia-module-xhtml5; do
    (
        cd "$module"
        mkdir -p target/test-classes
        find src/test/java -name '*.java' | sort > target/test-sources
        javac --release 11 -proc:none -encoding UTF-8 -g -cp "$cp" -d target/test-classes @target/test-sources
        cp -r src/test/resources/. target/test-classes/
        tests=$(find src/test/java -name '*Test.java' -o -name 'Test*.java' | sed 's|src/test/java/||;s|[.]java$||;s|/|.|g' | sort)
        java -Dbasedir="$PWD" -cp "target/test-classes:$cp" RunJupiter $tests
    )
    cp="$root/$module/target/test-classes:$cp"
done
