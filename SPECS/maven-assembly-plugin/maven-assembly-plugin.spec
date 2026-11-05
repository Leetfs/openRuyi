# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global artifact_dir %{repo}/org/apache/maven/plugins/%{name}/%{version}
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
%global xmvn_ext %{_datadir}/javapackages-bootstrap/maven/lib/ext
Name:           maven-assembly-plugin
Version:        3.8.0
Release:        %autorelease
Summary:        Create Maven project distributions
License:        Apache-2.0
URL:            https://maven.apache.org/plugins/maven-assembly-plugin/
VCS:            git:https://github.com/apache/maven-assembly-plugin
#!RemoteAsset:  sha256:7571a4d704f219051127259b1f7292f80cd422376ba463c2318214ddf639044c
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
#!RemoteAsset:  sha256:92443a5fe61eeba708528ec7c181dd9ae4495e2d02355bb8989e522f831e39c5
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-sources.jar
#!RemoteAsset:  sha256:45deefd1f842e35f0c1089eeecd057df632230ec6096ccc6fccfc639b95548d4
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/jdom/jdom2/2.0.6.1/jdom2-2.0.6.1-sources.jar
#!RemoteAsset:  sha256:2eb519f8820ff64e8001f9b4c2c6cb09296cdd99f5b4eed083d522ad3a6f784e
Source3:        https://maven-central.storage-download.googleapis.com/maven2/jaxen/jaxen/2.0.0/jaxen-2.0.0-sources.jar
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
The Assembly plugin builds distribution archives from assemblies of project\nfiles, dependencies and module artifacts.

%prep
%autosetup -n %{name}-%{version}
unzip -q %{SOURCE1} 'org/apache/maven/plugins/maven_assembly_plugin/HelpMojo.java' \
    'org/apache/maven/plugins/assembly/model/Assembly.java' \
    'org/apache/maven/plugins/assembly/model/Component.java' \
    'org/apache/maven/plugins/assembly/model/ContainerDescriptorHandlerConfig.java' \
    'org/apache/maven/plugins/assembly/model/DependencySet.java' \
    'org/apache/maven/plugins/assembly/model/FileItem.java' \
    'org/apache/maven/plugins/assembly/model/FileSet.java' \
    'org/apache/maven/plugins/assembly/model/ModuleBinaries.java' \
    'org/apache/maven/plugins/assembly/model/ModuleSet.java' \
    'org/apache/maven/plugins/assembly/model/ModuleSources.java' \
    'org/apache/maven/plugins/assembly/model/UnpackOptions.java' \
    'org/apache/maven/plugins/assembly/model/io/xpp3/AssemblyXpp3Reader.java' \
    'org/apache/maven/plugins/assembly/model/io/xpp3/AssemblyXpp3Writer.java' \
    'org/apache/maven/plugins/assembly/model/io/xpp3/ComponentXpp3Reader.java' \
    'org/apache/maven/plugins/assembly/model/io/xpp3/ComponentXpp3Writer.java' -d src/main/java
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
mvn -B -o -Dmaven.repo.local="$PWD/target/repo" org.eclipse.sisu:sisu-maven-plugin:1.0.0.MBI:main-index org.apache.maven.plugins:maven-plugin-plugin:3.9.0.MBI:descriptor
test -s target/classes/META-INF/sisu/javax.inject.Named
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
# The upstream component-descriptor test evaluates XPath against the archive.
mkdir -p target/xml-test/{jaxen,dom,classes}
unzip -qo %{SOURCE3} -d target/xml-test/jaxen
unzip -qo %{SOURCE2} -d target/xml-test/dom
find target/xml-test/jaxen/org/jaxen -name '*.java' ! -path '*/jaxen/jdom/*' ! -path '*/jaxen/dom4j/*' ! -path '*/jaxen/xom/*' | sort > target/xml-test/jaxen.list
javac --release 8 -proc:none -encoding UTF-8 -d target/xml-test/classes @target/xml-test/jaxen.list
find target/xml-test/dom -name '*.java' ! -name module-info.java | sort > target/xml-test/jdom.list
javac --release 8 -proc:none -cp "target/xml-test/classes:%{bootstrap_java}/*" -d target/xml-test/classes @target/xml-test/jdom.list
cp="target/xml-test/classes:$cp:%{bootstrap_java}/*"
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
mkdir descriptor
echo assembled > descriptor/probe.txt
cat > assembly.xml <<'EOF'
<assembly><id>sdk</id><formats><format>zip</format></formats><includeBaseDirectory>false</includeBaseDirectory><fileSets><fileSet><directory>descriptor</directory><outputDirectory>/</outputDirectory></fileSet></fileSets></assembly>
EOF
sed -i 's|</project>|<build><plugins><plugin><artifactId>maven-assembly-plugin</artifactId><version>%{version}</version><configuration><descriptors><descriptor>assembly.xml</descriptor></descriptors></configuration></plugin></plugins></build></project>|' pom.xml
mvn -B -o -Dmaven.repo.local="$PWD/repo" org.apache.maven.plugins:%{name}:%{version}:single
test "$(unzip -p target/sample-1-sdk.zip probe.txt)" = assembled

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/maven-assembly-plugin.xml
%{artifact_dir}/

%changelog
%autochangelog
