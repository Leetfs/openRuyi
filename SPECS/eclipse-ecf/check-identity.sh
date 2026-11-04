#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
application=$1
repo=/usr/share/maven-repository
platform=$repo/org/eclipse/platform
bootstrap=/usr/share/java/javapackages-bootstrap
base=$PWD/build
tests=tests/bundles/org.eclipse.ecf.tests.core/src
mkdir -p "$base/test/classes" "$base/test/configuration"
jars=()
for package in eclipse-equinox eclipse-equinox-services eclipse-core-jobs eclipse-core-runtime eclipse-core-net jna; do
    while IFS= read -r jar; do
        case "$jar" in
            *-sources.jar|*/org.eclipse.osgi/*|*/org.eclipse.osgi.compatibility.state/*) ;;
            "$repo"/*.jar) jars+=("$jar");;
        esac
    done < <(rpm -ql "$package")
done
framework="$platform/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar"
launcher="$platform/org.eclipse.equinox.launcher/1.7.100/org.eclipse.equinox.launcher-1.7.100.jar"
for coord in org.osgi.util.function/1.2.0 org.osgi.util.promise/1.3.0 org.osgi.service.component/1.5.1 org.osgi.service.prefs/1.1.2; do
    jars+=("$repo/org/osgi/$coord/${coord%%/*}-${coord##*/}.jar")
done
jars+=("$repo/org/apache/felix/org.apache.felix.scr/2.2.18/org.apache.felix.scr-2.2.18.jar")
jars+=("$base"/bundles/*.jar)
cp=$(IFS=:; echo "${jars[*]}")
javac --release 17 -proc:none -cp "$cp:$framework:$bootstrap/junit.jar" -d "$base/test/classes" \
    "$tests/org/eclipse/ecf/internal/tests/core/Activator.java" "$tests"/org/eclipse/ecf/tests/core/identity/*.java "$application"
cp "$bootstrap"/{junit.jar,hamcrest-core.jar} "$base/test/classes/"
cat > "$base/test/manifest.mf" <<'MF'
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-SymbolicName: org.eclipse.ecf.tests.core;singleton:=true
Bundle-Version: 1.2.0
Bundle-Activator: org.eclipse.ecf.internal.tests.core.Activator
Bundle-ClassPath: .,junit.jar,hamcrest-core.jar
Require-Bundle: org.eclipse.ecf,org.eclipse.equinox.app,org.eclipse.equinox.common
Import-Package: org.osgi.framework,org.osgi.util.tracker
MF
cat > "$base/test/classes/plugin.xml" <<'XML'
<?xml version="1.0" encoding="UTF-8"?>
<plugin><extension point="org.eclipse.core.runtime.applications" id="identity">
<application><run class="org.eclipse.ecf.tests.core.identity.IdentityApplication"/></application>
</extension></plugin>
XML
jar cfm "$base/test/identity-tests.jar" "$base/test/manifest.mf" -C "$base/test/classes" .
jars+=("$base/test/identity-tests.jar")
entries=()
for jar in "${jars[@]}"; do entries+=("reference:file:$jar@start"); done
(IFS=,; printf 'osgi.bundles=%s\nosgi.bundles.defaultStartLevel=4\n' "${entries[*]}") > "$base/test/configuration/config.ini"
cases=()
for file in "$tests"/org/eclipse/ecf/tests/core/identity/*Test.java; do
    if ! grep -q 'public abstract class' "$file"; then cases+=("$(basename "$file" .java)"); fi
done
java -Dosgi.framework="file:$framework" -jar "$launcher" -nosplash -consoleLog -configuration "$base/test/configuration" \
    -data "$base/test/workspace" -application org.eclipse.ecf.tests.core.identity "${cases[@]}" | tee "$base/test/results.log"
grep -E 'ECF identity suite ran [1-9][0-9]* tests with 0 failures' "$base/test/results.log"
