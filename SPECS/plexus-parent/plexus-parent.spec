# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           plexus-parent
Version:        24
Release:        %autorelease
Summary:        Shared Maven build models for Plexus components
License:        Apache-2.0
URL:            https://codehaus-plexus.github.io/plexus-pom/
VCS:            git:https://github.com/codehaus-plexus/plexus-pom
#!RemoteAsset:  sha256:89a1bc79e46c35ab108b7e215bb2c5c215ff8f3af1ae3cfef82d9a2b33b06c51
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/codehaus/plexus/plexus/%{version}/plexus-%{version}.pom
#!RemoteAsset:  sha256:8d3e51c3902fd7596e548eab121ebf6b0d4aa73857077f26a24fc86f9b8455b4
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/codehaus/plexus/plexus/19/plexus-19.pom
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source2:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  mvn(org.junit:junit-bom:pom:) == 5.13.4
BuildRequires:  mvn(org.junit:junit-bom:pom:) == 5.11.1
Provides:       mvn(org.codehaus.plexus:plexus:pom:) == %{version}
Provides:       mvn(org.codehaus.plexus:plexus:pom:) == 19
Requires:       mvn(org.junit:junit-bom:pom:) == 5.13.4
Requires:       mvn(org.junit:junit-bom:pom:) == 5.11.1

%description
The Plexus parent models define dependency and plugin versions inherited by
Plexus components, including the internationalization and Velocity services.

%prep
%setup -q -T -c
cp %{SOURCE2} LICENSE

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name} %{SOURCE0} %{SOURCE1}

%check
# Import both parent models and their JUnit BOMs in an offline Maven repository.
mkdir -p check/repo
cp -as %{_datadir}/maven-repository/. check/repo/
cp -a --remove-destination %{buildroot}%{_datadir}/maven-repository/. check/repo/
cd check
for version in %{version} 19; do
    cat > pom.xml <<EOF
<project><modelVersion>4.0.0</modelVersion>
<groupId>org.openruyi.check</groupId><artifactId>plexus-parent-consumer</artifactId><version>1</version>
<dependencyManagement><dependencies><dependency><groupId>org.codehaus.plexus</groupId><artifactId>plexus</artifactId><version>$version</version><type>pom</type><scope>import</scope></dependency></dependencies></dependencyManagement>
<dependencies><dependency><groupId>org.junit.jupiter</groupId><artifactId>junit-jupiter-api</artifactId></dependency></dependencies>
</project>
EOF
    %{_libexecdir}/javapackages-bootstrap/mvn -B -o -Dmaven.repo.local="$PWD/repo" validate
done

%files
%license LICENSE
%{_datadir}/maven-metadata/plexus-parent.xml
%{_datadir}/maven-repository/org/codehaus/plexus/plexus/

%changelog
%autochangelog
