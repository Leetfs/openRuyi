# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jacoco
Version:        0.8.14
Release:        %autorelease
Summary:        Java code coverage agent, reports and Maven plugin
License:        EPL-2.0 AND BSD-3-Clause AND Apache-2.0
URL:            https://www.jacoco.org/
VCS:            git:https://github.com/jacoco/jacoco
#!RemoteAsset:  sha256:764d75713a41473241b2bb88a69f813f786c87c8a6a5e6f7372b819f70e90bd4
Source0:        https://github.com/jacoco/jacoco/archive/refs/tags/v%{version}.tar.gz?/jacoco-%{version}.tar.gz
#!RemoteAsset:  sha256:f1a04ff2a01c443afa6697b3b85c35ef4e891730c9c8b7fb97e41b03fed8b794
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/jacoco/jacoco-maven-plugin/%{version}/jacoco-maven-plugin-%{version}-sources.jar
Source2:        build-jacoco.py
Source3:        install-jacoco.py
Source4:        check-jacoco.sh
BuildArch:      noarch
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin) == 3.6.1
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api) == 3.0
BuildRequires:  mvn(org.eclipse.jdt:ecj) == 3.32.0
BuildRequires:  mvn(org.ow2.asm:asm-bom:pom:) == 9.9
BuildRequires:  python3
BuildRequires:  unzip
Provides:       mvn(org.jacoco:jacoco-maven-plugin) == %{version}
Provides:       mvn(org.jacoco:org.jacoco.agent) == %{version}
Provides:       mvn(org.jacoco:org.jacoco.agent:jar:runtime) == %{version}
Provides:       mvn(org.jacoco:org.jacoco.build:pom:) == %{version}
Provides:       mvn(org.jacoco:org.jacoco.core) == %{version}
Provides:       mvn(org.jacoco:org.jacoco.report) == %{version}
Requires:       javapackages-bootstrap
Requires:       maven >= 3.9.9
Requires:       mvn(org.apache.maven.reporting:maven-reporting-api) == 3.0
Requires:       mvn(org.ow2.asm:asm-bom:pom:) == 9.9

%description
JaCoCo measures instruction, branch and line coverage of Java programs.
The runtime agent instruments classes as they load. The Maven plugin also
supports offline instrumentation and generates coverage reports.

%prep
%autosetup -n jacoco-%{version}
# The source classifier contains the generated help goal for this release.
unzip -p %{SOURCE1} org/jacoco/maven/HelpMojo.java > jacoco-maven-plugin/src/org/jacoco/maven/HelpMojo.java
test -s jacoco-maven-plugin/src/org/jacoco/maven/HelpMojo.java

%build
python3 %{SOURCE2}

%install
python3 %{SOURCE3} %{buildroot} %{_datadir}

%check
bash %{SOURCE4} %{buildroot}

%files
%license LICENSE.md org.jacoco.build/licenses/asm-9.9.html org.jacoco.build/licenses/googlecodeprettify-20100721.html
%{_datadir}/maven-metadata/jacoco.xml
%{_datadir}/maven-repository/org/jacoco/

%changelog
%autochangelog
