# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global artifact_dir %{repo}/org/codehaus/mojo/%{name}/%{version}
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
%global xmvn_ext %{_datadir}/javapackages-bootstrap/maven/lib/ext
Name:           build-helper-maven-plugin
Version:        3.6.1
Release:        %autorelease
Summary:        Additional Maven project, source and property goals
License:        MIT
URL:            https://www.mojohaus.org/build-helper-maven-plugin/
VCS:            git:https://github.com/mojohaus/build-helper-maven-plugin
#!RemoteAsset:  sha256:59014d16a348762107042e9d19d9845da0507cc20980a7e62303241b08cdf516
Source0:        https://github.com/mojohaus/build-helper-maven-plugin/archive/refs/tags/%{version}.tar.gz?/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:41e861308dbaa2bfaa772ad973c143d916a5ff199538ec744a47efb1782a61e1
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-sources.jar
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.apache-extras.beanshell:bsh) == 2.1.1
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:) == 91
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
BuildRequires:  unzip
BuildRequires:  xmlstarlet
Provides:       mvn(org.codehaus.mojo:build-helper-maven-plugin) == %{version}
Requires:       javapackages-bootstrap
Requires:       maven
Requires:       mvn(org.apache-extras.beanshell:bsh) == 2.1.1
Requires:       mvn(org.codehaus.mojo:mojo-parent:pom:) == 91

%description
MojoHaus Build Helper adds source roots and resources, attaches artifacts,
and computes project properties during a Maven build.

%prep
%autosetup
unzip -q %{SOURCE1} 'org/codehaus/mojo/build_helper_maven_plugin/HelpMojo.java' -d src/main/java
mkdir -p .xmvn target/classes
cp pom.xml target/upstream.pom
# Njord stages releases to Central. The descriptor build uses a local parent without that extension.
ns=http://maven.apache.org/POM/4.0.0
xmlstarlet ed -P -N m="$ns" -d '/m:project/m:build/m:extensions/m:extension[m:groupId="eu.maveniverse.maven.njord"]' \
    %{repo}/org/codehaus/mojo/mojo-parent/91/mojo-parent-91.pom > target/offline-parent.pom
xmlstarlet ed -P -L -N m="$ns" -s '/m:project/m:parent' -t elem -n relativePath -v target/offline-parent.pom pom.xml
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
<repository>%{_datadir}/maven-metadata</repository><repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF

%build
cp="%{_datadir}/maven/lib/*:%{repo}/org/apache-extras/beanshell/bsh/2.1.1/bsh-2.1.1.jar:%{bootstrap_java}/file-management.jar:%{bootstrap_java}/maven-plugin-annotations.jar:%{bootstrap_java}/plexus-utils.jar"
printf '%%s\n' "$cp" > target/classpath
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -g -encoding UTF-8 -proc:none -cp "$cp" -d target/classes @target/sources
cp -a src/main/resources/. target/classes/
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
mvn -B -o -Dmaven.repo.local="$PWD/target/repo" org.apache.maven.plugins:maven-plugin-plugin:3.9.0.MBI:descriptor
meta=target/classes/META-INF/maven/org.codehaus.mojo/%{name}
install -m644 target/upstream.pom "$meta/pom.xml"
printf 'artifactId=%%s\ngroupId=org.codehaus.mojo\nversion=%%s\n' '%{name}' '%{version}' > "$meta/pom.properties"
cp LICENSE.txt target/classes/META-INF/
jar cf target/%{name}.jar -C target/classes .

%install
path=%{artifact_dir}/%{name}-%{version}
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 target/%{name}.jar "%{buildroot}$path.jar"
install -m644 target/upstream.pom "%{buildroot}$path.pom"
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
<artifact><groupId>org.codehaus.mojo</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>jar</extension><path>$path.jar</path><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
<artifact><groupId>org.codehaus.mojo</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension><path>$path.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
mkdir -p target/tests
cp="target/classes:$(cat target/classpath)"
for jar in %{repo}/org/junit/platform/*/1.12.2/*.jar %{repo}/org/junit/jupiter/*/5.12.2/*.jar; do cp="$cp:$jar"; done
for n in junit-jupiter-params apiguardian-api opentest4j univocity-parsers; do cp="$cp:%{bootstrap_java}/$n.jar"; done
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 17 -g -proc:none -cp "$cp" -d target/tests @target/test-sources %{_libexecdir}/eclipse-equinox/RunJupiter.java
if test -d src/test/resources; then cp -a src/test/resources/. target/tests/; fi
tests=$(find src/test/java -name '*Test.java' | sed 's|^src/test/java/||;s|/|.|g;s|[.]java$||')
java -cp "target/tests:$cp" RunJupiter $tests
test "$(xmlstarlet sel -t -v 'count(/plugin/mojos/mojo)' target/classes/META-INF/maven/plugin.xml)" = 21

mkdir -p target/consumer/.xmvn
cd target/consumer
sed 's|<path>%{repo}|<path>%{buildroot}%{repo}|g' %{buildroot}%{_datadir}/maven-metadata/%{name}.xml > .xmvn/staged.xml
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
<repository>$PWD/.xmvn/staged.xml</repository><repository>%{_datadir}/maven-metadata</repository><repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
cat > pom.xml <<'EOF'
<project><modelVersion>4.0.0</modelVersion><groupId>org.openruyi.check</groupId><artifactId>compiler-path</artifactId><version>1</version>
<build><plugins><plugin><groupId>org.codehaus.mojo</groupId><artifactId>build-helper-maven-plugin</artifactId><version>%{version}</version>
<executions><execution><id>normalize</id><phase>validate</phase><goals><goal>regex-property</goal></goals><configuration>
<name>compiler-message-properties</name><value>C:\src\messages.properties</value><regex>\\</regex><replacement>/</replacement><failIfNoMatch>true</failIfNoMatch>
</configuration></execution><execution><id>check</id><phase>validate</phase><goals><goal>bsh-property</goal></goals><configuration>
<source>if (!"C:/src/messages.properties".equals(project.getProperties().getProperty("compiler-message-properties"))) throw new Exception("Unexpected normalized path");</source>
</configuration></execution></executions></plugin></plugins></build></project>
EOF
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
mvn -B -o -Dmaven.repo.local="$PWD/repo" validate
sed -i 's|C:/src/messages.properties|wrong-path|' pom.xml
if mvn -B -o -Dmaven.repo.local="$PWD/repo" validate > rejected.log 2>&1; then exit 1; fi
grep -F 'Unexpected normalized path' rejected.log

%files
%license LICENSE.txt
%doc README.md
%{_datadir}/maven-metadata/build-helper-maven-plugin.xml
%{artifact_dir}/

%changelog
%autochangelog
