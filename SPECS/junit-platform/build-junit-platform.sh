#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
bootstrap=/usr/share/java/javapackages-bootstrap
native=/usr/share/maven-repository/biz/aQute/bnd
bnd=$(find "$native" -name '*.jar' ! -name '*-sources.jar' -printf '%p:')
mkdir -p build/tools build/bundles
javac --release 17 -proc:none -cp "$bnd$bootstrap/*" -d build/tools "$1"
deps="$bootstrap/apiguardian-api.jar:$bootstrap/opentest4j.jar"
for name in junit-platform-commons junit-platform-engine junit-platform-launcher junit-jupiter-api junit-jupiter-engine junit-vintage-engine; do
    version=1.12.2
    if [[ "$name" != junit-platform-* ]]; then version=5.12.2; fi
    if test "$name" = junit-vintage-engine; then deps="$bootstrap/junit.jar:$bootstrap/hamcrest-core.jar:$deps"; fi
    out="$PWD/build/$name/classes"; mkdir -p "$out"
    root="$PWD/$name/src"
    sources="$root/main/java"
    if test "$name" = junit-jupiter-api; then
        # The release source classifier contains JRE.java generated from the tag's JTE template.
        sources="$PWD/build/$name/java"; mkdir -p "$sources"
        (cd "$sources"; unzip -q "$2")
    fi
    find "$sources" ! -name module-info.java -name '*.java' | sort > "build/$name/sources"
    javac --release 8 -g -proc:none -encoding UTF-8 -cp "$deps" -d "$out" @"build/$name/sources"
    if test -d "$root/main/resources"; then cp -r "$root/main/resources/." "$out/"; fi
    if test -d "$root/main/java9"; then
        files="$PWD/build/$name/java9"; find "$root/main/java9" -name '*.java' | sort > "$files"
        dest="$out/META-INF/versions/9"; mkdir -p "$dest"
        javac --release 9 -g -proc:none -cp "$out:$deps" -d "$dest" @"$files"
    fi
    module="$(find "$root/module" -name module-info.java)"
    module_name=$(basename "$(dirname "$module")")
    javac --release 9 -proc:none --module-path "$deps" --patch-module "$module_name=$out" -d "$out" "$module"
    title=$(sed -n 's/^description = "\(.*\)"$/\1/p' "$name/$name.gradle.kts"); test -n "$title"
    jar="$PWD/build/bundles/$name.jar"
    java -cp "build/tools:$bnd$bootstrap/*" BuildPlatformBundle "$name" "$out" "$jar" "$deps" "$title" "$version"
    deps="$jar:$deps"
done
