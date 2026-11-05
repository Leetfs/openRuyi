#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
root=$1
version=$2
metadata=maven-surefire
if test "$version" = 3.5.6; then metadata=maven-surefire-3.5.6; fi
work=$(mktemp -d "$PWD/consumer-XXXX")
cd "$work"
mkdir -p .xmvn repo target/test-classes
cp -as "$root/usr/share/maven-repository/." repo/
sed "s|<path>/usr|<path>$root/usr|g" "$root/usr/share/maven-metadata/$metadata.xml" > .xmvn/installed.xml
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
<repository>$PWD/.xmvn/installed.xml</repository><repository>/usr/share/maven-metadata</repository>
<repository>/usr/share/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
cat > pom.xml <<EOF
<project><modelVersion>4.0.0</modelVersion><groupId>org.openruyi.check</groupId><artifactId>test-fork</artifactId><version>1</version>
<dependencies>
<dependency><groupId>junit</groupId><artifactId>junit</artifactId><version>4.13.2</version><scope>test</scope></dependency>
<dependency><groupId>org.junit.jupiter</groupId><artifactId>junit-jupiter-engine</artifactId><version>5.12.2</version><scope>test</scope></dependency>
<dependency><groupId>org.junit.vintage</groupId><artifactId>junit-vintage-engine</artifactId><version>5.12.2</version><scope>test</scope></dependency>
</dependencies><build><plugins>
EOF
for plugin in maven-surefire-plugin maven-failsafe-plugin; do
    cat >> pom.xml <<EOF
<plugin><groupId>org.apache.maven.plugins</groupId><artifactId>$plugin</artifactId><version>$version</version>
<dependencies><dependency><groupId>org.apache.maven.surefire</groupId><artifactId>surefire-junit-platform</artifactId><version>$version</version></dependency></dependencies>
</plugin>
EOF
done
echo '</plugins></build></project>' >> pom.xml
cat > UnitTest.java <<'JAVA'
public class UnitTest {
    @org.junit.Test public void vintage() { org.junit.Assert.assertEquals(4, 2 + 2); }
}
JAVA
cat > JupiterTest.java <<'JAVA'
public class JupiterTest {
    @org.junit.jupiter.api.Test void jupiter() { org.junit.jupiter.api.Assertions.assertTrue(true); }
}
JAVA
cat > BrokenIT.java <<'JAVA'
public class BrokenIT {
    @org.junit.jupiter.api.Test void fails() { org.junit.jupiter.api.Assertions.fail("integration sentinel"); }
}
JAVA
cp=/usr/share/java/javapackages-bootstrap/junit.jar:/usr/share/java/javapackages-bootstrap/apiguardian-api.jar
cp="$cp:/usr/share/maven-repository/org/junit/jupiter/junit-jupiter-api/5.12.2/junit-jupiter-api-5.12.2.jar"
javac --release 8 -g -proc:none -cp "$cp" -d target/test-classes UnitTest.java JupiterTest.java BrokenIT.java
mvn_test() { mvn -B -o -Dmaven.repo.local="$PWD/repo" "$@"; }
mvn_test "org.apache.maven.plugins:maven-surefire-plugin:$version:help" -Ddetail -Dgoal=test > surefire-help.log
grep -F 'surefire:test' surefire-help.log
mvn_test "org.apache.maven.plugins:maven-failsafe-plugin:$version:help" -Ddetail -Dgoal=verify > failsafe-help.log
grep -F 'failsafe:verify' failsafe-help.log
mvn_test "org.apache.maven.plugins:maven-surefire-plugin:$version:test" > unit.log
mvn_test "org.apache.maven.plugins:maven-failsafe-plugin:$version:integration-test" > integration.log
if mvn_test "org.apache.maven.plugins:maven-failsafe-plugin:$version:verify" > verify.log 2>&1; then exit 1; fi
python3 - <<'PY'
from pathlib import Path
from xml.etree import ElementTree as ET

for directory, name, expected in [("surefire", "UnitTest", "0"), ("surefire", "JupiterTest", "0"),
                                  ("failsafe", "BrokenIT", "1")]:
    suite = ET.parse(Path("target") / (directory + "-reports") / ("TEST-" + name + ".xml")).getroot()
    assert suite.get("tests") == "1" and suite.get("failures") == expected and suite.get("errors") == "0"
    if expected == "1":
        assert "integration sentinel" in suite.find(".//failure").get("message")
summary = ET.parse("target/failsafe-reports/failsafe-summary.xml").getroot()
assert summary.findtext("completed") == "1" and summary.findtext("failures") == "1"
PY
