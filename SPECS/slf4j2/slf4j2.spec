# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global jpb %{_datadir}/java/javapackages-bootstrap
%global bundle_tools %{_libexecdir}/eclipse-equinox
%global repodir %{_datadir}/maven-repository/org/slf4j
Name:           slf4j2
Version:        2.0.17
Release:        %autorelease
Summary:        Simple Logging Facade for Java 2 API
License:        MIT
URL:            https://www.slf4j.org/
VCS:            git:https://github.com/qos-ch/slf4j
#!RemoteAsset:  sha256:5df6cd5ba67fe4d874e6b6a10b67431efc8c56442a4dfda0a4c814fe007cc2a9
Source0:        https://github.com/qos-ch/slf4j/archive/refs/tags/v_%{version}.tar.gz?/slf4j-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  maven >= 3.9.9
BuildRequires:  unzip
BuildRequires:  xmlstarlet
Provides:       mvn(org.slf4j:slf4j-api) == %{version}
Provides:       mvn(org.slf4j:slf4j-parent:pom:) == %{version}
Provides:       mvn(org.slf4j:slf4j-bom:pom:) == %{version}
Requires:       java-25-openjdk

%description
The SLF4J 2 API routes application logging through service providers.
Its Java module org.slf4j is also available to modular Java applications.

%prep
%autosetup -n slf4j-v_%{version}

%build
cd slf4j-api
mkdir -p target/classes target/module target/test-classes build/bundles .mvn .xmvn
find src/main/java -name '*.java' | sort > target/sources
javac --release 8 -encoding UTF-8 -proc:none -d target/classes @target/sources
javac --release 9 --module-version %{version} --patch-module org.slf4j=target/classes -d target/module src/main/java9/module-info.java
mkdir -p target/classes/META-INF/versions/9
install -m644 target/module/module-info.class target/classes/META-INF/versions/9/
cat > .xmvn/configuration.xml <<'EOF'
<configuration><resolverSettings><metadataRepositories><repository>/usr/share/maven-metadata</repository>
<repository>/usr/share/javapackages-bootstrap/maven-metadata</repository></metadataRepositories></resolverSettings></configuration>
EOF
# Generate the OSGi manifest from the released build instructions. The wagon extension publishes release artifacts.
mkdir -p target/models/parent target/models/api
cp ../pom.xml target/models/pom.xml
xmlstarlet ed -P -N m=http://maven.apache.org/POM/4.0.0 -d '/m:project/m:build/m:extensions' ../parent/pom.xml > target/models/parent/pom.xml
xmlstarlet ed -P -N m=http://maven.apache.org/POM/4.0.0 -s '/m:project/m:build' -t elem -n directory -v "$PWD/target" pom.xml > target/models/api/pom.xml
plugin=$(unzip -p %{jpb}/maven-bundle-plugin.jar META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
ext=%{_datadir}/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
mvn -B -o -f target/models/api/pom.xml -Dmaven.repo.local="$PWD/target/repo" "org.apache.felix:maven-bundle-plugin:$plugin:manifest"
jar cfm build/bundles/slf4j-api.jar target/classes/META-INF/MANIFEST.MF -C target/classes .

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name}-models pom.xml parent/pom.xml
%{bundle_tools}/install-bundles --symbolic-name slf4j.api %{buildroot} %{_datadir} %{name} slf4j-api/build/bundles slf4j-api/pom.xml

%check
cd slf4j-api
jar="$PWD/build/bundles/slf4j-api.jar"
jar --describe-module --file "$jar" --release 9 | grep -F 'org.slf4j@%{version}'
# Keep the test runtime free of a logging provider so the upstream no-binding tests exercise their fallback.
cp="$jar:%{jpb}/junit.jar:%{jpb}/hamcrest-core.jar"
find src/test/java -name '*.java' | sort > target/test-sources
javac --release 8 -proc:none -encoding UTF-8 -cp "$cp" -d target/test-classes @target/test-sources
# The binding modules subclass the abstract thread-initialization fixture.
find target/test-classes -type f \( -name 'Test*.class' -o -name '*Test.class' -o -name '*Tests.class' -o -name '*TestCase.class' \) \
    ! -name '*$*' ! -name AllTest.class ! -name PackageTest.class ! -name MultithreadedInitializationTest.class \
    | sed 's|target/test-classes/||;s|[.]class$||;s|/|.|g' | sort > target/suites
grep -Fx org.slf4j.basicTests.NoBindingTest target/suites
while IFS= read -r suite; do java -cp "target/test-classes:$cp" org.junit.runner.JUnitCore "$suite" || exit 1; done < target/suites
mkdir -p target/consumer/src/org/openruyi/check
echo 'module org.openruyi.check { requires org.slf4j; }' > target/consumer/src/module-info.java
cat > target/consumer/src/org/openruyi/check/Consumer.java <<'EOF'
package org.openruyi.check;
import org.slf4j.LoggerFactory;
public class Consumer {
    public static void main(String[] args) {
        LoggerFactory.getLogger(Consumer.class).atInfo().log("module consumer");
        if (!LoggerFactory.class.getModule().getName().equals("org.slf4j")) throw new AssertionError();
    }
}
EOF
javac --release 11 --module-path "$jar" -d target/consumer/classes target/consumer/src/module-info.java target/consumer/src/org/openruyi/check/Consumer.java
java --module-path "$jar:target/consumer/classes" -m org.openruyi.check/org.openruyi.check.Consumer

%files
%license LICENSE.txt
%{_datadir}/maven-metadata/slf4j2.xml
%{_datadir}/maven-metadata/slf4j2-models.xml
%{repodir}/slf4j-api/%{version}/
%{repodir}/slf4j-parent/%{version}/
%{repodir}/slf4j-bom/%{version}/

%changelog
%autochangelog
