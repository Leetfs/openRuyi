# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           junit-bom
Version:        6.1.3
Release:        %autorelease
Summary:        Maven dependency management for the JUnit test platform
License:        EPL-2.0
URL:            https://junit.org/
VCS:            git:https://github.com/junit-team/junit-framework
#!RemoteAsset:  sha256:5706e8f29a0a07f56efbbea4a0670793414194bb8d24d8143ba1e787a2f32856
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/junit/junit-bom/5.14.4/%{name}-5.14.4.pom
#!RemoteAsset:  sha256:ed2dcc7855bd460bccc93a1bf0c962e63b566ff7d8f1ded0f1f2593ba8183aaf
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/junit/junit-bom/5.14.2/%{name}-5.14.2.pom
#!RemoteAsset:  sha256:01b01dfa366550b40ac5760548a7d728b6109d17c451e83864d1e5e0ce862c94
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/junit/junit-bom/5.14.1/%{name}-5.14.1.pom
#!RemoteAsset:  sha256:cef80fec86454f6806bfb0df24669b5c6f32e2cb728539ea859f47dfdc9bbc17
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/junit/junit-bom/5.12.2/%{name}-5.12.2.pom
#!RemoteAsset:  sha256:5aa4cd44c111add178d1c2e2fe36d58a484012c80167df925f826cd64d411bf0
Source4:        https://raw.githubusercontent.com/junit-team/junit-framework/096fd696c1b22780e025a02417d42903e0022862/LICENSE.md
#!RemoteAsset:  sha256:f5aa47b366483e8d1f9bef10e67a0c66f66afc0f331c9f966b1310bad60d0f6f
Source5:        https://maven-central.storage-download.googleapis.com/maven2/org/junit/junit-bom/5.14.0/%{name}-5.14.0.pom
#!RemoteAsset:  sha256:d7a08a99b2502f0bb68cd4e1f984f0bf69324aaa208bd0f73366c03fc3548a42
Source6:        https://maven-central.storage-download.googleapis.com/maven2/org/junit/junit-bom/5.13.4/%{name}-5.13.4.pom
#!RemoteAsset:  sha256:fa68451ea830572ed43ffe51d75b6a05f7a5e665a602a51f49d6be02063a65f3
Source7:        https://maven-central.storage-download.googleapis.com/maven2/org/junit/junit-bom/5.13.1/%{name}-5.13.1.pom
#!RemoteAsset:  sha256:a9000043610a3e90c852e779a6b1a8eb724a9f312cf5f7ddd57862b010c65dc8
Source8:        https://maven-central.storage-download.googleapis.com/maven2/org/junit/junit-bom/%{version}/%{name}-%{version}.pom
#!RemoteAsset:  sha256:10937d44c425984cb8739225d34712e1a3145641ca93ac3f7ef186fa25f6babc
Source9:        https://maven-central.storage-download.googleapis.com/maven2/org/junit/junit-bom/5.10.3/junit-bom-5.10.3.pom
#!RemoteAsset:  sha256:7c826bc72beddc817dad9263027f9012a0f55a377d38df89c42932a2501c2bf0
Source10:       https://maven-central.storage-download.googleapis.com/maven2/org/junit/junit-bom/5.12.1/junit-bom-5.12.1.pom
#!RemoteAsset:  sha256:d48f54bc0598dab0e91a0d975c7d7c954666eac4fee63941876e3f92ea1e59c6
Source11:       https://maven-central.storage-download.googleapis.com/maven2/org/junit/junit-bom/5.13.0/junit-bom-5.13.0.pom
#!RemoteAsset:  sha256:c72124a9c9a79910c1858766b72c350e1a39244cbfb4b076348fbfe078281965
Source12:       https://maven-central.storage-download.googleapis.com/maven2/org/junit/junit-bom/5.11.1/junit-bom-5.11.1.pom
#!RemoteAsset:  sha256:169dd904a4b0f6520cffe658cc62292bfe9f3c14a989fa92120724cde43a9968
Source13:       https://maven-central.storage-download.googleapis.com/maven2/org/junit/junit-bom/5.10.2/junit-bom-5.10.2.pom
BuildArch:      noarch

BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  python3
Provides:       mvn(org.junit:junit-bom:pom:) == %{version}
Provides:       mvn(org.junit:junit-bom:pom:) == 5.10.3
Provides:       mvn(org.junit:junit-bom:pom:) == 5.14.4
Provides:       mvn(org.junit:junit-bom:pom:) == 5.14.2
Provides:       mvn(org.junit:junit-bom:pom:) == 5.14.1
Provides:       mvn(org.junit:junit-bom:pom:) == 5.14.0
Provides:       mvn(org.junit:junit-bom:pom:) == 5.13.4
Provides:       mvn(org.junit:junit-bom:pom:) == 5.13.1
Provides:       mvn(org.junit:junit-bom:pom:) == 5.12.2

Provides:       mvn(org.junit:junit-bom:pom:) == 5.12.1

Provides:       mvn(org.junit:junit-bom:pom:) == 5.13.0

Provides:       mvn(org.junit:junit-bom:pom:) == 5.11.1

Provides:       mvn(org.junit:junit-bom:pom:) == 5.10.2

%description
The JUnit bill of materials supplies compatible versions of the Jupiter,
Platform and Vintage modules for Maven projects.

%prep
%setup -q -c -T
cp %{SOURCE4} LICENSE.md

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name} %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13}

%check
# Import each installed model through Maven with an offline repository.
mkdir -p check/{.mvn,repo}
if test -d %{_datadir}/maven-repository; then cp -as %{_datadir}/maven-repository/. check/repo/; fi
cp -a --remove-destination %{buildroot}%{_datadir}/maven-repository/. check/repo/
cd check
for version in 5.10.2 5.11.1 %{version} 5.14.4 5.14.2 5.14.1 5.14.0 5.13.4 5.13.1 5.13.0 5.12.2 5.12.1 5.10.3; do
    cat > pom.xml <<EOF
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
<groupId>org.openruyi.check</groupId><artifactId>model-consumer</artifactId><version>1</version>
<dependencyManagement><dependencies><dependency>
<groupId>org.junit</groupId><artifactId>junit-bom</artifactId><version>$version</version>
<type>pom</type><scope>import</scope></dependency></dependencies></dependencyManagement>
<dependencies><dependency><groupId>org.junit.jupiter</groupId><artifactId>junit-jupiter-api</artifactId></dependency></dependencies>
</project>
EOF
    %{_libexecdir}/javapackages-bootstrap/mvn --batch-mode --offline -Dmaven.repo.local="$PWD/repo" validate
done

# Check the managed Platform and Jupiter versions in every released BOM.
python3 - %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} <<'PYCODE'
import sys
from xml.etree import ElementTree as ET
for pom in sys.argv[1:]:
    root = ET.parse(pom).getroot()
    version = root.findtext("{*}version")
    deps = root.findall("{*}dependencyManagement/{*}dependencies/{*}dependency")
    versions = {d.findtext("{*}artifactId"): d.findtext("{*}version") for d in deps}
    expected_size = 16 if version.startswith("6.") else 18
    assert len(versions) == len(deps) == expected_size
    assert versions["junit-jupiter-api"] == versions["junit-vintage-engine"] == version
    platform_version = version if version.startswith("6.") else "1." + version.split(".", 1)[1]
    assert versions["junit-platform-launcher"] == platform_version
PYCODE

%files
%license LICENSE.md
%{_datadir}/maven-metadata/junit-bom.xml
%{_datadir}/maven-repository/org/junit/junit-bom/

%changelog
%autochangelog
