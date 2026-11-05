#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
version=$1
for module in core maven; do
    out=build/$module
    classes=$out/classes
    mkdir -p "$classes" "$out/module"
    find "$module/src/main/java" -name '*.java' ! -name module-info.java | sort > "$out/sources"
    javac --release 8 -g -Xpkginfo:always -proc:none -encoding UTF-8 -cp build/core/classes -d "$classes" @"$out/sources"
    name=eu.maveniverse.domtrip
    if test "$module" = maven; then name=eu.maveniverse.domtrip.maven; fi
    javac --release 9 --module-path build/core/domtrip-core.jar --patch-module "$name=$classes" -d "$out/module" "$module/src/main/java/module-info.java"
    cp "$out/module/module-info.class" "$classes/"
    artifact=domtrip-$module
    meta=$classes/META-INF/maven/eu.maveniverse.maven.domtrip/$artifact
    mkdir -p "$meta"
    model=$2
    if test "$module" = maven; then model=$3; fi
    cp "$model" "$meta/pom.xml"
    printf 'artifactId=%s\ngroupId=eu.maveniverse.maven.domtrip\nversion=%s\n' "$artifact" "$version" > "$meta/pom.properties"
    cat > "$out/manifest" <<EOF
Specification-Title: eu.maveniverse.maven.domtrip:$artifact
Specification-Version: 1.5
Specification-Vendor: Maveniverse Team
Implementation-Title: eu.maveniverse.maven.domtrip:$artifact
Implementation-Version: $version
Implementation-Vendor: Maveniverse Team
EOF
    jar cfm "$out/$artifact.jar" "$out/manifest" -C "$classes" .
done
