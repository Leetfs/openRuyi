# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define jdk_home $(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
%global tool_home %{_datadir}/%{name}

Name:           javapackages-bootstrap
Version:        1.28.0
Release:        %autorelease
Summary:        Source bootstrap for Maven and Java build tools
License:        Apache-1.1 AND Apache-2.0 AND (Apache-2.0 OR EPL-2.0) AND (Apache-2.0 OR LGPL-2.0-or-later) AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND CPL-1.0 AND EPL-1.0 AND EPL-2.0 AND (EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0) AND LicenseRef-openRuyi-Public-Domain AND MIT AND Plexus AND SMLNJ AND Saxpath AND xpp
URL:            https://github.com/fedora-java/javapackages-bootstrap
#!RemoteAsset:  sha256:7ccdb1b9b1b9dea0ee58cc07e0babf6088b3e01fe5a9307c20936f41e3aec61f
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.zst
# The Fedora source RPM carries the component archives prepared by upstream's downstream.sh.
#!RemoteAsset:  sha256:6a78b22fbc5ae2151e683bbf862f326554e03e76dbac9f986ccd4cbb394384fe
Source1:        https://mirror.math.princeton.edu/pub/fedora/linux/releases/45/Everything/source/tree/Packages/j/%{name}-%{version}-2.fc45.src.rpm
Source2:        install-poms.py
# Set the published artifact ID in the Maven Plugin Plugin descriptor.
Patch2000:      2000-Write-the-Maven-Plugin-Plugin-artifact-ID.patch
# Build the Ant propertyfile task used to record JNI library metadata.
Patch2001:      2001-Build-the-Ant-propertyfile-task.patch
BuildArch:      noarch

BuildRequires:  byaccj
BuildRequires:  cpio
BuildRequires:  java-25-openjdk-devel
BuildRequires:  jurand
BuildRequires:  patch
BuildRequires:  python3
BuildRequires:  rpm
BuildRequires:  zstd
Provides:       javapackages-bootstrap(pom-install)
Requires:       java-25-openjdk-devel
Requires:       python3

%description
Java Packages Bootstrap builds Maven, XMvn, Ant and their Java libraries
from source with OpenJDK. Its private tool directory can be used to
bootstrap distributions that do not yet provide a Java build toolchain.

%prep
%autosetup -p1
mkdir component-sources archive
(cd component-sources && rpm2cpio %{SOURCE1} | cpio -id --quiet --no-absolute-filenames)
for descriptor in project/*.properties; do
    component=$(basename "$descriptor" .properties)
    mv "component-sources/$component.tar.zst" archive/
done
cp component-sources/%{name}-PACKAGE-LICENSING .
./downstream.sh prep-from-archive
# Apache Ant installs these four stylesheets alongside the JUnit report task.
ant_source=downstream/ant/src
ant_xsl=$ant_source/main/org/apache/tools/ant/taskdefs/optional/junit/xsl
install -d "$ant_xsl"
for style in junit-frames junit-noframes junit-frames-saxon junit-noframes-saxon; do
    install -m644 "$ant_source/etc/$style.xsl" "$ant_xsl/"
done

%build
JAVA_HOME=%{jdk_home} ./mbi.sh build -parallel

%install
JAVA_HOME=%{jdk_home} ./mbi.sh dist \
    -javaCmdPath=%{jdk_home}/bin/java \
    -basePackageName=%{name} \
    -installRoot=%{buildroot} \
    -mavenHomePath=%{tool_home}/maven \
    -metadataPath=%{tool_home}/maven-metadata \
    -artifactsPath=%{_datadir}/java \
    -launchersPath=%{_libexecdir}/%{name} \
    -licensesPath=%{_licensedir}/%{name}
install -p -m644 -t %{buildroot}%{_licensedir}/%{name} LICENSE NOTICE %{name}-PACKAGE-LICENSING

install -Dm755 %{SOURCE2} %{buildroot}%{_libexecdir}/%{name}/install-poms

%check
# Install a parent model and verify both its repository bytes and its indexed version.
mkdir -p build/pom-check
cat > build/pom-check/parent.pom <<'EOF'
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
<groupId>org.openruyi.check</groupId><artifactId>parent</artifactId><version>1</version><packaging>pom</packaging></project>
EOF
%{buildroot}%{_libexecdir}/%{name}/install-poms "$PWD/build/pom-check/root" %{_datadir} parent build/pom-check/parent.pom
cmp build/pom-check/parent.pom build/pom-check/root%{_datadir}/maven-repository/org/openruyi/check/parent/1/parent-1.pom
python3 - <<'PYCODE'
from xml.etree import ElementTree as ET
entry = ET.parse("build/pom-check/root%{_datadir}/maven-metadata/parent.xml").find("artifacts/artifact")
assert entry.findtext("groupId") == "org.openruyi.check"
assert entry.findtext("compatVersions/version") == "1"
assert entry.findtext("path") == "%{_datadir}/maven-repository/org/openruyi/check/parent/1/parent-1.pom"
PYCODE
# Exercise the bootstrapped Maven and Ant launchers.
JAVA_HOME=%{jdk_home} %{buildroot}%{_libexecdir}/%{name}/mvn --version
%{buildroot}%{_libexecdir}/%{name}/ant -version

mkdir -p build/ant-propertyfile
printf 'retained=original\n' > build/ant-propertyfile/jni.properties
cat > build/ant-propertyfile/build.xml <<'EOF'
<project default="jni-info"><target name="jni-info">
  <propertyfile file="jni.properties"><entry key="version" value="1.0"/><entry key="checksum" value="012345"/></propertyfile>
</target></project>
EOF
java -cp '%{buildroot}%{_datadir}/java/javapackages-bootstrap/ant.jar:%{buildroot}%{_datadir}/java/javapackages-bootstrap/ant-launcher.jar' \
    org.apache.tools.ant.Main -f build/ant-propertyfile/build.xml
grep -Fx 'retained=original' build/ant-propertyfile/jni.properties
grep -Fx 'version=1.0' build/ant-propertyfile/jni.properties
grep -Fx 'checksum=012345' build/ant-propertyfile/jni.properties

mkdir -p build/ant-junit-report/{input,result,html}
cat > build/ant-junit-report/input/TEST-ReportProbe.xml <<'EOF'
<testsuite name="ReportProbe" tests="1" failures="0" errors="0" skipped="0" time="0.1">
  <properties/><testcase name="passed" classname="ReportProbe" time="0.1"/>
</testsuite>
EOF
cat > build/ant-junit-report/build.xml <<'EOF'
<project default="report"><target name="report">
  <junitreport todir="result"><fileset dir="input" includes="TEST-*.xml"/>
    <report format="noframes" todir="html"/></junitreport>
</target></project>
EOF
jars=%{buildroot}%{_datadir}/java/javapackages-bootstrap
java -cp "$jars/ant.jar:$jars/ant-launcher.jar:$jars/ant-junit.jar:$jars/junit.jar" org.apache.tools.ant.Main -f build/ant-junit-report/build.xml
grep -F 'ReportProbe' build/ant-junit-report/html/junit-noframes.html > /dev/null

mkdir -p build/descriptor-check
(cd build/descriptor-check && %{jdk_home}/bin/jar -xf %{buildroot}%{_datadir}/java/%{name}/maven-plugin-plugin.jar META-INF/maven/plugin.xml)
grep -Eq '^  <artifactId>maven-plugin-plugin</artifactId>$' build/descriptor-check/META-INF/maven/plugin.xml

%files
%doc README.md
%license %{_licensedir}/javapackages-bootstrap/
%{tool_home}/
%{_datadir}/java/javapackages-bootstrap/
%{_libexecdir}/javapackages-bootstrap/

%changelog
%autochangelog
