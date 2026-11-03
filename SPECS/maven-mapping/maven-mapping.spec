# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository/org/apache/maven/shared/%{name}/%{version}

Name:           maven-mapping
Version:        3.0.0
Release:        %autorelease
Summary:        Artifact filename mapping for Apache Maven plugins
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-mapping/
VCS:            git:https://github.com/apache/maven-mapping
#!RemoteAsset:  sha256:853af6b2e388dedc064ef5091c890812d4cf894e37d088b1c0666a6f62467fd5
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  unzip
Provides:       mvn(org.apache.maven.shared:maven-mapping) == %{version}
Requires:       maven >= 3.9.9

%description
Maven Mapping expands filename templates using artifact coordinates,
extensions, classifiers and plugin-defined properties.

%prep
%autosetup

%build
mkdir -p build/classes
find src/main/java -name '*.java' | sort > build/sources
javac --release 8 -encoding UTF-8 -cp '%{_datadir}/maven/lib/*' -d build/classes @build/sources
install -d build/classes/META-INF
install -m644 LICENSE NOTICE build/classes/META-INF/
jar --create --file build/%{name}.jar -C build/classes .

%install
install -Dm644 build/%{name}.jar %{buildroot}%{repo_dir}/%{name}-%{version}.jar
install -m644 pom.xml %{buildroot}%{repo_dir}/%{name}-%{version}.pom
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>org.apache.maven.shared</groupId><artifactId>%{name}</artifactId><version>%{version}</version>
    <path>%{repo_dir}/%{name}-%{version}.jar</path></artifact>
  <artifact><groupId>org.apache.maven.shared</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{repo_dir}/%{name}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
cp="%{buildroot}%{repo_dir}/%{name}-%{version}.jar:%{_datadir}/maven/lib/*:%{_datadir}/java/javapackages-bootstrap/maven-plugin-testing-harness.jar:%{_datadir}/java/javapackages-bootstrap/junit.jar:%{_datadir}/java/javapackages-bootstrap/hamcrest-core.jar"
mkdir -p build/tests
find src/test/java -name '*.java' | sort > build/test-sources
javac --release 8 -encoding UTF-8 -cp "$cp" -d build/tests @build/test-sources
java -cp "build/tests:$cp" org.junit.runner.JUnitCore org.apache.maven.shared.mapping.MappingUtilsTest

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/maven-mapping.xml
%{repo_dir}/

%changelog
%autochangelog
