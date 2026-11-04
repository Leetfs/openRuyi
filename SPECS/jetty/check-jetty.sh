#!/bin/bash
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0
set -eu -o pipefail
root=$PWD
buildroot=$1
tycho_test=$2
https_site=$3
bootstrap=/usr/share/java/javapackages-bootstrap
repo=/usr/share/maven-repository
# The WorkDir extension incorporates the complete URI into the test directory name.
work=$(mktemp -d /tmp/jetty.XXXXXX)
cleanup() { [[ $(realpath -- "$work") == /tmp/jetty.?????? ]] && rm -rf -- "$work"; }
trap cleanup EXIT
mkdir -p "$work"/{fixtures,launcher,consumer}
cp="$repo/org/slf4j/slf4j-api/2.0.17/slf4j-api-2.0.17.jar:$repo/jakarta/servlet/jakarta.servlet-api/6.0.0/jakarta.servlet-api-6.0.0.jar"
for file in "$buildroot"/usr/share/maven-repository/org/eclipse/jetty/*/*/*.jar "$buildroot"/usr/share/maven-repository/org/eclipse/jetty/ee10/*/*/*.jar; do
    if test -f "$file"; then cp="$cp:$file"; fi
done
cp="$work/fixtures:$cp:$bootstrap/*"
find test-inputs/helper/src/main/java test-inputs/awaitility/awaitility/src/main/java jetty-core/jetty-slf4j-impl/src/main/java \
    tests/jetty-test-multipart/src/main/java -name '*.java' ! -name module-info.java | sort > "$work/fixture-sources"
javac --release 17 -proc:none -encoding UTF-8 -cp "$cp" -d "$work/fixtures" @"$work/fixture-sources"
cp -r jetty-core/jetty-slf4j-impl/src/main/resources/. "$work/fixtures/"
cp -r tests/jetty-test-multipart/src/main/resources/. "$work/fixtures/"
jimfs=test-inputs/jimfs/jimfs/src/main/java
javac --release 17 -proc:none -encoding UTF-8 \
    -sourcepath "$jimfs:test-inputs/error-prone:test-inputs/jspecify:test-inputs/auto-service:test-inputs/icu4j" \
    -cp "$cp" -d "$work/fixtures" "$jimfs/com/google/common/jimfs/"{Configuration,Jimfs}.java
# Jimfs registers its NIO provider through @AutoService.
grep -F '@AutoService(FileSystemProvider.class)' "$jimfs/com/google/common/jimfs/SystemJimfsFileSystemProvider.java"
mkdir -p "$work/fixtures/META-INF/services"
printf '%s\n' com.google.common.jimfs.SystemJimfsFileSystemProvider > "$work/fixtures/META-INF/services/java.nio.file.spi.FileSystemProvider"
# Surefire normally ends each fork after the test plan. Some thread-pool tests leave workers alive.
cat > "$work/RunJettySuites.java" <<'JAVA'
public class RunJettySuites {
    public static void main(String[] classes) {
        int status = 0;
        try (var site = new OfflineHttpsSite(java.nio.file.Path.of(System.getProperty("javax.net.ssl.trustStore")))) {
            RunJupiter.main(classes);
        } catch (Throwable failure) {
            failure.printStackTrace();
            status = 1;
        }
        System.exit(status);
    }
}
JAVA
javac --release 17 -proc:none -cp "$bootstrap/*" -d "$work/launcher" /usr/libexec/eclipse-equinox/RunJupiter.java "$https_site" "$work/RunJettySuites.java"
# Keep DNS and HTTPS resource tests reproducible inside the offline build service.
cat /etc/hosts > "$work/hosts"
printf '%s\n' '192.0.2.1 webtide.com' '192.0.2.2 www.google.com' '127.0.0.1 localhost' >> "$work/hosts"
"$(dirname "$(readlink -f "$(command -v java)")")/keytool" -genkeypair -alias jetty -dname CN=localhost -ext SAN=dns:localhost -keyalg RSA \
    -keystore "$work/site.p12" -storetype PKCS12 -storepass jetty-test -validity 2
for name in jetty-util jetty-http; do
    (
        module="$root/jetty-core/$name"
        local="$work/$name"
        mkdir -p "$local/target/"{classes,test-classes}
        cp -r "$module/src" "$module/pom.xml" "$local/"
        cd "$local"
        if test "$name" = jetty-util; then
            fixture=src/test/java/org/eclipse/jetty/util/resource/UrlResourceFactoryTest.java
            grep -F 'URI.create("https://webtide.com/")' "$fixture"
            sed -i 's|URI.create("https://webtide.com/")|URI.create(System.getProperty("jetty.test.site"))|' "$fixture"
        fi
        jar="$buildroot/usr/share/maven-repository/org/eclipse/jetty/$name/12.1.14/$name-12.1.14.jar"
        (cd target/classes; jar xf "$jar")
        cp -r src/test/resources/. target/test-classes/
        find src/test/java -name '*.java' ! -name module-info.java | sort > target/test-sources
        javac --release 17 -proc:none -encoding UTF-8 -cp "target/classes:$cp" -d target/test-classes @target/test-sources
        tests=$(find src/test/java -name '*Test.java' | sed 's|src/test/java/||;s|[.]java$||;s|/|.|g' | sort)
        java -Djdk.net.hosts.file="$work/hosts" -Djavax.net.ssl.trustStore="$work/site.p12" \
            -Djavax.net.ssl.trustStorePassword=jetty-test -XX:ActiveProcessorCount=4 -Xmx1200m -Dbasedir="$local" \
            -cp "$work/launcher:$local/target/test-classes:$local/target/classes:$cp" RunJettySuites $tests
    )
done
# Start the unmodified server rule from Tycho and exercise both HTTP response paths.
javac --release 17 -proc:none -encoding UTF-8 -cp "$cp" -d "$work/consumer" \
    test-inputs/tycho/{HttpServer,FileServerServlet,AbstractMonitorServlet}.java "$tycho_test"
java -cp "$work/consumer:$cp" org.junit.runner.JUnitCore TychoServerCompatibility
