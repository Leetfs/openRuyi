# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global artifact_dir %{repo}/org/apache/maven/shared/%{name}/%{version}
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
Name:           maven-shared-utils
Version:        3.3.4
Release:        %autorelease
Summary:        Maven shared utilities with overridable process environment handling
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-shared-utils/
VCS:            git:https://github.com/apache/maven-shared-utils
#!RemoteAsset:  sha256:5cccf13be755eb5bca4de69d3e27a1221bc956c243d2811866c2ce77218d82c0
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:      noarch
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.eclipse.jdt:ecj) == 3.32.0
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness) == 3.5.1
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:) == 34
BuildRequires:  unzip
Provides:       mvn(org.apache.maven.shared:%{name}) == %{version}
Requires:       javapackages-bootstrap
Requires:       mvn(org.apache.maven.shared:maven-shared-components:pom:) == 34

%description
Maven Shared Utils provides command-line execution, file scanning and
interpolation utilities. Surefire embeds this version to filter the
environment inherited by forked test processes.

%prep
%autosetup -n %{name}-%{version}
# CaseTest escapes text only when formatting a failed Unicode assertion.
sed -i 's/import org.apache.commons.text.StringEscapeUtils;/import org.apache.commons.lang3.StringEscapeUtils;/' src/test/java/org/apache/maven/shared/utils/CaseTest.java

%build
mkdir -p target/classes/META-INF/maven/org.apache.maven.shared/%{name}
find src/main/java -name '*.java' | sort > target/sources
cp=$(find %{_datadir}/maven/lib -name '*.jar' -printf '%%p:')
cp="$cp%{bootstrap_java}/jsr305.jar:%{bootstrap_java}/jansi.jar:%{bootstrap_java}/commons-io.jar"
java -jar %{repo}/org/eclipse/jdt/ecj/3.32.0/ecj-3.32.0.jar -source 1.7 -target 1.7 -g -proc:none -nowarn -encoding UTF-8 -classpath "$cp" -d target/classes @target/sources
cp -r src/main/resources/. target/classes/
cp LICENSE NOTICE target/classes/META-INF/
meta=target/classes/META-INF/maven/org.apache.maven.shared/%{name}
cp pom.xml "$meta/"
printf 'artifactId=%%s\ngroupId=org.apache.maven.shared\nversion=%%s\n' '%{name}' '%{version}' > "$meta/pom.properties"
printf 'Implementation-Title: Apache Maven Shared Utils\nImplementation-Version: %%s\nImplementation-Vendor: The Apache Software Foundation\nSpecification-Title: Apache Maven Shared Utils\nSpecification-Version: 3.3\nSpecification-Vendor: The Apache Software Foundation\n' '%{version}' > target/module.mf
jar cfm target/%{name}.jar target/module.mf -C target/classes .

%install
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 target/%{name}.jar %{buildroot}%{artifact_dir}/%{name}-%{version}.jar
install -m644 pom.xml %{buildroot}%{artifact_dir}/%{name}-%{version}.pom
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
<artifact><groupId>org.apache.maven.shared</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>jar</extension><path>%{artifact_dir}/%{name}-%{version}.jar</path><compatVersions><version>%{version}</version></compatVersions></artifact>
<artifact><groupId>org.apache.maven.shared</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension><path>%{artifact_dir}/%{name}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
mkdir -p target/test-classes
harness=%{repo}/org/apache/maven/plugin-testing/maven-plugin-testing-harness/3.5.1/maven-plugin-testing-harness-3.5.1.jar
cp="$PWD/target/%{name}.jar:$harness:%{_datadir}/maven/lib/*:%{_datadir}/maven/boot/*:%{bootstrap_java}/*"
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 8 -g -proc:none -encoding UTF-8 -cp "$cp" -d target/test-classes @target/test-sources
cp -r src/test/resources/. target/test-classes/
tests=$(find src/test/java -name '*Test.java' | sed 's|src/test/java/||;s|[.]java$||;s|/|.|g' | sort)
TEST_SHARED_ENV=TestValue java -Dbasedir="$PWD" -cp "target/test-classes:$cp" org.junit.runner.JUnitCore $tests
javap -verbose -classpath target/%{name}.jar org.apache.maven.shared.utils.cli.Commandline | grep -F 'major version: 51'

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/maven-shared-utils.xml
%{artifact_dir}/

%changelog
%autochangelog
