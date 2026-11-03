# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bootstrap_java %{_datadir}/java/javapackages-bootstrap

Name:           surefire-grouper
Version:        3.5.5
Release:        %autorelease
Summary:        Test group expression parser for Maven Surefire
License:        Apache-2.0
URL:            https://maven.apache.org/surefire/
VCS:            git:https://github.com/apache/maven-surefire
#!RemoteAsset:  sha256:87bd504e65ee537129bf4f510c8f0e741f14a8be32e830781cfca49d191c643b
Source0:        https://archive.apache.org/dist/maven/surefire/surefire-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:) == 47
BuildRequires:  mvn(org.junit:junit-bom:pom:) == 5.12.2
BuildRequires:  unzip
Provides:       mvn(org.apache.maven.surefire:surefire-grouper) == %{version}
Provides:       mvn(org.apache.maven.surefire:surefire:pom:) == %{version}
Requires:       java-25-openjdk
Requires:       mvn(org.apache.maven:maven-parent:pom:) == 47
Requires:       mvn(org.junit:junit-bom:pom:) == 5.12.2

%description
The Surefire grouping library parses category selection expressions and
matches test classes against AND, OR and inverse group filters.

%prep
%autosetup -n surefire-%{version}

%build
cd surefire-grouper
mkdir -p target/generated target/classes
java -cp %{bootstrap_java}/javacc.jar org.javacc.parser.Main -OUTPUT_DIRECTORY=target/generated src/main/javacc/category-expression.jj
find src/main/java target/generated -name '*.java' | sort > target/sources
javac --release 8 -encoding UTF-8 -d target/classes @target/sources
install -Dm644 ../LICENSE target/classes/META-INF/LICENSE
install -m644 ../NOTICE target/classes/META-INF/NOTICE
mkdir -p target/classes/META-INF/maven/org.apache.maven.surefire/surefire-grouper
install -m644 pom.xml target/classes/META-INF/maven/org.apache.maven.surefire/surefire-grouper/pom.xml
printf 'groupId=org.apache.maven.surefire\nartifactId=surefire-grouper\nversion=%{version}\n' > target/classes/META-INF/maven/org.apache.maven.surefire/surefire-grouper/pom.properties
jar --create --file target/%{name}.jar -C target/classes .

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name}-parent pom.xml
install -Dm644 surefire-grouper/pom.xml %{buildroot}%{_datadir}/maven-repository/org/apache/maven/surefire/surefire-grouper/%{version}/surefire-grouper-%{version}.pom
install -m644 surefire-grouper/target/%{name}.jar %{buildroot}%{_datadir}/maven-repository/org/apache/maven/surefire/surefire-grouper/%{version}/surefire-grouper-%{version}.jar
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>org.apache.maven.surefire</groupId><artifactId>surefire-grouper</artifactId><version>%{version}</version><extension>jar</extension>
    <path>%{_datadir}/maven-repository/org/apache/maven/surefire/surefire-grouper/%{version}/surefire-grouper-%{version}.jar</path></artifact>
  <artifact><groupId>org.apache.maven.surefire</groupId><artifactId>surefire-grouper</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/org/apache/maven/surefire/surefire-grouper/%{version}/surefire-grouper-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
# Resolve the released group parser and its parent model outside the Surefire checkout.
mkdir -p model-check/{.mvn,repo}
cp -as %{_datadir}/maven-repository/. model-check/repo/
cp -a --remove-destination %{buildroot}%{_datadir}/maven-repository/. model-check/repo/
cat > model-check/pom.xml <<'EOF'
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
<groupId>org.openruyi.check</groupId><artifactId>surefire-model</artifactId><version>1</version>
<dependencyManagement><dependencies><dependency><groupId>org.apache.maven.surefire</groupId><artifactId>surefire</artifactId>
<version>%{version}</version><type>pom</type><scope>import</scope></dependency></dependencies></dependencyManagement>
<dependencies><dependency><groupId>org.junit.jupiter</groupId><artifactId>junit-jupiter-api</artifactId></dependency></dependencies></project>
EOF
(cd model-check && %{_libexecdir}/javapackages-bootstrap/mvn -B --offline -Dmaven.repo.local="$PWD/repo" validate)
# Run the upstream group parser suite and compile a category matching consumer.
cd surefire-grouper
mkdir -p target/tests
cp="target/%{name}.jar:%{bootstrap_java}/junit.jar:%{bootstrap_java}/hamcrest-core.jar"
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 8 -encoding UTF-8 -cp "$cp" -d target/tests @target/test-sources
classes=$(sed -n '/Test\.java$/ {s@^src/test/java/@@;s@\.java$@@;s@/@.@g;p;}' target/test-sources)
java -ea -cp "target/tests:$cp" org.junit.runner.JUnitCore $classes
cat > target/CategoryCheck.java <<'EOF'
import org.apache.maven.surefire.group.parse.GroupMatcherParser;
class CategoryCheck {
    public static void main(String[] args) throws Exception {
        var groups = new GroupMatcherParser("java.lang.String OR java.lang.Integer").parse();
        if (!groups.enabled(String.class) || !groups.enabled(Integer.class) || groups.enabled(Double.class)) {
            throw new AssertionError("Unexpected category match");
        }
    }
}
EOF
java -cp "target/%{name}.jar" target/CategoryCheck.java

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/surefire-grouper-parent.xml
%{_datadir}/maven-repository/org/apache/maven/surefire/surefire/
%{_datadir}/maven-metadata/surefire-grouper.xml
%{_datadir}/maven-repository/org/apache/maven/surefire/surefire-grouper/

%changelog
%autochangelog
