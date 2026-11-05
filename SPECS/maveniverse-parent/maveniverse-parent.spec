# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           maveniverse-parent
Version:        52
Release:        %autorelease
Summary:        Shared Maven build model for Maveniverse projects
License:        EPL-2.0
URL:            https://github.com/maveniverse/parent
VCS:            git:https://github.com/maveniverse/parent
#!RemoteAsset:  sha256:ec0c2694d9958218506861f70a4c202efa746d7675b3a61ddcd95be43715f6ab
Source0:        https://maven-central.storage-download.googleapis.com/maven2/eu/maveniverse/maven/parent/parent/%{version}/parent-%{version}.pom
#!RemoteAsset:  sha256:8c349f80764d0648e645f41ef23772a70c995a0924b5235f735f4a3d09df127c
Source1:        https://raw.githubusercontent.com/maveniverse/parent/release-%{version}/LICENSE
BuildArch:      noarch
BuildRequires:  javapackages-bootstrap(pom-install)
Provides:       mvn(eu.maveniverse.maven.parent:parent:pom:) == %{version}

%description
The Maveniverse parent model provides shared dependency and plugin management
for Domtrip and other Maveniverse projects.

%prep
%setup -q -T -c
cp %{SOURCE1} LICENSE

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name} %{SOURCE0}

%check
mkdir -p check/repo
cd check
cp -as %{buildroot}%{_datadir}/maven-repository/. repo/
cat > pom.xml <<EOF
<project><modelVersion>4.0.0</modelVersion><groupId>org.openruyi.check</groupId><artifactId>parent-check</artifactId><version>1</version>
<dependencyManagement><dependencies><dependency><groupId>eu.maveniverse.maven.parent</groupId><artifactId>parent</artifactId><version>%{version}</version><type>pom</type><scope>import</scope></dependency>
</dependencies></dependencyManagement></project>
EOF
%{_libexecdir}/javapackages-bootstrap/mvn -B -o -Dmaven.repo.local="$PWD/repo" validate

%files
%license LICENSE
%{_datadir}/maven-metadata/maveniverse-parent.xml
%{_datadir}/maven-repository/eu/maveniverse/maven/parent/

%changelog
%autochangelog
