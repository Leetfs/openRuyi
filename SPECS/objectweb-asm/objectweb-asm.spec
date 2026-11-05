# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
Name:           objectweb-asm
Version:        9.10.1
Release:        %autorelease
Summary:        Java bytecode manipulation and analysis framework
License:        BSD-3-Clause
URL:            https://asm.ow2.io/
VCS:            git:https://gitlab.ow2.org/asm/asm
#!RemoteAsset:  sha256:ef72ea058b91514b750165591d7245c23bc3c60e11e14933f23a0cc4bc69b08c
Source0:        https://gitlab.ow2.org/asm/asm/-/archive/ASM_9_10_1/asm-ASM_9_10_1.tar.gz
#!RemoteAsset:  sha256:e1b1c3832ca3ac0a9e563c405f4c760118b5556a4920daee14058886197e094d
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/ow2/asm/asm/%{version}/asm-%{version}.pom
#!RemoteAsset:  sha256:963eebdea6e2e1ff25c9068b64a238e1585c99f8acd455595ac159a7f52b6c41
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/ow2/asm/asm-tree/%{version}/asm-tree-%{version}.pom
#!RemoteAsset:  sha256:534fbb85f643c2330691e92652ec40dd497b4f279ef13d829d85858905d33ba3
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/ow2/asm/asm-analysis/%{version}/asm-analysis-%{version}.pom
#!RemoteAsset:  sha256:ceb2c43f3a273db88af8652d89ed6312f3e91a1a1e0ffc6f7823169278cf795c
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/ow2/asm/asm-commons/%{version}/asm-commons-%{version}.pom
#!RemoteAsset:  sha256:fcea2bad7868ed18949a2e71c40cf26de1516d16440e63f585c3e05d285c0d2b
Source5:        https://maven-central.storage-download.googleapis.com/maven2/org/ow2/asm/asm-util/%{version}/asm-util-%{version}.pom
#!RemoteAsset:  sha256:83f0a83d0df77336a8d494dc73a1df2f036eb9005fa343923d5f6e6b4e158c7e
Source6:        https://maven-central.storage-download.googleapis.com/maven2/org/codehaus/janino/janino/3.1.9/janino-3.1.9-sources.jar
#!RemoteAsset:  sha256:b73148103e9742876db23469d8c34498376116f5b220eca887f446b50d727eed
Source7:        https://maven-central.storage-download.googleapis.com/maven2/org/codehaus/janino/commons-compiler/3.1.9/commons-compiler-3.1.9-sources.jar
Source8:        build-asm.py
Source9:        RetrofitModule.java
Source10:       check-asm.sh
Patch0:         0001-use-method-parameters-for-lambda-remapping.patch
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
BuildRequires:  mvn(org.ow2:ow2:pom:) == 1.5.1
BuildRequires:  python3
BuildRequires:  unzip
Provides:       mvn(org.ow2.asm:asm) == %{version}
Provides:       mvn(org.ow2.asm:asm-tree) == %{version}
Provides:       mvn(org.ow2.asm:asm-analysis) == %{version}
Provides:       mvn(org.ow2.asm:asm-commons) == %{version}
Provides:       mvn(org.ow2.asm:asm-util) == %{version}
Requires:       mvn(org.ow2:ow2:pom:) == 1.5.1

%description
ASM reads, creates and transforms Java classes. Its tree, analysis, commons
and utility modules provide higher-level visitors and bytecode verification.

%prep
%autosetup -n asm-ASM_9_10_1 -p1

%build
python3 %{SOURCE8} %{version} %{SOURCE9}

%install
metadata=%{buildroot}%{_datadir}/maven-metadata/%{name}.xml
install -d "$(dirname "$metadata")"
echo '<metadata><artifacts>' > "$metadata"
for pom in %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5}; do
    n=$(basename "$pom" -%{version}.pom)
    dir=%{repo}/org/ow2/asm/$n/%{version}
    install -Dm644 "build/bundles/$n.jar" "%{buildroot}$dir/$n-%{version}.jar"
    install -m644 "$pom" "%{buildroot}$dir/$n-%{version}.pom"
    cat >> "$metadata" <<EOF
<artifact><groupId>org.ow2.asm</groupId><artifactId>$n</artifactId><version>%{version}</version><extension>jar</extension><path>$dir/$n-%{version}.jar</path><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
<artifact><groupId>org.ow2.asm</groupId><artifactId>$n</artifactId><version>%{version}</version><extension>pom</extension><path>$dir/$n-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
EOF
done
echo '</artifacts></metadata>' >> "$metadata"

%check
bash %{SOURCE10} %{SOURCE6} %{SOURCE7}

%files
%license LICENSE.txt
%{_datadir}/maven-metadata/objectweb-asm.xml
%{repo}/org/ow2/asm/asm/
%{repo}/org/ow2/asm/asm-tree/
%{repo}/org/ow2/asm/asm-analysis/
%{repo}/org/ow2/asm/asm-commons/
%{repo}/org/ow2/asm/asm-util/

%changelog
%autochangelog
