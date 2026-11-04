# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           commons-parent
Version:        97
Release:        %autorelease
Summary:        Parent Maven model for Apache Commons projects
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-parent/
VCS:            git:https://github.com/apache/commons-parent
#!RemoteAsset:  sha256:b746bd35a5d824d1e310b3ed05e9452fdb54cab23cc28f16e482237439c364ec
Source0:        https://github.com/apache/commons-parent/archive/refs/tags/rel/commons-parent-%{version}.tar.gz
#!RemoteAsset:  sha256:17f40e7a20fcff77da81589c86db7458ca121454be606349f4959a7fcc26b84b
Source1:        https://github.com/apache/commons-parent/archive/refs/tags/rel/commons-parent-93.tar.gz
#!RemoteAsset:  sha256:2e57ca341b73efab756c35d43be3063aa82013fbd52414e93b835aeddde6effb
Source2:        https://github.com/apache/commons-parent/archive/refs/tags/rel/commons-parent-91.tar.gz
#!RemoteAsset:  sha256:d2af8747b8cb006a8ee286d02542645f72aa84e1b34f6a8c37b5133411ae9371
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/commons/commons-parent/95/commons-parent-95.pom
#!RemoteAsset:  sha256:94f6c027b15f6402995dd1b2c7ea35bfe1ebc88b6832b3134368b41998721953
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/commons/commons-parent/92/commons-parent-92.pom
#!RemoteAsset:  sha256:d50da9c39bdca823d618d1b4a03b73f196497fcb8616fd0da727c8623592a9bb
Source5:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/commons/commons-parent/69/commons-parent-69.pom
#!RemoteAsset:  sha256:fb8c5e55e30a7addb4ff210858a0e8d2494ed6757bbe19012da99d51586c3cbb
Source6:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/commons/commons-parent/22/commons-parent-22.pom
BuildArch:      noarch

BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  mvn(org.apache:apache:pom:) == 35
BuildRequires:  mvn(org.apache:apache:pom:) == 37
BuildRequires:  mvn(org.junit:junit-bom:pom:) == 5.13.4
BuildRequires:  mvn(org.junit:junit-bom:pom:) == 5.14.1
BuildRequires:  mvn(org.junit:junit-bom:pom:) == 5.14.2
Provides:       mvn(org.apache.commons:commons-parent:pom:) == 91
Provides:       mvn(org.apache.commons:commons-parent:pom:) == 93
Provides:       mvn(org.apache.commons:commons-parent:pom:) == 92
Provides:       mvn(org.apache.commons:commons-parent:pom:) == %{version}
Requires:       mvn(org.apache:apache:pom:) == 35
Requires:       mvn(org.apache:apache:pom:) == 37
Requires:       mvn(org.junit:junit-bom:pom:) == 5.13.4
Requires:       mvn(org.junit:junit-bom:pom:) == 5.14.1
Requires:       mvn(org.junit:junit-bom:pom:) == 5.14.2

Provides:       mvn(org.apache.commons:commons-parent:pom:) == 95

BuildRequires:  mvn(org.apache:apache:pom:) == 36

Requires:       mvn(org.apache:apache:pom:) == 36

Provides:       mvn(org.apache.commons:commons-parent:pom:) == 69

BuildRequires:  mvn(org.apache:apache:pom:) == 31
Requires:       mvn(org.apache:apache:pom:) == 31

BuildRequires:  mvn(org.junit:junit-bom:pom:) == 5.10.2
Requires:       mvn(org.junit:junit-bom:pom:) == 5.10.2

Provides:       mvn(org.apache.commons:commons-parent:pom:) == 22

BuildRequires:  mvn(org.apache:apache:pom:) == 9
Requires:       mvn(org.apache:apache:pom:) == 9

%description
The Commons parent manages dependency versions and shared build settings used by Apache Commons components.

%prep
%autosetup -n commons-parent-rel-commons-parent-%{version}
tar -xOf %{SOURCE1} commons-parent-rel-commons-parent-93/pom.xml > commons-parent-93.pom
tar -xOf %{SOURCE2} commons-parent-rel-commons-parent-91/pom.xml > commons-parent-91.pom

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name} commons-parent-91.pom commons-parent-93.pom pom.xml %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6}

%check
# Import each installed model through Maven with an offline repository.
mkdir -p check/{.mvn,repo}
if test -d %{_datadir}/maven-repository; then cp -as %{_datadir}/maven-repository/. check/repo/; fi
cp -a --remove-destination %{buildroot}%{_datadir}/maven-repository/. check/repo/
cd check
for version in 22 69 91 92 93 95 %{version}; do
    dependency='<dependencies><dependency><groupId>org.junit.jupiter</groupId><artifactId>junit-jupiter-api</artifactId></dependency></dependencies>'
    # Version 22 predates the JUnit Jupiter dependency management.
    if test "$version" = 22; then dependency=; fi
    cat > pom.xml <<EOF
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
<groupId>org.openruyi.check</groupId><artifactId>model-consumer</artifactId><version>1</version>
<dependencyManagement><dependencies><dependency>
<groupId>org.apache.commons</groupId><artifactId>commons-parent</artifactId><version>$version</version>
<type>pom</type><scope>import</scope></dependency></dependencies></dependencyManagement>
$dependency
</project>
EOF
    %{_libexecdir}/javapackages-bootstrap/mvn --batch-mode --offline -Dmaven.repo.local="$PWD/repo" validate
done

%files
%license LICENSE.txt NOTICE.txt
%{_datadir}/maven-metadata/commons-parent.xml
%{_datadir}/maven-repository/org/apache/commons/commons-parent/

%changelog
%autochangelog
