#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
base=$PWD
ext=/usr/share/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="-Dmaven.ext.class.path=$base/target/smart.jar:$ext/xmvn.jar:$ext/kojan-xml.jar"
tools=/usr/share/java/javapackages-bootstrap
repo=$base/target/repo
mkmodel() {
    mkdir -p .xmvn .mvn
    cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories><repository>/usr/share/maven-metadata</repository>
<repository>/usr/share/javapackages-bootstrap/maven-metadata</repository></metadataRepositories></resolverSettings></configuration>
EOF
}
cp -r src/test/projects/aggregator-plugin target/aggregator
cd target/aggregator
mkmodel
testgroup=io.takari.maven.smartbuilder.tests
version=0.1-SNAPSHOT
cat > pom.xml <<EOF
<project><modelVersion>4.0.0</modelVersion><groupId>$testgroup</groupId><artifactId>aggregator-plugin</artifactId>
<version>$version</version><packaging>maven-plugin</packaging></project>
EOF
mkdir -p target/classes
javac --release 8 -proc:none -encoding UTF-8 -cp "/usr/share/maven/lib/*:$tools/*" -d target/classes src/main/java/smartbuilder/tests/aggregator/AggregatorMojo.java
plugin=$(unzip -p "$tools/maven-plugin-plugin.jar" META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
mvn -B -o -Dmaven.repo.local="$repo" -DgoalPrefix=aggregator "org.apache.maven.plugins:maven-plugin-plugin:$plugin:descriptor"
javap -v -classpath target/classes smartbuilder.tests.aggregator.AggregatorMojo | grep -A4 'org.apache.maven.plugins.annotations.Mojo('
python3 - <<'PYMOJO'
from xml.etree import ElementTree as E
p=E.parse('target/classes/META-INF/maven/plugin.xml')
print([(m.findtext('goal'), m.findtext('aggregator'), m.findtext('implementation')) for m in p.findall('./mojos/mojo')])
m=next(m for m in p.findall('./mojos/mojo') if m.findtext('goal')=='aggregate')
assert m.findtext('aggregator')=='true'
PYMOJO
dest=$repo/io/takari/maven/smartbuilder/tests/aggregator-plugin/$version
mkdir -p "$dest"
cp pom.xml "$dest/aggregator-plugin-$version.pom"
jar cf "$dest/aggregator-plugin-$version.jar" -C target/classes .
cd "$base"
cp -r src/test/projects/basic-it target/basic-it
cd target/basic-it
mkmodel
python3 - <<'PYPINS'
from pathlib import Path
from xml.etree import ElementTree as E
from zipfile import ZipFile
ns='http://maven.apache.org/POM/4.0.0';E.register_namespace('',ns);tag=lambda n:'{'+ns+'}'+n
m=E.parse('pom.xml')
p=E.SubElement(E.SubElement(E.SubElement(m.getroot(),tag('build')),tag('pluginManagement')),tag('plugins'))
for n in ['maven-resources-plugin','maven-compiler-plugin','maven-surefire-plugin','maven-jar-plugin']:
 with ZipFile('/usr/share/java/javapackages-bootstrap/'+n+'.jar') as z:ver=E.fromstring(z.read('META-INF/maven/plugin.xml')).findtext('version')
 plugin=E.SubElement(p,tag('plugin'));E.SubElement(plugin,tag('artifactId')).text=n;E.SubElement(plugin,tag('version')).text=ver
m.write('pom.xml',encoding='UTF-8',xml_declaration=True)
PYPINS
mvn -B -o -Dmaven.repo.local="$repo" --builder smart -T2 -Dmaven.profile=true package
mvn -B -o -Dmaven.repo.local="$repo" --builder smart -T2 clean package "$testgroup:aggregator-plugin:$version:aggregate"
test -f target/aggregator.txt
for module in basic-it-module-{a,b,c}; do test ! -e "$module/target/aggregator.txt"; done
