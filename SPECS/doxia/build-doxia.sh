#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
version=$1
index_source=$(realpath "$2")
root=$PWD
generator=$(realpath "$3")
repo=/usr/share/maven-repository
bootstrap=/usr/share/java/javapackages-bootstrap
cp="$repo/org/apache/maven/doxia/doxia-sink-api/$version/doxia-sink-api-$version.jar:$repo/org/apache/commons/commons-lang3/3.20.0/commons-lang3-3.20.0.jar:$repo/org/apache/commons/commons-text/1.12.0/commons-text-1.12.0.jar:$repo/commons-io/commons-io/2.21.0/commons-io-2.21.0.jar"
for artifact in javax.inject slf4j-api plexus-utils plexus-xml; do
    cp="$cp:$bootstrap/$artifact.jar"
done
index_cp="$bootstrap/org.eclipse.sisu.inject.jar:$bootstrap/javax.inject.jar:$bootstrap/guice.jar:$bootstrap/asm.jar"
mkdir -p target/tools
python3 "$generator" "$root/doxia-modules/doxia-module-fml" "$root/target/model-repository"
javac -cp "$index_cp" -d target/tools "$index_source"
for module in doxia-core doxia-modules/doxia-module-apt doxia-modules/doxia-module-fml doxia-modules/doxia-module-xdoc doxia-modules/doxia-module-xhtml5; do
    (
        cd "$module"
        name=$(basename "$module")
        mkdir -p target/classes/META-INF/maven/org.apache.maven.doxia/"$name"
        find src/main/java -name '*.java' | sort > target/sources
        if test -d target/generated-sources/modello; then
            find target/generated-sources/modello -name '*.java' | sort >> target/sources
        fi
        javac --release 8 -proc:none -encoding UTF-8 -g -cp "$cp" -d target/classes @target/sources
        if test -d src/main/resources; then cp -r src/main/resources/. target/classes/; fi
        java -cp "$root/target/tools:target/classes:$index_cp:$cp" IndexNative target/classes
        meta=target/classes/META-INF/maven/org.apache.maven.doxia/$name
        cp pom.xml "$meta/"
        printf 'groupId=org.apache.maven.doxia\nartifactId=%s\nversion=%s\n' "$name" "$version" > "$meta/pom.properties"
        cp "$root/LICENSE" "$root/NOTICE" target/classes/META-INF/
        jar cf "target/$name.jar" -C target/classes .
    )
    cp="$root/$module/target/$(basename "$module").jar:$cp"
done
printf '%s\n' "$cp" > target/production-classpath
