# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global artifact_dir %{repo}/org/apache/maven/plugins/%{name}/%{version}
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
%global xmvn_ext %{_datadir}/javapackages-bootstrap/maven/lib/ext
Name:           maven-jar-plugin
Version:        3.5.0
Release:        %autorelease
Summary:        Create project archives with Maven
License:        Apache-2.0
URL:            https://maven.apache.org/plugins/maven-jar-plugin/
VCS:            git:https://github.com/apache/maven-jar-plugin
#!RemoteAsset:  sha256:f35bf0dbbb372cfd60efdf9ccf602a2c52e581851914e7f0187453b0bec5218d
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
#!RemoteAsset:  sha256:f37f4c7c97217a268441d16ee9f2e906df42f430d233e4a27e87f71096a4bbfc
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-sources.jar
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.11
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness) == 3.5.1
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:) == 45
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
BuildRequires:  mvn(org.mockito:mockito-core) == 4.11.0
BuildRequires:  mvn(commons-io:commons-io) == 2.21.0
BuildRequires:  unzip
Provides:       mvn(org.apache.maven.plugins:%{name}) == %{version}
Requires:       javapackages-bootstrap
Requires:       maven
Requires:       mvn(commons-io:commons-io) == 2.21.0
Requires:       mvn(org.apache.maven.plugins:maven-plugins:pom:) == 45

%description
The JAR plugin creates archives of project classes and test classes with\nMaven Archiver.

%prep
%autosetup -n %{name}-%{version}
unzip -q %{SOURCE1} 'org/apache/maven/plugins/maven_jar_plugin/HelpMojo.java' -d src/main/java
mkdir -p .xmvn target/classes
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
<repository>%{_datadir}/maven-metadata</repository><repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF

%build
cp="%{_datadir}/maven/lib/*:%{bootstrap_java}/*"
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -g -encoding UTF-8 -proc:none -cp "$cp" -d target/classes @target/sources
if test -d src/main/resources; then cp -a src/main/resources/. target/classes/; fi
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
mvn -B -o -Dmaven.repo.local="$PWD/target/repo" org.apache.maven.plugins:maven-plugin-plugin:3.9.0.MBI:descriptor
meta=target/classes/META-INF/maven/org.apache.maven.plugins/%{name}
install -m644 pom.xml "$meta/pom.xml"
printf 'artifactId=%%s\ngroupId=org.apache.maven.plugins\nversion=%%s\n' '%{name}' '%{version}' > "$meta/pom.properties"
cp LICENSE NOTICE target/classes/META-INF/
jar cf target/%{name}.jar -C target/classes .

%install
path=%{artifact_dir}/%{name}-%{version}
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 target/%{name}.jar "%{buildroot}$path.jar"
install -m644 pom.xml "%{buildroot}$path.pom"
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
<artifact><groupId>org.apache.maven.plugins</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>jar</extension><path>$path.jar</path><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
<artifact><groupId>org.apache.maven.plugins</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension><path>$path.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
mkdir -p target/test-classes
repo=%{repo}
cp="target/%{name}.jar:target/test-classes:%{_datadir}/maven/lib/*:%{_datadir}/maven/boot/*"
for dir in org/junit org/mockito org/apache/maven/plugin-testing org/codehaus/plexus/plexus-testing; do
    jars=$(find "$repo/$dir" -name '*.jar' ! -name '*-sources.jar' -printf '%%p:')
    cp="$jars$cp"
done
for n in junit-jupiter-params apiguardian-api opentest4j univocity-parsers junit hamcrest-core byte-buddy byte-buddy-agent objenesis maven-plugin-annotations plexus-utils plexus-archiver plexus-io plexus-java plexus-compiler-api plexus-compiler-manager plexus-compiler-javac maven-archiver plexus-build-api0 file-management commons-io asm asm-commons asm-tree; do
    cp="$cp:%{bootstrap_java}/$n.jar"
done
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 17 -g -proc:none -cp "$cp" -d target/test-classes @target/test-sources %{_libexecdir}/eclipse-equinox/RunJupiter.java
if test -d src/test/resources; then cp -a src/test/resources/. target/test-classes/; fi
tests=$(sed -n '/Test[.]java$/ {s@^src/test/java/@@;s@/@.@g;s@[.]java$@@;p;}' target/test-sources)
java -cp "$cp" RunJupiter $tests
mkdir -p target/consumer/.xmvn
cd target/consumer
sed 's|<path>%{repo}|<path>%{buildroot}%{repo}|g' %{buildroot}%{_datadir}/maven-metadata/%{name}.xml > .xmvn/staged.xml
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
<repository>$PWD/.xmvn/staged.xml</repository><repository>%{_datadir}/maven-metadata</repository><repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
cat > pom.xml <<'EOF'
<project><modelVersion>4.0.0</modelVersion><groupId>org.openruyi.check</groupId><artifactId>sample</artifactId><version>1</version></project>
EOF
mkdir -p target/classes
echo archived > target/classes/probe.txt
mvn -B -o -Dmaven.repo.local="$PWD/repo" org.apache.maven.plugins:%{name}:%{version}:jar
test "$(unzip -p target/sample-1.jar probe.txt)" = archived

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/maven-jar-plugin.xml
%{artifact_dir}/

%changelog
%autochangelog
