# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global artifact_dir %{repo}/org/apache/bcel/%{name}/%{version}
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
Name:           bcel
Version:        6.12.0
Release:        %autorelease
Summary:        Apache Commons Java bytecode engineering library
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-bcel/
VCS:            git:https://github.com/apache/commons-bcel
#!RemoteAsset:  sha256:dad7620e1245281cfdd129339e84458b1fc65f1ddaa0cb835538034ec1bcc029
Source0:        https://github.com/apache/commons-bcel/archive/refs/tags/rel/commons-bcel-%{version}.tar.gz
#!RemoteAsset:  sha256:af93599746a44a7097d36b4ebc017ace925e6f4318f6c326343f5b7255b3fc2b
Source1:        https://maven-central.storage-download.googleapis.com/maven2/commons-lang/commons-lang/2.0/commons-lang-2.0-sources.jar
#!RemoteAsset:  sha256:b7eca54ef11f4f82abe929b99de830662e2a8369aa66ecf653465550f4d96b79
Source2:        https://maven-central.storage-download.googleapis.com/maven2/wsdl4j/wsdl4j/1.5.3/wsdl4j-1.5.3-sources.jar
# BCEL tests inspect the signature-only Java EE classes, including a method with no Code attribute.
#!RemoteAsset:  sha256:a045eac0ff80c5c0fd29b680599f27598abff16b1e6c9df46ce962a4e0b1390e
Source3:        https://maven-central.storage-download.googleapis.com/maven2/javax/javaee-api/6.0/javaee-api-6.0.jar
Source4:        module-info.java
Source5:        check-bcel.sh
Patch0:         0001-check-runtime-module-descriptors-and-optional-kotlin.patch
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(commons-io:commons-io) == 2.21.0
BuildRequires:  mvn(net.java.dev.jna:jna-platform) == 5.18.1
BuildRequires:  mvn(org.apache.commons:commons-exec) == 1.6.0
BuildRequires:  mvn(org.apache.commons:commons-lang3) == 3.20.0
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:) == 95
BuildRequires:  mvn(org.eclipse.jdt:ecj) == 3.32.0
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
BuildRequires:  unzip
Provides:       mvn(org.apache.bcel:bcel) == %{version}
Requires:       mvn(commons-io:commons-io) == 2.21.0
Requires:       mvn(org.apache.commons:commons-lang3) == 3.20.0
Requires:       mvn(org.apache.commons:commons-parent:pom:) == 95

%description
Apache Commons BCEL parses, generates, rewrites and verifies Java class
files. The library exposes its APIs as a Java module and an OSGi bundle.

%prep
%autosetup -p1 -n commons-bcel-rel-commons-bcel-%{version}
mkdir -p target/{classes,java9,manifest} target/fixtures/{commons-lang-2.0,wsdl4j-1.5.3}/src .xmvn
unzip -q %{SOURCE1} -d target/fixtures/commons-lang-2.0/src
unzip -q %{SOURCE2} -d target/fixtures/wsdl4j-1.5.3/src
ln -s %{SOURCE3} target/fixtures/javaee-api.jar
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories><repository>%{_datadir}/maven-metadata</repository><repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository></metadataRepositories></resolverSettings></configuration>
EOF

%build
cp="%{repo}/org/apache/commons/commons-lang3/3.20.0/commons-lang3-3.20.0.jar:%{repo}/commons-io/commons-io/2.21.0/commons-io-2.21.0.jar"
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -Xpkginfo:always -g -proc:none -encoding UTF-8 -cp "$cp" -d target/classes @target/sources
javac --release 9 --module-version %{version} --module-path "$cp" --patch-module org.apache.bcel=target/classes -d target/java9 %{SOURCE4}
meta=target/classes/META-INF/maven/org.apache.bcel/%{name}
mkdir -p "$meta"
cp pom.xml "$meta/"
cp LICENSE.txt NOTICE.txt target/classes/META-INF/
printf 'artifactId=%%s\ngroupId=org.apache.bcel\nversion=%%s\n' '%{name}' '%{version}' > "$meta/pom.properties"
cat > bundle.pom <<EOF
<project><modelVersion>4.0.0</modelVersion><groupId>org.apache.bcel</groupId><artifactId>%{name}</artifactId><version>%{version}</version>
<dependencies><dependency><groupId>org.apache.commons</groupId><artifactId>commons-lang3</artifactId><version>3.20.0</version></dependency><dependency><groupId>commons-io</groupId><artifactId>commons-io</artifactId><version>2.21.0</version></dependency></dependencies>
<build><plugins><plugin><groupId>org.apache.felix</groupId><artifactId>maven-bundle-plugin</artifactId><version>5.1.9.MBI</version><configuration><manifestLocation>$PWD/target/manifest</manifestLocation><instructions>
<Bundle-SymbolicName>org.apache.bcel</Bundle-SymbolicName><Bundle-Name>Apache Commons BCEL</Bundle-Name><Bundle-Vendor>The Apache Software Foundation</Bundle-Vendor><Bundle-Version>%{version}</Bundle-Version>
<Export-Package>org.apache.bcel.*;version=%{version};-noimport:=true</Export-Package><Automatic-Module-Name>org.apache.bcel</Automatic-Module-Name><Multi-Release>true</Multi-Release>
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
<artifact><groupId>org.apache.bcel</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>jar</extension><path>%{artifact_dir}/%{name}-%{version}.jar</path><compatVersions><version>%{version}</version></compatVersions></artifact>
<artifact><groupId>org.apache.bcel</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension><path>%{artifact_dir}/%{name}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
bash %{SOURCE5}
java --module-path "target/%{name}.jar:%{repo}/org/apache/commons/commons-lang3/3.20.0/commons-lang3-3.20.0.jar:%{repo}/commons-io/commons-io/2.21.0/commons-io-2.21.0.jar" --add-modules org.apache.bcel -version

%files
%license LICENSE.txt NOTICE.txt
%{_datadir}/maven-metadata/bcel.xml
%{artifact_dir}/

%changelog
%autochangelog
