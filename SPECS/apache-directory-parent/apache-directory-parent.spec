# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           apache-directory-parent
Version:        2.1.8
Release:        %autorelease
Summary:        Parent models for the Apache Directory LDAP API
License:        Apache-2.0
URL:            https://directory.apache.org/api/
VCS:            git:https://github.com/apache/directory-ldap-api
#!RemoteAsset:  sha256:be7dcf1b69aa4c0583d22fca4c8f12e742991f724e049efe8ea2338b39879dfc
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/directory/api/api-parent/%{version}/api-parent-%{version}.pom
#!RemoteAsset:  sha256:e57c7123c1bebc2de429568fbc9df0019cf2b3b72531e3f722adc6c2e5412720
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/directory/project/project/51/project-51.pom
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source2:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  mvn(org.apache:apache:pom:) == 38
Provides:       mvn(org.apache.directory.api:api-parent:pom:) == %{version}
Provides:       mvn(org.apache.directory.project:project:pom:) == 51
Requires:       mvn(org.apache:apache:pom:) == 38

%description
The Apache Directory project and LDAP API parent models provide the
managed versions used by Maven consumers of the LDAP client API.

%prep
%setup -q -c -T
cp %{SOURCE2} LICENSE

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name} %{SOURCE0} %{SOURCE1}

%check
mkdir -p check/{.mvn,repo}
cp -as %{_datadir}/maven-repository/. check/repo/
cp -a --remove-destination %{buildroot}%{_datadir}/maven-repository/. check/repo/
cd check
cat > pom.xml <<'EOF'
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
<groupId>org.openruyi.check</groupId><artifactId>directory-consumer</artifactId><version>1</version>
<dependencyManagement><dependencies><dependency><groupId>org.apache.directory.api</groupId>
<artifactId>api-parent</artifactId><version>%{version}</version><type>pom</type><scope>import</scope></dependency></dependencies></dependencyManagement>
<dependencies><dependency><groupId>org.apache.directory.api</groupId><artifactId>api-ldap-client-api</artifactId></dependency></dependencies></project>
EOF
%{_libexecdir}/javapackages-bootstrap/mvn -B -o -Dmaven.repo.local="$PWD/repo" validate

%files
%license LICENSE
%{_datadir}/maven-metadata/apache-directory-parent.xml
%{_datadir}/maven-repository/org/apache/directory/api/api-parent/%{version}/
%{_datadir}/maven-repository/org/apache/directory/project/project/51/

%changelog
%autochangelog
