# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bootstrap_java %{_datadir}/java/javapackages-bootstrap

Name:           javaewah
Version:        1.2.3
Release:        %autorelease
Summary:        Compressed bitmaps for Java
License:        Apache-2.0
URL:            https://github.com/lemire/javaewah
VCS:            git:https://github.com/lemire/javaewah
#!RemoteAsset:  sha256:b4bf847129ff8af5c3e0e0a6c74c5b33486f540d4e5054ef54d165d26d1f02b1
Source0:        https://github.com/lemire/javaewah/archive/refs/tags/JavaEWAH-%{version}.tar.gz
Source1:        javaewah.mf
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  xmlstarlet
Provides:       mvn(com.googlecode.javaewah:JavaEWAH) == %{version}
Requires:       java-25-openjdk
Requires:       mvn(org.sonatype.oss:oss-parent:pom) == 5

%description
JavaEWAH implements word-aligned compressed bitmaps with fast logical
operations, iteration and serialization. JGit uses them for pack indexes.

%prep
%autosetup -n javaewah-JavaEWAH-%{version}

%build
mkdir -p target/classes target/module-info target/java9
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -encoding UTF-8 -d target/classes @target/sources
# The upstream moduleInfo exports all packages.
module=$(xmlstarlet sel -N m=http://maven.apache.org/POM/4.0.0 -t -v '//m:moduleInfo/m:name' pom.xml)
test "$module" = com.googlecode.javaewah
test "$(xmlstarlet sel -N m=http://maven.apache.org/POM/4.0.0 -t -v '//m:moduleInfo/m:exports' pom.xml)" = '*;'
{
    echo "module $module {"
    find target/classes -name '*.class' -printf '%%h\n' | sort -u | sed -e 's@^target/classes/@@' -e 's@/@.@g' -e 's@^@    exports @' -e 's@$@;@'
    echo '}'
} > target/module-info/module-info.java
javac --release 9 --module-version %{version} --patch-module "$module=target/classes" -d target/java9 target/module-info/module-info.java
mkdir -p target/classes/META-INF/maven/com.googlecode.javaewah/JavaEWAH
install -m644 pom.xml target/classes/META-INF/maven/com.googlecode.javaewah/JavaEWAH/pom.xml
printf 'groupId=com.googlecode.javaewah\nartifactId=JavaEWAH\nversion=%{version}\n' > target/classes/META-INF/maven/com.googlecode.javaewah/JavaEWAH/pom.properties
jar --create --file target/JavaEWAH.jar --manifest %{SOURCE1} -C target/classes . --release 9 -C target/java9 module-info.class

%install
install -Dm644 pom.xml %{buildroot}%{_datadir}/maven-repository/com/googlecode/javaewah/JavaEWAH/%{version}/JavaEWAH-%{version}.pom
install -m644 target/JavaEWAH.jar %{buildroot}%{_datadir}/maven-repository/com/googlecode/javaewah/JavaEWAH/%{version}/JavaEWAH-%{version}.jar
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>com.googlecode.javaewah</groupId><artifactId>JavaEWAH</artifactId><version>%{version}</version><extension>jar</extension>
    <path>%{_datadir}/maven-repository/com/googlecode/javaewah/JavaEWAH/%{version}/JavaEWAH-%{version}.jar</path></artifact>
  <artifact><groupId>com.googlecode.javaewah</groupId><artifactId>JavaEWAH</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/com/googlecode/javaewah/JavaEWAH/%{version}/JavaEWAH-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
jar --describe-module --file target/JavaEWAH.jar --release 9 | grep -F 'com.googlecode.javaewah@%{version}'
mkdir -p target/test-classes
find src/test/java -name '*.java' | sort > target/test-sources
cp="target/JavaEWAH.jar:%{bootstrap_java}/junit.jar:%{bootstrap_java}/hamcrest-core.jar"
javac --release 8 -encoding UTF-8 -cp "$cp" -d target/test-classes @target/test-sources
classes=$(sed -n '/Test\.java$/ {s@^src/test/java/@@;s@\.java$@@;s@/@.@g;p;}' target/test-sources)
java -ea -Xmx768m -cp "target/test-classes:$cp" org.junit.runner.JUnitCore $classes

%files
%license LICENSE LICENSE-2.0.txt
%{_datadir}/maven-metadata/javaewah.xml
%{_datadir}/maven-repository/com/googlecode/javaewah/JavaEWAH/

%changelog
%autochangelog
