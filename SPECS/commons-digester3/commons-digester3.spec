# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global artifact_dir %{repo}/org/apache/commons/%{name}/%{version}
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap

Name:           commons-digester3
Version:        3.2
Release:        %autorelease
Summary:        Rule-based XML object mapping
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-digester/
VCS:            git:https://github.com/apache/commons-digester
#!RemoteAsset:  sha256:d0d74ced1baec01d8eb2270fd78719aa4c230d5cc6d9076c7a9a617f66122c6c
Source0:        https://github.com/apache/commons-digester/archive/refs/tags/DIGESTER3_3_2.tar.gz
Source1:        RunJUnit.java
Patch2000:      2000-complete-offline-test-execution.patch
BuildArch:      noarch
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.eclipse.jdt:ecj) == 3.32.0
BuildRequires:  mvn(cglib:cglib) == 3.2.9
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:) == 22
Provides:       mvn(org.apache.commons:commons-digester3) == %{version}
Requires:       javapackages-bootstrap
Requires:       mvn(cglib:cglib) == 3.2.9
Requires:       mvn(org.apache.commons:commons-parent:pom:) == 22

%description
Commons Digester maps XML elements and attributes to Java objects through
configurable rules. Velocity Tools uses it to read tool configurations.

%prep
%autosetup -p1 -n commons-digester-DIGESTER3_3_2
mkdir -p .xmvn
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories><repository>%{_datadir}/maven-metadata</repository><repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository></metadataRepositories></resolverSettings></configuration>
EOF

%build
mkdir -p target/classes/META-INF/maven/org.apache.commons/%{name} target/manifest
cp="%{repo}/cglib/cglib/3.2.9/cglib-3.2.9.jar:%{bootstrap_java}/commons-beanutils.jar:%{bootstrap_java}/commons-logging.jar"
find src/main/java -name '*.java' | sort > target/sources
java -jar %{repo}/org/eclipse/jdt/ecj/3.32.0/ecj-3.32.0.jar -source 1.5 -target 1.5 -g -proc:none -encoding UTF-8 -classpath "$cp" -d target/classes @target/sources
cp -r src/main/resources/. target/classes/
meta=target/classes/META-INF/maven/org.apache.commons/%{name}
cp pom.xml "$meta/"
printf 'groupId=org.apache.commons\nartifactId=%%s\nversion=%%s\n' '%{name}' '%{version}' > "$meta/pom.properties"
cp LICENSE.txt NOTICE.txt target/classes/META-INF/
cat > bundle.pom <<EOF
<project><modelVersion>4.0.0</modelVersion><groupId>org.apache.commons</groupId><artifactId>%{name}</artifactId><version>%{version}</version>
<build><plugins><plugin><groupId>org.apache.felix</groupId><artifactId>maven-bundle-plugin</artifactId><version>5.1.9.MBI</version><configuration><manifestLocation>$PWD/target/manifest</manifestLocation><instructions>
<Bundle-SymbolicName>org.apache.commons.digester3</Bundle-SymbolicName><Bundle-Name>Apache Commons Digester</Bundle-Name><Bundle-Vendor>The Apache Software Foundation</Bundle-Vendor><Bundle-Version>3.2.0</Bundle-Version>
<Export-Package>org.apache.commons.digester3.*;version=3.2.0;-noimport:=true</Export-Package>
</instructions></configuration></plugin></plugins></build></project>
EOF
ext=%{_datadir}/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
mvn -B -o -f bundle.pom -Dmaven.repo.local="$PWD/target/repo" org.apache.felix:maven-bundle-plugin:5.1.9.MBI:manifest
jar cfm target/%{name}.jar target/manifest/MANIFEST.MF -C target/classes .

%install
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 target/%{name}.jar %{buildroot}%{artifact_dir}/%{name}-%{version}.jar
install -m644 pom.xml %{buildroot}%{artifact_dir}/%{name}-%{version}.pom
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
<artifact><groupId>org.apache.commons</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>jar</extension><path>%{artifact_dir}/%{name}-%{version}.jar</path><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
<artifact><groupId>org.apache.commons</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension><path>%{artifact_dir}/%{name}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
# Run all concrete upstream JUnit tests, including constructor-argument object creation.
mkdir -p target/test-classes target/launcher
cp="$PWD/target/%{name}.jar:%{repo}/cglib/cglib/3.2.9/cglib-3.2.9.jar:%{bootstrap_java}/*"
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 8 -g -proc:none -encoding UTF-8 -cp "$cp" -d target/test-classes @target/test-sources
cp -r src/test/resources/. target/test-classes/
javac -cp "$cp" -d target/launcher %{SOURCE1}
tests=$(find src/test/java -name '*Test.java' -o -name '*TestCase.java' -o -name 'Test*.java' | sed 's|src/test/java/||;s|[.]java$||;s|/|.|g' | sort)
# CGLIB uses ClassLoader.defineClass to create constructor proxies on the test JVM.
java --add-opens=java.base/java.lang=ALL-UNNAMED -Dorg.apache.commons.logging.Log=org.apache.commons.logging.impl.SimpleLog -Dorg.apache.commons.logging.simplelog.defaultlog=fatal -Dbasedir="$PWD" -cp "target/launcher:target/test-classes:$cp" RunJUnit $tests

%files
%license LICENSE.txt NOTICE.txt
%{_datadir}/maven-metadata/commons-digester3.xml
%{artifact_dir}/

%changelog
%autochangelog
