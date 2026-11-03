# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
%global xmvn_ext %{_datadir}/javapackages-bootstrap/maven/lib/ext

Name:           polyglot-common
Version:        0.8.1
Release:        %autorelease
Summary:        Common model mappings for Polyglot Maven
License:        EPL-1.0
URL:            https://github.com/takari/polyglot-maven
VCS:            git:https://github.com/takari/polyglot-maven
#!RemoteAsset:  sha256:aff4fa891bcff7f32188f42892f001f981d35d8e467d2ca156cd0f26a38fd994
Source0:        https://github.com/takari/polyglot-maven/archive/refs/tags/polyglot-%{version}.tar.gz
#!RemoteAsset:  sha256:f1100df2c3480fd39a589a1fb633ad8457b545c0835f8d3513c6b54ba70fb01c
Source1:        https://maven-central.storage-download.googleapis.com/maven2/io/takari/takari/70/takari-70.pom
Source2:        PolyglotCheck.java
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  unzip
Provides:       mvn(io.takari.polyglot:polyglot-common) == %{version}
Provides:       mvn(io.takari.polyglot:polyglot:pom:) == %{version}
Provides:       mvn(io.takari:takari:pom:) == 70
Requires:       maven >= 3.9.9

%description
Polyglot Maven provides model readers, writers and mappings for alternate
project model formats. This library contains their shared Maven extension API.

%prep
%autosetup -n polyglot-maven-polyglot-%{version}
# The parent imports the Maven BOM corresponding to its build and runtime.
maven_version=$(rpm -q --qf '%%{VERSION}' maven)
test -s %{_datadir}/maven-repository/org/apache/maven/maven/$maven_version/maven-$maven_version.pom
sed -i "s@<mavenVersion>3.9.9</mavenVersion>@<mavenVersion>$maven_version</mavenVersion>@" pom.xml
grep -F "<mavenVersion>$maven_version</mavenVersion>" pom.xml

%build
cd polyglot-common
mkdir -p target/classes/META-INF/takari target/classes/META-INF/maven/io.takari.polyglot/polyglot-common .xmvn
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -encoding UTF-8 -proc:none -cp '%{_datadir}/maven/lib/*:%{_datadir}/maven/boot/*' -d target/classes @target/sources
sed -e 's/${project.groupId}/io.takari.polyglot/g' -e 's/${project.artifactId}/polyglot-common/g' \
    -e 's/${project.version}/%{version}/g' src/main/resources-filtered/maven-polyglot.properties > target/classes/maven-polyglot.properties
printf 'groupId=io.takari.polyglot\nartifactId=polyglot-common\nversion=%{version}\n' > target/classes/META-INF/maven/io.takari.polyglot/polyglot-common/pom.properties
find target/classes/org -name '*.class' -printf '%%h\n' | sed 's@^target/classes/@@;s@/@.@g' | sort -u > target/classes/META-INF/takari/export-package
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
  <repository>%{_datadir}/maven-metadata</repository>
  <repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
cat > openruyi-index.pom <<EOF
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
  <groupId>io.takari.polyglot</groupId><artifactId>polyglot-common</artifactId><version>%{version}</version>
</project>
EOF
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
sisu=$(unzip -p %{bootstrap_java}/sisu-maven-plugin.jar META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
test -n "$sisu"
mvn -B --offline -f openruyi-index.pom -Dmaven.repo.local="$PWD/target/repository" "org.eclipse.sisu:sisu-maven-plugin:$sisu:main-index"
test -s target/classes/META-INF/sisu/javax.inject.Named
jar --create --file target/%{name}.jar -C target/classes .

%install
install -Dm644 polyglot-common/pom.xml %{buildroot}%{_datadir}/maven-repository/io/takari/polyglot/polyglot-common/%{version}/polyglot-common-%{version}.pom
install -m644 polyglot-common/target/%{name}.jar %{buildroot}%{_datadir}/maven-repository/io/takari/polyglot/polyglot-common/%{version}/polyglot-common-%{version}.jar
install -Dm644 pom.xml %{buildroot}%{_datadir}/maven-repository/io/takari/polyglot/polyglot/%{version}/polyglot-%{version}.pom
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/maven-repository/io/takari/takari/70/takari-70.pom
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>io.takari.polyglot</groupId><artifactId>polyglot-common</artifactId><version>%{version}</version><extension>jar</extension>
    <path>%{_datadir}/maven-repository/io/takari/polyglot/polyglot-common/%{version}/polyglot-common-%{version}.jar</path></artifact>
  <artifact><groupId>io.takari.polyglot</groupId><artifactId>polyglot-common</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/io/takari/polyglot/polyglot-common/%{version}/polyglot-common-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
  <artifact><groupId>io.takari.polyglot</groupId><artifactId>polyglot</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/io/takari/polyglot/polyglot/%{version}/polyglot-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
  <artifact><groupId>io.takari</groupId><artifactId>takari</artifactId><version>70</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/io/takari/takari/70/takari-70.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
cd polyglot-common
jar=target/%{name}.jar
unzip -p "$jar" META-INF/sisu/javax.inject.Named | grep -Fx 'org.sonatype.maven.polyglot.mapping.XmlMapping'
unzip -p "$jar" META-INF/takari/export-package | grep -Fx 'org.sonatype.maven.polyglot.mapping'
unzip -p "$jar" maven-polyglot.properties | grep -Fx 'version = %{version}'
java -ea -cp "$jar:%{_datadir}/maven/lib/*:%{_datadir}/maven/boot/*" %{SOURCE2} src/test/resources/org/sonatype/maven/polyglot/pom1.xml

# Resolve the installed model from a cold native Maven project.
mkdir -p target/consumer/{.xmvn,metadata,src/main/java}
cat > target/consumer/src/main/java/MappingConsumer.java <<'EOF'
import org.sonatype.maven.polyglot.mapping.XmlMapping;
class MappingConsumer {
    public static void main(String[] args) {
        if (!"default".equals(new XmlMapping().getFlavour())) throw new AssertionError();
    }
}
EOF
cd target/consumer
for file in %{_datadir}/maven-metadata/*.xml; do
    test "$(basename "$file")" = %{name}.xml || ln -s "$file" metadata/
done
sed 's@<path>/@<path>%{buildroot}/@g' %{buildroot}%{_datadir}/maven-metadata/%{name}.xml > metadata/%{name}.xml
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
  <repository>$PWD/metadata</repository><repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
maven_version=$(rpm -q --qf '%%{VERSION}' maven)
cat > pom.xml <<EOF
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
  <groupId>org.openruyi.check</groupId><artifactId>polyglot-consumer</artifactId><version>1</version>
  <properties><maven.compiler.release>17</maven.compiler.release></properties>
  <dependencies>
    <dependency><groupId>io.takari.polyglot</groupId><artifactId>polyglot-common</artifactId><version>%{version}</version></dependency>
    <dependency><groupId>org.apache.maven</groupId><artifactId>maven-core</artifactId><version>$maven_version</version></dependency>
  </dependencies>
</project>
EOF
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
compiler=$(unzip -p %{bootstrap_java}/maven-compiler-plugin.jar META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
test -n "$compiler"
mvn -B --offline -Dmaven.repo.local="$PWD/repository" "org.apache.maven.plugins:maven-compiler-plugin:$compiler:compile"
java -cp "target/classes:%{buildroot}%{_datadir}/maven-repository/io/takari/polyglot/polyglot-common/%{version}/*:%{_datadir}/maven/lib/*" MappingConsumer

%files
%license LICENSE.txt
%{_datadir}/maven-metadata/polyglot-common.xml
%{_datadir}/maven-repository/io/takari/polyglot/polyglot-common/
%{_datadir}/maven-repository/io/takari/polyglot/polyglot/
%{_datadir}/maven-repository/io/takari/takari/

%changelog
%autochangelog
