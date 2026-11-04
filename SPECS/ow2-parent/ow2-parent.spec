# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ow2-parent
Version:        1.5.1
Release:        %autorelease
Summary:        OW2 parent Maven model
License:        Apache-2.0
URL:            https://gitlab.ow2.org/ow2-lifecycle/ow2-parent-pom
VCS:            git:https://gitlab.ow2.org/ow2-lifecycle/ow2-parent-pom
#!RemoteAsset:  sha256:321ddbb7ee6fe4f53dea6b4cd6db74154d6bfa42391c1f763b361b9f485acf05
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/ow2/ow2/1.5.1/ow2-1.5.1.pom
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt?/ow2-LICENSE
BuildArch:      noarch
BuildRequires:  javapackages-bootstrap(pom-install)
Provides:       mvn(org.ow2:ow2:pom:) == 1.5.1

%description
The OW2 parent model supplies shared Maven settings used by projects
hosted by OW2.

%prep
%setup -q -c -T
cp %{SOURCE1} ow2-LICENSE

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
<groupId>org.ow2</groupId><artifactId>ow2</artifactId><version>1.5.1</version>
<type>pom</type><scope>import</scope></dependency></dependencies></dependencyManagement>
</project>
EOF
%{_libexecdir}/javapackages-bootstrap/mvn -B -o -Dmaven.repo.local="$PWD/repo" validate

%files
%license ow2-LICENSE
%{_datadir}/maven-metadata/ow2-parent.xml
%{_datadir}/maven-repository/org/ow2/ow2/1.5.1/

%changelog
%autochangelog
