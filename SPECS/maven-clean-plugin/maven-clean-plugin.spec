# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global compat_version 3.2.0
%global repo_dir %{_datadir}/maven-repository
%global artifact_dir %{repo_dir}/org/apache/maven/plugins/%{name}/%{compat_version}

Name:           maven-clean-plugin
Version:        3.5.0
Release:        %autorelease
Summary:        Apache Maven plugin for cleaning build outputs
License:        Apache-2.0
URL:            https://maven.apache.org/plugins/maven-clean-plugin/
VCS: git:https://github.com/apache/maven-clean-plugin
#!RemoteAsset:  sha256:649639360a48b0f8121e3cb7f7b1ba1259866fe77c744dc3ce2ea57f374cc981
Source0:        https://archive.apache.org/dist/maven/plugins/%{name}-%{compat_version}-source-release.zip
#!RemoteAsset:  sha256:d35e5ebcd751b5e5b1bd82c6f6fdd66711ee4cb1753a95fb59ab45246dad860f
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/maven-clean-plugin/3.2.0/maven-clean-plugin-3.2.0-sources.jar
Source2:        check-clean.sh
#!RemoteAsset:  sha256:d5ea0ea62d29ae3ecfff21ea02a4df51d4610511d78bf01e877945b0a0bd605f
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
#!RemoteAsset:  sha256:98e11e20101d4db7c81cafbe24fd1759a8a9c52800c182f37d1a22c1746e9d4f
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-sources.jar
Patch0:         0001-isolate-linux-clean-test-fixtures.patch
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness) == 3.5.1
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:) == 44
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing) == 2.1.0
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
BuildRequires:  mvn(org.mockito:mockito-junit-jupiter) == 4.11.0
BuildRequires:  java-25-openjdk-devel
BuildRequires:  maven >= 3.9.9
BuildRequires:  javapackages-bootstrap
BuildRequires:  unzip
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:) == 35
Provides:       mvn(org.apache.maven.plugins:maven-clean-plugin) == %{compat_version}
Provides:       mvn(org.apache.maven.plugins:maven-clean-plugin) == %{version}
Requires:       javapackages-bootstrap
Requires:       maven >= 3.9.9
Requires:       mvn(org.apache.maven.plugins:maven-plugins:pom:) == 35
Requires:       mvn(org.apache.maven.plugins:maven-plugins:pom:) == 44

%description
The Maven Clean plugin removes a project's build outputs and additional
configured file sets as part of the standard clean lifecycle.
%prep
%autosetup -N -n %{name}-%{compat_version}
# The release classifier supplies the generated help goal source.
mkdir -p src/main/java/org/apache/maven/plugins/clean
unzip -p %{SOURCE1} org/apache/maven/plugins/clean/HelpMojo.java > src/main/java/org/apache/maven/plugins/clean/HelpMojo.java
test -s src/main/java/org/apache/maven/plugins/clean/HelpMojo.java
unzip -q %{SOURCE3} -d newer
cd newer/%{name}-%{version}
%patch -P 0 -p1
unzip -q %{SOURCE4} 'org/apache/maven/plugins/maven_clean_plugin/HelpMojo.java' -d src/main/java

%build
mkdir -p target/classes target/test-classes .mvn .xmvn
cp='/usr/share/maven/lib/*'
for n in maven-plugin-annotations maven-shared-utils plexus-utils; do cp="$cp:/usr/share/java/javapackages-bootstrap/$n.jar"; done
find src/main/java -name '*.java' | sort > target/java
javac --release 8 -encoding UTF-8 -proc:none -cp "$cp" -d target/classes @target/java
cat > .xmvn/configuration.xml <<'EOF'
<configuration><resolverSettings><metadataRepositories><repository>/usr/share/maven-metadata</repository>
<repository>/usr/share/javapackages-bootstrap/maven-metadata</repository></metadataRepositories></resolverSettings></configuration>
EOF
cat > descriptor.pom <<EOF
<project><modelVersion>4.0.0</modelVersion><groupId>org.apache.maven.plugins</groupId><artifactId>maven-clean-plugin</artifactId><version>%{compat_version}</version><packaging>maven-plugin</packaging></project>
EOF
plugin=$(unzip -p /usr/share/java/javapackages-bootstrap/maven-plugin-plugin.jar META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
ext=/usr/share/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
mvn -B -o -f descriptor.pom -Dmaven.repo.local="$PWD/target/repo" -DgoalPrefix=clean "org.apache.maven.plugins:maven-plugin-plugin:$plugin:descriptor"
grep -F '<goal>clean</goal>' target/classes/META-INF/maven/plugin.xml
grep -F '<goal>help</goal>' target/classes/META-INF/maven/plugin.xml
mkdir -p target/classes/META-INF/maven/org.apache.maven.plugins/%{name}
install -m644 pom.xml target/classes/META-INF/maven/org.apache.maven.plugins/%{name}/pom.xml
jar cf target/plugin.jar -C target/classes .

cd newer/%{name}-%{version}
mkdir -p target/classes .xmvn
cp ../../.xmvn/configuration.xml .xmvn/
cp="%{_datadir}/maven/lib/*:%{_datadir}/java/javapackages-bootstrap/maven-plugin-annotations.jar"
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -encoding UTF-8 -g -proc:none -cp "$cp" -d target/classes @target/sources
mvn -B -o -Dmaven.repo.local="$PWD/target/repo" org.apache.maven.plugins:maven-plugin-plugin:3.9.0.MBI:descriptor
meta=target/classes/META-INF/maven/org.apache.maven.plugins/%{name}
test -s "$meta/plugin-help.xml"
cp pom.xml "$meta/"
cp LICENSE NOTICE target/classes/META-INF/
printf 'artifactId=%%s\\ngroupId=org.apache.maven.plugins\\nversion=%%s\\n' '%{name}' '%{version}' > "$meta/pom.properties"
printf 'Implementation-Title: Apache Maven Clean Plugin\\nImplementation-Version: %%s\\nSpecification-Title: Apache Maven Clean Plugin\\nSpecification-Version: 3.5\\n' '%{version}' > target/module.mf
jar cfm target/plugin.jar target/module.mf -C target/classes .

%install
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 target/plugin.jar %{buildroot}%{artifact_dir}/%{name}-%{compat_version}.jar
install -m644 pom.xml %{buildroot}%{artifact_dir}/%{name}-%{compat_version}.pom
newpath=%{repo_dir}/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}
mkdir -p "%{buildroot}$(dirname "$newpath")"
install -m644 newer/%{name}-%{version}/target/plugin.jar "%{buildroot}$newpath.jar"
install -m644 newer/%{name}-%{version}/pom.xml "%{buildroot}$newpath.pom"
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
 <artifact><groupId>org.apache.maven.plugins</groupId><artifactId>%{name}</artifactId><version>%{compat_version}</version><extension>jar</extension>
 <path>%{artifact_dir}/%{name}-%{compat_version}.jar</path><compatVersions><version>%{compat_version}</version><version>SYSTEM</version></compatVersions></artifact>
 <artifact><groupId>org.apache.maven.plugins</groupId><artifactId>%{name}</artifactId><version>%{compat_version}</version><extension>pom</extension>
 <path>%{artifact_dir}/%{name}-%{compat_version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
<artifact><groupId>org.apache.maven.plugins</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>jar</extension><path>$newpath.jar</path><compatVersions><version>%{version}</version></compatVersions></artifact>
<artifact><groupId>org.apache.maven.plugins</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension><path>$newpath.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version></compatVersions></artifact>
</artifacts></metadata>
EOF
%check
# Run the upstream file-set, exclusion and filesystem cases in the native Maven test harness.
cp='target/classes:/usr/share/maven/lib/*:/usr/share/maven/boot/*'
for n in maven-plugin-testing-harness maven-plugin-annotations maven-shared-utils plexus-utils junit hamcrest-core; do cp="$cp:/usr/share/java/javapackages-bootstrap/$n.jar"; done
find src/test/java -name '*.java' | sort > target/tests
javac --release 8 -encoding UTF-8 -proc:none -cp "$cp" -d target/test-classes @target/tests
cp -r src/test/resources/. target/test-classes/
java -Dbasedir="$PWD" -cp "target/test-classes:$cp" org.junit.runner.JUnitCore org.apache.maven.plugins.clean.CleanMojoTest
# Execute the implicit clean lifecycle on build outputs and confirm a neighboring directory survives.
bash %{SOURCE2} %{buildroot}

cd newer/%{name}-%{version}
src=$PWD
mkdir -p target/test-binaries target/consumer/src/test/resources
cp -r src/test/resources/. target/consumer/src/test/resources/
cp="%{buildroot}%{repo_dir}/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}.jar:%{_datadir}/maven/lib/*:%{_datadir}/maven/boot/*"
for dir in org/apache/maven/plugin-testing/maven-plugin-testing-harness org/codehaus/plexus/plexus-testing org/mockito org/junit/platform org/junit/jupiter; do
    jars=$(find "%{repo_dir}/$dir" -name '*.jar' ! -name '*-sources.jar' -printf '%%p:')
    cp="$jars$cp"
done
for n in commons-io commons-lang3 apiguardian-api opentest4j junit junit-jupiter-params hamcrest-core maven-plugin-annotations byte-buddy byte-buddy-agent objenesis asm asm-commons asm-tree; do
    cp="$cp:%{_datadir}/java/javapackages-bootstrap/$n.jar"
done
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 17 -g -encoding UTF-8 -proc:none -cp "$cp" -d target/test-binaries @target/test-sources
cp -r src/test/resources/. target/test-binaries/
cd target/consumer
java -Dbasedir="$PWD" -cp "$src/target/test-binaries:$cp" %{_libexecdir}/eclipse-equinox/RunJupiter.java org.apache.maven.plugins.clean.CleanMojoTest org.apache.maven.plugins.clean.CleanerTest
bash %{SOURCE2} %{buildroot} %{version}

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/maven-clean-plugin.xml
%{repo_dir}/org/apache/maven/plugins/maven-clean-plugin/

%changelog
%autochangelog
