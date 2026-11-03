# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global gav_dir %{_datadir}/maven-repository/org/codehaus/mojo/signature/java18/%{version}
%global sniffer_version 1.27

Name:           animal-sniffer-signature-java18
Version:        1.0
Release:        %autorelease
Summary:        Java 8 API reference data for Animal Sniffer
License:        Apache-2.0
URL:            https://central.sonatype.com/artifact/org.codehaus.mojo.signature/java18
#!RemoteAsset:  sha256:8cce892cfda0272e00dbdbf2acc607ffd5391734629fbdce349c5691ccf8d7fb
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/codehaus/mojo/signature/java18/%{version}/java18-%{version}.signature
#!RemoteAsset:  sha256:c6913b2cae11be98c69144840c36850be1d57fb9fc4a3c75a0e35520f8c3bacf
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/codehaus/mojo/signature/java18/%{version}/java18-%{version}.pom
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source2:        https://www.apache.org/licenses/LICENSE-2.0.txt
Source3:        CheckSignature.java
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.codehaus.mojo:animal-sniffer) == %{sniffer_version}
Provides:       mvn(org.codehaus.mojo.signature:java18:signature) == %{version}

%description
This reference lists classes, methods and fields in the Java 8 platform.
Animal Sniffer compares compiled applications against these signatures
to detect references to APIs introduced in later releases.

%prep
%setup -q -c -T
cp -p %{SOURCE2} LICENSE

%install
install -Dm644 %{SOURCE0} %{buildroot}%{gav_dir}/java18-%{version}.signature
install -Dm644 %{SOURCE1} %{buildroot}%{gav_dir}/java18-%{version}.pom
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>org.codehaus.mojo.signature</groupId><artifactId>java18</artifactId><extension>signature</extension><version>%{version}</version><path>%{gav_dir}/java18-%{version}.signature</path></artifact>
  <artifact><groupId>org.codehaus.mojo.signature</groupId><artifactId>java18</artifactId><extension>pom</extension><version>%{version}</version><path>%{gav_dir}/java18-%{version}.pom</path></artifact>
</artifacts></metadata>
EOF

%check
sniffer=%{_datadir}/maven-repository/org/codehaus/mojo/animal-sniffer/%{sniffer_version}/animal-sniffer-%{sniffer_version}.jar
java -cp "$sniffer:%{_datadir}/java/javapackages-bootstrap/*" %{SOURCE3} %{buildroot}%{gav_dir}/java18-%{version}.signature

%files
%license LICENSE
%{_datadir}/maven-metadata/animal-sniffer-signature-java18.xml
%{gav_dir}/

%changelog
%autochangelog
