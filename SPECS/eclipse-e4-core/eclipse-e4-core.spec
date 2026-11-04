# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global tools_dir %{_libexecdir}/eclipse-equinox
%global maven_repo %{_datadir}/maven-repository
%global platform_repo %{maven_repo}/org/eclipse/platform
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap

Name:           eclipse-e4-core
Version:        4.39
Release:        %autorelease
Summary:        Eclipse E4 contexts, dependency injection and services
License:        EPL-2.0
URL:            https://eclipse.dev/eclipse/
VCS:            git:https://github.com/eclipse-platform/eclipse.platform
#!RemoteAsset:  sha256:973e213b8f8abbbfe397ec12d3d43c2a31fa81231646f29c473fec877b6bbd53
Source0:        https://github.com/eclipse-platform/eclipse.platform/archive/refs/tags/R4_39.tar.gz
#!RemoteAsset:  sha256:5e46e0cbbd36de8f6b75168fe7245d683f3e304260117e41ec971405995583c1
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.e4.core.di.annotations/1.8.400/org.eclipse.e4.core.di.annotations-1.8.400.pom
#!RemoteAsset:  sha256:568402f8d68e9662d4973ab4b545279a0328c306855ed1527308b62385fa2f7f
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.e4.core.di/1.9.700/org.eclipse.e4.core.di-1.9.700.pom
#!RemoteAsset:  sha256:9d0beca0c988f11e6e8f9ad6fbbc238c30a4a2a9154ee9aa98b57d1c31ba9d81
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.e4.core.contexts/1.13.200/org.eclipse.e4.core.contexts-1.13.200.pom
#!RemoteAsset:  sha256:b3ce52838e4218db22e2a072a601719fea07041d19bfb0f2a64bf9746eb2cd39
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.e4.core.services/2.5.300/org.eclipse.e4.core.services-2.5.300.pom
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  eclipse-core-runtime
BuildRequires:  mvn(jakarta.annotation:jakarta.annotation-api) == 2.1.1
BuildRequires:  mvn(jakarta.inject:jakarta.inject-api) == 2.0.1
BuildRequires:  mvn(org.osgi:org.osgi.service.event) == 1.4.1
Provides:       mvn(org.eclipse.platform:org.eclipse.e4.core.di.annotations) == 1.8.400
Provides:       mvn(org.eclipse.platform:org.eclipse.e4.core.di) == 1.9.700
Provides:       mvn(org.eclipse.platform:org.eclipse.e4.core.contexts) == 1.13.200
Provides:       mvn(org.eclipse.platform:org.eclipse.e4.core.services) == 2.5.300
Requires:       eclipse-core-runtime
Requires:       mvn(jakarta.annotation:jakarta.annotation-api) == 2.1.1
Requires:       mvn(jakarta.inject:jakarta.inject-api) == 2.0.1
Requires:       mvn(org.osgi:org.osgi.service.event) == 1.4.1

%description
Eclipse E4 manages hierarchical contexts, injects application services and
delivers platform events.

%prep
%autosetup -n eclipse.platform-R4_39

%build
mkdir -p build/bundles
cp=$(find %{platform_repo} -name '*.jar' ! -name '*-sources.jar' -printf '%%p:')
cp="$cp%{maven_repo}/jakarta/annotation/jakarta.annotation-api/2.1.1/jakarta.annotation-api-2.1.1.jar:%{maven_repo}/jakarta/inject/jakarta.inject-api/2.0.1/jakarta.inject-api-2.0.1.jar:%{maven_repo}/org/osgi/org.osgi.service.event/1.4.1/org.osgi.service.event-1.4.1.jar:%{bootstrap_java}/javax.inject.jar:%{bootstrap_java}/jsr250-api.jar:%{bootstrap_java}/osgi.cmpn.jar"
for dir in runtime/bundles/org.eclipse.e4.core.di.annotations runtime/bundles/org.eclipse.e4.core.di runtime/bundles/org.eclipse.e4.core.contexts runtime/bundles/org.eclipse.e4.core.services; do
    name=$(basename "$dir")
    jar="$PWD/build/bundles/$name.jar"
    %{tools_dir}/build-bundle "$dir" "$jar" --release 17 --classpath "$cp"
    cp="$jar:$cp"
done
printf '%%s\n' "$cp" > build/classpath

%install
%{tools_dir}/install-bundles %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4}

%check
cp=$(cat build/classpath)
mkdir -p build/tests
tests=runtime/tests/org.eclipse.e4.core.tests/src
classes=()
sources=()
for name in InjectionWithoutOSGITest ContextInjectionTest InjectionOrderTest; do
    while IFS= read -r file; do
        sources+=("$file")
        classes+=("$(sed -n 's/^package \(.*\);/\1/p' "$file").$name")
    done < <(find "$tests" -name "$name.java" | sort)
done
javac --release 17 -proc:none -sourcepath "$tests" -cp "$cp:%{bootstrap_java}/*" -d build/tests %{tools_dir}/RunJupiter.java "${sources[@]}"
java -cp "build/tests:$cp:%{bootstrap_java}/*" RunJupiter "${classes[@]}"

%files
%license LICENSE
%{_datadir}/maven-metadata/eclipse-e4-core.xml
%{platform_repo}/org.eclipse.e4.core.di.annotations/
%{platform_repo}/org.eclipse.e4.core.di/
%{platform_repo}/org.eclipse.e4.core.contexts/
%{platform_repo}/org.eclipse.e4.core.services/

%changelog
%autochangelog
