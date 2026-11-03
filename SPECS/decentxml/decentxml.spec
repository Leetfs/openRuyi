# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository/de/pdark/%{name}/%{version}

Name:           decentxml
Version:        1.4
Release:        %autorelease
Summary:        Java XML parser that preserves document formatting
License:        BSD-3-Clause
URL:            https://code.google.com/archive/p/decentxml/
#!RemoteAsset:  sha256:80444a15f7f40e6b995131aeb11fb8b32209652dc703b275d214780f40cabdc8
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/decentxml/decentxml-%{version}-src.zip?generation=1453524921537000#/decentxml-%{version}-src.zip
#!RemoteAsset:  sha256:4f03503040be97dc04eb2fd5c7a448d197e720f069a6c6f33eba1b2c2bb17706
Source1:        https://www.w3.org/XML/Test/xmlts20031210.zip
# Report malformed input bytes as XML decoding errors.
Patch2000:      2000-Reject-malformed-byte-sequences-in-XML-streams.patch
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  unzip
Provides:       mvn(de.pdark:decentxml) == %{version}
Requires:       java-25-openjdk

%description
DecentXML reads, edits and writes XML while preserving the original
whitespace, comments, entity references and attribute quoting.

%prep
%autosetup -p1
unzip -q %{SOURCE1} 'xmlconf/xmltest/*' -d ..
test -s ../xmlconf/xmltest/valid/sa/001.xml

%build
mkdir -p build/classes
find src/main/java -name '*.java' | sort > build/sources
javac --release 8 -encoding UTF-8 -d build/classes @build/sources
jar --create --file build/%{name}.jar -C build/classes .

%install
install -Dm644 build/%{name}.jar %{buildroot}%{repo_dir}/%{name}-%{version}.jar
install -m644 pom.xml %{buildroot}%{repo_dir}/%{name}-%{version}.pom
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>de.pdark</groupId><artifactId>%{name}</artifactId><version>%{version}</version>
    <path>%{repo_dir}/%{name}-%{version}.jar</path></artifact>
  <artifact><groupId>de.pdark</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{repo_dir}/%{name}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
cp="%{buildroot}%{repo_dir}/%{name}-%{version}.jar:%{_datadir}/java/javapackages-bootstrap/junit.jar:%{_datadir}/java/javapackages-bootstrap/hamcrest-core.jar"
mkdir -p build/tests
find src/test/java -name '*.java' | sort > build/test-sources
# The namespace test contains a Latin-1 XML literal.
javac --release 8 -encoding ISO-8859-1 -cp "$cp" -d build/tests @build/test-sources
sed -n '/Test\.java$/ {s|^src/test/java/||; s|/|.|g; s|\.java$||; p;}' build/test-sources > build/test-classes
mapfile -t tests < build/test-classes
java -cp "build/tests:$cp" org.junit.runner.JUnitCore "${tests[@]}"

%files
%doc README
%license LICENSE
%{_datadir}/maven-metadata/decentxml.xml
%{repo_dir}/

%changelog
%autochangelog
