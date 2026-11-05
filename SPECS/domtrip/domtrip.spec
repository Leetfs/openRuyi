# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository/eu/maveniverse/maven/domtrip
Name:           domtrip
Version:        1.5.1
Release:        %autorelease
Summary:        Lossless XML and Maven POM editing libraries
License:        EPL-2.0
URL:            https://maveniverse.eu/projects/domtrip/
VCS:            git:https://github.com/maveniverse/domtrip
#!RemoteAsset:  sha256:60d155b8ee462444bd1a35e3d641e846ed0adc6a3ab54c7bd692cbf7257ff663
Source0:        https://github.com/maveniverse/domtrip/archive/refs/tags/1.5.1.tar.gz?/domtrip-1.5.1.tar.gz
#!RemoteAsset:  sha256:f109fb70888e5ec9b42ffd42d2324004a35f9b0eb64ec89092134f0dee3128cc
Source1:        https://maven-central.storage-download.googleapis.com/maven2/eu/maveniverse/maven/domtrip/domtrip/%{version}/domtrip-%{version}.pom
#!RemoteAsset:  sha256:7d8ecbd2a7b860ef85b359134b5371c6ed23124cef2a45954a9773bf50c7ac3b
Source2:        https://maven-central.storage-download.googleapis.com/maven2/eu/maveniverse/maven/domtrip/domtrip-core/%{version}/domtrip-core-%{version}.pom
#!RemoteAsset:  sha256:415b72e29795d7f86711497150fff7fe12e809f2c481f8d591d07b7cedebb5ef
Source3:        https://maven-central.storage-download.googleapis.com/maven2/eu/maveniverse/maven/domtrip/domtrip-maven/%{version}/domtrip-maven-%{version}.pom
#!RemoteAsset:  sha256:e5b0a1fdd14bf61ea78a41eff7d6777abb602f480483e59897c3a3e247973187
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/dom4j/dom4j/2.2.0/dom4j-2.2.0-sources.jar
#!RemoteAsset:  sha256:7d865e649e3dda2a26d9aee3f7f2e9e10569aee688463feb57d0bda16745eaa2
Source5:        https://maven-central.storage-download.googleapis.com/maven2/jaxen/jaxen/1.1.6/jaxen-1.1.6-sources.jar
Source6:        build-domtrip.sh
Source7:        check-domtrip.sh
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  mvn(eu.maveniverse.maven.parent:parent:pom:) == 52
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
BuildRequires:  unzip
Provides:       mvn(eu.maveniverse.maven.domtrip:domtrip:pom:) == %{version}
Provides:       mvn(eu.maveniverse.maven.domtrip:domtrip-core) == %{version}
Provides:       mvn(eu.maveniverse.maven.domtrip:domtrip-maven) == %{version}
Requires:       mvn(eu.maveniverse.maven.parent:parent:pom:) == 52

%description
Domtrip edits XML while preserving comments, formatting and source order.
Its Maven module edits POM elements and dependency coordinates.

%prep
%autosetup -n domtrip-%{version}

%build
bash %{SOURCE6} %{version} %{SOURCE2} %{SOURCE3}

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name}-models %{SOURCE1}
metadata=%{buildroot}%{_datadir}/maven-metadata/%{name}.xml
echo '<metadata><artifacts>' > "$metadata"
for module in core maven; do
    name=domtrip-$module
    jar=%{repo}/$name/%{version}/$name-%{version}.jar
    install -Dm644 "build/$module/$name.jar" "%{buildroot}$jar"
    model=%{SOURCE2}
    if test "$module" = maven; then model=%{SOURCE3}; fi
    pom=%{repo}/$name/%{version}/$name-%{version}.pom
    install -m644 "$model" "%{buildroot}$pom"
    cat >> "$metadata" <<EOF
<artifact><groupId>eu.maveniverse.maven.domtrip</groupId><artifactId>$name</artifactId><version>%{version}</version><extension>jar</extension><path>$jar</path><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
<artifact><groupId>eu.maveniverse.maven.domtrip</groupId><artifactId>$name</artifactId><version>%{version}</version><extension>pom</extension><path>$pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
EOF
done
echo '</artifacts></metadata>' >> "$metadata"

%check
bash %{SOURCE7} %{SOURCE4} %{SOURCE5}

%files
%license LICENSE
%doc README.md
%{_datadir}/maven-metadata/domtrip.xml
%{_datadir}/maven-metadata/domtrip-models.xml
%{repo}/

%changelog
%autochangelog
