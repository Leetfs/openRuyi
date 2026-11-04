# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           apache-parent
Version:        38
Release:        %autorelease
Summary:        Parent Maven models for Apache software
License:        Apache-2.0
URL:            https://maven.apache.org/pom/
VCS:            git:https://github.com/apache/maven-apache-parent
#!RemoteAsset:  sha256:0510ea280b414d49e777822118d970288110652f846b59c01a99b9416d10e9f9
Source0:        https://github.com/apache/maven-apache-parent/archive/refs/tags/apache-%{version}.tar.gz
#!RemoteAsset:  sha256:524ec4787aff73af6b3a9fafa154c7f1881b648299b663fdbfcadda1286f2353
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/apache/37/apache-37.pom
#!RemoteAsset:  sha256:ea297dcd114136e8b8e8b630230d52a76c2fc69f6c5db25d672b1857000728b8
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/apache/35/apache-35.pom
#!RemoteAsset:  sha256:e68fc19a48cec582a6732fd0b10dbfe9feca25060963def89e547f8a3759d379
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/apache/25/apache-25.pom
#!RemoteAsset:  sha256:9e9323a26ba8eb2394efef0c96d31b70df570808630dc147cab1e73541cc5194
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/apache/4/apache-4.pom
#!RemoteAsset:  sha256:1397ce1db433adc9f223dbf07496d133681448751f4ae29e58f68e78fb4b6c25
Source5:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/apache/7/apache-7.pom
#!RemoteAsset:  sha256:d78bd8524c5f8380a190a6525686629a95dfe512df21111383a6d8c0923a4415
Source6:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/apache/33/apache-33.pom
#!RemoteAsset:  sha256:3671ae9d4d062ae3bb985731c76088bb2f6f7d7254e2d304ee9f690b97651328
Source7:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/apache/34/apache-34.pom
#!RemoteAsset:  sha256:e18874396fa7e5fe74759292a6412b170be0a87f9f3f757656016becf1ea3459
Source8:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/apache/36/apache-36.pom
#!RemoteAsset:  sha256:bc10624e0623f36577fac5639ca2936d3240ed152fb6d8d533ab4d270543491c
Source9:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/apache/23/apache-23.pom
#!RemoteAsset:  sha256:3e49037174820bbd0df63420a977255886398954c2a06291fa61f727ac35b377
Source10:       https://maven-central.storage-download.googleapis.com/maven2/org/apache/apache/29/apache-29.pom
#!RemoteAsset:  sha256:555d0c9eaa69c042aff924927b9381e8f8174136d355eead445224452e6291cc
Source11:       https://maven-central.storage-download.googleapis.com/maven2/org/apache/apache/31/apache-31.pom
#!RemoteAsset:  sha256:4946e60a547c8eda69f3bc23c5b6f0dadcf8469ea49b1d1da7de34aecfcf18dd
Source12:       https://maven-central.storage-download.googleapis.com/maven2/org/apache/apache/9/apache-9.pom
BuildArch:      noarch

BuildRequires:  javapackages-bootstrap(pom-install)
Provides:       mvn(org.apache:apache:pom:) == %{version}
Provides:       mvn(org.apache:apache:pom:) == 33
Provides:       mvn(org.apache:apache:pom:) == 37
Provides:       mvn(org.apache:apache:pom:) == 35
Provides:       mvn(org.apache:apache:pom:) == 29
Provides:       mvn(org.apache:apache:pom:) == 25
Provides:       mvn(org.apache:apache:pom:) == 23
Provides:       mvn(org.apache:apache:pom:) == 7
Provides:       mvn(org.apache:apache:pom:) == 4

Provides:       mvn(org.apache:apache:pom:) == 34

Provides:       mvn(org.apache:apache:pom:) == 36

Provides:       mvn(org.apache:apache:pom:) == 31

Provides:       mvn(org.apache:apache:pom:) == 9

%description
These release models provide the shared parent settings inherited by Apache Maven and Commons projects.

%prep
%autosetup -n maven-apache-parent-apache-%{version}

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name} pom.xml %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12}

%check
# Import each installed model through Maven with an offline repository.
mkdir -p check/{.mvn,repo}
if test -d %{_datadir}/maven-repository; then cp -as %{_datadir}/maven-repository/. check/repo/; fi
cp -a --remove-destination %{buildroot}%{_datadir}/maven-repository/. check/repo/
cd check
for version in 9 31 %{version} 37 36 35 34 33 29 25 23 7 4; do
    cat > pom.xml <<EOF
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
<groupId>org.openruyi.check</groupId><artifactId>model-consumer</artifactId><version>1</version>
<dependencyManagement><dependencies><dependency>
<groupId>org.apache</groupId><artifactId>apache</artifactId><version>$version</version>
<type>pom</type><scope>import</scope></dependency></dependencies></dependencyManagement>
</project>
EOF
    %{_libexecdir}/javapackages-bootstrap/mvn --batch-mode --offline -Dmaven.repo.local="$PWD/repo" validate
done

%files
%license LICENSE
%{_datadir}/maven-metadata/apache-parent.xml
%{_datadir}/maven-repository/org/apache/apache/

%changelog
%autochangelog
