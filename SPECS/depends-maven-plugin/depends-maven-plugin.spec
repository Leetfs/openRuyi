# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
%global xmvn_ext %{_datadir}/javapackages-bootstrap/maven/lib/ext

Name:           depends-maven-plugin
Version:        1.5.0
Release:        %autorelease
Summary:        Maven plugin for generating dependency properties
License:        Apache-2.0
URL:            https://servicemix.apache.org/
VCS:            git:https://github.com/apache/servicemix-maven-plugins
#!RemoteAsset:  sha256:2972748087af67d384389b37f9b0d3edf8fb1dd2a1a7b25beb127306e1851996
Source0:        https://github.com/apache/servicemix-maven-plugins/archive/refs/tags/depends-maven-plugin-%{version}.tar.gz
#!RemoteAsset:  sha256:d89978cffcf778ea85eaa8a4a15ea10f5108119ccd0abf4cb758b6091ebcf5aa
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/servicemix/tooling/maven-plugins-pom/7/maven-plugins-pom-7.pom
#!RemoteAsset:  sha256:00fff3d7dad849a7cee02bb2998396292858aac996457ba20f40c85f61b88252
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/servicemix/servicemix-pom/5/servicemix-pom-5.pom
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  python3
BuildRequires:  unzip
Provides:       mvn(org.apache.servicemix.tooling:depends-maven-plugin) == %{version}
Provides:       mvn(org.apache.servicemix.tooling:maven-plugins-pom:pom:) == 7
Provides:       mvn(org.apache.servicemix:servicemix-pom:pom:) == 5
Requires:       maven >= 3.9.9

%description
The Apache ServiceMix Depends Maven Plugin writes project and dependency
coordinates, versions, scopes and artifact types to a properties file.

%prep
%autosetup -n servicemix-maven-plugins-depends-maven-plugin-%{version}
# The tagged checkout carries the next plugin parent. Use the published parents.
install -m644 %{SOURCE1} maven-plugins-pom/pom.xml
mkdir -p repo/org/apache/servicemix/servicemix-pom/5
install -m644 %{SOURCE2} repo/org/apache/servicemix/servicemix-pom/5/servicemix-pom-5.pom
# Maven 3 supplies the former maven-project classes through core and compat.
python3 - "$(rpm -q --qf '%%{VERSION}' maven)" <<'PYMODEL'
from copy import deepcopy
from pathlib import Path
from xml.etree import ElementTree as ET
import sys
path = Path("depends-maven-plugin/pom.xml")
uri = "http://maven.apache.org/POM/4.0.0"
ET.register_namespace("", uri)
ET.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")
model = ET.parse(path)
deps = model.find("{*}dependencies")
for dep in list(deps):
    if dep.findtext("{*}groupId") == "org.apache.maven":
        name = dep.find("{*}artifactId")
        dep.find("{*}version").text = sys.argv[1]
        ET.SubElement(dep, "{" + uri + "}scope").text = "provided"
        if name.text == "maven-project":
            name.text = "maven-core"
            compat = deepcopy(dep)
            compat.find("{*}artifactId").text = "maven-compat"
            deps.append(compat)
model.write(path, encoding="utf-8", xml_declaration=True)
PYMODEL

%build
cd depends-maven-plugin
mkdir -p target/classes .xmvn
find src/main/java -name '*.java' | sort > target/sources
cp="%{_datadir}/maven/lib/*:%{_datadir}/maven/boot/*:%{bootstrap_java}/maven-plugin-annotations.jar:%{bootstrap_java}/plexus-build-api0.jar"
javac --release 8 -proc:none -encoding UTF-8 -cp "$cp" -d target/classes @target/sources
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
  <repository>%{_datadir}/maven-metadata</repository>
  <repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
plugin=$(unzip -p %{bootstrap_java}/maven-plugin-plugin.jar META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
test -n "$plugin"
mvn -B --offline -Dmaven.repo.local="$PWD/../repo" -DgoalPrefix=depends "org.apache.maven.plugins:maven-plugin-plugin:$plugin:descriptor"
grep -F '<goal>generate-depends-file</goal>' target/classes/META-INF/maven/plugin.xml
mkdir -p target/classes/META-INF/maven/org.apache.servicemix.tooling/depends-maven-plugin
install -m644 pom.xml target/classes/META-INF/maven/org.apache.servicemix.tooling/depends-maven-plugin/pom.xml
printf 'groupId=org.apache.servicemix.tooling\nartifactId=depends-maven-plugin\nversion=%{version}\n' > target/classes/META-INF/maven/org.apache.servicemix.tooling/depends-maven-plugin/pom.properties
jar --create --file target/%{name}.jar -C target/classes .

%install
install -Dm644 depends-maven-plugin/pom.xml %{buildroot}%{_datadir}/maven-repository/org/apache/servicemix/tooling/depends-maven-plugin/%{version}/depends-maven-plugin-%{version}.pom
install -m644 depends-maven-plugin/target/%{name}.jar %{buildroot}%{_datadir}/maven-repository/org/apache/servicemix/tooling/depends-maven-plugin/%{version}/depends-maven-plugin-%{version}.jar
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/maven-repository/org/apache/servicemix/tooling/maven-plugins-pom/7/maven-plugins-pom-7.pom
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/maven-repository/org/apache/servicemix/servicemix-pom/5/servicemix-pom-5.pom
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>org.apache.servicemix.tooling</groupId><artifactId>depends-maven-plugin</artifactId><version>%{version}</version><extension>jar</extension>
    <path>%{_datadir}/maven-repository/org/apache/servicemix/tooling/depends-maven-plugin/%{version}/depends-maven-plugin-%{version}.jar</path></artifact>
  <artifact><groupId>org.apache.servicemix.tooling</groupId><artifactId>depends-maven-plugin</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/org/apache/servicemix/tooling/depends-maven-plugin/%{version}/depends-maven-plugin-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
  <artifact><groupId>org.apache.servicemix.tooling</groupId><artifactId>maven-plugins-pom</artifactId><version>7</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/org/apache/servicemix/tooling/maven-plugins-pom/7/maven-plugins-pom-7.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
  <artifact><groupId>org.apache.servicemix</groupId><artifactId>servicemix-pom</artifactId><version>5</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/org/apache/servicemix/servicemix-pom/5/servicemix-pom-5.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
mkdir -p check/{.xmvn,metadata,empty,repo/org/openruyi/check/leaf/1.2.3}
cd check
for file in %{_datadir}/maven-metadata/*.xml; do
    test "$(basename "$file")" = %{name}.xml || ln -s "$file" metadata/
done
sed 's@<path>/@<path>%{buildroot}/@g' %{buildroot}%{_datadir}/maven-metadata/%{name}.xml > metadata/%{name}.xml
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
  <repository>$PWD/metadata</repository><repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
leaf=repo/org/openruyi/check/leaf/1.2.3/leaf-1.2.3
cat > "$leaf.pom" <<'EOF'
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
  <groupId>org.openruyi.check</groupId><artifactId>leaf</artifactId><version>1.2.3</version>
</project>
EOF
jar --create --file "$leaf.jar" -C empty .
cat > pom.xml <<'EOF'
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
  <groupId>org.openruyi.check</groupId><artifactId>consumer</artifactId><version>1</version>
  <dependencies><dependency><groupId>org.openruyi.check</groupId><artifactId>leaf</artifactId><version>1.2.3</version></dependency></dependencies>
  <build><plugins><plugin><groupId>org.apache.servicemix.tooling</groupId><artifactId>depends-maven-plugin</artifactId><version>%{version}</version>
    <configuration><outputFile>${project.build.directory}/classes/META-INF/sisu/connect.dependencies</outputFile></configuration>
  </plugin></plugins></build>
</project>
EOF
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
mvn -B --offline -Dmaven.repo.local="$PWD/repo" org.apache.servicemix.tooling:depends-maven-plugin:%{version}:generate-depends-file
file=target/classes/META-INF/sisu/connect.dependencies
grep -Fx 'org.openruyi.check/consumer/version = 1' "$file"
grep -Fx 'org.openruyi.check/leaf/version = 1.2.3' "$file"
grep -Fx 'org.openruyi.check/leaf/scope = compile' "$file"

%files
%license maven-plugins-pom/LICENSE maven-plugins-pom/NOTICE
%{_datadir}/maven-metadata/depends-maven-plugin.xml
%{_datadir}/maven-repository/org/apache/servicemix/tooling/depends-maven-plugin/
%{_datadir}/maven-repository/org/apache/servicemix/tooling/maven-plugins-pom/
%{_datadir}/maven-repository/org/apache/servicemix/servicemix-pom/

%changelog
%autochangelog
