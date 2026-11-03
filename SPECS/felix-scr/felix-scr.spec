# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bundle org.apache.felix.scr
%global repo_dir %{_datadir}/maven-repository/org/apache/felix/%{bundle}/%{version}
%global osgi_repo %{_datadir}/maven-repository/org/osgi
%global framework %{_datadir}/maven-repository/org/eclipse/platform/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar
%global gogo %{_datadir}/maven-repository/org/apache/felix/org.apache.felix.gogo.runtime/1.1.6/org.apache.felix.gogo.runtime-1.1.6.jar
%global component %{osgi_repo}/org.osgi.service.component/1.5.1/org.osgi.service.component-1.5.1.jar
%global promise %{osgi_repo}/org.osgi.util.promise/1.3.0/org.osgi.util.promise-1.3.0.jar
%global function %{osgi_repo}/org.osgi.util.function/1.2.0/org.osgi.util.function-1.2.0.jar
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
%global xmvn_ext %{_datadir}/javapackages-bootstrap/maven/lib/ext

Name:           felix-scr
Version:        2.2.18
Release:        %autorelease
Summary:        Apache Felix OSGi Declarative Services runtime
License:        Apache-2.0
URL:            https://felix.apache.org/documentation/subprojects/apache-felix-service-component-runtime.html
VCS:            git:https://github.com/apache/felix-dev
#!RemoteAsset:  sha256:9a55a44c947cd56ee1e428bdb063e1be203ef3aa4b4e4463b4ccdf5c7f31afd3
Source0:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/felix/%{bundle}/%{version}/%{bundle}-%{version}-source-release.zip
Source1:        ScrCheck.java
Source2:        RunUnitTests.java
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.apache.felix:org.apache.felix.gogo.runtime) == 1.1.6
BuildRequires:  mvn(org.codehaus.mojo:animal-sniffer-annotations) == 1.27
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.osgi) == 3.24.100
BuildRequires:  mvn(org.mockito:mockito-core) == 4.11.0
BuildRequires:  mvn(org.osgi:org.osgi.service.component) == 1.5.1
BuildRequires:  unzip
Provides:       mvn(org.apache.felix:org.apache.felix.scr) == %{version}
Requires:       eclipse-equinox >= 4.39
Requires:       osgi-compendium >= 8.1.0

%description
Felix SCR activates and deactivates OSGi declarative components, tracks
their required services, and exposes registered component descriptions
and configurations through the Service Component Runtime API.

%prep
%autosetup -n %{bundle}-%{version}

%build
mkdir -p target/classes/META-INF .xmvn repository
annotations=%{_datadir}/maven-repository/org/codehaus/mojo/animal-sniffer-annotations/1.27/animal-sniffer-annotations-1.27.jar
cp="%{component}:%{promise}:%{function}:%{framework}:%{gogo}:$annotations:%{bootstrap_java}/osgi.annotation.jar:%{bootstrap_java}/osgi.cmpn.jar"
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -encoding UTF-8 -proc:none -cp "$cp" -d target/classes @target/sources
install -m644 LICENSE NOTICE DEPENDENCIES target/classes/META-INF/
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
  <repository>%{_datadir}/maven-metadata</repository>
  <repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
cat > bundle-pom.xml <<'XML'
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion><groupId>org.apache.felix</groupId>
  <artifactId>%{bundle}</artifactId><version>%{version}</version><name>Apache Felix Declarative Services</name>
  <dependencies>
    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.service.component</artifactId><version>1.5.1</version><scope>system</scope><systemPath>%{component}</systemPath></dependency>
    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.util.promise</artifactId><version>1.3.0</version><scope>system</scope><systemPath>%{promise}</systemPath></dependency>
    <dependency><groupId>org.osgi</groupId><artifactId>org.osgi.util.function</artifactId><version>1.2.0</version><scope>system</scope><systemPath>%{function}</systemPath></dependency>
    <dependency><groupId>org.eclipse.platform</groupId><artifactId>org.eclipse.osgi</artifactId><version>3.24.100</version><scope>system</scope><systemPath>%{framework}</systemPath></dependency>
    <dependency><groupId>org.apache.felix</groupId><artifactId>org.apache.felix.gogo.runtime</artifactId><version>1.1.6</version><scope>system</scope><systemPath>%{gogo}</systemPath></dependency>
    <dependency><groupId>org.osgi</groupId><artifactId>osgi.cmpn</artifactId><version>7</version><scope>system</scope><systemPath>%{bootstrap_java}/osgi.cmpn.jar</systemPath></dependency>
  </dependencies>
  <build><plugins><plugin><groupId>org.apache.felix</groupId><artifactId>maven-bundle-plugin</artifactId><version>5.1.9.MBI</version>
    <configuration><instructions><_include>bnd.bnd</_include><Bundle-SymbolicName>%{bundle}</Bundle-SymbolicName>
      <Require-Capability>osgi.ee;filter:="(&amp;(osgi.ee=JavaSE)(version=1.8))"</Require-Capability>
    </instructions></configuration>
  </plugin></plugins></build>
</project>
XML
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
mvn --batch-mode --offline -Dmaven.repo.local="$PWD/repository" -f bundle-pom.xml org.apache.felix:maven-bundle-plugin:5.1.9.MBI:bundle

%install
install -Dm644 target/%{bundle}-%{version}.jar %{buildroot}%{repo_dir}/%{bundle}-%{version}.jar
install -m644 pom.xml %{buildroot}%{repo_dir}/%{bundle}-%{version}.pom
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>org.apache.felix</groupId><artifactId>%{bundle}</artifactId><version>%{version}</version>
    <path>%{repo_dir}/%{bundle}-%{version}.jar</path></artifact>
  <artifact><groupId>org.apache.felix</groupId><artifactId>%{bundle}</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{repo_dir}/%{bundle}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
jar=%{buildroot}%{repo_dir}/%{bundle}-%{version}.jar
mockito=%{_datadir}/maven-repository/org/mockito/mockito-core/4.11.0/mockito-core-4.11.0.jar
cp="$jar:%{component}:%{promise}:%{function}:%{framework}:%{gogo}:$mockito:%{bootstrap_java}/*"
mkdir -p target/test-classes target/client/OSGI-INF
find src/test/java/org/apache/felix/scr/impl -name '*.java' | sort > target/test-sources
# ActivateMethodTest loads the package-less upstream fixture by name.
printf '%%s\n' src/test/java/DefaultPackageClass.java >> target/test-sources
javac --release 8 -encoding UTF-8 -cp "$cp" -sourcepath src/test/java -d target/test-classes @target/test-sources
mapfile -t tests < <(sed -n '/Test\.java$/ {s|^src/test/java/||; s|/|.|g; s|\.java$||; p;}' target/test-sources)
# LoggerTest closes its process output streams, so write the JUnit results separately.
status=0
java -cp "target/test-classes:src/test/resources:$cp" %{SOURCE2} target/test-results.txt "${tests[@]}" || status=$?
cat target/test-results.txt
test "$status" -eq 0
cat > target/Echo.java <<'JAVA'
package packaging;
public class Echo implements java.util.function.Supplier<String> {
    public String get() { return "active"; }
}
JAVA
javac --release 8 -d target/client target/Echo.java
cat > target/client/OSGI-INF/echo.xml <<'XML'
<scr:component xmlns:scr="http://www.osgi.org/xmlns/scr/v1.3.0" name="packaging.echo">
  <implementation class="packaging.Echo"/><service><provide interface="java.util.function.Supplier"/></service>
</scr:component>
XML
cat > target/client.MF <<'EOF'
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-SymbolicName: packaging.consumer
Bundle-Version: 1.0.0
Service-Component: OSGI-INF/echo.xml

EOF
jar --create --file target/client.jar --manifest target/client.MF -C target/client .
java -cp %{framework} %{SOURCE1} "$PWD/target/framework" %{function} %{promise} %{component} "$jar" target/client.jar

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/felix-scr.xml
%{repo_dir}/

%changelog
%autochangelog
