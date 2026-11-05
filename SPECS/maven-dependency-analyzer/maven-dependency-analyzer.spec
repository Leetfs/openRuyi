# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global artifact_dir %{repo}/org/apache/maven/shared/%{name}/%{version}
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap

Name:           maven-dependency-analyzer
Version:        1.17.1
Release:        %autorelease
Summary:        Maven bytecode dependency analysis
License:        Apache-2.0
URL:            https://maven.apache.org/shared/%{name}/
VCS:            git:https://github.com/apache/%{name}
#!RemoteAsset:  sha256:994eeb95346ab1cbfea4a87c9be4490a0d627b18483cb0ea7d6939b593d3baa6
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        IndexNative.java
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:) == 48
BuildRequires:  maven >= 3.9.15
BuildRequires:  mvn(org.ow2.asm:asm) == 9.10.1
BuildRequires:  mvn(org.mockito:mockito-junit-jupiter) == 4.11.0
BuildRequires:  mvn(org.assertj:assertj-bom:pom:) == 3.27.7
BuildRequires:  unzip
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
Provides:       mvn(org.apache.maven.shared:%{name}) == %{version}
Requires:       javapackages-bootstrap
Requires:       mvn(org.apache.maven.shared:maven-shared-components:pom:) == 48
Requires:       mvn(org.ow2.asm:asm) == 9.10.1
Requires:       maven >= 3.9.15
Requires:       mvn(org.assertj:assertj-bom:pom:) == 3.27.7

%description
Maven Dependency Analyzer inspects class files and project dependencies to
identify undeclared and unused artifacts.

%prep
%autosetup -n %{name}-%{version}

%build
mkdir -p target/classes/META-INF/maven/org.apache.maven.shared/%{name} target/tools
cp="%{repo}/org/ow2/asm/asm/9.10.1/asm-9.10.1.jar:%{_datadir}/maven/lib/*:%{_datadir}/maven/boot/*:%{bootstrap_java}/javax.inject.jar"
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -encoding UTF-8 -g -proc:none -cp "$cp" -d target/classes @target/sources
index_cp="%{bootstrap_java}/org.eclipse.sisu.inject.jar:%{bootstrap_java}/javax.inject.jar:%{bootstrap_java}/guice.jar:%{bootstrap_java}/asm.jar"
javac -cp "$index_cp" -d target/tools %{SOURCE1}
java -cp "target/tools:target/classes:$index_cp:$cp" IndexNative target/classes
test -s target/classes/META-INF/sisu/javax.inject.Named
meta=target/classes/META-INF/maven/org.apache.maven.shared/%{name}
cp pom.xml "$meta/pom.xml"
printf 'groupId=org.apache.maven.shared\nartifactId=%%s\nversion=%%s\n' '%{name}' '%{version}' > "$meta/pom.properties"
cp LICENSE NOTICE target/classes/META-INF/
jar cf target/%{name}.jar -C target/classes .

%install
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 target/%{name}.jar %{buildroot}%{artifact_dir}/%{name}-%{version}.jar
install -m644 pom.xml %{buildroot}%{artifact_dir}/%{name}-%{version}.pom
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
<artifact><groupId>org.apache.maven.shared</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>jar</extension><path>%{artifact_dir}/%{name}-%{version}.jar</path><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
<artifact><groupId>org.apache.maven.shared</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension><path>%{artifact_dir}/%{name}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
# Analyze the original fixtures from the target/test-classes path used by upstream.
mkdir -p target/test-classes
cp=$(find %{repo}/org/junit/jupiter %{repo}/org/junit/platform -name '*-5.12.2.jar' -o -name '*-1.12.2.jar' | paste -sd:)
asm_cp=$(find %{repo}/org/ow2/asm -name '*-9.10.1.jar' -printf '%%p:')
cp="$PWD/target/%{name}.jar:$asm_cp$cp:%{_datadir}/maven/lib/*:%{_datadir}/maven/boot/*:"
for artifact in mockito-core mockito-junit-jupiter; do
    cp="$cp%{repo}/org/mockito/$artifact/4.11.0/$artifact-4.11.0.jar:"
done
for artifact in junit-jupiter-params assertj-core apiguardian-api opentest4j byte-buddy byte-buddy-agent objenesis javax.inject; do
    cp="$cp%{bootstrap_java}/$artifact.jar:"
done
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 8 -encoding UTF-8 -g -proc:none -cp "$cp" -d target/test-classes @target/test-sources
cp -r src/test/resources/. target/test-classes/
tests=$(find src/test/java -name '*Test.java' | sed 's|src/test/java/||;s|[.]java$||;s|/|.|g' | sort)
java -cp "target/test-classes:$cp" %{_libexecdir}/eclipse-equinox/RunJupiter.java $tests

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/maven-dependency-analyzer.xml
%{artifact_dir}/

%changelog
%autochangelog
