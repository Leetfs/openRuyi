# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global suite_dir %{_datadir}/maven-repository/org/apache/maven/surefire
%global artifact_dir %{suite_dir}/%{name}/%{version}
Name:           surefire-shadefire
Version:        3.5.2
Release:        %autorelease
Summary:        Relocated JUnit provider for building Apache Maven Surefire
License:        Apache-2.0
URL:            https://maven.apache.org/surefire/
VCS:            git:https://github.com/apache/maven-surefire
#!RemoteAsset:  sha256:2f559c1567589aa472fc334ab21ecba4ff47035ce38414170e5a0fddf7883441
Source0:        https://archive.apache.org/dist/maven/surefire/surefire-%{version}-source-release.zip
#!RemoteAsset:  sha256:a46d943853d51134140995772923ca518d7921a3a6a06e1a4c3f51f6641c8d94
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/surefire/surefire-shadefire/%{version}/surefire-shadefire-%{version}.pom
Source2:        build-shadefire.py
Source3:        check-provider.sh
BuildArch:      noarch
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin) == 3.6.1
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:) == 43
BuildRequires:  python3
BuildRequires:  unzip
Provides:       mvn(org.apache.maven.surefire:surefire-shadefire) == %{version}
Provides:       mvn(org.apache.maven.surefire:surefire:pom:) == %{version}
Requires:       java-25-openjdk
Requires:       mvn(org.apache.maven:maven-parent:pom:) == 43

%description
Surefire uses a relocated copy of its JUnit Platform provider to run tests
while building a newer version. The provider runs in a forked JVM and
transmits test results back to Maven.

%prep
%autosetup -n surefire-%{version}

%build
python3 %{SOURCE2} "$PWD" "$PWD/build/bootstrap"

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name}-models pom.xml
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 build/bootstrap/repo/org/apache/maven/surefire/%{name}/%{version}/%{name}-%{version}.jar %{buildroot}%{artifact_dir}/
install -m644 %{SOURCE1} %{buildroot}%{artifact_dir}/%{name}-%{version}.pom
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
 <artifact><groupId>org.apache.maven.surefire</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>jar</extension>
 <path>%{artifact_dir}/%{name}-%{version}.jar</path><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
 <artifact><groupId>org.apache.maven.surefire</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension>
 <path>%{artifact_dir}/%{name}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
bash %{SOURCE3} %{buildroot}

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/surefire-shadefire.xml
%{_datadir}/maven-metadata/surefire-shadefire-models.xml
%{artifact_dir}/
%{suite_dir}/surefire/%{version}/

%changelog
%autochangelog
