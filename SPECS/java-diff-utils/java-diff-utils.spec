# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
%global xmvn_ext %{_datadir}/javapackages-bootstrap/maven/lib/ext

Name:           java-diff-utils
Version:        4.17
Release:        %autorelease
Summary:        Diff and patch operations for Java
License:        Apache-2.0
URL:            https://java-diff-utils.github.io/java-diff-utils/
VCS:            git:https://github.com/java-diff-utils/java-diff-utils
#!RemoteAsset:  sha256:860162748b8e3db9302e65c0aacce4da7931fa4aca31d560b1ab991421ebabdd
Source0:        https://github.com/java-diff-utils/java-diff-utils/archive/refs/tags/java-diff-utils-parent-%{version}.tar.gz
Source1:        java-diff-utils.mf
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  unzip
Provides:       mvn(io.github.java-diff-utils:java-diff-utils) == %{version}
Provides:       mvn(io.github.java-diff-utils:java-diff-utils-parent:pom:) == %{version}
Requires:       java-25-openjdk

%description
Java Diff Utils compares sequences and text files, creates and applies unified
diffs, and can generate side-by-side views of changes.

%prep
%autosetup -n java-diff-utils-java-diff-utils-parent-%{version}

%build
cd java-diff-utils
mkdir -p target/classes
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -encoding UTF-8 -d target/classes @target/sources
mkdir -p target/classes/META-INF/maven/io.github.java-diff-utils/java-diff-utils
install -m644 pom.xml target/classes/META-INF/maven/io.github.java-diff-utils/java-diff-utils/pom.xml
printf 'groupId=io.github.java-diff-utils\nartifactId=java-diff-utils\nversion=%{version}\n' > target/classes/META-INF/maven/io.github.java-diff-utils/java-diff-utils/pom.properties
jar --create --file target/%{name}.jar --manifest %{SOURCE1} -C target/classes .

%install
install -Dm644 java-diff-utils/pom.xml %{buildroot}%{_datadir}/maven-repository/io/github/java-diff-utils/java-diff-utils/%{version}/java-diff-utils-%{version}.pom
install -m644 java-diff-utils/target/%{name}.jar %{buildroot}%{_datadir}/maven-repository/io/github/java-diff-utils/java-diff-utils/%{version}/java-diff-utils-%{version}.jar
install -Dm644 pom.xml %{buildroot}%{_datadir}/maven-repository/io/github/java-diff-utils/java-diff-utils-parent/%{version}/java-diff-utils-parent-%{version}.pom
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>io.github.java-diff-utils</groupId><artifactId>java-diff-utils</artifactId><version>%{version}</version><extension>jar</extension>
    <path>%{_datadir}/maven-repository/io/github/java-diff-utils/java-diff-utils/%{version}/java-diff-utils-%{version}.jar</path></artifact>
  <artifact><groupId>io.github.java-diff-utils</groupId><artifactId>java-diff-utils</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/io/github/java-diff-utils/java-diff-utils/%{version}/java-diff-utils-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
  <artifact><groupId>io.github.java-diff-utils</groupId><artifactId>java-diff-utils-parent</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/io/github/java-diff-utils/java-diff-utils-parent/%{version}/java-diff-utils-parent-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
cd java-diff-utils
mkdir -p target/test-classes .xmvn
find src/test/java -name '*.java' | sort > target/test-sources
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
    <dependency><groupId>org.assertj</groupId><artifactId>assertj-core</artifactId><version>SYSTEM</version><scope>test</scope></dependency>
  </dependencies>
</project>
EOF
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
surefire=$(unzip -p %{bootstrap_java}/maven-surefire-plugin.jar META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
test -n "$surefire"
mvn -B --offline -f openruyi-tests.pom -Dmaven.repo.local="$PWD/target/test-repository" \
    -DfailIfNoTests=true "org.apache.maven.plugins:maven-surefire-plugin:$surefire:test"

%files
%license LICENSE
%{_datadir}/maven-metadata/java-diff-utils.xml
%{_datadir}/maven-repository/io/github/java-diff-utils/java-diff-utils/
%{_datadir}/maven-repository/io/github/java-diff-utils/java-diff-utils-parent/

%changelog
%autochangelog
