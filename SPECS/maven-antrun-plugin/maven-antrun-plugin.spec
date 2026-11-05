# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global artifact_dir %{repo}/org/apache/maven/plugins/%{name}/%{version}
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
%global xmvn_ext %{_datadir}/javapackages-bootstrap/maven/lib/ext
Name:           maven-antrun-plugin
Version:        3.2.0
Release:        %autorelease
Summary:        Execute Apache Ant tasks from Maven
License:        Apache-2.0
URL:            https://maven.apache.org/plugins/maven-antrun-plugin/
VCS:            git:https://github.com/apache/maven-antrun-plugin
#!RemoteAsset:  sha256:db6eb94fff3c174cb6424401534a27ca7a7c3810f236b62a0e514bd9951d9467
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
#!RemoteAsset:  sha256:47ccb83c2c35cffb5b0cd57e05bf42b17efc44bebe97597741af23d2ea531ffe
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-sources.jar
# Historical test tools execute the upstream calculator grammar through the plugin classpath.
#!RemoteAsset:  sha256:df903d542f8d2536d91eb9377afe745f23b3ee0b5ab407686403664b78699df2
Source2:        https://www.antlr2.org/download/antlr-2.7.4.tar.gz
#!RemoteAsset:  sha256:045e6ac70203c783f55f16a819ab5cd1b28e626c464e11006d74b618504a1b86
Source3:        https://raw.githubusercontent.com/apache/ant/rel/1.6.5/src/main/org/apache/tools/ant/taskdefs/optional/ANTLR.java
Source4:        check-antrun-it.py
Source5:        CheckInvoker.java
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.11
BuildRequires:  mvn(org.apache-extras.beanshell:bsh) == 2.1.1
BuildRequires:  mvn(org.apache.maven.plugins:maven-clean-plugin) == 3.5.0
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin) == 3.6.2
BuildRequires:  mvn(org.apache.maven.plugins:maven-install-plugin) == 3.1.4
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:) == 45
BuildRequires:  mvn(org.apache.maven.plugins:maven-resources-plugin) == 3.5.0
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin) == 3.5.5
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin) == 3.6.1
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
BuildRequires:  python3
BuildRequires:  unzip
Provides:       mvn(org.apache.maven.plugins:maven-antrun-plugin) == %{version}
Requires:       javapackages-bootstrap
Requires:       maven
Requires:       mvn(org.apache.maven.plugins:maven-plugins:pom:) == 45

%description
The Maven AntRun plugin executes Ant targets inside the Maven lifecycle.
It exposes the project's dependencies and properties to Ant tasks.

%prep
%autosetup -n %{name}-%{version}
unzip -q %{SOURCE1} 'org/apache/maven/plugins/maven_antrun_plugin/HelpMojo.java' 'org/apache/maven/plugins/antrun/taskconfig/*.java' -d src/main/java
mkdir -p .xmvn target/classes
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
<repository>%{_datadir}/maven-metadata</repository><repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF

%build
cp="%{_datadir}/maven/lib/*:%{bootstrap_java}/ant.jar:%{bootstrap_java}/ant-launcher.jar:%{bootstrap_java}/maven-plugin-annotations.jar:%{bootstrap_java}/plexus-utils.jar"
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -g -encoding UTF-8 -proc:none -cp "$cp" -d target/classes @target/sources
cp -a src/main/resources/. target/classes/
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
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
mkdir -p target/test-classes
cp="target/classes:%{_datadir}/maven/lib/*:%{bootstrap_java}/ant.jar"
for jar in %{repo}/org/junit/platform/*/1.12.2/*.jar %{repo}/org/junit/jupiter/*/5.12.2/*.jar; do cp="$cp:$jar"; done
for n in apiguardian-api opentest4j hamcrest-core xmlunit-core xmlunit-matchers plexus-utils; do cp="$cp:%{bootstrap_java}/$n.jar"; done
find src/test/java -name '*.java' | sort > target/tests
javac --release 17 -g -proc:none -cp "$cp" -d target/test-classes @target/tests %{_libexecdir}/eclipse-equinox/RunJupiter.java
cp -a src/test/resources/. target/test-classes/
tests=$(find src/test/java -name '*Test.java' | sed 's|^src/test/java/||;s|/|.|g;s|[.]java$||')
java -cp "target/test-classes:$cp" RunJupiter $tests
python3 %{SOURCE4} %{buildroot} %{SOURCE2} %{SOURCE3} %{SOURCE5}

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/maven-antrun-plugin.xml
%{artifact_dir}/

%changelog
%autochangelog
