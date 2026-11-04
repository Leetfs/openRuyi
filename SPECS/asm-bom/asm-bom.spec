# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           asm-bom
Version:        9.10.1
Release:        %autorelease
Summary:        Maven dependency management for ASM
License:        BSD-3-Clause
URL:            https://asm.ow2.io/
VCS:            git:https://gitlab.ow2.org/asm/asm
#!RemoteAsset:  sha256:709472d69cf785d4b679eee0e6e0575d4b104476ddf35265ef1117e73c129cd4
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/ow2/asm/asm-bom/9.10.1/asm-bom-9.10.1.pom
#!RemoteAsset:  sha256:293b6af371eee28b0ff16f0334ea19e20a3d5522143faa4b95b346855507879a
Source1:        https://gitlab.ow2.org/asm/asm/-/raw/38c169b1d7609085c8fdcede23767899ae4e1d77/LICENSE.txt?/asm-bom-LICENSE
#!RemoteAsset:  sha256:0fa27336fa7b62923ca9bdc69526ebe712a3bfb1f7ee8bf76c4a0b3f85f19d62
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/ow2/asm/asm-bom/9.9/asm-bom-9.9.pom
BuildArch:      noarch
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  mvn(org.ow2:ow2:pom:) == 1.5.1
Provides:       mvn(org.ow2.asm:asm-bom:pom:) == 9.10.1
Provides:       mvn(org.ow2.asm:asm-bom:pom:) == 9.9
Requires:       mvn(org.ow2:ow2:pom:) == 1.5.1

%description
The ASM BOM defines compatible versions for JVM class readers, writers,
bytecode visitors and analysis libraries.

%prep
%setup -q -c -T
cp %{SOURCE1} asm-bom-LICENSE

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name} %{SOURCE0} %{SOURCE2}

%check
# Import the installed release model into a fresh Maven consumer.
mkdir -p check/{.mvn,repo}
if test -d %{_datadir}/maven-repository; then cp -as %{_datadir}/maven-repository/. check/repo/; fi
cp -a --remove-destination %{buildroot}%{_datadir}/maven-repository/. check/repo/
cd check
for version in %{version} 9.9; do
cat > pom.xml <<EOF
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
<groupId>org.openruyi.check</groupId><artifactId>model-consumer</artifactId><version>1</version>
<dependencyManagement><dependencies><dependency>
<groupId>org.ow2.asm</groupId><artifactId>asm-bom</artifactId><version>$version</version>
<type>pom</type><scope>import</scope></dependency></dependencies></dependencyManagement>
<dependencies><dependency><groupId>org.ow2.asm</groupId><artifactId>asm</artifactId></dependency></dependencies>
</project>
EOF
%{_libexecdir}/javapackages-bootstrap/mvn -B -o -Dmaven.repo.local="$PWD/repo" validate
done

%files
%license asm-bom-LICENSE
%{_datadir}/maven-metadata/asm-bom.xml
%{_datadir}/maven-repository/org/ow2/asm/asm-bom/9.10.1/
%{_datadir}/maven-repository/org/ow2/asm/asm-bom/9.9/

%changelog
%autochangelog
