#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
buildroot=$1
version=${2:-3.2.0}
work=$PWD/target/native-clean-check
mkdir -p "$work"/{.mvn,.xmvn,target/classes,keep}
sed "s|<path>/usr/share/|<path>$buildroot/usr/share/|g" \
    "$buildroot/usr/share/maven-metadata/maven-clean-plugin.xml" > "$work/.xmvn/clean.xml"
cat > "$work/.xmvn/configuration.xml" <<EOF
<configuration><resolverSettings><metadataRepositories>
<repository>$work/.xmvn/clean.xml</repository><repository>/usr/share/maven-metadata</repository>
<repository>/usr/share/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
plugin=
if test "$#" -ge 2; then
    plugin="<build><plugins><plugin><artifactId>maven-clean-plugin</artifactId><version>$version</version></plugin></plugins></build>"
fi
cat > "$work/pom.xml" <<EOF
<project><modelVersion>4.0.0</modelVersion><groupId>org.openruyi.check</groupId><artifactId>clean-consumer</artifactId><version>1</version>$plugin</project>
EOF
echo marker > "$work/target/classes/stale"
echo retained > "$work/keep/file"
cd "$work"
ext=/usr/share/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="${MAVEN_OPTS:-} -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
mvn -B -o -Dmaven.repo.local="$work/repo" clean
test ! -e target && grep -Fx retained keep/file
mvn -B -o -Dmaven.repo.local="$work/repo" org.apache.maven.plugins:maven-clean-plugin:$version:help -Ddetail -Dgoal=clean
