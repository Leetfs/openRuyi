# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           assertj-bom
Version:        3.27.7
Release:        %autorelease
Summary:        Bill of materials for AssertJ libraries
License:        Apache-2.0
URL:            https://github.com/assertj/assertj
VCS:            git:https://github.com/assertj/assertj
#!RemoteAsset:  sha256:1c09f6c04c905e1e5cdb22d5dfa5f11a496e19e881de0850b523ed53a0519f5b
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/assertj/assertj-bom/%{version}/assertj-bom-%{version}.pom
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch
BuildRequires:  javapackages-bootstrap(pom-install)
Provides:       mvn(org.assertj:assertj-bom:pom:) == %{version}

%description
The AssertJ bill of materials defines compatible versions of its assertion
libraries for Maven and Gradle dependency management.

%prep
%setup -q -T -c
cp %{SOURCE1} LICENSE

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name} %{SOURCE0}

%check
# Resolve an unversioned AssertJ dependency through the installed BOM offline.
mkdir -p check/repo
cd check
cp -as %{buildroot}%{_datadir}/maven-repository/. repo/
cat > pom.xml <<EOF
<project><modelVersion>4.0.0</modelVersion><groupId>org.openruyi.check</groupId><artifactId>parent-check</artifactId><version>1</version>
<dependencyManagement><dependencies><dependency><groupId>org.assertj</groupId><artifactId>assertj-bom</artifactId><version>%{version}</version><type>pom</type><scope>import</scope></dependency>
</dependencies></dependencyManagement>
<dependencies><dependency><groupId>org.assertj</groupId><artifactId>assertj-core</artifactId></dependency></dependencies></project>
EOF
%{_libexecdir}/javapackages-bootstrap/mvn -B -o -Dmaven.repo.local="$PWD/repo" validate

%files
%license LICENSE
%{_datadir}/maven-metadata/assertj-bom.xml
%{_datadir}/maven-repository/org/assertj/assertj-bom/

%changelog
%autochangelog
