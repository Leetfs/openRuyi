#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
base=$PWD; bootstrap=/usr/share/java/javapackages-bootstrap
classpath=$(cat target/powermock-classpath)
mkdir -p target/test-fixtures
# The configuration tests change and restore the environment using this upstream rule.
rule=$(find target/system-rules -name EnvironmentVariables.java)
javac --release 8 -proc:none -cp "$bootstrap/junit.jar" -d target/test-fixtures "$rule"
classpath="$base/target/test-fixtures:$classpath"
for name in powermock-core powermock-module-junit4-common powermock-module-junit4; do
    dir=$(find . -type d -name "$name" | grep -E '^\./(powermock-core|powermock-modules/[^/]+)$')
    out="$base/target/tests/$name"; mkdir -p "$out"
    find "$dir/src/test/java" -name '*.java' | sort > "$out/sources"
    javac --release 8 -g -proc:none -encoding UTF-8 -cp "$classpath" -d "$out" @"$out/sources"
    if test -d "$dir/src/test/resources"; then cp -r "$dir/src/test/resources/." "$out/"; fi
    # The abstract parameterized transformer superclass is inherited by its concrete test classes.
    tests=$(find "$dir/src/test/java" -name '*Test.java' ! -name AbstractBaseMockTransformerTest.java |
        sed "s|^$dir/src/test/java/||;s|/|.|g;s|[.]java$||" | sort)
    java -Xmx768m --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED \
        --add-opens=java.base/java.util=ALL-UNNAMED -cp "$out:$classpath" org.junit.runner.JUnitCore $tests
done
javac --release 8 -proc:none -cp "$classpath" -d target/test-fixtures "$1"
java --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED \
    --add-opens=java.base/java.util=ALL-UNNAMED -cp "$classpath" org.junit.runner.JUnitCore StaticServiceTest
# The Maven resolver must see the modules' published transitive dependencies.
model="$base/target/model-check"
mkdir -p "$model"/{metadata,.xmvn,repo}
for file in /usr/share/maven-metadata/*.xml; do
    case "$(basename "$file")" in powermock.xml|powermock-reflect.xml) continue ;; esac
    ln -s "$file" "$model/metadata/$(basename "$file")"
done
python3 - "$2" "$model" <<'PY'
from pathlib import Path
import xml.etree.ElementTree as ET
import sys
root,model=map(Path,sys.argv[1:])
for src in (root/"usr/share/maven-metadata").glob("powermock*.xml"):
    tree=ET.parse(src)
    for path in tree.findall(".//artifact/path"):
        path.text=str(root/Path(path.text).relative_to("/"))
    tree.write(model/"metadata"/src.name, encoding="utf-8")
PY
cd "$model"
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
<repository>$model/metadata</repository><repository>/usr/share/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
cat > pom.xml <<'EOF'
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
<groupId>org.openruyi.check</groupId><artifactId>powermock-consumer</artifactId><version>1</version><dependencies>
<dependency><groupId>org.powermock</groupId><artifactId>powermock-module-junit4</artifactId><version>2.0.9</version></dependency>
<dependency><groupId>org.powermock</groupId><artifactId>powermock-api-mockito2</artifactId><version>2.0.9</version></dependency>
</dependencies></project>
EOF
/usr/libexec/javapackages-bootstrap/mvn -B -o -Dmaven.repo.local="$model/repo" \
    org.apache.maven.plugins:maven-dependency-plugin:build-classpath -Dmdep.outputFile="$model/runtime"
for artifact in powermock-module-junit4-common powermock-api-support powermock-core powermock-reflect; do
    test "$(tr ':' '\n' < runtime | grep -c "/$artifact-2.0.9.jar$")" = 1
done
