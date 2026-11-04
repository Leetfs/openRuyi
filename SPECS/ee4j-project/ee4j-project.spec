# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ee4j-project
Version:        1.0.9
Release:        %autorelease
Summary:        Parent Maven models for Eclipse Enterprise for Java projects
License:        EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://projects.eclipse.org/projects/ee4j
VCS:            git:https://github.com/eclipse-ee4j/ee4j
#!RemoteAsset:  sha256:15635147c296be5d2a1f3fd7dc793abc7468924c6e930cf926abb8948cf4649c
Source0:        https://github.com/eclipse-ee4j/ee4j/archive/refs/tags/%{version}.tar.gz
#!RemoteAsset:  sha256:4e7d8329d8da7dcf30779d824241be145f27108932f5a5a24eb907677bc8d72d
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/ee4j/project/1.0.6/project-1.0.6.pom
#!RemoteAsset:  sha256:205c039a42cbae3556efbeb04a483eb3a3cf9550bd75bf84260dc8f28218f105
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/ee4j/project/1.0.7/project-1.0.7.pom
BuildArch:      noarch

BuildRequires:  javapackages-bootstrap(pom-install)
Provides:       mvn(org.eclipse.ee4j:project:pom:) == %{version}
Provides:       mvn(org.eclipse.ee4j:project:pom:) == 1.0.6
Provides:       mvn(org.eclipse.ee4j:project:pom:) == 1.0.7

%description
The Eclipse EE4J parent models supply the shared build configuration used
by Jakarta Dependency Injection, Jakarta Annotations and Jakarta Servlet.

%prep
%autosetup -n ee4j-%{version}

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name} parent/pom.xml %{SOURCE1} %{SOURCE2}

%check
# Import each installed model through Maven with an offline repository.
mkdir -p check/{.mvn,repo}
if test -d %{_datadir}/maven-repository; then cp -as %{_datadir}/maven-repository/. check/repo/; fi
cp -a --remove-destination %{buildroot}%{_datadir}/maven-repository/. check/repo/
cd check
for version in %{version} 1.0.6 1.0.7; do
    cat > pom.xml <<EOF
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
<groupId>org.openruyi.check</groupId><artifactId>model-consumer</artifactId><version>1</version>
<dependencyManagement><dependencies><dependency>
<groupId>org.eclipse.ee4j</groupId><artifactId>project</artifactId><version>$version</version>
<type>pom</type><scope>import</scope></dependency></dependencies></dependencyManagement>
</project>
EOF
    %{_libexecdir}/javapackages-bootstrap/mvn --batch-mode --offline -Dmaven.repo.local="$PWD/repo" validate
done

%files
%license LICENSE.txt
%{_datadir}/maven-metadata/ee4j-project.xml
%{_datadir}/maven-repository/org/eclipse/ee4j/project/

%changelog
%autochangelog
