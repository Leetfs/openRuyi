# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jackson-bom
Version:        2.22.2
Release:        %autorelease
Summary:        Maven dependency management for Jackson
License:        Apache-2.0
URL:            https://github.com/FasterXML/jackson-bom
VCS:            git:https://github.com/FasterXML/jackson-bom
#!RemoteAsset:  sha256:a93ad5b8462f8d5920b128647a9b9f236342b4fd4e71287da9f7187fd8642f02
Source0:        https://maven-central.storage-download.googleapis.com/maven2/com/fasterxml/jackson/jackson-bom/2.22.2/jackson-bom-2.22.2.pom
#!RemoteAsset:  sha256:7d45a7efb69df207bed7cc54b87a0bb012f10952c095570a273b49485da0d129
Source1:        https://maven-central.storage-download.googleapis.com/maven2/com/fasterxml/jackson/jackson-parent/2.22/jackson-parent-2.22.pom
#!RemoteAsset:  sha256:9206b7dd67fb138036576c3dfca947a2a8f3e2c4d2d9c1f2d1dea519b3a4dae1
Source2:        https://maven-central.storage-download.googleapis.com/maven2/com/fasterxml/oss-parent/79/oss-parent-79.pom
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source3:        https://raw.githubusercontent.com/FasterXML/jackson-bom/062d76d67a3619238e00d4d62f9bdb51cfe6cd52/LICENSE?/jackson-bom-LICENSE
#!RemoteAsset:  sha256:c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4
Source4:        https://raw.githubusercontent.com/FasterXML/oss-parent/c2c66103363fb80978a365494418c2da361236a7/LICENSE?/oss-parent-LICENSE
BuildArch:      noarch
BuildRequires:  javapackages-bootstrap(pom-install)
Provides:       mvn(com.fasterxml.jackson:jackson-bom:pom:) == 2.22.2
Provides:       mvn(com.fasterxml.jackson:jackson-parent:pom:) == 2.22
Provides:       mvn(com.fasterxml:oss-parent:pom:) == 79

%description
The Jackson BOM and its parent models select a consistent set of Jackson
artifact versions for Maven applications.

%prep
%setup -q -c -T
cp %{SOURCE3} jackson-bom-LICENSE
cp %{SOURCE4} oss-parent-LICENSE

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name} %{SOURCE0} %{SOURCE1} %{SOURCE2}

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
<groupId>com.fasterxml.jackson</groupId><artifactId>jackson-bom</artifactId><version>2.22.2</version>
<type>pom</type><scope>import</scope></dependency></dependencies></dependencyManagement>
<dependencies><dependency><groupId>com.fasterxml.jackson.core</groupId><artifactId>jackson-core</artifactId></dependency></dependencies>
</project>
EOF
%{_libexecdir}/javapackages-bootstrap/mvn -B -o -Dmaven.repo.local="$PWD/repo" validate

%files
%license jackson-bom-LICENSE oss-parent-LICENSE
%{_datadir}/maven-metadata/jackson-bom.xml
%{_datadir}/maven-repository/com/fasterxml/jackson/jackson-bom/2.22.2/
%{_datadir}/maven-repository/com/fasterxml/jackson/jackson-parent/2.22/
%{_datadir}/maven-repository/com/fasterxml/oss-parent/79/

%changelog
%autochangelog
