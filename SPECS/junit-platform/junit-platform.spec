# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global release_tag 5.12.2
%global repo %{_datadir}/maven-repository
Name:           junit-platform
Version:        1.12.2
Release:        %autorelease
Summary:        JUnit Platform discovery and test execution
License:        EPL-2.0
URL:            https://junit.org/
VCS:            git:https://github.com/junit-team/junit-framework
#!RemoteAsset:  sha256:d1228e5de6f5d52575cbac6a4aa0f00a6ece194decbf6fbe2deb607c90a1113c
Source0:        https://github.com/junit-team/junit-framework/archive/refs/tags/r%{release_tag}.tar.gz?/junit-framework-%{release_tag}.tar.gz
#!RemoteAsset:  sha256:4f2b8a9065c909c6892d8622d553b6ab0a70321624499e3b69c1289f59ecc077
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/junit/platform/junit-platform-commons/%{version}/junit-platform-commons-%{version}.pom
#!RemoteAsset:  sha256:9480b18a7965769d0083c2cb71105423f5302a8f046bb2047e6dbff09f383490
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/junit/platform/junit-platform-engine/%{version}/junit-platform-engine-%{version}.pom
#!RemoteAsset:  sha256:619145cd215d32225372be625bba28683d74142fee1a5dfdb1c64b52fe9c0b51
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/junit/platform/junit-platform-launcher/%{version}/junit-platform-launcher-%{version}.pom
#!RemoteAsset:  sha256:babbccb7ae82e7ed4f14c140fb11f21fc6ac595c60e8cafe445fbc84d938adab
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/junit/jupiter/junit-jupiter-api/%{release_tag}/junit-jupiter-api-%{release_tag}-sources.jar
Source5:        BuildPlatformBundle.java
Source6:        build-junit-platform.sh
Source7:        check-junit-platform.sh
#!RemoteAsset:  sha256:566282166489bd40b12c3507b995e48f8e025e09a05e7d16dd2b98dc642cf7de
Source8:        https://maven-central.storage-download.googleapis.com/maven2/org/junit/jupiter/junit-jupiter-api/%{release_tag}/junit-jupiter-api-%{release_tag}.pom
#!RemoteAsset:  sha256:3c719174509be9db1fa817ac63b78b21f1f67d068be471da3d04781bd4402aa3
Source9:        https://maven-central.storage-download.googleapis.com/maven2/org/junit/jupiter/junit-jupiter-engine/%{release_tag}/junit-jupiter-engine-%{release_tag}.pom
#!RemoteAsset:  sha256:6ea58b6031e64703751fd6fd647e94c3362792c3c9510acfccba610eeb0011d7
Source10:       https://maven-central.storage-download.googleapis.com/maven2/org/junit/vintage/junit-vintage-engine/%{release_tag}/junit-vintage-engine-%{release_tag}.pom
Source11:       VintageExecution.java
BuildArch:      noarch
BuildRequires:  mvn(org.mockito:mockito-junit-jupiter) == 4.11.0
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.bndlib) == 7.2.3
BuildRequires:  mvn(org.junit:junit-bom:pom:) == %{release_tag}
BuildRequires:  unzip
Provides:       mvn(org.junit.platform:junit-platform-commons) == %{version}
Provides:       mvn(org.junit.platform:junit-platform-engine) == %{version}
Provides:       mvn(org.junit.platform:junit-platform-launcher) == %{version}
Requires:       javapackages-bootstrap
Requires:       mvn(org.junit:junit-bom:pom:) == %{release_tag}

%description
JUnit Platform provides the discovery and execution interfaces used by
test engines, build tools and IDEs. It includes the common utilities,
engine API and launcher, including support for test output directories.

%package     -n junit-jupiter
Version:        %{release_tag}
Summary:        Java API and test engine for JUnit Jupiter
Requires:       junit-platform = 1.12.2
Requires:       javapackages-bootstrap
Provides:       mvn(org.junit.jupiter:junit-jupiter-api) == %{release_tag}
Provides:       mvn(org.junit.jupiter:junit-jupiter-engine) == %{release_tag}

%description -n junit-jupiter
The Jupiter Java API supplies assertions, annotations and extensions for
writing tests. Its engine discovers and executes them on the JUnit Platform.
The Kotlin assertion extensions require the Kotlin compiler and are omitted.

%package     -n junit-vintage-engine
Version:        %{release_tag}
Summary:        JUnit Platform engine for JUnit 3 and JUnit 4 tests
Provides:       mvn(org.junit.vintage:junit-vintage-engine) == %{release_tag}
Requires:       junit-platform = 1.12.2
Requires:       javapackages-bootstrap

%description -n junit-vintage-engine
The Vintage engine discovers and runs JUnit 3 and JUnit 4 tests through
the JUnit Platform launcher.

%prep
%autosetup -n junit-framework-r%{release_tag}

%build
bash %{SOURCE6} %{SOURCE5} %{SOURCE4}

%install
%{_libexecdir}/eclipse-equinox/install-bundles %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1} %{SOURCE2} %{SOURCE3}
%{_libexecdir}/eclipse-equinox/install-bundles %{buildroot} %{_datadir} junit-jupiter build/bundles %{SOURCE8} %{SOURCE9}
%{_libexecdir}/eclipse-equinox/install-bundles %{buildroot} %{_datadir} junit-vintage-engine build/bundles %{SOURCE10}

%check
bash %{SOURCE7} %{SOURCE11}

%files
%license LICENSE.md NOTICE.md
%{_datadir}/maven-metadata/junit-platform.xml
%{repo}/org/junit/platform/junit-platform-commons/
%{repo}/org/junit/platform/junit-platform-engine/
%{repo}/org/junit/platform/junit-platform-launcher/

%files -n junit-jupiter
%license LICENSE.md NOTICE.md
%{_datadir}/maven-metadata/junit-jupiter.xml
%{repo}/org/junit/jupiter/junit-jupiter-api/
%{repo}/org/junit/jupiter/junit-jupiter-engine/

%files -n junit-vintage-engine
%license LICENSE.md NOTICE.md
%{_datadir}/maven-metadata/junit-vintage-engine.xml
%{repo}/org/junit/vintage/junit-vintage-engine/

%changelog
%autochangelog
