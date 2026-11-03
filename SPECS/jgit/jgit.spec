# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
%global jgit_version %{version}.202603022253-r

Name:           jgit
Version:        7.6.0
Release:        %autorelease
Summary:        Git repository access and operations for Java
License:        BSD-3-Clause
URL:            https://eclipse.dev/jgit/
VCS:            git:https://github.com/eclipse-jgit/jgit
#!RemoteAsset:  sha256:ce697d3c2d2ef5d6e26591688e261c9f74d5cf3307ec37b6bb7e8b706f8aa9bf
Source0:        https://github.com/eclipse-jgit/jgit/archive/refs/tags/v%{version}.202603022253-r.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  eclipse-equinox-build >= 4.39
BuildRequires:  mvn(com.googlecode.javaewah:JavaEWAH) == 1.2.3
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.osgi) == 3.24.100
Provides:       mvn(org.eclipse.jgit:org.eclipse.jgit) == %{jgit_version}
Provides:       mvn(org.eclipse.jgit:org.eclipse.jgit-parent:pom:) == %{jgit_version}
Requires:       java-25-openjdk
Requires:       javapackages-bootstrap
Requires:       mvn(com.googlecode.javaewah:JavaEWAH) == 1.2.3

%description
JGit implements Git repository storage, revision walking, diffs, merges and
pack indexes in Java. The core library exposes these operations to Java
applications, Eclipse and Maven plugins.

%prep
%autosetup -n jgit-%{version}.202603022253-r

%build
mkdir -p build
ewah=%{_datadir}/maven-repository/com/googlecode/javaewah/JavaEWAH/1.2.3/JavaEWAH-1.2.3.jar
framework=%{_datadir}/maven-repository/org/eclipse/platform/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar
cp="$ewah:$framework:%{bootstrap_java}/commons-codec.jar:%{bootstrap_java}/slf4j-api.jar:%{bootstrap_java}/osgi.annotation.jar:%{bootstrap_java}/osgi.cmpn.jar"
%{_libexecdir}/eclipse-equinox/build-bundle org.eclipse.jgit "$PWD/build/org.eclipse.jgit.jar" --release 17 --classpath "$cp"
printf '%%s\n' "$cp" > build/classpath

%install
install -Dm644 org.eclipse.jgit/pom.xml %{buildroot}%{_datadir}/maven-repository/org/eclipse/jgit/org.eclipse.jgit/%{jgit_version}/org.eclipse.jgit-%{jgit_version}.pom
install -m644 build/org.eclipse.jgit.jar %{buildroot}%{_datadir}/maven-repository/org/eclipse/jgit/org.eclipse.jgit/%{jgit_version}/org.eclipse.jgit-%{jgit_version}.jar
install -Dm644 pom.xml %{buildroot}%{_datadir}/maven-repository/org/eclipse/jgit/org.eclipse.jgit-parent/%{jgit_version}/org.eclipse.jgit-parent-%{jgit_version}.pom
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>org.eclipse.jgit</groupId><artifactId>org.eclipse.jgit</artifactId><version>%{jgit_version}</version><extension>jar</extension>
    <path>%{_datadir}/maven-repository/org/eclipse/jgit/org.eclipse.jgit/%{jgit_version}/org.eclipse.jgit-%{jgit_version}.jar</path></artifact>
  <artifact><groupId>org.eclipse.jgit</groupId><artifactId>org.eclipse.jgit</artifactId><version>%{jgit_version}</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/org/eclipse/jgit/org.eclipse.jgit/%{jgit_version}/org.eclipse.jgit-%{jgit_version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
  <artifact><groupId>org.eclipse.jgit</groupId><artifactId>org.eclipse.jgit-parent</artifactId><version>%{jgit_version}</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/org/eclipse/jgit/org.eclipse.jgit-parent/%{jgit_version}/org.eclipse.jgit-parent-%{jgit_version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
cp="build/org.eclipse.jgit.jar:$(cat build/classpath):%{bootstrap_java}/gson.jar:%{bootstrap_java}/junit.jar:%{bootstrap_java}/hamcrest-core.jar:%{bootstrap_java}/hamcrest.jar"
tests=org.eclipse.jgit.test/tst
support=org.eclipse.jgit.junit/src
mkdir -p build/tests
for test in api/InitCommandTest api/AddCommandTest api/CommitCommandTest lib/AbbreviatedObjectIdTest lib/BitmapIndexTest lib/ObjectIdSerializerTest; do
    echo "$tests/org/eclipse/jgit/$test.java"
done > build/test-sources
javac --release 17 -encoding UTF-8 -cp "$cp" -sourcepath "$tests:$support:org.eclipse.jgit.lfs/src" -d build/tests @build/test-sources
classes=$(sed -e "s@^$tests/@@" -e 's@\.java$@@' -e 's@/@.@g' build/test-sources)
java -ea -cp "build/tests:org.eclipse.jgit.test/tst-rsrc:org.eclipse.jgit.lfs/resources:$support:$cp" org.junit.runner.JUnitCore $classes

%files
%license LICENSE
%{_datadir}/maven-metadata/jgit.xml
%{_datadir}/maven-repository/org/eclipse/jgit/org.eclipse.jgit/
%{_datadir}/maven-repository/org/eclipse/jgit/org.eclipse.jgit-parent/

%changelog
%autochangelog
