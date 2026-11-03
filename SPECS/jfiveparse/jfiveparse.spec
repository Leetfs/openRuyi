# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
%global xmvn_ext %{_datadir}/javapackages-bootstrap/maven/lib/ext

Name:           jfiveparse
Version:        2.0.0
Release:        %autorelease
Summary:        HTML5 parser and serializer for Java
License:        Apache-2.0
URL:            https://github.com/digitalfondue/jfiveparse
VCS:            git:https://github.com/digitalfondue/jfiveparse
#!RemoteAsset:  sha256:119f1c6161823077a9e4d7c6055b8d627d5b60f9e56e680082e19d53340c3ae2
Source0:        https://github.com/digitalfondue/jfiveparse/archive/refs/tags/jfiveparse-%{version}.tar.gz
#!RemoteAsset:  sha256:839838e97c63b63c3aa73135646c007bef125fa135613c6500907efcd70d4f1f
Source1:        https://github.com/html5lib/html5lib-tests/archive/e4463205ac3c4500e1379103daadfdcfe5e33af5.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  unzip
Provides:       mvn(ch.digitalfondue.jfiveparse:jfiveparse) == %{version}
Requires:       java-25-openjdk
# The published Maven model imports the Jupiter and Platform versions from this BOM.
Requires:       mvn(org.junit:junit-bom:pom:) == 5.12.2

%description
JFiveParse implements HTML tokenization, tree construction and serialization.
It includes a DOM interface and supports conversion to the W3C DOM.

%prep
%autosetup -n jfiveparse-jfiveparse-%{version}
tar -xf %{SOURCE1} --strip-components=1 -C src/test/resources/html5lib-tests

%build
mkdir -p target/classes
find src/main/java -name '*.java' | sort > target/sources
javac --release 17 -encoding UTF-8 -d target/classes @target/sources
cp -a src/main/resources/. target/classes/
mkdir -p target/classes/META-INF/maven/ch.digitalfondue.jfiveparse/jfiveparse
install -m644 pom.xml target/classes/META-INF/maven/ch.digitalfondue.jfiveparse/jfiveparse/pom.xml
printf 'groupId=ch.digitalfondue.jfiveparse\nartifactId=jfiveparse\nversion=%{version}\n' > target/classes/META-INF/maven/ch.digitalfondue.jfiveparse/jfiveparse/pom.properties
jar --create --file target/%{name}.jar --module-version %{version} -C target/classes .

%install
install -Dm644 pom.xml %{buildroot}%{_datadir}/maven-repository/ch/digitalfondue/jfiveparse/jfiveparse/%{version}/jfiveparse-%{version}.pom
install -m644 target/%{name}.jar %{buildroot}%{_datadir}/maven-repository/ch/digitalfondue/jfiveparse/jfiveparse/%{version}/jfiveparse-%{version}.jar
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>ch.digitalfondue.jfiveparse</groupId><artifactId>jfiveparse</artifactId><version>%{version}</version><extension>jar</extension>
    <path>%{_datadir}/maven-repository/ch/digitalfondue/jfiveparse/jfiveparse/%{version}/jfiveparse-%{version}.jar</path></artifact>
  <artifact><groupId>ch.digitalfondue.jfiveparse</groupId><artifactId>jfiveparse</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/ch/digitalfondue/jfiveparse/jfiveparse/%{version}/jfiveparse-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
jar --describe-module --file target/%{name}.jar | grep -F 'ch.digitalfondue.jfiveparse@%{version}'
# The three Jazzer fuzz targets in FuzzTest are disabled by upstream.
mkdir -p target/test-classes .xmvn
find src/test/java -name '*.java' ! -name 'FuzzTest.java' | sort > target/test-sources
javac --release 17 -encoding UTF-8 -cp 'target/classes:%{bootstrap_java}/*' -d target/test-classes @target/test-sources
if test -d src/test/resources; then cp -a src/test/resources/. target/test-classes/; fi
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
  <repository>%{_datadir}/maven-metadata</repository>
  <repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
cat > openruyi-tests.pom <<EOF
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion><groupId>org.openruyi.build</groupId><artifactId>%{name}-tests</artifactId><version>1</version>
  <dependencies>
    <dependency><groupId>org.junit.jupiter</groupId><artifactId>junit-jupiter</artifactId><version>SYSTEM</version><scope>test</scope></dependency>
    <dependency><groupId>com.google.code.gson</groupId><artifactId>gson</artifactId><version>SYSTEM</version><scope>test</scope></dependency>
    <dependency><groupId>org.jsoup</groupId><artifactId>jsoup</artifactId><version>SYSTEM</version><scope>test</scope></dependency>
  </dependencies>
</project>
EOF
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
surefire=$(unzip -p %{bootstrap_java}/maven-surefire-plugin.jar META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
test -n "$surefire"
mvn -B --offline -f openruyi-tests.pom -Dmaven.repo.local="$PWD/target/test-repository" \
    -DfailIfNoTests=true "org.apache.maven.plugins:maven-surefire-plugin:$surefire:test"

%files
%license LICENSE.txt
%{_datadir}/maven-metadata/jfiveparse.xml
%{_datadir}/maven-repository/ch/digitalfondue/jfiveparse/jfiveparse/

%changelog
%autochangelog
