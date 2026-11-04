# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
%global bundle_tools %{_libexecdir}/eclipse-equinox

Name:           commons-net
Version:        3.13.0
Release:        %autorelease
Summary:        FTP and network protocol client library for Java
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-net/
VCS:            git:https://github.com/apache/commons-net
#!RemoteAsset:  sha256:9dd1e9ae1dc236ee8ad92754cb7666be9ad333335717d75a46a4b2f71155fdef
Source0:        https://archive.apache.org/dist/commons/net/source/commons-net-3.13.0-src.tar.gz
#!RemoteAsset:  sha256:a049b90c283db5ead61a5b23ffeaccec0ac4decda0a182d5bbe8fc12c1b257e5
Source1:        https://github.com/apache/mina-ftpserver/archive/refs/tags/ftpserver-parent-1.2.1.tar.gz?/mina-ftpserver-1.2.1.tar.gz
#!RemoteAsset:  sha256:9c4474353ad04a149f9d00ed5666c96b15aaa25a714e07bd6d25bab8f701d8b6
Source2:        https://github.com/apache/mina/archive/refs/tags/2.2.4.tar.gz?/mina-2.2.4.tar.gz
#!RemoteAsset:  sha256:ba3c723d8b05e327dd4f74901bd2aefabde6718f8804e083c51164929eb58bf8
Source3:        https://archive.apache.org/dist/commons/collections/source/commons-collections4-4.5.0-src.tar.gz
Source4:        module-info.java
Patch2000:      2000-Run-CIDR-cases-with-a-JUnit-method-source.patch
BuildArch:      noarch

BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:) == 97
BuildRequires:  mvn(commons-io:commons-io) == 2.21.0
BuildRequires:  unzip
Provides:       mvn(commons-net:commons-net) == %{version}
Requires:       java-25-openjdk
Requires:       mvn(org.apache.commons:commons-parent:pom:) == 97
Requires:       mvn(commons-io:commons-io) == 2.21.0

%description
Apache Commons Net supplies clients for FTP, FTPS, NNTP, NTP, Telnet and
other network protocols used by Java applications and Eclipse Tycho.

%prep
%autosetup -p1 -n %{name}-%{version}-src
mkdir ftp mina collections
tar xf %{SOURCE1} -C ftp --strip-components=1
tar xf %{SOURCE2} -C mina --strip-components=1
tar xf %{SOURCE3} -C collections --strip-components=1

%build
mkdir -p target/classes/META-INF target/java9 target/manifest build/bundles .xmvn .mvn
find src/main/java -name '*.java' | sort > target/main-sources
javac --release 8 -Xpkginfo:always -proc:none -encoding UTF-8 -cp %{repo_dir}/commons-io/commons-io/2.21.0/commons-io-2.21.0.jar -d target/classes @target/main-sources
cp -r src/main/resources/. target/classes/
install -m644 LICENSE.txt NOTICE.txt target/classes/META-INF/
mkdir -p target/classes/META-INF/maven/commons-net/commons-net
install -m644 pom.xml target/classes/META-INF/maven/commons-net/commons-net/pom.xml
printf 'groupId=commons-net\nartifactId=%{name}\nversion=%{version}\n' > target/classes/META-INF/maven/commons-net/commons-net/pom.properties
# The release adds a Java 9 descriptor to its Java 8 library.
javac --release 9 --module-version %{version} --patch-module org.apache.commons.net=target/classes --module-path %{repo_dir}/commons-io/commons-io/2.21.0/commons-io-2.21.0.jar -d target/java9 %{SOURCE4}
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories><repository>%{_datadir}/maven-metadata</repository>
<repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository></metadataRepositories></resolverSettings></configuration>
EOF
# Generate the OSGi manifest with the Apache Commons release's Bnd package instructions.
plugin=$(unzip -p %{bootstrap_java}/maven-bundle-plugin.jar META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
test -n "$plugin"
cat > bundle.pom <<EOF
<project><modelVersion>4.0.0</modelVersion><groupId>commons-net</groupId><artifactId>commons-net</artifactId><version>%{version}</version>
<dependencies><dependency><groupId>commons-io</groupId><artifactId>commons-io</artifactId><version>2.21.0</version></dependency></dependencies>
<build><plugins><plugin><groupId>org.apache.felix</groupId><artifactId>maven-bundle-plugin</artifactId><version>$plugin</version>
<configuration><manifestLocation>$PWD/target/manifest</manifestLocation><instructions>
<Bundle-SymbolicName>org.apache.commons.commons-net</Bundle-SymbolicName><Bundle-Name>Apache Commons Net</Bundle-Name>
<Bundle-Version>%{version}</Bundle-Version><Export-Package>org.apache.commons.*;version=%{version};-noimport:=true</Export-Package>
<Import-Package>*</Import-Package><Multi-Release>true</Multi-Release>
<Bundle-License>https://www.apache.org/licenses/LICENSE-2.0.txt</Bundle-License><_reproducible>true</_reproducible>
</instructions></configuration></plugin></plugins></build></project>
EOF
ext=%{_datadir}/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
mvn -B --offline -f bundle.pom -Dmaven.repo.local="$PWD/target/repo" "org.apache.felix:maven-bundle-plugin:$plugin:manifest"
# The release calculates OSGi exports before the JAR plugin excludes the examples.
mkdir -p build/payload
(cd target/classes && tar --exclude='./org/apache/commons/net/examples' -cf - .) | tar xf - -C build/payload
jar --create --file build/bundles/%{name}.jar --manifest target/manifest/MANIFEST.MF -C build/payload .
jar --update --file build/bundles/%{name}.jar --release 9 -C target/java9 module-info.class

%install
%{bundle_tools}/install-bundles --symbolic-name org.apache.commons.commons-net %{buildroot} %{_datadir} %{name} build/bundles pom.xml

%check
# Verify the packaged Java 9 module and run the upstream default JUnit suites.
jar --describe-module --file build/bundles/%{name}.jar --release 9 | grep -F 'org.apache.commons.net@%{version}'
mkdir -p target/test-classes
# The example index and loopback NTP server are used only by the tests.
find src/test/java -name '*.java' | sort > target/test-sources
mkdir -p target/test-classes/org/apache/commons/net/examples
cp -r target/classes/org/apache/commons/net/examples/. target/test-classes/org/apache/commons/net/examples/
javac --release 17 -proc:none -encoding UTF-8 \
    -sourcepath src/test/java:ftp/ftplet-api/src/main/java:ftp/core/src/main/java:mina/mina-core/src/main/java:collections/src/main/java \
    -cp 'build/bundles/%{name}.jar:target/test-classes:%{repo_dir}/commons-io/commons-io/2.21.0/commons-io-2.21.0.jar:%{bootstrap_java}/*' -d target/test-classes @target/test-sources
cp -r src/test/resources/. target/test-classes/
cp -r ftp/core/src/main/resources/. target/test-classes/
test -s target/test-classes/org/apache/commons/net/test-data/file.txt
# Use the JUnit result as the exit status after all test callbacks complete.
cat > target/RunTests.java <<'JAVA'
class RunTests {
    public static void main(String[] args) {
        try {
            RunJupiter.main(args);
        } catch (Throwable failure) {
            failure.printStackTrace();
            System.exit(1);
        }
        System.exit(0);
    }
}
JAVA
mkdir -p target/test-launcher
javac --release 17 -cp '%{bootstrap_java}/*' -d target/test-launcher %{bundle_tools}/RunJupiter.java target/RunTests.java
# The release omits POP3 and functional cases requiring external services.
tests=$(find src/test/java \( -name 'Test*.java' -o -name '*Test.java' -o -name '*Tests.java' -o -name '*TestCase.java' \) ! -name '*FunctionalTest.java' ! -name 'POP3*Test.java' | sed 's|^src/test/java/||;s|/|.|g;s|[.]java$||' | sort)
java -cp 'target/test-launcher:build/bundles/%{name}.jar:target/test-classes:%{repo_dir}/commons-io/commons-io/2.21.0/commons-io-2.21.0.jar:%{bootstrap_java}/*' RunTests $tests

%files
%license LICENSE.txt NOTICE.txt
%doc README.md
%{_datadir}/maven-metadata/commons-net.xml
%{repo_dir}/commons-net/commons-net/

%changelog
%autochangelog
