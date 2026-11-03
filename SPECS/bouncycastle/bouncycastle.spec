# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository/org/bouncycastle

Name:           bouncycastle
Version:        1.86
Release:        %autorelease
Summary:        Java cryptography provider and OpenPGP implementation
License:        MIT AND Apache-2.0
URL:            https://www.bouncycastle.org/
VCS:            git:https://github.com/bcgit/bc-java
#!RemoteAsset:  sha256:e3ecdb75d17f5cceac19cad6dc5f462b536e2b6a64935960fa51222e2f612727
Source0:        https://github.com/bcgit/bc-java/archive/refs/tags/r1rv86.tar.gz
#!RemoteAsset:  sha256:970b70cb75a184639b6fb9ba3c465aca6a4e1a5f3fff4d65ce8574b2fd79ef38
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/bouncycastle/bcprov-jdk18on/%{version}/bcprov-jdk18on-%{version}.pom
#!RemoteAsset:  sha256:2209b3e5d1eb2bb3c593b824c1b8f142b05dea8e9df7400b0f33f2b91a0741fa
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/bouncycastle/bcutil-jdk18on/%{version}/bcutil-jdk18on-%{version}.pom
#!RemoteAsset:  sha256:d3d5dd3151038d94e0bfdd5930da4961b9d7e30932229cced0b5bf452246bd72
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/bouncycastle/bcpg-jdk18on/%{version}/bcpg-jdk18on-%{version}.pom
Source4:        build-openpgp.xml
Source5:        complete-jars.py
Source6:        WrapBundle.java
Source7:        RunVectors.java
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source8:        https://www.apache.org/licenses/LICENSE-2.0.txt
Patch2000:      2000-Place-MOD-identifiers-in-bcutil.patch
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  python3
Provides:       mvn(org.bouncycastle:bcpg-jdk18on) == %{version}
Provides:       mvn(org.bouncycastle:bcprov-jdk18on) == %{version}
Provides:       mvn(org.bouncycastle:bcutil-jdk18on) == %{version}
Requires:       java-25-openjdk

%description
Bouncy Castle implements cryptographic primitives, Java security providers
and an OpenPGP API. These libraries read keys and packets, generate and
verify signatures and implement the encodings shared by the provider
and OpenPGP modules.

%prep
%autosetup -n bc-java-r1rv86 -p1
cp %{SOURCE4} build-openpgp.xml
cp -p %{SOURCE8} LICENSE-Apache-2.0.txt
mkdir -p core/src/test/data core/src/main/resources
for module in core prov tls pkix pg mail util jmail; do mkdir -p "$module/src/test/resources"; done
mkdir -p build/poms
cp %{SOURCE1} build/poms/bcprov.pom
cp %{SOURCE2} build/poms/bcutil.pom
cp %{SOURCE3} build/poms/bcpg.pom

%build
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
%{_libexecdir}/javapackages-bootstrap/ant -f build-openpgp.xml -Djunit.jar.home=%{_datadir}/java/javapackages-bootstrap/junit.jar \
    -Drelease.debug=true -Dbc.javac.source=1.8 -Dbc.javac.target=1.8 openpgp
%{_bindir}/python3 %{SOURCE5} %{version} %{SOURCE6}

%install
metadata=%{buildroot}%{_datadir}/maven-metadata/%{name}.xml
install -d "$(dirname "$metadata")"
echo '<metadata><artifacts>' > "$metadata"
for module in bcprov bcutil bcpg; do
    artifact=$module-jdk18on
    directory=%{repo_dir}/$artifact/%{version}
    install -Dm644 build/openruyi/$artifact-%{version}.jar %{buildroot}$directory/$artifact-%{version}.jar
    install -m644 build/poms/$module.pom %{buildroot}$directory/$artifact-%{version}.pom
    for extension in pom jar; do
        cat >> "$metadata" <<EOF
<artifact><groupId>org.bouncycastle</groupId><artifactId>$artifact</artifactId>
<extension>$extension</extension><version>%{version}</version><path>$directory/$artifact-%{version}.$extension</path>
<compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions>
<properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
EOF
    done
done
echo '</artifacts></metadata>' >> "$metadata"

%check
jars="build/openruyi/*:%{_datadir}/java/javapackages-bootstrap/junit.jar:%{_datadir}/java/javapackages-bootstrap/hamcrest-core.jar"
mkdir -p build/openpgp-tests
find pg/src/test/java -name '*.java' | sort > build/pg-test-sources
javac -encoding UTF-8 -cp "$jars" -d build/openpgp-tests \
    -sourcepath pg/src/test/java:core/src/test/java \
    @build/pg-test-sources \
    core/src/test/java/org/bouncycastle/crypto/test/SHA256DigestTest.java \
    core/src/test/java/org/bouncycastle/crypto/test/AESTest.java %{SOURCE7}
java -cp "build/openpgp-tests:$jars:pg/src/test/resources" org.junit.runner.JUnitCore \
    org.bouncycastle.bcpg.test.AllTests org.bouncycastle.gpg.keybox.AllTests org.bouncycastle.gpg.test.AllTests \
    org.bouncycastle.openpgp.api.test.AllTests org.bouncycastle.openpgp.test.AllTests
java -cp "build/openpgp-tests:$jars" org.bouncycastle.crypto.test.RunVectors

%files
%doc README.md
%license LICENSE.md LICENSE.html LICENSE-Apache-2.0.txt
%{_datadir}/maven-metadata/bouncycastle.xml
%{repo_dir}/bcpg-jdk18on/
%{repo_dir}/bcprov-jdk18on/
%{repo_dir}/bcutil-jdk18on/

%changelog
%autochangelog
