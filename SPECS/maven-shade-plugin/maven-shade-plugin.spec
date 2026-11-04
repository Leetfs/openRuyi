# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository
%global artifact_dir %{repo_dir}/org/apache/maven/plugins/%{name}/%{version}

Name:           maven-shade-plugin
Version:        3.6.1
Release:        %autorelease
Summary:        Apache Maven plugin for combining and relocating Java dependencies
License:        Apache-2.0
URL:            https://maven.apache.org/plugins/maven-shade-plugin/
VCS:            git:https://github.com/apache/maven-shade-plugin
#!RemoteAsset:  sha256:2c2d767373f7fe00a45507ddc6db5cbfda1e11f4d9a900980e1b0b6be33d4590
Source0:        https://archive.apache.org/dist/maven/plugins/%{name}-%{version}-source-release.zip
#!RemoteAsset:  sha256:bf3881a18d157ae7f12c4234c0ea492ab6c2e26dc2062427822fcde5822a2c56
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-sources.jar
#!RemoteAsset:  sha256:87b1e3ffb66259efc09628266d933ec81a8e04a706dfebfb41e29f4d6638ea8a
Source2:        https://github.com/xmlunit/xmlunit/archive/refs/tags/v2.10.3.tar.gz?/xmlunit-2.10.3.tar.gz
Source3:        check-shade.sh
BuildArch:      noarch
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:) == 45
BuildRequires:  mvn(org.mockito:mockito-core) == 4.11.0
BuildRequires:  mvn(org.vafer:jdependency) == 2.10
BuildRequires:  unzip
Provides:       mvn(org.apache.maven.plugins:maven-shade-plugin) == %{version}
Requires:       javapackages-bootstrap
Requires:       maven >= 3.9.9
Requires:       mvn(org.apache.maven.plugins:maven-plugins:pom:) == 45
Requires:       mvn(org.vafer:jdependency) == 2.10

%description
The Apache Maven Shade plugin combines a project and its dependencies into
a single JAR. It can relocate packages and remove unused dependency classes.

%prep
%autosetup -n %{name}-%{version}
# The source classifier includes the help goal generated for this release.
help=org/apache/maven/plugins/maven_shade_plugin/HelpMojo.java
mkdir -p "src/main/java/$(dirname "$help")"
unzip -p %{SOURCE1} "$help" > "src/main/java/$help"
test -s "src/main/java/$help"
mkdir xmlunit
tar xf %{SOURCE2} --strip-components=1 -C xmlunit

%build
mkdir -p target/classes target/test-classes .mvn .xmvn
cp='%{repo_dir}/org/vafer/jdependency/2.10/jdependency-2.10.jar:/usr/share/maven/lib/*:/usr/share/maven/boot/*'
for n in maven-plugin-annotations asm asm-tree asm-commons jdom2 commons-compress; do
    cp="$cp:/usr/share/java/javapackages-bootstrap/$n.jar"
done
printf '%%s\n' "$cp" > target/classpath
find src/main/java -name '*.java' | sort > target/main-sources
javac --release 8 -encoding UTF-8 -processor org.eclipse.sisu.space.SisuIndexAPT6 -cp "$cp" -d target/classes @target/main-sources
grep -Fx org.apache.maven.plugins.shade.DefaultShader target/classes/META-INF/sisu/javax.inject.Named
cat > .xmvn/configuration.xml <<'EOF'
<configuration><resolverSettings><metadataRepositories><repository>/usr/share/maven-metadata</repository>
<repository>/usr/share/javapackages-bootstrap/maven-metadata</repository></metadataRepositories></resolverSettings></configuration>
EOF
plugin=$(unzip -p /usr/share/java/javapackages-bootstrap/maven-plugin-plugin.jar META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
ext=/usr/share/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
mvn -B -o -Dmaven.repo.local="$PWD/target/repo" -DgoalPrefix=shade "org.apache.maven.plugins:maven-plugin-plugin:$plugin:descriptor"
grep -F '<goal>shade</goal>' target/classes/META-INF/maven/plugin.xml
grep -F '<goal>help</goal>' target/classes/META-INF/maven/plugin.xml
meta=target/classes/META-INF/maven/org.apache.maven.plugins/%{name}
test -s "$meta/plugin-help.xml"
install -m644 pom.xml "$meta/pom.xml"
jar cf target/plugin.jar -C target/classes .

%install
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 target/plugin.jar %{buildroot}%{artifact_dir}/%{name}-%{version}.jar
install -m644 pom.xml %{buildroot}%{artifact_dir}/%{name}-%{version}.pom
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
 <artifact><groupId>org.apache.maven.plugins</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>jar</extension>
 <path>%{artifact_dir}/%{name}-%{version}.jar</path><compatVersions><version>%{version}</version><version>SYSTEM</version></compatVersions></artifact>
 <artifact><groupId>org.apache.maven.plugins</groupId><artifactId>%{name}</artifactId><version>%{version}</version><extension>pom</extension>
 <path>%{artifact_dir}/%{name}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
# Compile the upstream tests and their XMLUnit legacy adapter against Maven's native test runtime.
cp="target/classes:$(cat target/classpath):%{repo_dir}/org/mockito/mockito-core/4.11.0/mockito-core-4.11.0.jar"
for n in maven-plugin-testing-harness maven-dependency-tree maven-shared-utils junit hamcrest-core xmlunit-core byte-buddy byte-buddy-agent objenesis asm-analysis asm-util; do
    cp="$cp:/usr/share/java/javapackages-bootstrap/$n.jar"
done
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 17 -sourcepath src/test/java:xmlunit/xmlunit-legacy/src/main/java -proc:none -encoding UTF-8 -cp "$cp" -d target/test-classes @target/test-sources
cp -r src/test/resources/. target/test-classes/
classes=$(find src/test/java -name '*Test.java' ! -name 'Abstract*' | sed 's|src/test/java/||;s|[.]java$||;s|/|.|g' | sort)
java -cp "target/test-classes:$cp" org.junit.runner.JUnitCore $classes
bash %{SOURCE3} %{buildroot}

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/maven-shade-plugin.xml
%{repo_dir}/org/apache/maven/plugins/maven-shade-plugin/

%changelog
%autochangelog
