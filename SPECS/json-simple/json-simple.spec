# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global artifact_dir %{repo}/com/github/cliftonlabs/%{name}/%{version}
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap

Name:           json-simple
Version:        3.0.2
Release:        %autorelease
Summary:        JSON encoding and decoding for Java
License:        Apache-2.0
URL:            https://github.com/cliftonlabs/json-simple
VCS:            git:https://github.com/cliftonlabs/json-simple
#!RemoteAsset:  sha256:c46cfd891cf79bdaa255d047a4604cd0608d3f8d04cfef4f16dec166587391e1
Source0:        https://github.com/cliftonlabs/json-simple/archive/refs/tags/json-simple-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.eclipse.jdt:ecj) == 3.32.0
Provides:       mvn(com.github.cliftonlabs:json-simple) == %{version}

%description
JSON Simple reads and writes JSON objects, arrays, numbers and strings.
It supplies the JSON data tools used by Velocity Tools.

%prep
%autosetup -n json-simple-json-simple-%{version}

%build
mkdir -p target/classes/META-INF/maven/com.github.cliftonlabs/%{name}
# The release contains the lexer generated from src/main/lex/jsonstrict.lex by JFlex 1.4.3.
find src/main/java -name '*.java' | sort > target/sources
java -jar %{repo}/org/eclipse/jdt/ecj/3.32.0/ecj-3.32.0.jar -source 1.7 -target 1.7 -g -proc:none -encoding UTF-8 -d target/classes @target/sources
meta=target/classes/META-INF/maven/com.github.cliftonlabs/%{name}
cp pom.xml "$meta/"
printf 'groupId=com.github.cliftonlabs\nartifactId=%%s\nversion=%%s\n' '%{name}' '%{version}' > "$meta/pom.properties"
cp LICENSE target/classes/META-INF/
printf 'Implementation-Title: JSON.simple\nImplementation-Version: %%s\nSpecification-Title: JSON.simple\nSpecification-Version: 3.0\n' '%{version}' > target/module.mf
jar cfm target/%{name}.jar target/module.mf -C target/classes .

%install
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 target/%{name}.jar %{buildroot}%{artifact_dir}/%{name}-%{version}.jar
install -m644 pom.xml %{buildroot}%{artifact_dir}/%{name}-%{version}.pom
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
<artifact><groupId>com.github.cliftonlabs</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>jar</extension><path>%{artifact_dir}/%{name}-%{version}.jar</path><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
<artifact><groupId>com.github.cliftonlabs</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension><path>%{artifact_dir}/%{name}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
# Run every upstream test of JSON objects, arrays, encoding, decoding and lexical errors.
mkdir -p target/test-classes
cp="target/%{name}.jar:%{bootstrap_java}/junit.jar:%{bootstrap_java}/hamcrest-core.jar"
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 8 -g -proc:none -encoding UTF-8 -cp "$cp" -d target/test-classes @target/test-sources
tests=$(find src/test/java -name '*Test.java' | sed 's|src/test/java/||;s|[.]java$||;s|/|.|g' | sort)
java -cp "target/test-classes:$cp" org.junit.runner.JUnitCore $tests
# Preserve the release's Java 7 class-file compatibility.
javap -verbose -classpath target/%{name}.jar com.github.cliftonlabs.json_simple.Jsoner | grep -F 'major version: 51'

%files
%license LICENSE
%doc README CHANGELOG
%{_datadir}/maven-metadata/json-simple.xml
%{artifact_dir}/

%changelog
%autochangelog
