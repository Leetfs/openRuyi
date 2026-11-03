# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository/biz/aQute/bnd
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
%global xmvn_ext %{_datadir}/javapackages-bootstrap/maven/lib/ext
%global modules biz.aQute.bnd.util biz.aQute.bndlib biz.aQute.repository biz.aQute.resolve biz.aQute.bnd.maven bnd-maven-plugin

Name:           bnd-maven-plugin
Version:        7.2.3
Release:        %autorelease
Summary:        Bnd Maven plugin and OSGi repository libraries
License:        (Apache-2.0 OR EPL-2.0) AND Apache-2.0 AND LicenseRef-openRuyi-Public-Domain
URL:            https://bnd.bndtools.org/
VCS:            git:https://github.com/bndtools/bnd
#!RemoteAsset:  sha256:9a288c44bae4cc71dedfe28cb3dd334df4f124dc18465bf578956fd6b233e1f3
Source0:        https://github.com/bndtools/bnd/archive/refs/tags/%{version}.tar.gz
#!RemoteAsset:  sha256:ea6237dd8e96e14396e1162addd0cd8e9d1910eded54d9a9a94842798f9a8654
Source1:        https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/biz.aQute.bnd.util/%{version}/biz.aQute.bnd.util-%{version}-sources.jar
#!RemoteAsset:  sha256:a3d9ce9ddfde800b1aa6b817e449fa7a376678c6fb8ecebf99f3a23377bea274
Source2:        https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/biz.aQute.bndlib/%{version}/biz.aQute.bndlib-%{version}-sources.jar
#!RemoteAsset:  sha256:b9d2138061dbddf5ed19b7b147b7662c3a3c160ca5a3001ea8edb81639af4bae
Source3:        https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/biz.aQute.resolve/%{version}/biz.aQute.resolve-%{version}-sources.jar
#!RemoteAsset:  sha256:ff58c7ffa7ac8b4c87b0fe29bb7e4f9ecf91dfda598f5cd535c5278e23e5c449
Source4:        https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/biz.aQute.repository/%{version}/biz.aQute.repository-%{version}-sources.jar
#!RemoteAsset:  sha256:11b41ec7fa4414bc04701084c7ad1f9b6771445823025977b0ad80b1bdf14a33
Source5:        https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/biz.aQute.bnd.maven/%{version}/biz.aQute.bnd.maven-%{version}-sources.jar
#!RemoteAsset:  sha256:fc6ae6543147caffab0f5d4ac2f4c80d973cc123c3d7a1de6559bdeb7c73144d
Source6:        https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/bnd-maven-plugin/%{version}/bnd-maven-plugin-%{version}-sources.jar
#!RemoteAsset:  sha256:e17cdc6436b8dd96d38872adc95b2ee02ac8468aaf9e028ca1bb79e61a62cdfa
Source7:        https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/biz.aQute.bnd.util/%{version}/biz.aQute.bnd.util-%{version}.pom
#!RemoteAsset:  sha256:3f4dde54fe2cd76ee83cfaab1d968d334b142262cef1ac0ed824d07fe09bec01
Source8:        https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/biz.aQute.bndlib/%{version}/biz.aQute.bndlib-%{version}.pom
#!RemoteAsset:  sha256:7f0e8015e226723854fecd09702681a5dcc361395f39f68af7a2bb527a99fdbd
Source9:        https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/biz.aQute.resolve/%{version}/biz.aQute.resolve-%{version}.pom
#!RemoteAsset:  sha256:ba9736e4001d85300dcd64e7473615fcda6d8ef4fce0f2329e584b2d65560bf1
Source10:       https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/biz.aQute.repository/%{version}/biz.aQute.repository-%{version}.pom
#!RemoteAsset:  sha256:4c64b862f601c51df17bc8762a986c84fc0e879c52cc854a022e5861d434e044
Source11:       https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/biz.aQute.bnd.maven/%{version}/biz.aQute.bnd.maven-%{version}.pom
#!RemoteAsset:  sha256:2168ff09eaf1eed75154d66dd470ac5c737acd9381fe768dde9f36b2ca832fea
Source12:       https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/bnd-maven-plugin/%{version}/bnd-maven-plugin-%{version}.pom
#!RemoteAsset:  sha256:7b40a3d04e40cfc8fc6b23f507bfe64618725978831c05a3395a77b48a256dff
Source13:       https://maven-central.storage-download.googleapis.com/maven2/org/apache/felix/org.apache.felix.resolver/2.0.4/org.apache.felix.resolver-2.0.4-source-release.zip
#!RemoteAsset:  sha256:dcd8ae80967c399986c4b1d0c060373bcba9456e337fc258bfcef4c273693b0d
Source14:       https://raw.githubusercontent.com/tukaani-project/xz-java/v1.9/COPYING
Source15:       build-bnd.py
Source16:       BndManifest.java
Source17:       osgi-imports.properties
#!RemoteAsset:  sha256:ec8bfdb2500d99aa0b9f92d732b0d89b854dcbc96c65c6b6d98e6da8ead65f67
Source18:       https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/biz.aQute.junit/%{version}/biz.aQute.junit-%{version}-sources.jar
#!RemoteAsset:  sha256:2d1d930266375a7a522ee540fb0211667737d382cb3dfc4e0e69fceb6885d579
Source19:       https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/biz.aQute.launcher/%{version}/biz.aQute.launcher-%{version}-sources.jar
#!RemoteAsset:  sha256:7949a11af59c49a2ab508f58c62baead873dee2392da3b355644b9f2a15cb934
Source20:       https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/biz.aQute.remote.launcher/%{version}/biz.aQute.remote.launcher-%{version}-sources.jar
#!RemoteAsset:  sha256:39c49717dd22f9c5550821e33486d3f103c0da4629d14af939bcf74d8ed133e7
Source21:       https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/biz.aQute.tester/%{version}/biz.aQute.tester-%{version}-sources.jar
#!RemoteAsset:  sha256:088732a24e4ad2ff5f2c3a3e65ad800815efaf9a3aa9944e9a992043624f97ef
Source22:       https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/biz.aQute.tester.junit-platform/%{version}/biz.aQute.tester.junit-platform-%{version}-sources.jar
#!RemoteAsset:  sha256:ae3e4eefcb6a6977f36ceea64bfadae70ab1252b09a25a0e714ec3aed8d9e960
Source23:       https://maven-central.storage-download.googleapis.com/maven2/biz/aQute/bnd/biz.aQute.bnd.embedded-repo/%{version}/biz.aQute.bnd.embedded-repo-%{version}.pom
Source24:       build-embedded.py
Source25:       BuildNativeBundle.java
Source26:       CheckEmbeddedPlugins.java
#!RemoteAsset:  sha256:9648bb2891b9813970bddb68d4be8a5e6ec8280d0180a53dfb29236b579c55bb
Source27:       https://raw.githubusercontent.com/junit-team/junit4/r4.13.2/LICENSE-junit.txt
#!RemoteAsset:  sha256:1cde867cab5c8e842929da5391cef98b4017314822270e934e8e2eef3767c666
Source28:       https://raw.githubusercontent.com/hamcrest/JavaHamcrest/hamcrest-java-1.3/LICENSE.txt?/hamcrest-LICENSE.txt
BuildArch:      noarch

BuildRequires:  eclipse-equinox-build >= 4.39
BuildRequires:  mvn(org.apache.felix:org.apache.felix.gogo.runtime) == 1.1.6
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.apache.maven.shared:maven-mapping) == 3.0.0
BuildRequires:  mvn(org.eclipse.jdt:org.eclipse.jdt.annotation) == 2.4.100
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.osgi) == 3.24.100
BuildRequires:  mvn(org.osgi:org.osgi.service.log) == 1.3.0
BuildRequires:  mvn(org.osgi:org.osgi.util.function) == 1.2.0
BuildRequires:  mvn(org.osgi:org.osgi.util.promise) == 1.3.0
BuildRequires:  python3
Provides:       mvn(biz.aQute.bnd:biz.aQute.bnd.util) == %{version}
Provides:       mvn(biz.aQute.bnd:biz.aQute.bndlib) == %{version}
Provides:       mvn(biz.aQute.bnd:biz.aQute.resolve) == %{version}
Provides:       mvn(biz.aQute.bnd:biz.aQute.repository) == %{version}
Provides:       mvn(biz.aQute.bnd:biz.aQute.bnd.maven) == %{version}
Provides:       mvn(biz.aQute.bnd:bnd-maven-plugin) == %{version}
Requires:       eclipse-equinox >= 4.39
Requires:       javapackages-bootstrap
Requires:       maven >= 3.9.9
Requires:       maven-mapping >= 3.0.0
Requires:       osgi-compendium >= 8.1.0
Requires:       osgi-service-log >= 1.3.0

%description
Bnd analyzes Java bytecode to generate OSGi manifests and resolve bundle
requirements. The Maven plugin processes project classes and resources
into OSGi bundles and supplies Maven repository integration.

%package     -n bnd-embedded-repo
Summary:        Native Bnd launchers and test runners for embedded workspaces
License:        (Apache-2.0 OR EPL-2.0) AND Apache-2.0 AND EPL-1.0 AND BSD-3-Clause
Provides:       mvn(biz.aQute.bnd:biz.aQute.bnd.embedded-repo) == %{version}
Requires:       bnd-maven-plugin = %{version}-%{release}

%description -n bnd-embedded-repo
The embedded repository provides the Bnd launcher, remote launcher, JUnit 4
tester and JUnit Platform tester used by Bnd workspaces and Tycho.

%prep
%autosetup -n bnd-%{version}
cp %{SOURCE14} xz-COPYING
cp %{SOURCE27} junit4-LICENSE.txt
cp %{SOURCE28} hamcrest-LICENSE.txt

%build
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
%{_bindir}/python3 %{SOURCE15} %{_sourcedir} %{version}
python3 %{SOURCE24} %{_sourcedir} %{SOURCE25} %{version}

%install
metadata=%{buildroot}%{_datadir}/maven-metadata/%{name}.xml
install -d "$(dirname "$metadata")"
echo '<metadata><artifacts>' > "$metadata"
for name in %{modules}; do
    directory=%{repo_dir}/$name/%{version}
    install -Dm644 "build/openruyi/$name-%{version}.jar" "%{buildroot}$directory/$name-%{version}.jar"
    install -m644 "build/openruyi/poms/$name-%{version}.pom" "%{buildroot}$directory/$name-%{version}.pom"
    for extension in pom jar; do
        cat >> "$metadata" <<EOF
<artifact><groupId>biz.aQute.bnd</groupId><artifactId>$name</artifactId>
<extension>$extension</extension><version>%{version}</version><path>$directory/$name-%{version}.$extension</path>
<compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions>
<properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
EOF
    done
done
echo '</artifacts></metadata>' >> "$metadata"

embedded=%{repo_dir}/biz.aQute.bnd.embedded-repo/%{version}
install -Dm644 build/embedded/biz.aQute.bnd.embedded-repo-%{version}.jar "%{buildroot}$embedded/biz.aQute.bnd.embedded-repo-%{version}.jar"
install -m644 %{SOURCE23} "%{buildroot}$embedded/biz.aQute.bnd.embedded-repo-%{version}.pom"
cat > %{buildroot}%{_datadir}/maven-metadata/bnd-embedded-repo.xml <<EOF
<metadata><artifacts>
<artifact><groupId>biz.aQute.bnd</groupId><artifactId>biz.aQute.bnd.embedded-repo</artifactId><version>%{version}</version><extension>jar</extension><path>$embedded/biz.aQute.bnd.embedded-repo-%{version}.jar</path><compatVersions><version>%{version}</version></compatVersions></artifact>
<artifact><groupId>biz.aQute.bnd</groupId><artifactId>biz.aQute.bnd.embedded-repo</artifactId><version>%{version}</version><extension>pom</extension><path>$embedded/biz.aQute.bnd.embedded-repo-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
embedded_cp="$(cat build/embedded/classpath):$PWD/build/embedded/biz.aQute.bnd.embedded-repo-%{version}.jar"
javac --release 17 -cp "$embedded_cp" -d build/embedded %{SOURCE26}
java -cp "build/embedded:$embedded_cp" CheckEmbeddedPlugins "$PWD/build/embedded/check-workspace"
java -javaagent:build/embedded/bundles/biz.aQute.launcher.pre.jar -version

export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
base="$PWD/build/openruyi"
cp="$base/*:%{_datadir}/maven-repository/org/osgi/org.osgi.service.log/1.3.0/org.osgi.service.log-1.3.0.jar"
cp="$cp:%{_datadir}/maven-repository/org/osgi/org.osgi.util.function/1.2.0/org.osgi.util.function-1.2.0.jar"
cp="$cp:%{_datadir}/maven-repository/org/osgi/org.osgi.util.promise/1.3.0/org.osgi.util.promise-1.3.0.jar"
cp="$cp:%{_datadir}/maven-repository/org/eclipse/platform/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar:%{_datadir}/maven/lib/*:%{bootstrap_java}/*"
for item in biz.aQute.bnd.util/aQute.bnd.result.ResultTest biz.aQute.bndlib/aQute.bnd.properties.PropertiesLineReaderTest \
    biz.aQute.repository/aQute.maven.api.ArchiveTest biz.aQute.repository/aQute.maven.provider.MetadataTest; do
    module=${item%%/*}
    test_class=${item##*/}
    classes="$base/test-classes/$test_class"
    mkdir -p "$classes"
    (
        cd "$module"
        javac --release 17 -cp "$cp" -sourcepath test -d "$classes" "test/${test_class//.//}.java"
        java -cp "$classes:$cp" %{_libexecdir}/eclipse-equinox/RunJupiter.java "$test_class"
    )
done
consumer="$base/consumer"
mkdir -p "$consumer"/{.mvn,.xmvn,metadata,repository,src/main/java/org/openruyi/bnd}
python3 - "%{buildroot}" "$consumer/metadata" <<'PYTHON'
from pathlib import Path
import sys
from xml.etree import ElementTree as ET

root, output = map(Path, sys.argv[1:])
file = "bnd-maven-plugin.xml"
model = ET.parse(root / "usr/share/maven-metadata" / file)
for path in model.findall(".//artifact/path"):
    path.text = str(root / Path(path.text).relative_to("/"))
model.write(output / file, encoding="utf-8", xml_declaration=True)
PYTHON
cat > "$consumer/.xmvn/configuration.xml" <<EOF
<configuration><resolverSettings><metadataRepositories>
  <repository>$consumer/metadata</repository><repository>%{_datadir}/maven-metadata</repository>
  <repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
cat > "$consumer/src/main/java/org/openruyi/bnd/Api.java" <<'JAVA'
package org.openruyi.bnd;
public interface Api { String value(); }
JAVA
cat > "$consumer/pom.xml" <<'XML'
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
  <groupId>org.openruyi.test</groupId><artifactId>bnd-consumer</artifactId><version>1.0.0</version>
  <build><plugins>
    <plugin><artifactId>maven-resources-plugin</artifactId><version>3.3.1.MBI</version></plugin>
    <plugin><artifactId>maven-compiler-plugin</artifactId><version>3.12.1.MBI</version><configuration><release>17</release></configuration></plugin>
    <plugin><groupId>biz.aQute.bnd</groupId><artifactId>bnd-maven-plugin</artifactId><version>%{version}</version>
      <executions><execution><id>process-bundle</id><phase>process-classes</phase><goals><goal>bnd-process</goal></goals>
        <configuration><bnd><![CDATA[Bundle-SymbolicName: org.openruyi.bnd.consumer
Export-Package: org.openruyi.bnd;version=1.0.0]]></bnd></configuration>
      </execution></executions>
    </plugin>
  </plugins></build>
</project>
XML
export MAVEN_OPTS="$MAVEN_OPTS -Xlog:class+load=info:file=$consumer/classload.log"
(cd "$consumer" && mvn --offline --batch-mode -Dmaven.repo.local="$consumer/repository" process-classes)
grep -F 'aQute.bnd.osgi.Analyzer source:' "$consumer/classload.log" | grep -F '/biz.aQute.bndlib-%{version}.jar'
grep -F 'Bundle-SymbolicName: org.openruyi.bnd.consumer' "$consumer/target/classes/META-INF/MANIFEST.MF"
grep -F 'Export-Package: org.openruyi.bnd;version="1.0.0"' "$consumer/target/classes/META-INF/MANIFEST.MF"

%files
%doc README.md
%license LICENSE xz-COPYING build/openruyi/felix-resolver-LICENSE build/openruyi/felix-resolver-NOTICE
%{_datadir}/maven-metadata/bnd-maven-plugin.xml
%{repo_dir}/
%exclude %{repo_dir}/biz.aQute.bnd.embedded-repo/

%files -n bnd-embedded-repo
%license LICENSE junit4-LICENSE.txt hamcrest-LICENSE.txt
%{repo_dir}/biz.aQute.bnd.embedded-repo/
%{_datadir}/maven-metadata/bnd-embedded-repo.xml

%changelog
%autochangelog
