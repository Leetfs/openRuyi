#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
root=$PWD
buildroot=$1
version=0.8.14
native="$buildroot/usr/share/maven-repository/org/jacoco"
work=$root/build/coverage-test
mkdir -p "$work"
cp='/usr/share/java/javapackages-bootstrap/*'
for module in org.jacoco.core org.jacoco.report org.jacoco.agent; do
    cp="$native/$module/$version/$module-$version.jar:$cp"
done
cp="$root/org.jacoco.agent.rt/target/classes:$cp"
suites=(org.jacoco.core.test org.jacoco.report.test org.jacoco.agent.rt.test org.jacoco.agent.test)
for suite in "${suites[@]}"; do
    output="$work/$suite"
    mkdir -p "$output"
    find "$suite/src" -name '*.java' | sort > "$output/sources"
    javac --release 17 -proc:none -encoding UTF-8 -cp "$cp" -d "$output" @"$output/sources"
    (cd "$suite/src"; find . -type f ! -name '*.java' -exec cp --parents '{}' "$output/" \;)
    cp="$output:$cp"
done
for suite in "${suites[@]}"; do
    (cd "$suite"; tests=$(find src -name '*Test.java' | sed 's|src/||;s|[.]java$||;s|/|.|g' | sort)
     java -cp "$cp" org.junit.runner.JUnitCore $tests)
done
# Exercise the packaged plugin in a cold native Maven repository.
mkdir -p "$work/consumer/"{.mvn,.xmvn,target/classes,src/main/java}
cd "$work/consumer"
repo="$PWD/repo"
sed "s|<path>/usr/share/|<path>$buildroot/usr/share/|g" "$buildroot/usr/share/maven-metadata/jacoco.xml" > .xmvn/staged.xml
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories><repository>$PWD/.xmvn/staged.xml</repository>
<repository>/usr/share/maven-metadata</repository><repository>/usr/share/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
cat > pom.xml <<'EOF'
<project><modelVersion>4.0.0</modelVersion><groupId>org.openruyi.check</groupId><artifactId>coverage-consumer</artifactId><version>1</version></project>
EOF
cat > src/main/java/Measured.java <<'JAVA'
public class Measured {
    public static int answer(boolean flag) { return flag ? 41 : 17; }
    public static void main(String[] args) { if (answer(true) != 41) throw new AssertionError(); }
}
JAVA
javac -g -d target/classes src/main/java/Measured.java
cp target/classes/Measured.class original.class
ext=/usr/share/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="${MAVEN_OPTS:-} -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
mvn_check() { mvn -B -o -Dmaven.repo.local="$repo" "org.jacoco:jacoco-maven-plugin:$version:$1"; }
agent="$native/org.jacoco.agent/$version/org.jacoco.agent-$version-runtime.jar"
mvn_check prepare-agent > agent-goal.log
grep -F -- '-javaagent:' agent-goal.log
java "-javaagent:$agent=destfile=$PWD/target/jacoco.exec" -cp target/classes Measured
mvn_check report
python3 - <<'PY'
from pathlib import Path
from xml.etree import ElementTree as ET
cls=ET.parse(Path("target/site/jacoco/jacoco.xml")).find(".//class[@name='Measured']")
assert cls is not None and int(cls.find("counter[@type='INSTRUCTION']").get("covered")) > 0
PY
mvn_check instrument
if cmp -s original.class target/classes/Measured.class; then exit 1; fi
java -Djacoco-agent.destfile="$PWD/target/offline.exec" -cp "target/classes:$agent" Measured
test -s target/offline.exec
mvn_check restore-instrumented-classes
cmp original.class target/classes/Measured.class
