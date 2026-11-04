# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global artifact jakarta.inject-api
%global group jakarta.inject
%global symbolic jakarta.inject.jakarta.inject-api
%global module jakarta.inject
%global bundle_tools %{_libexecdir}/eclipse-equinox
%global mvnrepo %{_datadir}/maven-repository

Name:           jakarta-inject-api
Version:        2.0.1
Release:        %autorelease
Summary:        Jakarta dependency injection annotations
License:        Apache-2.0
URL:            https://jakarta.ee/specifications/dependency-injection/
VCS:            git:https://github.com/jakartaee/inject
#!RemoteAsset:  sha256:51df7e4b118f67f37eb55128dfe475a55b702581609987b06908d744bc5ee33c
Source0:        https://github.com/jakartaee/inject/archive/refs/tags/%{version}.tar.gz
Source1:        ApiCheck.java
BuildArch:      noarch

BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.eclipse.ee4j:project:pom:) == 1.0.6
Provides:       mvn(jakarta.inject:jakarta.inject-api) == %{version}
Requires:       java-25-openjdk
Requires:       mvn(org.eclipse.ee4j:project:pom:) == 1.0.6

%description
The Jakarta Inject API defines injection points, named bindings, scopes, qualifiers and providers.

%prep
%autosetup -n inject-2.0.1

%build
src=./src/main/java
model=./pom.xml
mkdir -p build/{classes,source-content,bundles,sources}
# The API targets Java 8 and its explicit module descriptor targets Java 9.
find "$src" -name '*.java' ! -name module-info.java | sort > build/classes.list
javac --release 8 -proc:none -encoding UTF-8 -d build/classes @build/classes.list
javac --release 9 --patch-module %{module}=build/classes -d build/classes "$src/module-info.java"
meta=META-INF/maven/%{group}/%{artifact}
mkdir -p "build/classes/$meta"
cp "$model" "build/classes/$meta/pom.xml"
printf 'groupId=%{group}\nartifactId=%{artifact}\nversion=%{version}\n' > "build/classes/$meta/pom.properties"
cp LICENSE.txt NOTICE.md build/classes/META-INF/
cat > build/bundle.mf <<'EOF'
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-Name: Jakarta dependency injection annotations
Bundle-SymbolicName: %{symbolic}
Bundle-Version: %{version}
Bundle-Vendor: Eclipse Foundation
Export-Package: jakarta.inject;version="2.0.1"
Require-Capability: osgi.ee;filter:="(&(osgi.ee=JavaSE)(version=1.8))"
EOF
jar --create --file build/bundles/%{artifact}.jar --manifest build/bundle.mf --module-version %{version} -C build/classes .
cp -a "$src/." build/source-content/
mkdir -p build/source-content/META-INF
cp LICENSE.txt NOTICE.md build/source-content/META-INF/
cat > build/source.mf <<'EOF'
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-SymbolicName: %{symbolic}.source
Bundle-Version: %{version}
Bundle-Name: Source Bundle for %{symbolic}
Eclipse-SourceBundle: %{symbolic};version="%{version}";roots:="."
EOF
jar --create --file build/sources/%{artifact}.jar --manifest build/source.mf -C build/source-content .

%install
%{bundle_tools}/install-bundles --symbolic-name %{symbolic} --sources build/sources %{buildroot} %{_datadir} %{name} build/bundles ./pom.xml

%check
# Compile and run a named JPMS consumer against the packaged public APIs.
mkdir -p build/consumer/classes
echo 'module org.openruyi.check { requires %{module}; }' > build/consumer/module-info.java
jar="$PWD/build/bundles/%{artifact}.jar"
javac --release 17 --module-path "$jar" -d build/consumer/classes build/consumer/module-info.java %{SOURCE1}
java --module-path "$jar:build/consumer/classes" -m org.openruyi.check/check.ApiCheck
# Check release bytecode, module exports, and attached source code.
jar --describe-module --file "$jar" | grep -F '%{module}@%{version}'
javap -verbose -classpath "$jar" jakarta.inject.Inject | grep -F 'major version: 52'
jar tf build/sources/%{artifact}.jar | grep -Fx 'jakarta/inject/Inject.java'
# Validate the consumer model and its original EE4J parent offline.
mkdir -p build/model/.mvn
cp -as %{mvnrepo}/. build/model/repository
cp -a --remove-destination %{buildroot}%{mvnrepo}/. build/model/repository/
cat > build/model/pom.xml <<'EOF'
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
<groupId>org.openruyi.check</groupId><artifactId>api-consumer</artifactId><version>1</version>
<dependencyManagement><dependencies><dependency><groupId>%{group}</groupId><artifactId>%{artifact}</artifactId>
<version>%{version}</version><type>pom</type><scope>import</scope></dependency></dependencies></dependencyManagement></project>
EOF
(cd build/model && %{_libexecdir}/javapackages-bootstrap/mvn -B --offline -Dmaven.repo.local="$PWD/repository" validate)

%files
%license LICENSE.txt NOTICE.md
%{_datadir}/maven-metadata/jakarta-inject-api.xml
%{mvnrepo}/jakarta/inject/%{artifact}/

%changelog
%autochangelog
