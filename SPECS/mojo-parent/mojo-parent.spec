# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mojo-parent
Version:        94
Release:        %autorelease
Summary:        Parent Maven model for MojoHaus projects
License:        Apache-2.0
URL:            https://www.mojohaus.org/mojo-parent/
VCS:            git:https://github.com/mojohaus/mojo-parent
#!RemoteAsset:  sha256:641e90e0b70f34ad14d2473aef9b81bc039edff573f2f8b37eecd4cc6869dc03
Source0:        https://github.com/mojohaus/mojo-parent/archive/refs/tags/%{version}.tar.gz?/mojo-parent-%{version}.tar.gz
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
#!RemoteAsset:  sha256:6c75af0e0cfae6a7e3fb4db3478771d6c5d65a9a238c35dc6410f153d81877b1
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/codehaus/mojo/mojo-parent/91/mojo-parent-91.pom
BuildArch:      noarch

BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  mvn(org.junit:junit-bom:pom:) == 5.14.0
BuildRequires:  mvn(org.junit:junit-bom:pom:) == 5.13.0
Provides:       mvn(org.codehaus.mojo:mojo-parent:pom:) == %{version}
Requires:       mvn(org.junit:junit-bom:pom:) == 5.13.0
Requires:       mvn(org.junit:junit-bom:pom:) == 5.14.0

Provides:       mvn(org.codehaus.mojo:mojo-parent:pom:) == 91

%description
The MojoHaus parent defines build properties and dependency versions shared
by MojoHaus libraries and Maven plugins, including Extra Enforcer Rules.

%prep
%autosetup -n mojo-parent-%{version}
cp %{SOURCE1} LICENSE.txt

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name} pom.xml %{SOURCE2}

%check
# Resolve the parent and the JUnit API version it imports through an empty Maven project.
mkdir -p check/{.mvn,repo}
cp -as %{_datadir}/maven-repository/. check/repo/
cp -a --remove-destination %{buildroot}%{_datadir}/maven-repository/. check/repo/
cd check
for version in %{version} 91; do
cat > pom.xml <<EOF
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
<groupId>org.openruyi.check</groupId><artifactId>consumer</artifactId><version>1</version>
<dependencyManagement><dependencies><dependency><groupId>org.codehaus.mojo</groupId>
<artifactId>mojo-parent</artifactId><version>$version</version><type>pom</type><scope>import</scope>
</dependency></dependencies></dependencyManagement>
<dependencies><dependency><groupId>org.junit.jupiter</groupId><artifactId>junit-jupiter-api</artifactId></dependency></dependencies>
</project>
EOF
%{_libexecdir}/javapackages-bootstrap/mvn --batch-mode --offline -Dmaven.repo.local="$PWD/repo" validate
done

%files
%license LICENSE.txt
%doc README.md
%{_datadir}/maven-metadata/mojo-parent.xml
%{_datadir}/maven-repository/org/codehaus/mojo/mojo-parent/

%changelog
%autochangelog
