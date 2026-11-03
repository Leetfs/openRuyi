# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bundle org.apache.felix.gogo.runtime
%global repo_dir %{_datadir}/maven-repository/org/apache/felix/%{bundle}/%{version}
%global framework %{_datadir}/maven-repository/org/eclipse/platform/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
%global xmvn_ext %{_datadir}/javapackages-bootstrap/maven/lib/ext

Name:           felix-gogo-runtime
Version:        1.1.6
Release:        %autorelease
Summary:        Apache Felix Gogo command processor for OSGi
License:        Apache-2.0
URL:            https://felix.apache.org/documentation/subprojects/apache-felix-gogo.html
VCS:            git:https://github.com/apache/felix-dev
#!RemoteAsset:  sha256:67719e8c2c347e4cb08ac1a4c3626cec53cfd8a1aeaffd60f25914a5e6ac563a
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/felix/%{bundle}/%{version}/%{bundle}-%{version}-source-release.zip
Source1:        GogoCheck.java
# Backport the Mockito argument matcher change from apache/felix-dev@679b07d5.
Patch0:         1000-Use-the-current-Mockito-argument-matcher.patch
# Backport the pipe tests from the same upstream commit.
Patch1:         1001-Use-the-upstream-Gogo-pipe-test-cases.patch
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.osgi) == 3.24.100
BuildRequires:  mvn(org.mockito:mockito-core) == 4.11.0
BuildRequires:  unzip
Provides:       mvn(org.apache.felix:org.apache.felix.gogo.runtime) == %{version}
Requires:       java-25-openjdk

%description
Gogo supplies the command processor, sessions, converters and command
annotations used by OSGi console services.

%prep
%autosetup -n %{bundle}-%{version} -p1

%build
mkdir -p target/classes/META-INF .xmvn repository
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -encoding UTF-8 -cp '%{framework}:%{bootstrap_java}/osgi.annotation.jar:%{bootstrap_java}/osgi.cmpn.jar' \
    -d target/classes @target/sources
install -m644 LICENSE NOTICE target/classes/META-INF/
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
  <repository>%{_datadir}/maven-metadata</repository>
  <repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
cat > bundle-pom.xml <<'XML'
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion><groupId>org.apache.felix</groupId>
  <artifactId>%{bundle}</artifactId><version>%{version}</version><name>Apache Felix Gogo Runtime</name>
  <dependencies>
    <dependency><groupId>org.eclipse.platform</groupId><artifactId>org.eclipse.osgi</artifactId><version>3.24.100</version><scope>system</scope><systemPath>%{framework}</systemPath></dependency>
    <dependency><groupId>org.osgi</groupId><artifactId>osgi.annotation</artifactId><version>8</version><scope>system</scope><systemPath>%{bootstrap_java}/osgi.annotation.jar</systemPath></dependency>
    <dependency><groupId>org.osgi</groupId><artifactId>osgi.cmpn</artifactId><version>7</version><scope>system</scope><systemPath>%{bootstrap_java}/osgi.cmpn.jar</systemPath></dependency>
  </dependencies>
  <build><plugins><plugin><groupId>org.apache.felix</groupId><artifactId>maven-bundle-plugin</artifactId><version>5.1.9.MBI</version>
    <configuration><instructions>
      <Bundle-SymbolicName>%{bundle}</Bundle-SymbolicName>
      <Export-Package>!org.apache.felix.gogo.runtime.util.function,org.apache.felix.gogo.runtime.*;version=%{version},org.apache.felix.service.command,org.apache.felix.service.command.annotations,org.apache.felix.service.threadio</Export-Package>
      <Import-Package>org.osgi.service.event;resolution:=optional;version="[1.3,2)",org.osgi.framework;version="[1.8,2)",org.osgi.util.tracker;version="[1.5,2)",*</Import-Package>
    </instructions></configuration>
  </plugin></plugins></build>
</project>
XML
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
mvn --offline --batch-mode -Dmaven.repo.local="$PWD/repository" -f bundle-pom.xml org.apache.felix:maven-bundle-plugin:5.1.9.MBI:bundle

%install
install -Dm644 target/%{bundle}-%{version}.jar %{buildroot}%{repo_dir}/%{bundle}-%{version}.jar
install -m644 pom.xml %{buildroot}%{repo_dir}/%{bundle}-%{version}.pom
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>org.apache.felix</groupId><artifactId>%{bundle}</artifactId><version>%{version}</version>
    <path>%{repo_dir}/%{bundle}-%{version}.jar</path></artifact>
  <artifact><groupId>org.apache.felix</groupId><artifactId>%{bundle}</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{repo_dir}/%{bundle}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
jar=%{buildroot}%{repo_dir}/%{bundle}-%{version}.jar
cp="$jar:%{framework}:%{bootstrap_java}/osgi.cmpn.jar:%{bootstrap_java}/junit.jar:%{bootstrap_java}/hamcrest-core.jar"
cp="$cp:%{_datadir}/maven-repository/org/mockito/mockito-core/4.11.0/mockito-core-4.11.0.jar"
for library in byte-buddy byte-buddy-agent objenesis asm asm-commons; do cp="$cp:%{bootstrap_java}/$library.jar"; done
mkdir -p target/test-classes
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 8 -encoding UTF-8 -cp "$cp" -d target/test-classes @target/test-sources
mapfile -t tests < <(find src/test/java -name '*.java' -exec grep -lE '^[[:space:]]*@Test\b' '{}' + | sort | sed -e 's|^src/test/java/||' -e 's|/|.|g' -e 's|\.java$||')
java -cp "target/test-classes:$cp" org.junit.runner.JUnitCore "${tests[@]}"
java -cp %{framework} %{SOURCE1} "$jar" "$PWD/target/framework-storage"

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/felix-gogo-runtime.xml
%{repo_dir}/

%changelog
%autochangelog
