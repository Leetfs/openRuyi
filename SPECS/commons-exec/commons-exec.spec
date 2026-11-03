# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
%global xmvn_ext %{_datadir}/javapackages-bootstrap/maven/lib/ext

Name:           commons-exec
Version:        1.6.0
Release:        %autorelease
Summary:        Library for executing external processes in Java
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-exec/
VCS:            git:https://github.com/apache/commons-exec
#!RemoteAsset:  sha256:9f17e83c014fdd07a9ae7b5d912b274e44b90c3db00d97780f759b050a360b03
Source0:        https://github.com/apache/commons-exec/archive/refs/tags/rel/commons-exec-%{version}.tar.gz
Source1:        commons-exec.mf
#!RemoteAsset:  sha256:ad48e978a582f804b132bce4212c047a05f6479df985b1578f59a611070479ae
Source2:        https://github.com/junit-pioneer/junit-pioneer/archive/refs/tags/v1.9.1.tar.gz
# Exercise the watchdog without privileged ICMP sockets on Linux.
Patch2000:      2000-Exercise-Linux-watchdogs-without-an-ICMP-socket.patch
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  unzip
Provides:       mvn(org.apache.commons:commons-exec) == %{version}
Requires:       java-25-openjdk
Requires:       mvn(org.apache.commons:commons-parent:pom:) == 93

%description
Apache Commons Exec runs external commands, handles their streams and exit
codes, and can terminate processes after a timeout.

%prep
%autosetup -p1 -n commons-exec-rel-commons-exec-%{version}

%build
mkdir -p target/classes/META-INF target/module-info target/java9
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -encoding UTF-8 -d target/classes @target/sources
install -m644 LICENSE.txt NOTICE.txt target/classes/META-INF/
mkdir -p target/classes/META-INF/maven/org.apache.commons/commons-exec
install -m644 pom.xml target/classes/META-INF/maven/org.apache.commons/commons-exec/pom.xml
printf 'groupId=org.apache.commons\nartifactId=commons-exec\nversion=%{version}\n' > target/classes/META-INF/maven/org.apache.commons/commons-exec/pom.properties
# The upstream Maven build generates the Java 9 descriptor for the four public packages.
cat > target/module-info/module-info.java <<'EOF'
module org.apache.commons.exec {
    exports org.apache.commons.exec;
    exports org.apache.commons.exec.environment;
    exports org.apache.commons.exec.launcher;
    exports org.apache.commons.exec.util;
}
EOF
javac --release 9 --module-version %{version} --patch-module org.apache.commons.exec=target/classes \
    -d target/java9 target/module-info/module-info.java
jar --create --file target/%{name}.jar --manifest %{SOURCE1} -C target/classes . --release 9 -C target/java9 module-info.class

%install
install -Dm644 pom.xml %{buildroot}%{_datadir}/maven-repository/org/apache/commons/commons-exec/%{version}/commons-exec-%{version}.pom
install -m644 target/%{name}.jar %{buildroot}%{_datadir}/maven-repository/org/apache/commons/commons-exec/%{version}/commons-exec-%{version}.jar
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>org.apache.commons</groupId><artifactId>commons-exec</artifactId><version>%{version}</version><extension>jar</extension>
    <path>%{_datadir}/maven-repository/org/apache/commons/commons-exec/%{version}/commons-exec-%{version}.jar</path></artifact>
  <artifact><groupId>org.apache.commons</groupId><artifactId>commons-exec</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/org/apache/commons/commons-exec/%{version}/commons-exec-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
# Validate the module descriptor and run the upstream process execution tests.
jar --describe-module --file target/%{name}.jar --release 9 | grep -F 'org.apache.commons.exec@%{version}'
mkdir -p target/test-classes .xmvn
# Only the system-property Jupiter extension is used by the upstream tests.
mkdir -p target/pioneer
tar xf %{SOURCE2} --strip-components=4 -C target/pioneer junit-pioneer-1.9.1/src/main/java/org/junitpioneer
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 17 -encoding UTF-8 -cp 'target/classes:%{bootstrap_java}/*' -d target/test-classes -sourcepath src/test/java:target/pioneer @target/test-sources
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
    <dependency><groupId>org.apache.commons</groupId><artifactId>commons-lang3</artifactId><version>SYSTEM</version><scope>test</scope></dependency>
  </dependencies>
</project>
EOF
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
surefire=$(unzip -p %{bootstrap_java}/maven-surefire-plugin.jar META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
test -n "$surefire"
mvn -B --offline -f openruyi-tests.pom -Dmaven.repo.local="$PWD/target/test-repository" \
    -DfailIfNoTests=true "org.apache.maven.plugins:maven-surefire-plugin:$surefire:test"

%files
%license LICENSE.txt NOTICE.txt
%{_datadir}/maven-metadata/commons-exec.xml
%{_datadir}/maven-repository/org/apache/commons/commons-exec/

%changelog
%autochangelog
