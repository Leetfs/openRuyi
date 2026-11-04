#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
buildroot=$1
w=$PWD/build/provider-consumer
mkdir -p "$w"/{.mvn,.xmvn,target/test-classes}
cd "$w"
for metadata in surefire-shadefire surefire-shadefire-models; do
    sed "s|<path>/usr/share/|<path>$buildroot/usr/share/|g" "$buildroot/usr/share/maven-metadata/$metadata.xml" > ".xmvn/$metadata.xml"
done
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
<repository>$w/.xmvn/surefire-shadefire.xml</repository><repository>$w/.xmvn/surefire-shadefire-models.xml</repository>
<repository>/usr/share/maven-metadata</repository><repository>/usr/share/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
jp=/usr/share/java/javapackages-bootstrap
version=$(unzip -p "$jp/maven-surefire-plugin.jar" META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
cat > pom.xml <<EOF
<project><modelVersion>4.0.0</modelVersion><groupId>org.openruyi.check</groupId><artifactId>provider-test</artifactId><version>1</version>
<dependencies><dependency><groupId>org.junit.jupiter</groupId><artifactId>junit-jupiter-api</artifactId><version>5.12.2</version><scope>test</scope></dependency>
<dependency><groupId>org.junit.jupiter</groupId><artifactId>junit-jupiter-engine</artifactId><version>5.12.2</version><scope>test</scope></dependency></dependencies>
<build><plugins><plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-surefire-plugin</artifactId><version>$version</version>
<dependencies><dependency><groupId>org.apache.maven.surefire</groupId><artifactId>surefire-shadefire</artifactId><version>3.5.2</version></dependency></dependencies></plugin></plugins></build></project>
EOF
cat > PassingTest.java <<'EOF'
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
public class PassingTest { @Test void adds() { assertEquals(42, 6 * 7); } }
EOF
cat > FailingTest.java <<'EOF'
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.fail;
public class FailingTest { @Test void propagates() { fail("intentional provider failure"); } }
EOF
javac --release 8 -proc:none -cp "$jp/*" -d target/test-classes PassingTest.java FailingTest.java
ext=/usr/share/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="${MAVEN_OPTS:-} -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
run() { mvn -B -o -Dmaven.repo.local="$w/repo" -DfailIfNoTests=true -Dtest="$1" "org.apache.maven.plugins:maven-surefire-plugin:$version:test"; }
run PassingTest > passing.log
grep -F 'Using configured provider org.apache.maven.shadefire.surefire.junitplatform.JUnitPlatformProvider' passing.log
if run FailingTest > failing.log 2>&1; then exit 1; fi
python3 - <<'PY'
from pathlib import Path
from xml.etree import ElementTree
root=Path("target/surefire-reports")
for name,expected in [("PassingTest","0"),("FailingTest","1")]:
    suite=ElementTree.parse(root/("TEST-"+name+".xml")).getroot()
    assert suite.get("tests")=="1" and suite.get("failures")==expected
    if expected=="1": assert "intentional provider failure" in suite.find(".//failure").get("message")
PY
