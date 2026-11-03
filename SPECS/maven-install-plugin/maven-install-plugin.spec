# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository
%define build_mvn %{_libexecdir}/javapackages-bootstrap/mvn --batch-mode --offline -Dmaven.repo.local="$PWD/local-repository"

Name:           maven-install-plugin
Version:        3.1.4
Release:        %autorelease
Summary:        Install Maven artifacts into a local repository
License:        Apache-2.0
URL:            https://maven.apache.org/plugins/maven-install-plugin/
VCS:            git:https://github.com/apache/maven-install-plugin
#!RemoteAsset:  sha256:b09860ad4ffaf676ef81beba65e5fd80c6e093735d10a463e851a4d2aa489289
Source0:        https://github.com/apache/maven-install-plugin/archive/refs/tags/maven-install-plugin-%{version}.tar.gz
#!RemoteAsset:  sha256:d45bd34064a6032e728f77d58800cca77ca16f59abcfda4f3b0b60b7833e4edf
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/%{name}/3.1.1/%{name}-3.1.1-source-release.zip
#!RemoteAsset:  sha256:68ed00285f59173b87f5dc2fca92db11626d5693bcb8781273f31a9d47c5e932
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/%{name}/3.1.1/%{name}-3.1.1-sources.jar
Patch0:         0001-use-the-injected-local-repository-manager-in-3.1.1-tests.patch
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:) == 39
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness) == 3.5.1
BuildRequires:  unzip
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.mockito:mockito-core) == 4.11.0
Provides:       mvn(org.apache.maven.plugins:maven-install-plugin) == %{version}
Provides:       mvn(org.apache.maven.plugins:maven-install-plugin) == 3.1.1
Requires:       mvn(org.apache.maven.plugins:maven-plugins:pom:) == 39
Requires:       javapackages-bootstrap

%description
The Maven Install Plugin places project artifacts, POMs and their
attachments into a local repository for use by other Maven builds.

%prep
%autosetup -N -n maven-install-plugin-maven-install-plugin-%{version}
mkdir -p .xmvn local-repository
if test -d %{repo_dir}; then cp -as %{repo_dir}/. local-repository/; fi
cat > .xmvn/configuration.xml <<EOF
<configuration>
  <repositories><repository><id>install</id><type>maven</type>
    <properties><root>usr/share/maven-repository</root></properties>
  </repository></repositories>
  <installerSettings><metadataDir>usr/share/maven-metadata</metadataDir></installerSettings>
  <artifactManagement><rule><artifactGlob/>
    <versions><version>%{version}</version><version>SYSTEM</version></versions>
  </rule></artifactManagement>
  <resolverSettings><metadataRepositories>
    <repository>%{_datadir}/maven-metadata</repository>
    <repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
  </metadataRepositories></resolverSettings>
</configuration>
EOF

unzip -q %{SOURCE1} -d compat
cd compat/%{name}-3.1.1
%patch -P 0 -p1
unzip -q %{SOURCE2} 'org/apache/maven/plugins/maven_install_plugin/HelpMojo.java' -d src/main/java

%build
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
%{build_mvn} org.apache.maven.plugins:maven-resources-plugin:resources \
    org.apache.maven.plugins:maven-compiler-plugin:compile \
    org.apache.maven.plugins:maven-plugin-plugin:descriptor \
    org.apache.maven.plugins:maven-jar-plugin:jar \
    org.fedoraproject.xmvn:xmvn-mojo:install

cd compat/%{name}-3.1.1
mkdir -p target/classes .xmvn
cp ../../.xmvn/configuration.xml .xmvn/
cp="%{_datadir}/maven/lib/*:%{_datadir}/java/javapackages-bootstrap/maven-plugin-annotations.jar"
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -g -proc:none -encoding UTF-8 -cp "$cp" -d target/classes @target/sources
ext=%{_datadir}/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
mvn -B -o -Dmaven.repo.local="$PWD/target/repo" org.apache.maven.plugins:maven-plugin-plugin:3.9.0.MBI:descriptor
meta=target/classes/META-INF/maven/org.apache.maven.plugins/%{name}
mkdir -p "$meta"
cp LICENSE NOTICE target/classes/META-INF/
cp pom.xml "$meta/"
printf 'artifactId=%%s\ngroupId=org.apache.maven.plugins\nversion=3.1.1\n' '%{name}' > "$meta/pom.properties"
jar cf target/plugin.jar -C target/classes .

%install
%{_libexecdir}/javapackages-bootstrap/xmvn-install -R "$PWD/.xmvn-reactor" -d %{buildroot} -n %{name}

path=%{repo_dir}/org/apache/maven/plugins/%{name}/3.1.1/%{name}-3.1.1
mkdir -p "%{buildroot}$(dirname "$path")"
install -m644 compat/%{name}-3.1.1/target/plugin.jar "%{buildroot}$path.jar"
install -m644 compat/%{name}-3.1.1/pom.xml "%{buildroot}$path.pom"
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}-compat.xml <<EOF
<metadata><artifacts>
<artifact><groupId>org.apache.maven.plugins</groupId><artifactId>%{name}</artifactId><version>3.1.1</version><extension>jar</extension><path>$path.jar</path><compatVersions><version>3.1.1</version></compatVersions></artifact>
<artifact><groupId>org.apache.maven.plugins</groupId><artifactId>%{name}</artifactId><version>3.1.1</version><extension>pom</extension><path>$path.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>3.1.1</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
%{build_mvn} org.apache.maven.plugins:maven-resources-plugin:testResources \
    org.apache.maven.plugins:maven-compiler-plugin:testCompile \
    org.apache.maven.plugins:maven-surefire-plugin:test
test -s target/surefire-reports/TEST-org.apache.maven.plugins.install.InstallMojoTest.xml
test -s target/surefire-reports/TEST-org.apache.maven.plugins.install.InstallFileMojoTest.xml

cd compat/%{name}-3.1.1
mkdir -p target/test-classes
cp="$PWD/target/plugin.jar:%{repo_dir}/org/apache/maven/plugin-testing/maven-plugin-testing-harness/3.5.1/maven-plugin-testing-harness-3.5.1.jar:%{_datadir}/maven/lib/*:%{_datadir}/maven/boot/*"
for dir in org/codehaus/plexus/plexus-testing org/mockito; do
    jars=$(find "%{repo_dir}/$dir" -name '*.jar' ! -name '*-sources.jar' -printf '%%p:')
    cp="$jars$cp"
done
for n in maven-plugin-annotations plexus-archiver plexus-io plexus-build-api0 commons-io commons-compress commons-lang3 commons-codec xz apiguardian-api opentest4j junit hamcrest-core byte-buddy byte-buddy-agent objenesis asm asm-commons asm-tree; do
    cp="$cp:%{_datadir}/java/javapackages-bootstrap/$n.jar"
done
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 17 -g -proc:none -encoding UTF-8 -cp "$cp" -d target/test-classes @target/test-sources
cp -r src/test/resources/. target/test-classes/
java -Dbasedir="$PWD" -cp "target/test-classes:$cp" org.junit.runner.JUnitCore org.apache.maven.plugins.install.InstallFileMojoTest org.apache.maven.plugins.install.InstallMojoTest
mkdir -p target/consumer/.xmvn
cd target/consumer
sed 's|<path>%{repo_dir}|<path>%{buildroot}%{repo_dir}|g' %{buildroot}%{_datadir}/maven-metadata/%{name}-compat.xml > .xmvn/staged.xml
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories><repository>$PWD/.xmvn/staged.xml</repository><repository>%{_datadir}/maven-metadata</repository><repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository></metadataRepositories></resolverSettings></configuration>
EOF
echo sample > payload.txt
jar cf payload.jar payload.txt
ext=%{_datadir}/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
mvn -B -o -Dmaven.repo.local="$PWD/repo" org.apache.maven.plugins:%{name}:3.1.1:install-file -DlocalRepositoryPath="$PWD/installed" -Dfile="$PWD/payload.jar" -DgroupId=org.openruyi.fixture -DartifactId=sample -Dversion=1.2 -Dpackaging=jar -DgeneratePom=true
cmp payload.jar installed/org/openruyi/fixture/sample/1.2/sample-1.2.jar
test -s installed/org/openruyi/fixture/sample/1.2/sample-1.2.pom

%files
%doc README.md
%license LICENSE NOTICE
%{_datadir}/maven-metadata/maven-install-plugin*.xml
%{repo_dir}/org/apache/maven/plugins/maven-install-plugin/

%changelog
%autochangelog
