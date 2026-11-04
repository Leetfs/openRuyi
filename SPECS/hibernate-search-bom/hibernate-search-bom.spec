# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           hibernate-search-bom
Version:        8.4.0.Final
Release:        %autorelease
Summary:        Maven dependency management for Hibernate Search
License:        Apache-2.0
URL:            https://hibernate.org/search/
VCS:            git:https://github.com/hibernate/hibernate-search
#!RemoteAsset:  sha256:5c2dffb295e2598d8e67a301cc3ef749d76943028000cf8ce7bc3212b875aa02
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/hibernate/search/hibernate-search-bom/8.4.0.Final/hibernate-search-bom-8.4.0.Final.pom
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source1:        https://raw.githubusercontent.com/hibernate/hibernate-search/7369a18fc526aaffba13336fdcdc95a333702b19/LICENSE.txt?/hibernate-search-bom-LICENSE
BuildArch:      noarch
BuildRequires:  javapackages-bootstrap(pom-install)
Provides:       mvn(org.hibernate.search:hibernate-search-bom:pom:) == 8.4.0.Final

%description
The Hibernate Search BOM defines compatible versions for search engines,
backends and object mapping integrations.

%prep
%setup -q -c -T
cp %{SOURCE1} hibernate-search-bom-LICENSE

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name} %{SOURCE0}

%check
# Import the installed release model into a fresh Maven consumer.
mkdir -p check/{.mvn,repo}
if test -d %{_datadir}/maven-repository; then cp -as %{_datadir}/maven-repository/. check/repo/; fi
cp -a --remove-destination %{buildroot}%{_datadir}/maven-repository/. check/repo/
cd check
cat > pom.xml <<'EOF'
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
<groupId>org.openruyi.check</groupId><artifactId>model-consumer</artifactId><version>1</version>
<dependencyManagement><dependencies><dependency>
<groupId>org.hibernate.search</groupId><artifactId>hibernate-search-bom</artifactId><version>8.4.0.Final</version>
<type>pom</type><scope>import</scope></dependency></dependencies></dependencyManagement>
<dependencies><dependency><groupId>org.hibernate.search</groupId><artifactId>hibernate-search-engine</artifactId></dependency></dependencies>
</project>
EOF
%{_libexecdir}/javapackages-bootstrap/mvn -B -o -Dmaven.repo.local="$PWD/repo" validate

%files
%license hibernate-search-bom-LICENSE
%{_datadir}/maven-metadata/hibernate-search-bom.xml
%{_datadir}/maven-repository/org/hibernate/search/hibernate-search-bom/8.4.0.Final/

%changelog
%autochangelog
