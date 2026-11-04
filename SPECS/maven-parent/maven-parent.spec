# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           maven-parent
Version:        48
Release:        %autorelease
Summary:        Parent Maven models for Apache Maven projects
License:        Apache-2.0
URL:            https://maven.apache.org/pom/
VCS:            git:https://github.com/apache/maven-parent
#!RemoteAsset:  sha256:4d93d91cc2fd4e16f6a18d1c5cf15f305b4ae12dc549801eebbd19d7ac0f05a2
Source0:        https://github.com/apache/maven-parent/archive/refs/tags/maven-parent-%{version}.tar.gz
#!RemoteAsset:  sha256:82d0112ba1907ff5fd13a2485829c97df66c6a81e075359a561a422f7d1582d3
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/maven-parent/47/maven-parent-47.pom
#!RemoteAsset:  sha256:00cc44a14d41057121e84104765efc661e1a6a5d04cf5ec1d6b65b422dabc665
Source2:        https://github.com/apache/maven-parent/archive/refs/tags/maven-parent-45.tar.gz
#!RemoteAsset:  sha256:e4ae585aa3a6c723ccdc4556b0b4ece63b7885fbb3e9a7ad52a5b6f728df2e68
Source3:        https://github.com/apache/maven-parent/archive/refs/tags/maven-parent-35.tar.gz
#!RemoteAsset:  sha256:81fe14cb9779d36e0c610e1049e5b32a6b9974957f257921acf628b31c5486c8
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/maven-parent/10/maven-parent-10.pom
#!RemoteAsset:  sha256:70cef83d246309a2aa355c38f2004edda3621ae0bc5c55a7a139eaeef4d1231a
Source5:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/maven-parent/16/maven-parent-16.pom
#!RemoteAsset:  sha256:6a58eb24291600f75ce0fe369b73fe6700f575ace4b664724d3cd0a6b85b63ee
Source6:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/shared/maven-shared-components/15/maven-shared-components-15.pom
#!RemoteAsset:  sha256:468a1262e9aaa5febf9d604e2836267f815351f2b4520f28fb17f53c71e33554
Source7:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/maven-parent/43/maven-parent-43.pom
#!RemoteAsset:  sha256:1c0a088d7352d52ea8f3581d05778c0c4a679613fff2c58737fba55f1007fe24
Source8:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/maven-parent/44/maven-parent-44.pom
#!RemoteAsset:  sha256:58ddbb8e429cb5e9054c2f5f7b7cdfeb7adbcdfda21d92b67f67fa2b94edf982
Source9:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/maven-plugins/47/maven-plugins-47.pom
#!RemoteAsset:  sha256:3bd3d07c910477091bb9602f931f696c4aa115c86a322bff6a604ec7543afc07
Source10:       https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/shared/maven-shared-components/47/maven-shared-components-47.pom
#!RemoteAsset:  sha256:d7801d725de2abb706efb931e22eac5df4d0c7fc8c9ea9a4d9986782407aaff7
Source11:       https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/maven-plugins/44/maven-plugins-44.pom
#!RemoteAsset:  sha256:1a8faf7a6a2b848acb26a959954ee115c0d79dbe75a6206fb3b8c7c2f45a237f
Source12:       https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/maven-parent/34/maven-parent-34.pom
#!RemoteAsset:  sha256:64d0edb5f21cfff600b1c3ab7d45f9754cd18ba5fbf83b3d1bb7c4849437d8e3
Source13:       https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/shared/maven-shared-components/34/maven-shared-components-34.pom
#!RemoteAsset:  sha256:cfe4820aa1d96ae51d1dc5b0e2a9dc582c42478c24c95ca8238f547e60bef721
Source14:       https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/maven-parent/39/maven-parent-39.pom
#!RemoteAsset:  sha256:18085afbef3a17942b442135a3f0e77018cda66edd33c6b18fd18440661bc29e
Source15:       https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/maven-plugins/39/maven-plugins-39.pom
#!RemoteAsset:  sha256:57014e98ba621d9d254cf79ad4dfcdcf690290fd97a935bab9ebe72bd5be40d3
Source16:       https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/maven-plugins/48/maven-plugins-48.pom
#!RemoteAsset:  sha256:6072dd103bdba3199584c5b73ed45b00567cd3ea918e2160b10bc7437c9e8181
Source17:       https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/shared/maven-shared-components/43/maven-shared-components-43.pom
#!RemoteAsset:  sha256:4a8f3bc226f6f1b7f7362fa2a6e1da451561f86783ec512176e1c467a03708eb
Source18:       https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/shared/maven-shared-components/48/maven-shared-components-48.pom
BuildArch:      noarch

BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  mvn(org.apache:apache:pom:) == 38
BuildRequires:  mvn(org.apache:apache:pom:) == 37
BuildRequires:  mvn(org.apache:apache:pom:) == 35
BuildRequires:  mvn(org.apache:apache:pom:) == 33
BuildRequires:  mvn(org.apache:apache:pom:) == 25
BuildRequires:  mvn(org.apache:apache:pom:) == 29
BuildRequires:  mvn(org.apache:apache:pom:) == 23
BuildRequires:  mvn(org.apache:apache:pom:) == 7
BuildRequires:  mvn(org.apache:apache:pom:) == 4
BuildRequires:  mvn(org.junit:junit-bom:pom:) == 5.14.4
BuildRequires:  mvn(org.junit:junit-bom:pom:) == 5.14.2
BuildRequires:  mvn(org.junit:junit-bom:pom:) == 5.13.1
BuildRequires:  mvn(org.junit:junit-bom:pom:) == 5.10.3
Provides:       mvn(org.apache.maven:maven-parent:pom:) == %{version}
Provides:       mvn(org.apache.maven:maven-parent:pom:) == 43
Provides:       mvn(org.apache.maven:maven-parent:pom:) == 47
Provides:       mvn(org.apache.maven:maven-parent:pom:) == 45
Provides:       mvn(org.apache.maven:maven-parent:pom:) == 35
Provides:       mvn(org.apache.maven:maven-parent:pom:) == 39
Provides:       mvn(org.apache.maven.plugins:maven-plugins:pom:) == 39
Provides:       mvn(org.apache.maven:maven-parent:pom:) == 34
Provides:       mvn(org.apache.maven.shared:maven-shared-components:pom:) == 34
Provides:       mvn(org.apache.maven:maven-parent:pom:) == 16
Provides:       mvn(org.apache.maven:maven-parent:pom:) == 10
Provides:       mvn(org.apache.maven.shared:maven-shared-components:pom:) == 15
Provides:       mvn(org.apache.maven.plugins:maven-plugins:pom:) == 45
Provides:       mvn(org.apache.maven.plugins:maven-plugins:pom:) == 35
Requires:       mvn(org.apache:apache:pom:) == 38
Requires:       mvn(org.apache:apache:pom:) == 37
Requires:       mvn(org.apache:apache:pom:) == 35
Requires:       mvn(org.apache:apache:pom:) == 33
Requires:       mvn(org.apache:apache:pom:) == 25
Requires:       mvn(org.apache:apache:pom:) == 29
Requires:       mvn(org.apache:apache:pom:) == 23
Requires:       mvn(org.apache:apache:pom:) == 7
Requires:       mvn(org.apache:apache:pom:) == 4
Requires:       mvn(org.junit:junit-bom:pom:) == 5.14.4
Requires:       mvn(org.junit:junit-bom:pom:) == 5.14.2
Requires:       mvn(org.junit:junit-bom:pom:) == 5.13.1
Requires:       mvn(org.junit:junit-bom:pom:) == 5.10.3

Provides:       mvn(org.apache.maven:maven-parent:pom:) == 44

Provides:       mvn(org.apache.maven.plugins:maven-plugins:pom:) == 47
Provides:       mvn(org.apache.maven.plugins:maven-plugins:pom:) == 44

Provides:       mvn(org.apache.maven.shared:maven-shared-components:pom:) == 47

BuildRequires:  mvn(org.apache:apache:pom:) == 34

Requires:       mvn(org.apache:apache:pom:) == 34

BuildRequires:  mvn(org.junit:junit-bom:pom:) == 5.12.1

Requires:       mvn(org.junit:junit-bom:pom:) == 5.12.1

Provides:       mvn(org.apache.maven.plugins:maven-plugins:pom:) == 48

Provides:       mvn(org.apache.maven.shared:maven-shared-components:pom:) == 43

Provides:       mvn(org.apache.maven.shared:maven-shared-components:pom:) == 48

%description
The Apache Maven parent provides shared dependency and plugin versions for Maven and its toolchain.

%prep
%autosetup -n maven-parent-maven-parent-%{version}
mkdir version-35 version-45
tar xf %{SOURCE2} --strip-components=1 -C version-45
tar xf %{SOURCE3} --strip-components=1 -C version-35

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name} pom.xml %{SOURCE1} version-{35,45}/{pom.xml,maven-plugins/pom.xml} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18}

%check
# Import each installed model through Maven with an offline repository.
mkdir -p check/{.mvn,repo}
if test -d %{_datadir}/maven-repository; then cp -as %{_datadir}/maven-repository/. check/repo/; fi
cp -a --remove-destination %{buildroot}%{_datadir}/maven-repository/. check/repo/
cd check
for coordinate in org.apache.maven.shared:maven-shared-components:48 org.apache.maven.shared:maven-shared-components:43 org.apache.maven.plugins:maven-plugins:48 org.apache.maven:maven-parent:%{version} org.apache.maven:maven-parent:47 \
    org.apache.maven:maven-parent:45 org.apache.maven:maven-parent:44 org.apache.maven:maven-parent:43 org.apache.maven:maven-parent:39 org.apache.maven.plugins:maven-plugins:39 org.apache.maven:maven-parent:35 org.apache.maven:maven-parent:34 org.apache.maven.shared:maven-shared-components:34 \
    org.apache.maven.plugins:maven-plugins:44 org.apache.maven.plugins:maven-plugins:45 org.apache.maven.plugins:maven-plugins:35 \
    org.apache.maven:maven-parent:16 org.apache.maven:maven-parent:10 org.apache.maven.shared:maven-shared-components:15 org.apache.maven.shared:maven-shared-components:47 org.apache.maven.plugins:maven-plugins:47; do
    IFS=: read -r group artifact version <<< "$coordinate"
    # The older parent models predate the JUnit BOM import.
    junit=
    if test "$version" -ge 45; then
        junit='<dependencies><dependency><groupId>org.junit.jupiter</groupId><artifactId>junit-jupiter-api</artifactId></dependency></dependencies>'
    fi
    cat > pom.xml <<EOF
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
<groupId>org.openruyi.check</groupId><artifactId>model-consumer</artifactId><version>1</version>
<dependencyManagement><dependencies><dependency>
<groupId>$group</groupId><artifactId>$artifact</artifactId><version>$version</version>
<type>pom</type><scope>import</scope></dependency></dependencies></dependencyManagement>
$junit
</project>
EOF
    %{_libexecdir}/javapackages-bootstrap/mvn --batch-mode --offline -Dmaven.repo.local="$PWD/repo" validate
done

%files
%license LICENSE
%{_datadir}/maven-metadata/maven-parent.xml
%{_datadir}/maven-repository/org/apache/maven/shared/maven-shared-components/
%{_datadir}/maven-repository/org/apache/maven/maven-parent/
%{_datadir}/maven-repository/org/apache/maven/plugins/maven-plugins/

%changelog
%autochangelog
