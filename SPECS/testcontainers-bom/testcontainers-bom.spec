# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           testcontainers-bom
Version:        2.0.5
Release:        %autorelease
Summary:        Maven dependency management for Testcontainers
License:        MIT
URL:            https://java.testcontainers.org/
VCS:            git:https://github.com/testcontainers/testcontainers-java
#!RemoteAsset:  sha256:bbba1376021fbf4e14663a61f10cd1aff14a5d74fb55f1a14be6fd6de83d7eef
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/testcontainers/testcontainers-bom/2.0.5/testcontainers-bom-2.0.5.pom
#!RemoteAsset:  sha256:2159220a6d068db4dc329a5f9f1f4670abdfbe225942a5e46c7330ffa98f89d4
Source1:        https://raw.githubusercontent.com/testcontainers/testcontainers-java/5c448202ac69d073f746433d3e79f6a2bf0ec585/LICENSE?/testcontainers-bom-LICENSE
BuildArch:      noarch
BuildRequires:  javapackages-bootstrap(pom-install)
Provides:       mvn(org.testcontainers:testcontainers-bom:pom:) == 2.0.5

%description
The Testcontainers BOM defines compatible versions for Java test fixtures
and their container-specific modules.

%prep
%setup -q -c -T
cp %{SOURCE1} testcontainers-bom-LICENSE

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
<groupId>org.testcontainers</groupId><artifactId>testcontainers-bom</artifactId><version>2.0.5</version>
<type>pom</type><scope>import</scope></dependency></dependencies></dependencyManagement>
<dependencies><dependency><groupId>org.testcontainers</groupId><artifactId>testcontainers</artifactId></dependency></dependencies>
</project>
EOF
%{_libexecdir}/javapackages-bootstrap/mvn -B -o -Dmaven.repo.local="$PWD/repo" validate

%files
%license testcontainers-bom-LICENSE
%{_datadir}/maven-metadata/testcontainers-bom.xml
%{_datadir}/maven-repository/org/testcontainers/testcontainers-bom/2.0.5/

%changelog
%autochangelog
