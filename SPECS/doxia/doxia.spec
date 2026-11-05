# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global doxia_repo %{repo}/org/apache/maven/doxia

Name:           doxia
Version:        2.0.0
Release:        %autorelease
Summary:        Maven document processing and markup modules
License:        Apache-2.0
URL:            https://maven.apache.org/doxia/
VCS:            git:https://github.com/apache/maven-doxia
#!RemoteAsset:  sha256:46932b1aea6ee980aee484e96e4e9eedc0d2a7b192b9ed42b16a9903556fe96c
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/doxia/doxia/%{version}/doxia-%{version}-source-release.zip
Source1:        IndexNative.java
Source2:        build-doxia.sh
Source3:        check-doxia.sh
Source4:        generate-model.py
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api) == %{version}
BuildRequires:  mvn(org.apache.commons:commons-lang3) == 3.20.0
BuildRequires:  mvn(org.apache.commons:commons-text) == 1.12.0
BuildRequires:  mvn(commons-io:commons-io) == 2.21.0
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing) == 2.1.0
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
BuildRequires:  python3
BuildRequires:  unzip
Provides:       mvn(org.apache.maven.doxia:doxia-core) == %{version}
Provides:       mvn(org.apache.maven.doxia:doxia-module-fml) == %{version}
Provides:       mvn(org.apache.maven.doxia:doxia-module-apt) == %{version}
Provides:       mvn(org.apache.maven.doxia:doxia-module-xdoc) == %{version}
Provides:       mvn(org.apache.maven.doxia:doxia-module-xhtml5) == %{version}
Provides:       mvn(org.apache.maven.doxia:doxia-modules:pom:) == %{version}
Requires:       javapackages-bootstrap
Requires:       mvn(org.apache.maven.doxia:doxia-sink-api) == %{version}
Requires:       mvn(org.apache.commons:commons-lang3) == 3.20.0
Requires:       mvn(org.apache.commons:commons-text) == 1.12.0
Requires:       mvn(commons-io:commons-io) == 2.21.0

%description
Doxia parses and renders documentation using shared sink interfaces.
The core services and APT, FML, XDoc and XHTML modules support Maven reports.

%package        tests
Summary:        Shared Doxia parser and sink test fixtures
Provides:       mvn(org.apache.maven.doxia:doxia-core:jar:tests) == %{version}
Requires:       %{name} = %{version}-%{release}
Requires:       mvn(org.codehaus.plexus:plexus-testing) == 2.1.0
Requires:       mvn(org.junit.jupiter:junit-jupiter-api) == 5.12.2

%description    tests
The Doxia core test archive provides sink event recording, parser assertions
and XML validation helpers used by the Doxia Site Tools test suites.

%prep
%autosetup -n doxia-%{version}

%build
bash %{SOURCE2} %{version} %{SOURCE1} %{SOURCE4}

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name}-models doxia-modules/pom.xml
metadata=%{buildroot}%{_datadir}/maven-metadata/%{name}.xml
echo '<metadata><artifacts>' > "$metadata"
for artifact in doxia-core doxia-module-apt doxia-module-fml doxia-module-xdoc doxia-module-xhtml5; do
    source=$artifact
    if test "$artifact" != doxia-core; then source=doxia-modules/$artifact; fi
    destination=%{doxia_repo}/$artifact/%{version}
    mkdir -p "%{buildroot}$destination"
    install -m644 "$source/target/$artifact.jar" "%{buildroot}$destination/$artifact-%{version}.jar"
    install -m644 "$source/pom.xml" "%{buildroot}$destination/$artifact-%{version}.pom"
    cat >> "$metadata" <<EOF
<artifact><groupId>org.apache.maven.doxia</groupId><artifactId>$artifact</artifactId><version>%{version}</version><extension>jar</extension><path>$destination/$artifact-%{version}.jar</path><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
<artifact><groupId>org.apache.maven.doxia</groupId><artifactId>$artifact</artifactId><version>%{version}</version><extension>pom</extension><path>$destination/$artifact-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
EOF
done
echo '</artifacts></metadata>' >> "$metadata"

%check
# Exercise the original core and markup suites with their shared test documents.
bash %{SOURCE3} %{version}
# Publish the tested core fixtures under the upstream Maven tests classifier.
jar cf doxia-core/target/doxia-core-tests.jar -C doxia-core/target/test-classes .
install -Dm644 doxia-core/target/doxia-core-tests.jar %{buildroot}%{doxia_repo}/doxia-core/%{version}/doxia-core-%{version}-tests.jar
cat > %{buildroot}%{_datadir}/maven-metadata/doxia-tests.xml <<EOF
<metadata><artifacts>
<artifact><groupId>org.apache.maven.doxia</groupId><artifactId>doxia-core</artifactId><version>%{version}</version><extension>jar</extension><classifier>tests</classifier><path>%{doxia_repo}/doxia-core/%{version}/doxia-core-%{version}-tests.jar</path><compatVersions><version>%{version}</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%files
%license LICENSE NOTICE
%doc README.md
%{_datadir}/maven-metadata/doxia.xml
%{_datadir}/maven-metadata/doxia-models.xml
%{doxia_repo}/doxia-core/%{version}/
%exclude %{doxia_repo}/doxia-core/%{version}/doxia-core-%{version}-tests.jar
%{doxia_repo}/doxia-module-apt/%{version}/
%{doxia_repo}/doxia-module-fml/%{version}/
%{doxia_repo}/doxia-module-xdoc/%{version}/
%{doxia_repo}/doxia-module-xhtml5/%{version}/
%{doxia_repo}/doxia-modules/%{version}/

%files tests
%{_datadir}/maven-metadata/doxia-tests.xml
%{doxia_repo}/doxia-core/%{version}/doxia-core-%{version}-tests.jar

%changelog
%autochangelog
