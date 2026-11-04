# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo %{_datadir}/maven-repository
%global artifact_dir %{repo}/org/apache/maven/plugins/%{name}/%{version}
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
%global xmvn_ext %{_datadir}/javapackages-bootstrap/maven/lib/ext
Name:           maven-resources-plugin
Version:        3.5.0
Release:        %autorelease
Summary:        Copy and filter Maven project resources
License:        Apache-2.0
URL:            https://maven.apache.org/plugins/maven-resources-plugin/
VCS:            git:https://github.com/apache/maven-resources-plugin
#!RemoteAsset:  sha256:7e3e7203f80eb8b5b2c0a2fc7d6565062bd29a98c7a71f1456b5e7fd0a40a009
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
#!RemoteAsset:  sha256:b7bf6cadd6ca4e0970b93e0825a36e30755afe3496158710d4694f2f6c82fdea
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-sources.jar
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.12
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:) == 47
BuildRequires:  mvn(org.apache.maven.shared:maven-filtering) == %{version}
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness) == 3.5.1
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
BuildRequires:  mvn(org.mockito:mockito-junit-jupiter) == 4.11.0
BuildRequires:  unzip
Provides:       mvn(org.apache.maven.plugins:%{name}) == %{version}
Requires:       javapackages-bootstrap
Requires:       maven >= 3.9.12
Requires:       mvn(org.apache.maven.shared:maven-filtering) == %{version}
Requires:       mvn(org.apache.maven.plugins:maven-plugins:pom:) == 47

%description
The Maven Resources Plugin copies main and test resources, interpolates
properties, and selects how to detect changes in existing output files.

%prep
%autosetup -n %{name}-%{version}
# The release source classifier contains the Java source for the generated help goal.
unzip -q %{SOURCE1} 'org/apache/maven/plugins/maven_resources_plugin/HelpMojo.java' -d src/main/java
mkdir -p .xmvn target/classes
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
<repository>%{_datadir}/maven-metadata</repository>
<repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF

%build
cp="%{repo}/org/apache/maven/shared/maven-filtering/%{version}/maven-filtering-%{version}.jar:%{_datadir}/maven/lib/*:%{bootstrap_java}/maven-plugin-annotations.jar:%{bootstrap_java}/plexus-build-api0.jar"
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -g -encoding UTF-8 -proc:none -cp "$cp" -d target/classes @target/sources
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
mvn -B -o -Dmaven.repo.local="$PWD/target/repo" org.apache.maven.plugins:maven-plugin-plugin:3.9.0.MBI:descriptor
meta=target/classes/META-INF/maven/org.apache.maven.plugins/%{name}
test -s "$meta/plugin-help.xml"
cp pom.xml "$meta/"
printf 'artifactId=%%s\ngroupId=org.apache.maven.plugins\nversion=%%s\n' '%{name}' '%{version}' > "$meta/pom.properties"
cp LICENSE NOTICE target/classes/META-INF/
printf 'Specification-Title: Apache Maven Resources Plugin\nSpecification-Version: 3.5\nSpecification-Vendor: The Apache Software Foundation\nImplementation-Title: Apache Maven Resources Plugin\nImplementation-Version: %%s\nImplementation-Vendor: The Apache Software Foundation\n' '%{version}' > target/module.mf
jar cfm target/%{name}.jar target/module.mf -C target/classes .

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
mkdir -p target/test-classes
cp="$PWD/target/classes:%{_datadir}/maven/lib/*:%{_datadir}/maven/boot/*"
for dir in org/apache/maven/plugin-testing/maven-plugin-testing-harness org/apache/maven/shared/maven-filtering org/codehaus/plexus/plexus-testing org/mockito org/junit/platform org/junit/jupiter; do
    jars=$(find "%{repo}/$dir" -name '*.jar' ! -name '*-sources.jar' -printf '%%p:')
    cp="$jars$cp"
done
for n in maven-plugin-annotations plexus-archiver plexus-io plexus-build-api0 commons-io commons-compress commons-lang3 commons-codec xz apiguardian-api opentest4j junit junit-jupiter-params hamcrest-core byte-buddy byte-buddy-agent objenesis asm asm-commons asm-tree; do
    cp="$cp:%{bootstrap_java}/$n.jar"
done
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 17 -g -encoding UTF-8 -proc:none -cp "$cp" -d target/test-classes @target/test-sources
if test -d src/test/resources; then cp -r src/test/resources/. target/test-classes/; fi
tests=$(find src/test/java -name '*Test.java' | sed 's|src/test/java/||;s|[.]java$||;s|/|.|g' | sort)
java -Dbasedir="$PWD" -cp "target/test-classes:target/classes:$cp" %{_libexecdir}/eclipse-equinox/RunJupiter.java $tests

# Read the staged plugin as an offline Maven consumer using the SDK filtering configuration.
mkdir -p target/consumer/.xmvn target/consumer/src/main/resources
cd target/consumer
sed 's|<path>%{repo}|<path>%{buildroot}%{repo}|g' %{buildroot}%{_datadir}/maven-metadata/%{name}.xml > .xmvn/plugin.xml
sed "/<metadataRepositories>/a <repository>$PWD/.xmvn/plugin.xml</repository>" ../../.xmvn/configuration.xml > .xmvn/configuration.xml
cat > pom.xml <<'POM'
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
<groupId>org.openruyi.check</groupId><artifactId>branding</artifactId><version>1.2.3</version>
<properties><project.build.sourceEncoding>UTF-8</project.build.sourceEncoding></properties>
<build><resources><resource><directory>src/main/resources</directory><filtering>true</filtering>
</resource></resources><plugins><plugin><groupId>org.apache.maven.plugins</groupId>
<artifactId>maven-resources-plugin</artifactId><version>%{version}</version>
<configuration><changeDetection>${mode}</changeDetection></configuration>
</plugin></plugins></build></project>
POM
printf 'version=${project.version}\n' > src/main/resources/about.mappings
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
mkdir -p target/classes
for mode in always never timestamp; do
    echo sentinel > target/classes/about.mappings
    touch -r src/main/resources/about.mappings target/classes/about.mappings
    mvn -B -o -Dmaven.repo.local="$PWD/repo" -Dmode="$mode" org.apache.maven.plugins:%{name}:%{version}:resources
    case "$mode" in
        always) grep -Fx 'version=1.2.3' target/classes/about.mappings ;;
        *) grep -Fx sentinel target/classes/about.mappings ;;
    esac
done
if mvn -B -o -Dmaven.repo.local="$PWD/repo" -Dmode=invalid org.apache.maven.plugins:%{name}:%{version}:resources > invalid.log 2>&1; then exit 1; fi
grep -F 'Invalid value for changeDetection: invalid' invalid.log

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/maven-resources-plugin.xml
%{artifact_dir}/

%changelog
%autochangelog
