# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global artifact_dir %{repo}/org/apache/maven/shared/%{name}/%{version}
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
Name:           maven-filtering
Version:        3.5.0
Release:        %autorelease
Summary:        Resource filtering and change detection for Maven
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-filtering/
VCS:            git:https://github.com/apache/maven-filtering
#!RemoteAsset:  sha256:38abe91dc079f9d2b9234d6dded40d8df4eb6e79a4835a0bc449bdc84cabb8db
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/shared/maven-filtering/%{version}/maven-filtering-%{version}-source-release.zip
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.12
BuildRequires:  mvn(commons-io:commons-io) == 2.21.0
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:) == 47
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing) == 2.1.0
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
BuildRequires:  mvn(org.mockito:mockito-core) == 4.11.0
BuildRequires:  mvn(org.slf4j:slf4j-simple) == 1.7.36
BuildRequires:  unzip
Provides:       mvn(org.apache.maven.shared:maven-filtering) == %{version}
Requires:       javapackages-bootstrap
Requires:       maven >= 3.9.12
Requires:       mvn(org.apache.maven.shared:maven-shared-components:pom:) == 47
Requires:       mvn(org.slf4j:slf4j-api) == 1.7.36

%description
Maven Filtering copies resources, interpolates project properties and
detects changed files for incremental and repeatable resource processing.

%prep
%autosetup -n maven-filtering-%{version}

%build
mkdir -p target/classes/META-INF/maven/org.apache.maven.shared/%{name}
cp="%{_datadir}/maven/lib/*:%{bootstrap_java}/plexus-build-api0.jar"
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -g -encoding UTF-8 -processor org.eclipse.sisu.space.SisuIndexAPT6 -cp "$cp" -d target/classes @target/sources
for type in DefaultMavenFileFilter DefaultMavenReaderFilter DefaultMavenResourcesFiltering; do
    grep -Fx "org.apache.maven.shared.filtering.$type" target/classes/META-INF/sisu/javax.inject.Named
done
cp LICENSE NOTICE target/classes/META-INF/
meta=target/classes/META-INF/maven/org.apache.maven.shared/%{name}
cp pom.xml "$meta/"
printf 'artifactId=%%s\ngroupId=org.apache.maven.shared\nversion=%%s\n' %{name} %{version} > "$meta/pom.properties"
printf 'Implementation-Title: Apache Maven Filtering\nImplementation-Version: %%s\nImplementation-Vendor: The Apache Software Foundation\n' %{version} > target/module.mf
jar cfm target/%{name}.jar target/module.mf -C target/classes .

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
mkdir -p target/test-classes
api=%{repo}/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.jar
simple=%{repo}/org/slf4j/slf4j-simple/1.7.36/slf4j-simple-1.7.36.jar
cp="$PWD/target/%{name}.jar:$simple:$api:%{_datadir}/maven/lib/*:%{_datadir}/maven/boot/*"
for dir in org/junit/platform org/junit/jupiter org/codehaus/plexus/plexus-testing org/mockito commons-io; do
    jars=$(find "%{repo}/$dir" -name '*.jar' ! -name '*-sources.jar' -printf '%%p:')
    cp="$jars$cp"
done
for n in junit-jupiter-params apiguardian-api opentest4j junit hamcrest-core byte-buddy byte-buddy-agent objenesis asm asm-commons asm-tree plexus-build-api0; do
    cp="$cp:%{bootstrap_java}/$n.jar"
done
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 17 -g -encoding UTF-8 -proc:none -cp "$cp" -d target/test-classes @target/test-sources
cp -r src/test/resources/. target/test-classes/
tests=$(find src/test/java -name '*Test.java' ! -name AbstractInterpolatorFilterReaderLineEndingTest.java | sed 's|src/test/java/||;s|[.]java$||;s|/|.|g' | sort)
# The upstream assertions inspect the logger name and the resource paths written to stderr.
java -Dbasedir="$PWD" -Dorg.slf4j.simpleLogger.defaultLogLevel=info -Dorg.slf4j.simpleLogger.showLogName=true \
    -Dorg.slf4j.simpleLogger.showShortLogName=true -Dorg.slf4j.simpleLogger.showThreadName=false \
    -cp "target/test-classes:$cp" %{_libexecdir}/eclipse-equinox/RunJupiter.java $tests

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/maven-filtering.xml
%{artifact_dir}/

%changelog
%autochangelog
