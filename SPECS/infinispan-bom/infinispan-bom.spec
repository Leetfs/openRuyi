# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           infinispan-bom
Version:        16.2.3
Release:        %autorelease
Summary:        Maven dependency management for Infinispan
License:        Apache-2.0
URL:            https://infinispan.org/
VCS:            git:https://github.com/infinispan/infinispan
#!RemoteAsset:  sha256:edd177a3e3bd9a747ad9afc4163dee92c7fafce429b6ee0ef0684456d2d772ba
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/infinispan/infinispan-bom/16.2.3/infinispan-bom-16.2.3.pom
#!RemoteAsset:  sha256:b91e73f4f38201568a5d456eb93fd620c79026a03859c4cd98f47976d726623e
Source1:        https://raw.githubusercontent.com/infinispan/infinispan/b886d3010ae9d70c0f330bb5e0aba394b462238e/LICENSE.md?/infinispan-bom-LICENSE
BuildArch:      noarch
BuildRequires:  javapackages-bootstrap(pom-install)
Provides:       mvn(org.infinispan:infinispan-bom:pom:) == 16.2.3

%description
The Infinispan BOM defines compatible versions for the data grid API,
cache stores and client modules.

%prep
%setup -q -c -T
cp %{SOURCE1} infinispan-bom-LICENSE

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
<groupId>org.infinispan</groupId><artifactId>infinispan-bom</artifactId><version>16.2.3</version>
<type>pom</type><scope>import</scope></dependency></dependencies></dependencyManagement>
<dependencies><dependency><groupId>org.infinispan</groupId><artifactId>infinispan-api</artifactId></dependency></dependencies>
</project>
EOF
%{_libexecdir}/javapackages-bootstrap/mvn -B -o -Dmaven.repo.local="$PWD/repo" validate

%files
%license infinispan-bom-LICENSE
%{_datadir}/maven-metadata/infinispan-bom.xml
%{_datadir}/maven-repository/org/infinispan/infinispan-bom/16.2.3/

%changelog
%autochangelog
