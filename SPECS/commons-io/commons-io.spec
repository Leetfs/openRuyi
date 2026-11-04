# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
%global bundle_tools %{_libexecdir}/eclipse-equinox

Name:           commons-io
Version:        2.21.0
Release:        %autorelease
Summary:        Java utilities for stream, file and filesystem operations
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-io/
VCS:            git:https://github.com/apache/commons-io
#!RemoteAsset:  sha256:63554054a3e79dde69fe75d0016600982a77dbae013994b335cd9d5ad1822667
Source0:        https://archive.apache.org/dist/commons/io/source/commons-io-2.21.0-src.tar.gz
#!RemoteAsset:  sha256:ad48e978a582f804b132bce4212c047a05f6479df985b1578f59a611070479ae
Source1:        https://github.com/junit-pioneer/junit-pioneer/archive/refs/tags/v1.9.1.tar.gz
#!RemoteAsset:  sha256:ebe70e2f96a3bc9b70eece33281a64d6cb3dbeed830a3690e0ea8a9d8dee5fee
Source2:        https://github.com/google/jimfs/archive/refs/tags/v1.3.1.tar.gz?/jimfs-1.3.1.tar.gz
#!RemoteAsset:  sha256:ece67aaeea60a2845010b301f1a4e5bcf9a91fda7594cf3599ad4c9501a29b2c
Source3:        https://maven-central.storage-download.googleapis.com/maven2/com/google/errorprone/error_prone_annotations/2.39.0/error_prone_annotations-2.39.0-sources.jar
#!RemoteAsset:  sha256:adf0898191d55937fb3192ba971826f4f294292c4a960740f3c27310e7b70296
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/jspecify/jspecify/1.0.0/jspecify-1.0.0-sources.jar
#!RemoteAsset:  sha256:371bc06d861278f8048157b5172fd5e830410cdd9cddf1cca02cd9ead7b64fff
Source5:        https://maven-central.storage-download.googleapis.com/maven2/com/google/auto/service/auto-service-annotations/1.1.1/auto-service-annotations-1.1.1-sources.jar
#!RemoteAsset:  sha256:2dd9da85182efca525aa269db573e0ed54943767d6af3afc50d0ede51e63d01a
Source6:        https://maven-central.storage-download.googleapis.com/maven2/com/ibm/icu/icu4j/77.1/icu4j-77.1-sources.jar
Source7:        module-info.java
Source8:        serve-xml.py
Patch2000:      2000-Allow-loopback-servers-in-stream-tests.patch
BuildArch:      noarch

BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:) == 91
BuildRequires:  mvn(org.mockito:mockito-core) == 4.11.0
BuildRequires:  openssl
BuildRequires:  python3
BuildRequires:  unzip
Provides:       mvn(commons-io:commons-io) == %{version}
Requires:       java-25-openjdk
Requires:       mvn(org.apache.commons:commons-parent:pom:) == 91

%description
Apache Commons IO provides stream adapters, file utilities, comparators
and filesystem monitors for Java applications.

%prep
%autosetup -p1 -n %{name}-%{version}-src
mkdir -p jimfs pioneer
tar xf %{SOURCE1} --strip-components=1 -C pioneer
tar xf %{SOURCE2} --strip-components=1 -C jimfs
mkdir -p error-prone
unzip -q %{SOURCE3} 'com/google/errorprone/annotations/*.java' -d error-prone
mkdir -p jspecify
unzip -q %{SOURCE4} 'org/jspecify/annotations/*.java' -d jspecify
mkdir -p auto-service
unzip -q %{SOURCE5} 'com/google/auto/service/*.java' -d auto-service
mkdir -p icu4j
unzip -q %{SOURCE6} 'com/ibm/icu/*.java' -d icu4j

%build
mkdir -p target/classes/META-INF target/java9 target/manifest build/bundles .xmvn .mvn
find src/main/java -name '*.java' | sort > target/main-sources
javac --release 8 -Xpkginfo:always -proc:none -encoding UTF-8 -d target/classes @target/main-sources
install -m644 LICENSE.txt NOTICE.txt target/classes/META-INF/
mkdir -p target/classes/META-INF/maven/commons-io/commons-io
install -m644 pom.xml target/classes/META-INF/maven/commons-io/commons-io/pom.xml
printf 'groupId=commons-io\nartifactId=%{name}\nversion=%{version}\n' > target/classes/META-INF/maven/commons-io/commons-io/pom.properties
# The release adds a Java 9 descriptor to its Java 8 library.
javac --release 9 --module-version %{version} --patch-module org.apache.commons.io=target/classes -d target/java9 %{SOURCE7}
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories><repository>%{_datadir}/maven-metadata</repository>
<repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository></metadataRepositories></resolverSettings></configuration>
EOF
# Generate the OSGi manifest with the Apache Commons release's Bnd package instructions.
plugin=$(unzip -p %{bootstrap_java}/maven-bundle-plugin.jar META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
test -n "$plugin"
cat > bundle.pom <<EOF
<project><modelVersion>4.0.0</modelVersion><groupId>commons-io</groupId><artifactId>commons-io</artifactId><version>%{version}</version>
<build><plugins><plugin><groupId>org.apache.felix</groupId><artifactId>maven-bundle-plugin</artifactId><version>$plugin</version>
<configuration><manifestLocation>$PWD/target/manifest</manifestLocation><instructions>
<Bundle-SymbolicName>org.apache.commons.commons-io</Bundle-SymbolicName><Bundle-Name>Apache Commons IO</Bundle-Name>
<Bundle-Version>%{version}</Bundle-Version><Export-Package>org.apache.commons.io;org.apache.commons.io.comparator;org.apache.commons.io.filefilter;org.apache.commons.io.input;org.apache.commons.io.output;version=1.4.9999;-noimport:=true,org.apache.commons.io;org.apache.commons.io.comparator;org.apache.commons.io.filefilter;org.apache.commons.io.input;org.apache.commons.io.output;org.apache.commons.io.*;version=%{version};-noimport:=true</Export-Package>
<Import-Package>sun.nio.ch;resolution:=optional,sun.misc;resolution:=optional,*</Import-Package><Multi-Release>true</Multi-Release>
<Bundle-License>https://www.apache.org/licenses/LICENSE-2.0.txt</Bundle-License><_reproducible>true</_reproducible>
</instructions></configuration></plugin></plugins></build></project>
EOF
ext=%{_datadir}/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
mvn -B --offline -f bundle.pom -Dmaven.repo.local="$PWD/target/repo" "org.apache.felix:maven-bundle-plugin:$plugin:manifest"
jar --create --file build/bundles/%{name}.jar --manifest target/manifest/MANIFEST.MF -C target/classes .
jar --update --file build/bundles/%{name}.jar --release 9 -C target/java9 module-info.class

%install
%{bundle_tools}/install-bundles --symbolic-name org.apache.commons.commons-io %{buildroot} %{_datadir} %{name} build/bundles pom.xml

%check
# Verify the packaged Java 9 module and run the upstream default JUnit suites.
jar --describe-module --file build/bundles/%{name}.jar --release 9 | grep -F 'org.apache.commons.io@%{version}'
mkdir -p target/test-classes
# JMH sources implement separately invoked benchmarks and are outside the Surefire suite.
find src/test/java -name '*.java' ! -path '*/org/apache/commons/io/jmh/*' | sort > target/test-sources
# Compile the external test utilities with their own supported Java level.
javac --release 17 -proc:none -encoding UTF-8 -sourcepath jimfs/jimfs/src/main/java:pioneer/src/main/java:error-prone:jspecify:auto-service:icu4j -cp '%{bootstrap_java}/*' -d target/test-classes jimfs/jimfs/src/main/java/com/google/common/jimfs/Configuration.java jimfs/jimfs/src/main/java/com/google/common/jimfs/Jimfs.java pioneer/src/main/java/org/junitpioneer/jupiter/DefaultLocale.java pioneer/src/main/java/org/junitpioneer/jupiter/cartesian/CartesianTest.java
# Commons IO is compiled against Java 8, before the additional FileSystems.newFileSystem(Path, Map) overload.
javac --release 8 -proc:none -encoding UTF-8 -Xmaxerrs 500 -cp 'target/classes:target/test-classes:%{repo_dir}/org/mockito/mockito-core/4.11.0/mockito-core-4.11.0.jar:%{bootstrap_java}/*' -d target/test-classes @target/test-sources
if test -d src/test/resources; then cp -r src/test/resources/. target/test-classes/; fi
if test -d jimfs/jimfs/src/main/resources; then cp -r jimfs/jimfs/src/main/resources/. target/test-classes/; fi
# Jimfs discovers its file-system provider through the JDK service registry.
mkdir -p target/test-classes/META-INF/services
printf 'com.google.common.jimfs.SystemJimfsFileSystemProvider\n' > target/test-classes/META-INF/services/java.nio.file.spi.FileSystemProvider
mkdir -p target/test-classes/mockito-extensions
printf 'mock-maker-inline\n' > target/test-classes/mockito-extensions/org.mockito.plugins.MockMaker
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
tests=$(find src/test/java \( -name 'Test*.java' -o -name '*Test.java' -o -name '*Tests.java' -o -name '*TestCase.java' \) | sed 's|^src/test/java/||;s|/|.|g;s|[.]java$||' | sort)
# Serve the HTTP and HTTPS cases over loopback with a private test trust store.
mkdir -p target/network-test
openssl req -x509 -newkey rsa:2048 -nodes -days 1 -subj '/CN=127.0.0.1' -addext 'subjectAltName=IP:127.0.0.1' -keyout target/network-test/key.pem -out target/network-test/cert.pem
"$(dirname "$(readlink -f "$(command -v javac)")")/keytool" -importcert -noprompt -alias loopback -file target/network-test/cert.pem -keystore target/network-test/trust.p12 -storetype PKCS12 -storepass changeit
python3 %{SOURCE8} target/network-test > target/network-test/server.log 2>&1 &
server_pid=$!
trap 'kill "$server_pid" 2>/dev/null || :' EXIT
for attempt in {1..100}; do
    test ! -s target/network-test/ports || break
    kill -0 "$server_pid"
    sleep 0.1
done
read -r http https < target/network-test/ports
network=("-Dcommons.io.test.http=http://127.0.0.1:$http/" "-Dcommons.io.test.https=https://127.0.0.1:$https/"
    "-Djavax.net.ssl.trustStore=$PWD/target/network-test/trust.p12" "-Djavax.net.ssl.trustStorePassword=changeit")

java "${network[@]}" -XX:+EnableDynamicAgentLoading -cp 'target/test-launcher:build/bundles/%{name}.jar:target/test-classes:%{repo_dir}/org/mockito/mockito-core/4.11.0/mockito-core-4.11.0.jar:%{bootstrap_java}/*' RunTests $tests

%files
%license LICENSE.txt NOTICE.txt
%doc README.md
%{_datadir}/maven-metadata/commons-io.xml
%{repo_dir}/commons-io/commons-io/

%changelog
%autochangelog
