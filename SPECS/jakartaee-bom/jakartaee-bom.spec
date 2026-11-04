# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jakartaee-bom
Version:        10.0.0
Release:        %autorelease
Summary:        Jakarta EE platform dependency management
License:        EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://jakarta.ee/specifications/platform/10/
VCS:            git:https://github.com/jakartaee/jakartaee-api
#!RemoteAsset:  sha256:e9ece31d10be350c08fbf1d7ca3a9ae6b0ad21db6296b4bf414108e3a82c6320
Source0:        https://github.com/jakartaee/jakartaee-api/archive/refs/tags/%{version}.tar.gz?/jakartaee-api-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  mvn(org.eclipse.ee4j:project:pom:) == 1.0.7
Provides:       mvn(jakarta.platform:jakarta.jakartaee-bom:pom:) == %{version}
Provides:       mvn(jakarta.platform:jakartaee-api-parent:pom:) == %{version}
Requires:       mvn(org.eclipse.ee4j:project:pom:) == 1.0.7

%description
The Jakarta EE platform BOM supplies compatible versions for Servlet and
the other Jakarta EE specification APIs.

%prep
%autosetup -n jakartaee-api-%{version}

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name} pom.xml jakartaee-bom/pom.xml

%check
mkdir -p check/{.mvn,repo}
cp -as %{_datadir}/maven-repository/. check/repo/
cp -a --remove-destination %{buildroot}%{_datadir}/maven-repository/. check/repo/
cd check
cat > pom.xml <<'EOF'
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
<groupId>org.openruyi.check</groupId><artifactId>servlet-consumer</artifactId><version>1</version>
<dependencyManagement><dependencies><dependency><groupId>jakarta.platform</groupId>
<artifactId>jakarta.jakartaee-bom</artifactId><version>%{version}</version><type>pom</type><scope>import</scope>
</dependency></dependencies></dependencyManagement>
<dependencies><dependency><groupId>jakarta.servlet</groupId><artifactId>jakarta.servlet-api</artifactId></dependency></dependencies></project>
EOF
%{_libexecdir}/javapackages-bootstrap/mvn -B -o -Dmaven.repo.local="$PWD/repo" validate

%files
%license LICENSE.txt
%{_datadir}/maven-metadata/jakartaee-bom.xml
%{_datadir}/maven-repository/jakarta/platform/jakartaee-api-parent/%{version}/
%{_datadir}/maven-repository/jakarta/platform/jakarta.jakartaee-bom/%{version}/

%changelog
%autochangelog
