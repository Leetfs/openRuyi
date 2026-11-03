# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository/org/tukaani/xz/%{version}

Name:           xz-java
Version:        1.12
Release:        %autorelease
Summary:        XZ compression and random access for Java applications
License:        0BSD
URL:            https://tukaani.org/xz/java.html
VCS:            git:https://github.com/tukaani-project/xz-java
#!RemoteAsset:  sha256:cb3c097fe612a4b5e6bc58ec2d2c571b0e9a3c26049f14efaa959492d59de00b
Source0:        https://github.com/tukaani-project/xz-java/archive/refs/tags/v%{version}.tar.gz
Source1:        XzCheck.java
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  xz
Provides:       mvn(org.tukaani:xz) == %{version}
Requires:       java-25-openjdk

%description
XZ for Java reads and writes XZ streams, supports LZMA2 and block filters,
and provides seekable access to compressed files. The JAR includes its
OSGi identity and Java module descriptor.

%prep
%autosetup

%build
%{_libexecdir}/javapackages-bootstrap/ant -noinput jar pom

%install
install -Dm644 build/jar/xz.jar %{buildroot}%{repo_dir}/xz-%{version}.jar
install -m644 build/pom/xz.pom %{buildroot}%{repo_dir}/xz-%{version}.pom
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
EOF
for extension in jar pom; do
    cat >> %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
  <artifact><groupId>org.tukaani</groupId><artifactId>xz</artifactId><version>%{version}</version><extension>$extension</extension>
    <path>%{repo_dir}/xz-%{version}.$extension</path><compatVersions><version>%{version}</version><version>1.10</version><version>SYSTEM</version></compatVersions>
    <properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
EOF
done
echo '</artifacts></metadata>' >> %{buildroot}%{_datadir}/maven-metadata/%{name}.xml

%check
jar=%{buildroot}%{repo_dir}/xz-%{version}.jar
echo '937b44d869c059c39f07ae194d8cd6219f5aebf2200ef9707f0b50b7837da281  build/pom/xz.pom' | sha256sum -c -
jar --describe-module --file "$jar" --release 9 | grep -F 'org.tukaani.xz'
mkdir -p build/test-data
java -cp "$jar" %{SOURCE1} encode build/test-data
xz -dc build/test-data/java.xz | cmp - build/test-data/payload
xz -c build/test-data/payload > build/test-data/native.xz
java -cp "$jar" %{SOURCE1} verify build/test-data

%files
%doc AUTHORS.md NEWS.md README.md
%license COPYING LICENSES/0BSD.txt
%{_datadir}/maven-metadata/xz-java.xml
%{repo_dir}/

%changelog
%autochangelog
