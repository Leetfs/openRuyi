#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
buildroot=$1
version=$2
work=$PWD/target/bytecode-check
mkdir -p "$work"/{.mvn,.xmvn,classes,repo}
sed "s|<path>/usr/share/|<path>$buildroot/usr/share/|g" \
    "$buildroot/usr/share/maven-metadata/extra-enforcer-rules.xml" > "$work/.xmvn/rules.xml"
cat > "$work/.xmvn/configuration.xml" <<EOF
<configuration><resolverSettings><metadataRepositories>
<repository>$work/.xmvn/rules.xml</repository><repository>/usr/share/maven-metadata</repository>
<repository>/usr/share/javapackages-bootstrap/maven-metadata</repository></metadataRepositories></resolverSettings></configuration>
EOF
cd "$work"
artifact=repo/org/openruyi/check/bytecode/1
mkdir -p "$artifact"
echo 'public class Java17 {}' > Java17.java
javac --release 17 -d classes Java17.java
jar cf "$artifact/bytecode-1.jar" -C classes .
cat > "$artifact/bytecode-1.pom" <<EOF
<project><modelVersion>4.0.0</modelVersion><groupId>org.openruyi.check</groupId><artifactId>bytecode</artifactId><version>1</version></project>
EOF
cat > pom.xml <<EOF
<project><modelVersion>4.0.0</modelVersion><groupId>org.openruyi.check</groupId><artifactId>consumer</artifactId><version>1</version>
<dependencies><dependency><groupId>org.openruyi.check</groupId><artifactId>bytecode</artifactId><version>1</version></dependency></dependencies>
<build><plugins><plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-enforcer-plugin</artifactId><version>3.6.2</version>
<dependencies><dependency><groupId>org.codehaus.mojo</groupId><artifactId>extra-enforcer-rules</artifactId><version>$version</version></dependency></dependencies>
<configuration><rules><enforceBytecodeVersion><maxJdkVersion>\${maxJdk}</maxJdkVersion></enforceBytecodeVersion></rules></configuration>
</plugin></plugins></build></project>
EOF
ext=/usr/share/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="${MAVEN_OPTS:-} -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
goal=org.apache.maven.plugins:maven-enforcer-plugin:3.6.2:enforce
mvn -B -o -Dmaven.repo.local="$PWD/repo" -DmaxJdk=17 "$goal"
if mvn -B -o -Dmaven.repo.local="$PWD/repo" -DmaxJdk=8 "$goal" > rejected.log 2>&1; then exit 1; fi
grep -E 'Found Banned Dependency: org.openruyi.check:bytecode|Restricted to .*Java17' rejected.log
