# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global artifact_dir %{repo}/org/apache/commons/%{name}/%{version}
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
Name:           commons-text
Version:        1.12.0
Release:        %autorelease
Summary:        Apache Commons utilities for text processing
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-text/
VCS:            git:https://github.com/apache/commons-text
#!RemoteAsset:  sha256:fee43a27f1addf4dcb87b5f7f17d72d7c58b90e1ef148c0b9a2228bf6bc41e5c
Source0:        https://github.com/apache/commons-text/archive/refs/tags/rel/commons-text-%{version}.tar.gz
# Commons RNG supplies the random-number fixtures used by ParsedDecimalTest.
#!RemoteAsset:  sha256:e56a0e3457dc5a5212ff01313fdd912975cd792b26db46e8e0652b712fdce455
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/commons/commons-rng-client-api/1.5/commons-rng-client-api-1.5-sources.jar
#!RemoteAsset:  sha256:33c758c222cc36b6f497c233c564ab8bfbab64c7e3987d25056eed83fa1fefa9
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/commons/commons-rng-core/1.5/commons-rng-core-1.5-sources.jar
#!RemoteAsset:  sha256:ac16f04ed6cad3d3992aab4ba3a01ef8e396f5d5a59df508ebd3d8f500b80fca
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/commons/commons-rng-simple/1.5/commons-rng-simple-1.5-sources.jar
# Rhino supplies a JSR-223 JavaScript engine for the original script lookup tests.
#!RemoteAsset:  sha256:d3be964dc5fd505b79432a3d57659420d3ad6a8be9eea8406e1b0a4e7c6f06f2
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/mozilla/rhino/1.7.15/rhino-1.7.15-sources.jar
#!RemoteAsset:  sha256:9dcd3d44bba2d82c0c5176b737106943d75c9dbf14caff5fcad5525cdfe93b31
Source5:        https://maven-central.storage-download.googleapis.com/maven2/org/mozilla/rhino-engine/1.7.15/rhino-engine-1.7.15-sources.jar
Source6:        module-info.java
Source7:        check-commons-text.sh
Patch2000:      2000-use-local-network-test-fixtures.patch
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:) == 69
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
BuildRequires:  mvn(org.apache.commons:commons-lang3) == 3.20.0
BuildRequires:  mvn(commons-io:commons-io) == 2.21.0
BuildRequires:  mvn(org.mockito:mockito-junit-jupiter) == 4.11.0
BuildRequires:  python3
BuildRequires:  unzip
Provides:       mvn(org.apache.commons:%{name}) == %{version}
Requires:       mvn(org.apache.commons:commons-parent:pom:) == 69
Requires:       mvn(org.apache.commons:commons-lang3) == 3.20.0

%description
Apache Commons Text provides string escaping, substitution, similarity
algorithms and text processing utilities.

%prep
%autosetup -p1 -n commons-text-rel-commons-text-%{version}
mkdir -p target/{classes,java9,manifest} .xmvn
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories><repository>%{_datadir}/maven-metadata</repository><repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository></metadataRepositories></resolverSettings></configuration>
EOF

%build
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -Xpkginfo:always -g -parameters -proc:none -encoding ISO-8859-1 -cp %{repo}/org/apache/commons/commons-lang3/3.20.0/commons-lang3-3.20.0.jar -d target/classes @target/sources
javac --release 9 --module-version %{version} --module-path %{repo}/org/apache/commons/commons-lang3/3.20.0/commons-lang3-3.20.0.jar --patch-module org.apache.commons.text=target/classes -d target/java9 %{SOURCE6}
meta=target/classes/META-INF/maven/org.apache.commons/%{name}
mkdir -p "$meta"
cp pom.xml "$meta/"
cp LICENSE.txt NOTICE.txt target/classes/META-INF/
printf 'artifactId=%%s\ngroupId=org.apache.commons\nversion=%%s\n' '%{name}' '%{version}' > "$meta/pom.properties"
cat > bundle.pom <<EOF
<project><modelVersion>4.0.0</modelVersion><groupId>org.apache.commons</groupId><artifactId>%{name}</artifactId><version>%{version}</version>
<build><plugins><plugin><groupId>org.apache.felix</groupId><artifactId>maven-bundle-plugin</artifactId><version>5.1.9.MBI</version><configuration><manifestLocation>$PWD/target/manifest</manifestLocation><instructions>
<Bundle-SymbolicName>org.apache.commons.text</Bundle-SymbolicName><Bundle-Name>Apache Commons Text</Bundle-Name><Bundle-Vendor>The Apache Software Foundation</Bundle-Vendor><Bundle-Version>%{version}</Bundle-Version>
<Export-Package>org.apache.commons.text.*;version=%{version};-noimport:=true</Export-Package><Automatic-Module-Name>org.apache.commons.text</Automatic-Module-Name><Multi-Release>true</Multi-Release>
</instructions></configuration></plugin></plugins></build></project>
EOF
ext=%{_datadir}/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
mvn -B -o -f bundle.pom -Dmaven.repo.local="$PWD/target/repo" org.apache.felix:maven-bundle-plugin:5.1.9.MBI:manifest
jar cfm target/%{name}.jar target/manifest/MANIFEST.MF -C target/classes .
jar --update --file target/%{name}.jar --release 9 -C target/java9 module-info.class

%install
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 target/%{name}.jar %{buildroot}%{artifact_dir}/%{name}-%{version}.jar
install -m644 pom.xml %{buildroot}%{artifact_dir}/%{name}-%{version}.pom
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
<artifact><groupId>org.apache.commons</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>jar</extension><path>%{artifact_dir}/%{name}-%{version}.jar</path><compatVersions><version>%{version}</version></compatVersions></artifact>
<artifact><groupId>org.apache.commons</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension><path>%{artifact_dir}/%{name}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
# Run all functional tests with source-built RNG and JavaScript engine fixtures.
bash %{SOURCE7} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5}
# Verify the Java 9 module descriptor resolves its installed Lang dependency.
java --module-path target/%{name}.jar:%{repo}/org/apache/commons/commons-lang3/3.20.0/commons-lang3-3.20.0.jar --add-modules org.apache.commons.text -version

%files
%license LICENSE.txt NOTICE.txt
%{_datadir}/maven-metadata/commons-text.xml
%{artifact_dir}/

%changelog
%autochangelog
