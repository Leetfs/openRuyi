# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           netty-bom
Version:        4.2.18.Final
Release:        %autorelease
Summary:        Maven dependency management for Netty
License:        Apache-2.0
URL:            https://netty.io/
VCS:            git:https://github.com/netty/netty
#!RemoteAsset:  sha256:1274869dd11559b8490099a7e6f3ed94eddfade282be91627863cac8fc705663
Source0:        https://maven-central.storage-download.googleapis.com/maven2/io/netty/netty-bom/4.2.18.Final/netty-bom-4.2.18.Final.pom
#!RemoteAsset:  sha256:aac73b3148f6d1d7111dbca32099f68d26c644c6813ae1e4f05f6579aa2663fe
Source1:        https://raw.githubusercontent.com/netty/netty/2521f494432e27415a567d3a81a9eb907abf20b3/LICENSE.txt?/netty-bom-LICENSE
BuildArch:      noarch
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  sonatype-oss-parent >= 7
Provides:       mvn(io.netty:netty-bom:pom:) == 4.2.18.Final
Requires:       sonatype-oss-parent >= 7

%description
The Netty BOM defines compatible versions for the Netty transport, buffer
and codec modules.

%prep
%setup -q -c -T
cp %{SOURCE1} netty-bom-LICENSE

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
<groupId>io.netty</groupId><artifactId>netty-bom</artifactId><version>4.2.18.Final</version>
<type>pom</type><scope>import</scope></dependency></dependencies></dependencyManagement>
<dependencies><dependency><groupId>io.netty</groupId><artifactId>netty-buffer</artifactId></dependency></dependencies>
</project>
EOF
%{_libexecdir}/javapackages-bootstrap/mvn -B -o -Dmaven.repo.local="$PWD/repo" validate

%files
%license netty-bom-LICENSE
%{_datadir}/maven-metadata/netty-bom.xml
%{_datadir}/maven-repository/io/netty/netty-bom/4.2.18.Final/

%changelog
%autochangelog
