# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository
%global artifact_dir %{repo_dir}/org/vafer/%{name}/%{version}

Name:           jdependency
Version:        2.10
Release:        %autorelease
Summary:        Java class dependency analyzer
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/tcurdt/jdependency
VCS: git:https://github.com/tcurdt/jdependency
#!RemoteAsset:  sha256:cfa1e2e4fcad8340b01417c04c527124bf4ed19ca45b1f90adb003875124db32
Source0:        https://github.com/tcurdt/jdependency/archive/refs/tags/jdependency-2.10.tar.gz?/jdependency-2.10.tar.gz
#!RemoteAsset:  sha256:36274a190ec95d9cf07f509d72c5d38ba14b6c3efb7f1ea796af0a5f992b1b98
Source1:        https://github.com/apache/maven-shade-plugin/archive/refs/tags/maven-shade-plugin-3.5.1.tar.gz?/shade-3.5.1.tar.gz
#!RemoteAsset:  sha256:ba3c723d8b05e327dd4f74901bd2aefabde6718f8804e083c51164929eb58bf8
Source2:        https://archive.apache.org/dist/commons/collections/source/commons-collections4-4.5.0-src.tar.gz
#!RemoteAsset:  sha256:ab53f259ab5f6483d3dbb0235469e078d4a22cfd890771ab04f87db3a5b46067
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/vafer/jdependency/%{version}/jdependency-%{version}.pom
#!RemoteAsset:  sha256:293b6af371eee28b0ff16f0334ea19e20a3d5522143faa4b95b346855507879a
Source4:        https://gitlab.ow2.org/asm/asm/-/raw/4e6de6cb3dcddb00a2bbf7bbb9ee40f0c15281c5/LICENSE.txt
Source5:        BootstrapShade.java
BuildArch:      noarch
BuildRequires:  python3
BuildRequires:  java-25-openjdk-devel
BuildRequires:  maven >= 3.9.9
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(commons-io:commons-io) == 2.21.0
Provides:       mvn(org.vafer:jdependency) == %{version}
Requires:       java-25-openjdk

%description
jdependency analyzes class files and JARs to compute their directed dependency
graph. Maven Shade uses this graph to retain referenced classes when building
a minimized JAR.
%prep
%autosetup -n jdependency-jdependency-%{version}
cp %{SOURCE4} ASM-LICENSE.txt
cp %{_licensedir}/commons-io/NOTICE.txt Commons-IO-NOTICE.txt
mkdir shade collections
tar xf %{SOURCE2} --strip-components=1 -C collections
tar xf %{SOURCE1} --strip-components=1 -C shade
%build
mkdir -p target/classes target/test-classes target/shader
io=/usr/share/maven-repository/commons-io/commons-io/2.21.0/commons-io-2.21.0.jar
base=/usr/share/java/javapackages-bootstrap
cp="$io:/usr/share/maven/lib/*:$base/*"
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -encoding UTF-8 -proc:none -cp "$cp" -d target/classes @target/sources
mkdir -p target/classes/META-INF
cp LICENSE.txt target/classes/META-INF/LICENSE.txt
cp ASM-LICENSE.txt target/classes/META-INF/ASM-LICENSE.txt
cp Commons-IO-NOTICE.txt target/classes/META-INF/NOTICE.txt
jar cf target/plain.jar -C target/classes .
# Use the release's Shade engine and graph filter to retain its relocated public ASM superclass.
javac --release 8 -proc:none -encoding UTF-8 -sourcepath shade/src/main/java:collections/src/main/java -cp "target/plain.jar:$cp" -d target/shader %{SOURCE5}
java -cp "target/shader:target/plain.jar:$cp" BootstrapShade target/plain.jar target/jdependency.jar "$io" "$base"/asm{,-commons,-analysis,-tree,-util}.jar
%install
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 target/jdependency.jar %{buildroot}%{artifact_dir}/%{name}-%{version}.jar
install -m644 %{SOURCE3} %{buildroot}%{artifact_dir}/%{name}-%{version}.pom
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
 <artifact><groupId>org.vafer</groupId><artifactId>%{name}</artifactId><extension>jar</extension><version>%{version}</version>
 <path>%{artifact_dir}/%{name}-%{version}.jar</path></artifact>
 <artifact><groupId>org.vafer</groupId><artifactId>%{name}</artifactId><extension>pom</extension><version>%{version}</version>
 <path>%{artifact_dir}/%{name}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
# Verify graph traversal and bytecode reading using the upstream classpath, JAR and directory fixtures.
cp -r src/test/resources/. target/test-classes/
find src/test/java -name '*.java' | sort > target/test-sources
cp="target/jdependency.jar:/usr/share/java/javapackages-bootstrap/junit.jar:/usr/share/java/javapackages-bootstrap/hamcrest-core.jar"
javac --release 8 -encoding UTF-8 -proc:none -cp "$cp" -d target/test-classes @target/test-sources
# Execute the upstream resources target, then run all five input modes in its configured working directory.
python3 - <<'PYFIXTURES'
from pathlib import Path
from xml.etree import ElementTree as E
r=E.parse('pom.xml')
e=next(e for p in r.findall('./{*}build/{*}plugins/{*}plugin') if p.findtext('{*}artifactId')=='maven-antrun-plugin' for e in p.findall('./{*}executions/{*}execution') if e.findtext('{*}phase')=='process-test-resources')
t=e.find('./{*}configuration/{*}target'); assert t is not None
for node in t.iter():node.tag=node.tag.split('}')[-1]
t.set('name','prepare');root=E.Element('project',{'default':'prepare','basedir':'.'});root.append(t)
E.ElementTree(root).write('test-resources.xml',encoding='utf-8')
PYFIXTURES
java -cp '/usr/share/java/javapackages-bootstrap/ant.jar:/usr/share/java/javapackages-bootstrap/ant-launcher.jar' org.apache.tools.ant.Main \
    -Dtest.workingDirectory="$PWD/target/test-working-directory" -f test-resources.xml
base=$PWD
(cd target/test-working-directory && java -cp "$base/target/test-classes:$base/target/jdependency.jar:/usr/share/java/javapackages-bootstrap/junit.jar:/usr/share/java/javapackages-bootstrap/hamcrest-core.jar" \
    org.junit.runner.JUnitCore org.vafer.jdependency.ClazzpathUnitTestCase org.vafer.jdependency.DependencyUtilsTestCase org.vafer.jdependency.ClazzpathTestCase)
# Compare all public signatures with the released 2.10 JAR, including relocated parameter types.
types=$(sed 's|src/main/java/||;s|[.]java$||;s|/|.|g' target/sources | sort)
javap -classpath target/jdependency.jar -public $types > target/public-api
echo 'e697b36e5aa278b2265b26f8f25252d84e50961a7417c89c2d6cfc2c21a01b99  target/public-api' | sha256sum -c -
%files
%license LICENSE.txt ASM-LICENSE.txt Commons-IO-NOTICE.txt
%doc README.md
%{_datadir}/maven-metadata/jdependency.xml
%{repo_dir}/org/vafer/jdependency/

%changelog
%autochangelog
