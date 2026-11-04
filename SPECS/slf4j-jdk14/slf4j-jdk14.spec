# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository
Name:           slf4j-jdk14
Version:        1.7.36
Release:        %autorelease
Summary:        SLF4J binding for the Java logging framework
License:        MIT
URL:            https://www.slf4j.org/
VCS:            git:https://github.com/qos-ch/slf4j
#!RemoteAsset:  sha256:a2deaffa191c81abbf830d4060eb84129f31b9b3b945b7791344e8875b595286
Source0:        https://github.com/qos-ch/slf4j/archive/refs/tags/v_%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  mvn(org.eclipse.jdt:ecj) == 3.32.0
BuildRequires:  mvn(org.slf4j:slf4j-api) == %{version}
Provides:       mvn(org.slf4j:slf4j-jdk14) == %{version}
Provides:       mvn(org.slf4j:slf4j-parent:pom:) == %{version}
Requires:       mvn(org.slf4j:slf4j-api) == %{version}

%description
This binding forwards SLF4J log records to java.util.logging and provides
the org.slf4j.impl package required by the SLF4J 1.7 OSGi bundle.

%package     -n slf4j-simple
Summary:        SLF4J binding for configurable console logging
Provides:       mvn(org.slf4j:slf4j-simple) == %{version}
Requires:       mvn(org.slf4j:slf4j-api) == %{version}
Requires:       mvn(org.slf4j:slf4j-parent:pom:) == %{version}

%description -n slf4j-simple
The simple SLF4J backend writes log messages to a stream or a file and
supports per-logger levels, timestamps and short or qualified logger names.

%prep
%autosetup -n slf4j-v_%{version}

%build
api=%{repo_dir}/org/slf4j/slf4j-api/%{version}/slf4j-api-%{version}.jar
mkdir -p build/{bundles,tests}
for name in slf4j-jdk14 slf4j-simple; do
    out="$PWD/build/classes/$name"
    mkdir -p "$out/META-INF/maven/org.slf4j/$name"
    find "$name/src/main/java" -name '*.java' | sort > build/sources
    java -jar %{repo_dir}/org/eclipse/jdt/ecj/3.32.0/ecj-3.32.0.jar -proc:none -nowarn -encoding UTF-8 \
        -source 1.5 -target 1.5 -cp "$api" -d "$out" @build/sources
    cp "$name/pom.xml" "$out/META-INF/maven/org.slf4j/$name/pom.xml"
    if test "$name" = slf4j-jdk14; then
        module=org.slf4j.jul; symbolic=slf4j.jdk14; description='SLF4J JDK14 Binding'
    else
        module=org.slf4j.simple; symbolic=slf4j.simple; description='SLF4J Simple Binding'
    fi
    cat > build/binding.mf <<EOF
Manifest-Version: 1.0
Automatic-Module-Name: $module
Bundle-ManifestVersion: 2
Bundle-SymbolicName: $symbolic
Bundle-Version: %{version}
Bundle-Name: $name
Bundle-Description: $description
Bundle-Vendor: SLF4J.ORG
Bundle-RequiredExecutionEnvironment: J2SE-1.5
Export-Package: org.slf4j.impl;version=1.7.36
Import-Package: org.slf4j;version=1.7.36,org.slf4j.spi;version=1.7.36,org.slf4j.helpers;version=1.7.36,org.slf4j.event;version=1.7.36
EOF
    jar cfm "build/bundles/$name.jar" build/binding.mf -C "$out" .
done

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name}-model pom.xml
%{_libexecdir}/eclipse-equinox/install-bundles --symbolic-name slf4j.jdk14 %{buildroot} %{_datadir} %{name} build/bundles slf4j-jdk14/pom.xml

%{_libexecdir}/eclipse-equinox/install-bundles --symbolic-name slf4j.simple %{buildroot} %{_datadir} slf4j-simple build/bundles slf4j-simple/pom.xml

%check
api=%{repo_dir}/org/slf4j/slf4j-api/%{version}/slf4j-api-%{version}.jar
cp="build/bundles/%{name}.jar:$api:%{_datadir}/java/javapackages-bootstrap/junit.jar:%{_datadir}/java/javapackages-bootstrap/hamcrest-core.jar"
find slf4j-api/src/test/java slf4j-jdk14/src/test/java -name '*.java' | sort > build/test-sources
javac --release 8 -proc:none -encoding UTF-8 -cp "$cp" -d build/tests @build/test-sources
find slf4j-jdk14/src/test/java -name '*Test.java' | sed 's|slf4j-jdk14/src/test/java/||;s|[.]java$||;s|/|.|g' | sort > build/suites
while IFS= read -r suite; do java -XX:ActiveProcessorCount=4 -cp "build/tests:$cp" org.junit.runner.JUnitCore "$suite" || exit 1; done < build/suites

base=$PWD; mkdir -p build/simple-tests
cp="$base/build/bundles/slf4j-simple.jar:$api:%{_datadir}/java/javapackages-bootstrap/junit.jar:%{_datadir}/java/javapackages-bootstrap/hamcrest-core.jar"
find slf4j-api/src/test/java slf4j-simple/src/test/java -name '*.java' | sort > build/simple-sources
javac --release 8 -proc:none -encoding UTF-8 -cp "$cp" -d build/simple-tests @build/simple-sources
cp -r slf4j-simple/src/test/resources/. build/simple-tests/
cd slf4j-simple
find src/test/java -name '*Test.java' | sed 's|src/test/java/||;s|[.]java$||;s|/|.|g' | sort > "$base/build/simple-suites"
while IFS= read -r suite; do
    java -XX:ActiveProcessorCount=4 -cp "$base/build/simple-tests:$cp" org.junit.runner.JUnitCore "$suite" || exit 1
done < "$base/build/simple-suites"

%files
%license LICENSE.txt
%{_datadir}/maven-metadata/slf4j-jdk14-model.xml
%{_datadir}/maven-metadata/slf4j-jdk14.xml
%{repo_dir}/org/slf4j/slf4j-jdk14/%{version}/
%{repo_dir}/org/slf4j/slf4j-parent/%{version}/

%files -n slf4j-simple
%license LICENSE.txt
%{_datadir}/maven-metadata/slf4j-simple.xml
%{repo_dir}/org/slf4j/slf4j-simple/%{version}/

%changelog
%autochangelog
