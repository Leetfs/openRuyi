# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global artifact jakarta.annotation-api
%global group jakarta.annotation
%global symbolic jakarta.annotation-api
%global module jakarta.annotation
%global bundle_tools %{_libexecdir}/eclipse-equinox
%global mvnrepo %{_datadir}/maven-repository

Name:           jakarta-annotation-api
Version:        3.0.0
Release:        %autorelease
Summary:        Jakarta lifecycle, security and SQL annotations
License:        EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://jakarta.ee/specifications/annotations/
VCS:            git:https://github.com/jakartaee/common-annotations-api
#!RemoteAsset:  sha256:d076d0b1990fc63fc7ad09cdad7cde8cd0c3b0c217c029f322b9af7527c2e06b
Source0:        https://github.com/jakartaee/common-annotations-api/archive/refs/tags/%{version}.tar.gz
Source1:        ApiCheck.java
#!RemoteAsset:  sha256:06eccfd01cd59bb1d3778c13a12759363b0f58e5d05f97c68db83c9d703c57b5
Source2:        https://github.com/jakartaee/common-annotations-api/archive/refs/tags/2.1.1.tar.gz?/jakarta-annotation-2.1.1.tar.gz
BuildArch:      noarch

BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.eclipse.ee4j:project:pom:) == 1.0.9
BuildRequires:  mvn(org.eclipse.ee4j:project:pom:) == 1.0.7
Provides:       mvn(jakarta.annotation:jakarta.annotation-api) == %{version}
Provides:       mvn(jakarta.annotation:jakarta.annotation-api) == 2.1.1
Requires:       java-25-openjdk
Requires:       mvn(org.eclipse.ee4j:project:pom:) == 1.0.9
Requires:       mvn(org.eclipse.ee4j:project:pom:) == 1.0.7

%description
The Jakarta Annotations API defines application lifecycle callbacks, role declarations, and data source metadata.

%prep
%autosetup -n common-annotations-api-3.0.0

mkdir annotations-2.1.1
tar xf %{SOURCE2} --strip-components=1 -C annotations-2.1.1

%build
src=api/src/main/java
model=api/pom.xml
mkdir -p build/{classes,source-content,bundles,sources}
find "$src" -name '*.java' | sort > build/classes.list
javac --release 11 -proc:none -encoding UTF-8 -d build/classes @build/classes.list
meta=META-INF/maven/%{group}/%{artifact}
mkdir -p "build/classes/$meta"
cp "$model" "build/classes/$meta/pom.xml"
printf 'groupId=%{group}\nartifactId=%{artifact}\nversion=%{version}\n' > "build/classes/$meta/pom.properties"
cp LICENSE.md NOTICE.md build/classes/META-INF/
cat > build/bundle.mf <<'EOF'
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-Name: Jakarta lifecycle, security and SQL annotations
Bundle-SymbolicName: %{symbolic}
Bundle-Version: %{version}
Bundle-Vendor: Eclipse Foundation
Export-Package: jakarta.annotation;version="3.0.0",jakarta.annotation.security;version="3.0.0",jakarta.annotation.sql;version="3.0.0"
Require-Capability: osgi.ee;filter:="(&(osgi.ee=JavaSE)(version=11))"
Import-Package: java.lang,java.lang.annotation
EOF
jar --create --file build/bundles/%{artifact}.jar --manifest build/bundle.mf --module-version %{version} -C build/classes .
cp -a "$src/." build/source-content/
mkdir -p build/source-content/META-INF
cp LICENSE.md NOTICE.md build/source-content/META-INF/
cat > build/source.mf <<'EOF'
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-SymbolicName: %{symbolic}.source
Bundle-Version: %{version}
Bundle-Name: Source Bundle for %{symbolic}
Eclipse-SourceBundle: %{symbolic};version="%{version}";roots:="."
EOF
jar --create --file build/sources/%{artifact}.jar --manifest build/source.mf -C build/source-content .

# The 2.1 line exports the Java 8 annotations imported by Eclipse E4.
mkdir -p build/compat/{classes,bundles}
src=annotations-2.1.1/api/src/main/java
find "$src" -name '*.java' ! -name module-info.java | sort > build/compat/sources
javac --release 8 -proc:none -encoding UTF-8 -d build/compat/classes @build/compat/sources
javac --release 9 --patch-module %{module}=build/compat/classes --module-version 2.1.1 -d build/compat/classes "$src/module-info.java"
mkdir -p build/compat/classes/META-INF
install -m644 annotations-2.1.1/{LICENSE.md,NOTICE.md} build/compat/classes/META-INF/
cat > build/compat/MANIFEST.MF <<'EOF'
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-Name: Jakarta Annotation API
Bundle-SymbolicName: jakarta.annotation-api
Bundle-Version: 2.1.1
Bundle-Vendor: Eclipse Foundation
Export-Package: jakarta.annotation;version="2.1.1",jakarta.annotation.security;version="2.1.1",jakarta.annotation.sql;version="2.1.1"
Require-Capability: osgi.ee;filter:="(&(osgi.ee=JavaSE)(version=1.8))"
EOF
jar cfm build/compat/bundles/%{artifact}.jar build/compat/MANIFEST.MF -C build/compat/classes .

%install
%{bundle_tools}/install-bundles %{buildroot} %{_datadir} %{name}-compat build/compat/bundles annotations-2.1.1/api/pom.xml
%{bundle_tools}/install-bundles --symbolic-name %{symbolic} --sources build/sources %{buildroot} %{_datadir} %{name} build/bundles api/pom.xml

%check
# Compile and run a named JPMS consumer against the packaged public APIs.
mkdir -p build/consumer/classes
echo 'module org.openruyi.check { requires %{module}; }' > build/consumer/module-info.java
jar="$PWD/build/bundles/%{artifact}.jar"
javac --release 17 --module-path "$jar" -d build/consumer/classes build/consumer/module-info.java %{SOURCE1}
java --module-path "$jar:build/consumer/classes" -m org.openruyi.check/check.ApiCheck
# Check release bytecode, module exports, and attached source code.
jar --describe-module --file "$jar" | grep -F '%{module}@%{version}'
javap -verbose -classpath "$jar" jakarta.annotation.PostConstruct | grep -F 'major version: 55'
jar tf build/sources/%{artifact}.jar | grep -Fx 'jakarta/annotation/PostConstruct.java'
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

# Exercise the Java 8 compatibility API through its Java 9 module descriptor.
cat > build/CompatCheck.java <<'EOF'
package check;
import jakarta.annotation.PostConstruct;
import jakarta.annotation.Resource;
import jakarta.annotation.security.RolesAllowed;
@RolesAllowed("builder")
public class CompatCheck {
    @Resource(name="target") String value;
    @PostConstruct void start() {}
    public static void main(String[] args) throws Exception {
        if (!CompatCheck.class.getDeclaredMethod("start").isAnnotationPresent(PostConstruct.class)
            || !CompatCheck.class.getDeclaredField("value").getAnnotation(Resource.class).name().equals("target")
            || !CompatCheck.class.getAnnotation(RolesAllowed.class).value()[0].equals("builder")) throw new AssertionError();
    }
}
EOF
mkdir -p build/compat/consumer
javac --release 11 --module-path build/compat/bundles/%{artifact}.jar -d build/compat/consumer build/consumer/module-info.java build/CompatCheck.java
java --module-path build/compat/bundles/%{artifact}.jar:build/compat/consumer -m org.openruyi.check/check.CompatCheck

%files
%license LICENSE.md NOTICE.md
%{_datadir}/maven-metadata/jakarta-annotation-api.xml
%{_datadir}/maven-metadata/jakarta-annotation-api-compat.xml
%{mvnrepo}/jakarta/annotation/%{artifact}/

%changelog
%autochangelog
