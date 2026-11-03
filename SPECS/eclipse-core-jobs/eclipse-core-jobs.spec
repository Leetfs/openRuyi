# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bundle org.eclipse.core.jobs
%global platform_repo %{_datadir}/maven-repository/org/eclipse/platform
%global bundle_tools %{_libexecdir}/eclipse-equinox

Name:           eclipse-core-jobs
Version:        3.15.700
Release:        %autorelease
Summary:        Eclipse background job scheduler
License:        EPL-2.0
URL:            https://eclipse.dev/eclipse/
VCS:            git:https://github.com/eclipse-platform/eclipse.platform
#!RemoteAsset:  sha256:d73c297c8316924c7dedda2b6d8ff248ce21bd4ba72a41025f4e2569a891fc06
Source0:        https://github.com/eclipse-platform/eclipse.platform/archive/refs/tags/R4_38.tar.gz
#!RemoteAsset:  sha256:394540a2d8c73e35511f3d5ff09d9f364766e0fe2cb5e6f857c4dfab097d3adf
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/%{bundle}/%{version}/%{bundle}-%{version}.pom
Source2:        JobsCheck.java
BuildArch:      noarch

BuildRequires:  eclipse-equinox-build >= 4.39
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.common) == 3.20.300
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.osgi) == 3.24.100
Provides:       mvn(org.eclipse.platform:org.eclipse.core.jobs) == %{version}
Requires:       eclipse-equinox >= 4.39

%description
The Eclipse job manager schedules background work, coordinates conflicting
scheduling rules and reports progress to applications running on Equinox.

%prep
%autosetup -n eclipse.platform-R4_38

%build
framework=%{platform_repo}/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar
common=%{platform_repo}/org.eclipse.equinox.common/3.20.300/org.eclipse.equinox.common-3.20.300.jar
%{bundle_tools}/build-bundle runtime/bundles/%{bundle} build/bundles/%{bundle}.jar --release 17 --classpath "$framework:$common"

%install
%{bundle_tools}/install-bundles %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1}

%check
framework=%{platform_repo}/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar
common=%{platform_repo}/org.eclipse.equinox.common/3.20.300/org.eclipse.equinox.common-3.20.300.jar
jobs=%{buildroot}%{platform_repo}/%{bundle}/%{version}/%{bundle}-%{version}.jar
java -cp "$framework" %{SOURCE2} "$common" "$jobs" "$PWD/build/storage"
test_src=runtime/tests/org.eclipse.core.tests.runtime/src
tests=$test_src/org/eclipse/core/tests/runtime/jobs
cp="$jobs:$common:$framework"
for library in junit-platform-launcher junit-platform-engine junit-platform-commons junit-jupiter-api junit-jupiter-engine apiguardian-api opentest4j junit hamcrest-core assertj-core; do
    cp="$cp:%{_datadir}/java/javapackages-bootstrap/$library.jar"
done
mkdir -p build/tests
javac --release 17 -cp "$cp" -sourcepath "$test_src:runtime/tests/org.eclipse.core.tests.harness/src" -d build/tests "$tests/JobQueueTest.java" "$tests/MultiRuleTest.java"
java -cp "build/tests:$cp" %{bundle_tools}/RunJupiter.java org.eclipse.core.tests.runtime.jobs.JobQueueTest org.eclipse.core.tests.runtime.jobs.MultiRuleTest

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/eclipse-core-jobs.xml
%{platform_repo}/%{bundle}/

%changelog
%autochangelog
