# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global osgi_repo %{_datadir}/maven-repository/org/osgi
%global framework %{_datadir}/maven-repository/org/eclipse/platform/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar
%global bundle_tools %{_libexecdir}/eclipse-equinox
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap

Name:           osgi-compendium
Version:        8.1.0
Release:        %autorelease
Summary:        OSGi Declarative Services API, promises and functional interfaces
License:        Apache-2.0
URL:            https://docs.osgi.org/specification/osgi.cmpn/
VCS:            git:https://github.com/osgi/osgi
#!RemoteAsset:  sha256:935bbe30bd3e39da6802118e2b526347e0610b64bcc8d758cc6e2d37cc621de9
Source0:        https://github.com/osgi/osgi/archive/refs/tags/%{version}.cmpn.tar.gz
#!RemoteAsset:  sha256:f4edd84181157d436818d46565d480379c1b07001d5cb130b406719729115ea8
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/osgi/org.osgi.util.function/1.2.0/org.osgi.util.function-1.2.0.pom
#!RemoteAsset:  sha256:adcc8af5c7be67b052105e0c9dcab8de26dac6f19bc5a9ab72946a33276c7100
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/osgi/org.osgi.util.promise/1.3.0/org.osgi.util.promise-1.3.0.pom
# Published Maven model from https://maven-central.storage-download.googleapis.com/maven2/org/osgi/org.osgi.service.component/1.5.1/org.osgi.service.component-1.5.1.pom
Source3:        org.osgi.service.component-1.5.1.pom
# OSGi 8.1 companion bundle headers, including the published import ranges.
Source4:        org.osgi.util.function.mf
Source5:        org.osgi.util.promise.mf
Source6:        org.osgi.service.component.mf
# PromiseTest uses the assertion library pinned by cnf/ext/junit.bnd.
#!RemoteAsset:  sha256:f03e11fbfe981b53e4812fa9d8c06620f159d8c5309a1ee16c3f5b0d0f1a3373
Source7:        https://github.com/osgi/osgi-test/archive/refs/tags/1.2.0.tar.gz
#!RemoteAsset:  sha256:5ef72894a9a31ad4226c61dc4a105f9b75672d3d41ce3aca5e89a7d691e00283
Source8:        https://maven-central.storage-download.googleapis.com/maven2/org/osgi/org.osgi.namespace.extender/1.0.1/org.osgi.namespace.extender-1.0.1.pom
#!RemoteAsset:  sha256:77e35d26d494efb24d9e9f37cb124ea5c0e376308527a9a5d9db48767b611a37
Source9:        https://maven-central.storage-download.googleapis.com/maven2/org/osgi/org.osgi.service.component.annotations/1.5.1/org.osgi.service.component.annotations-1.5.1.pom
# The extender is compiled for Java 8 with the distribution JDK.
Source10:       org.osgi.namespace.extender.mf
Source11:       org.osgi.service.component.annotations.mf
# The extender namespace was last released with the OSGi 6 source tree.
#!RemoteAsset:  sha256:bff6b8f778ee2ad0c53667ccdea907ec7f1715ed63b437a4d9b88028a68af849
Source12:       https://maven-central.storage-download.googleapis.com/maven2/org/osgi/org.osgi.namespace.extender/1.0.1/org.osgi.namespace.extender-1.0.1-sources.jar
#!RemoteAsset:  sha256:d6009acd3b459019c24e5c5f9d6e70b6f52c19c722c3a72d6a1795751eac81cc
Source13:       https://maven-central.storage-download.googleapis.com/maven2/org/osgi/org.osgi.service.repository/1.1.0/org.osgi.service.repository-1.1.0-sources.jar
#!RemoteAsset:  sha256:4066fca715aac32fe3ce0bc7bf81297bfd7130ebb6090cc9652adf7b2a807f19
Source14:       https://maven-central.storage-download.googleapis.com/maven2/org/osgi/org.osgi.service.repository/1.1.0/org.osgi.service.repository-1.1.0.pom
Source15:       org.osgi.service.repository.mf
Source16:       RepositoryWiring.java
#!RemoteAsset:  sha256:077fc604225b3720da15452738e91d843bd851ba45cba5ade275e5e988f1844f
Source17:       https://maven-central.storage-download.googleapis.com/maven2/org/osgi/org.osgi.service.event/1.4.1/org.osgi.service.event-1.4.1-sources.jar
#!RemoteAsset:  sha256:51495ce540f383ef63f191183999ddf43f81f7357b111b7f2cb706a7bbe1caf8
Source18:       https://maven-central.storage-download.googleapis.com/maven2/org/osgi/org.osgi.service.event/1.4.1/org.osgi.service.event-1.4.1.pom
Source19:       org.osgi.service.event.mf
Source20:       EventWiring.java
#!RemoteAsset:  sha256:e41fa65b9f8549475465403acbd5e4581f7c65bda79c9fb64417b36557555ebe
Source21:       https://maven-central.storage-download.googleapis.com/maven2/org/osgi/org.osgi.namespace.implementation/1.0.0/org.osgi.namespace.implementation-1.0.0-sources.jar
#!RemoteAsset:  sha256:643a997a8fde9dd69ae56862363f78cce2798a41062acb05ef90734ec0b6f901
Source22:       https://maven-central.storage-download.googleapis.com/maven2/org/osgi/org.osgi.namespace.implementation/1.0.0/org.osgi.namespace.implementation-1.0.0.pom
Source23:       org.osgi.namespace.implementation.mf
BuildArch:      noarch

BuildRequires:  eclipse-equinox-build >= 4.39
BuildRequires:  unzip
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.osgi) == 3.24.100
Provides:       mvn(org.osgi:org.osgi.service.event) == 1.4.1
Provides:       mvn(org.osgi:org.osgi.service.repository) == 1.1.0
Provides:       mvn(org.osgi:org.osgi.util.function) == 1.2.0
Provides:       mvn(org.osgi:org.osgi.util.promise) == 1.3.0
Provides:       mvn(org.osgi:org.osgi.service.component) == 1.5.1
Provides:       mvn(org.osgi:org.osgi.namespace.extender) == 1.0.1
Provides:       mvn(org.osgi:org.osgi.namespace.implementation) == 1.0.0
Provides:       mvn(org.osgi:org.osgi.service.component.annotations) == 1.5.1
Requires:       eclipse-equinox >= 4.39

%description
The Compendium companion bundles define the Declarative Services API, its
runtime data transfer objects, functional interfaces and asynchronous
promises for OSGi applications.

%prep
%autosetup -n osgi-%{version}.cmpn
echo '9edc17a6148f2a015e9cba5bf0ab824890c623ec58b373e5c7d475d6dfde9989  %{SOURCE3}' | sha256sum -c -
mkdir -p event-release
unzip -q %{SOURCE17} -d event-release
mkdir -p implementation-release
unzip -q %{SOURCE21} -d implementation-release
mkdir -p repository-release
unzip -q %{SOURCE13} -d repository-release
mkdir -p extender-release
unzip -q %{SOURCE12} -d extender-release
mkdir -p test-assertions
tar xf %{SOURCE7} --strip-components=1 -C test-assertions

%build
cp="%{framework}:%{bootstrap_java}/osgi.annotation.jar"
mkdir -p build/bundles
for manifest in %{SOURCE4} %{SOURCE5} %{SOURCE11} %{SOURCE6} %{SOURCE10} %{SOURCE15} %{SOURCE19} %{SOURCE23}; do
    name=$(basename "$manifest" .mf)
    classes="$PWD/build/$name"
    mkdir -p "$classes/META-INF" "$classes/OSGI-OPT/src"
    src="$name/src"
    case "$name" in
        org.osgi.service.component.annotations)
            src=org.osgi.service.component/src
            subtree=org/osgi/service/component/annotations ;;
        org.osgi.service.event)
            src=event-release
            subtree=org/osgi/service/event ;;
        org.osgi.service.repository)
            src=repository-release
            subtree=org/osgi/service/repository ;;
        org.osgi.namespace.implementation)
            src=implementation-release
            subtree=org/osgi/namespace/implementation ;;
        org.osgi.namespace.extender)
            src=extender-release
            subtree=org/osgi/namespace/extender ;;
        *) subtree=org ;;
    esac
    find "$src/$subtree" -name '*.java' | sort > build/sources
    if test "$name" = org.osgi.service.component; then
        sed -i '\|/org/osgi/service/component/annotations/|d' build/sources
    fi
    javac --release 8 -implicit:none -sourcepath "$src" -encoding UTF-8 -cp "$cp:%{bootstrap_java}/osgi.cmpn.jar" -d "$classes" @build/sources
    install -m644 LICENSE NOTICE "$classes/META-INF/"
    while read -r source; do
        install -Dm644 "$source" "$classes/OSGI-OPT/src/${source#"$src/"}"
    done < build/sources
    if test "$name" = org.osgi.namespace.extender; then
        install -m644 extender-release/LICENSE extender-release/about.html "$classes/"
        install -m644 "$src/$subtree/packageinfo" "$classes/$subtree/"
        install -m644 "$src/$subtree/packageinfo" "$classes/OSGI-OPT/src/$subtree/"
    fi
    if test "$name" = org.osgi.service.component; then
        mkdir -p "$classes/xmlns"
        cp -r xmlns/scr "$classes/xmlns/"
    fi
    jar="$PWD/build/bundles/$name.jar"
    jar --create --file "$jar" --manifest "$manifest" -C "$classes" .
    cp="$jar:$cp"
done
printf '%%s\n' "$cp" > build/classpath

%install
%{bundle_tools}/install-bundles --qualifier 201505202024 %{buildroot} %{_datadir} %{name}-repository build/bundles %{SOURCE14}
%{bundle_tools}/install-bundles %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE8} %{SOURCE9}

%{bundle_tools}/install-bundles --qualifier 202109301733 %{buildroot} %{_datadir} %{name}-event build/bundles %{SOURCE18}

%{bundle_tools}/install-bundles --qualifier 201505202024 %{buildroot} %{_datadir} %{name}-implementation build/bundles %{SOURCE22}

%check
cp=$(cat build/classpath)
for library in junit-platform-launcher junit-platform-engine junit-platform-commons junit-jupiter-api junit-jupiter-engine apiguardian-api opentest4j assertj-core; do
    cp="$cp:%{bootstrap_java}/$library.jar"
done
mkdir -p build/tests
tests=org.osgi.test.cases.promise/src
assertions=test-assertions/org.osgi.test.assertj.promise/src/main/java
support=test-assertions/org.osgi.test.common/src/main/java
javac --release 17 -encoding UTF-8 -cp "$cp" -sourcepath "$tests:org.osgi.test.support/src:$assertions:$support" -d build/tests \
    "$tests/org/osgi/test/cases/promise/junit/PromiseTest.java"
java -cp "build/tests:$cp" %{bundle_tools}/RunJupiter.java org.osgi.test.cases.promise.junit.PromiseTest
jar tf build/bundles/org.osgi.service.component.jar | grep -Fx 'xmlns/scr/v1.5.0/scr.xsd'

javap -classpath build/bundles/org.osgi.namespace.extender.jar -constants org.osgi.namespace.extender.ExtenderNamespace | grep -F '"osgi.extender"'
javap -classpath build/bundles/org.osgi.service.component.annotations.jar org.osgi.service.component.annotations.Component | grep -F 'java.lang.String name()'
if jar tf build/bundles/org.osgi.service.component.jar | grep -q '^org/osgi/service/component/annotations/'; then exit 1; fi

# Resolve the Repository bundle and verify its asynchronous API uses the registered Promise bundle.
java -cp %{framework} %{SOURCE16} "$PWD/build/repository-state" \
    build/bundles/org.osgi.util.function.jar build/bundles/org.osgi.util.promise.jar build/bundles/org.osgi.service.repository.jar

java -cp %{framework} %{SOURCE20} "$PWD/build/event-state" build/bundles/org.osgi.service.event.jar

# Verify the namespace constants used by capability filters and the framework's Resource API.
javap -classpath build/bundles/org.osgi.namespace.implementation.jar -constants org.osgi.namespace.implementation.ImplementationNamespace > build/implementation-api
grep -F 'extends org.osgi.resource.Namespace' build/implementation-api
grep -F '"osgi.implementation"' build/implementation-api
grep -F '"version"' build/implementation-api

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/osgi-compendium.xml
%{_datadir}/maven-metadata/osgi-compendium-repository.xml
%{_datadir}/maven-metadata/osgi-compendium-event.xml
%{_datadir}/maven-metadata/osgi-compendium-implementation.xml
%{osgi_repo}/org.osgi.namespace.implementation/
%{osgi_repo}/org.osgi.service.event/
%{osgi_repo}/org.osgi.service.repository/
%{osgi_repo}/org.osgi.util.function/
%{osgi_repo}/org.osgi.util.promise/
%{osgi_repo}/org.osgi.service.component/
%{osgi_repo}/org.osgi.namespace.extender/
%{osgi_repo}/org.osgi.service.component.annotations/

%changelog
%autochangelog
