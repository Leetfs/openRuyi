# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global platform_repo %{_datadir}/maven-repository/org/eclipse/platform
%global bundle_tools %{_libexecdir}/eclipse-equinox

Name:           eclipse-equinox-p2
Version:        4.38
Release:        %autorelease
Summary:        Eclipse p2 provisioning metadata, repositories and publisher
License:        EPL-2.0
URL:            https://equinox.eclipseprojects.io/
VCS:            git:https://github.com/eclipse-equinox/p2
#!RemoteAsset:  sha256:076b3b6b749e175477e1f28a79ca926fd6acd8af4cb7937d82dc6d79887a7f58
Source0:        https://github.com/eclipse-equinox/p2/archive/refs/tags/R4_38.tar.gz
#!RemoteAsset:  sha256:f0206499a65fc816a69cd5b1709c0f403b6cc1018f7d311bedd100af31eda775
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.p2.core/2.13.200/org.eclipse.equinox.p2.core-2.13.200.pom
#!RemoteAsset:  sha256:c9175a590db21dca05799ea18daf3bae7b657647a3c3fe571a634b3faa804534
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.p2.metadata/2.9.600/org.eclipse.equinox.p2.metadata-2.9.600.pom
#!RemoteAsset:  sha256:07253777a48f1dd945c5582f35051a44f314cb2d1359334fa8e0aa92651a5ce1
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.p2.repository/2.9.600/org.eclipse.equinox.p2.repository-2.9.600.pom
#!RemoteAsset:  sha256:197c3e4964a3d580e7212c4d6c905ac98d04047c6fb48e36190de4468f92ba19
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.p2.jarprocessor/1.3.600/org.eclipse.equinox.p2.jarprocessor-1.3.600.pom
#!RemoteAsset:  sha256:990844f33e96a27d2c64c4ee4b13dce1a0add790abfc64b8829b10360cd34580
Source5:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.p2.artifact.repository/1.5.800/org.eclipse.equinox.p2.artifact.repository-1.5.800.pom
#!RemoteAsset:  sha256:c5822cbd63c1363fad82c114df8d7a0104edc1ba5f131120b01a249fbd34094a
Source6:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.p2.metadata.repository/1.5.700/org.eclipse.equinox.p2.metadata.repository-1.5.700.pom
#!RemoteAsset:  sha256:3af02f624d559e80f64d3375de39050999cf92b71c3e9b90d57f7a8336b40c01
Source7:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.p2.publisher/1.9.600/org.eclipse.equinox.p2.publisher-1.9.600.pom
Source8:        P2AgentCheck.java
BuildArch:      noarch

BuildRequires:  eclipse-equinox-build(nested-jars)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.apache.felix:org.apache.felix.scr) == 2.2.18
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.core.runtime) == 3.34.200
BuildRequires:  mvn(org.tukaani:xz) == 1.12
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk18on) == 1.86
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.core.jobs) == 3.15.700
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.common) == 3.20.300
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.registry) == 3.12.600
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.preferences) == 3.12.100
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.app) == 1.7.600
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.security) == 1.4.700
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.osgi) == 3.24.100
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.p2.core) == 2.13.200
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.p2.metadata) == 2.9.600
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.p2.repository) == 2.9.600
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.p2.jarprocessor) == 1.3.600
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.p2.artifact.repository) == 1.5.800
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.p2.metadata.repository) == 1.5.700
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.p2.publisher) == 1.9.600
Requires:       bouncycastle >= 1.86
Requires:       eclipse-core-jobs >= 3.15.700
Requires:       eclipse-equinox >= 4.39
Requires:       eclipse-equinox-services >= 4.39
Requires:       eclipse-core-runtime >= 4.39
Requires:       felix-scr >= 2.2.18
Requires:       xz-java >= 1.12

%description
Eclipse p2 represents installable units and their requirements, reads
artifact and metadata repositories, and publishes provisioning metadata
from application bundles.

%prep
%autosetup -n p2-R4_38

%build
framework=%{platform_repo}/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar
common=%{platform_repo}/org.eclipse.equinox.common/3.20.300/org.eclipse.equinox.common-3.20.300.jar
jobs=%{platform_repo}/org.eclipse.core.jobs/3.15.700/org.eclipse.core.jobs-3.15.700.jar
cp="$framework:$common:$jobs:%{_datadir}/java/javapackages-bootstrap/osgi.annotation.jar:%{_datadir}/java/javapackages-bootstrap/osgi.cmpn.jar:%{_datadir}/maven-repository/org/tukaani/xz/1.12/xz-1.12.jar"
for coordinate in org.eclipse.equinox.registry/3.12.600 org.eclipse.equinox.preferences/3.12.100 org.eclipse.equinox.app/1.7.600 org.eclipse.equinox.security/1.4.700; do
    name=${coordinate%%/*}
    version=${coordinate##*/}
    cp="$cp:%{platform_repo}/$coordinate/$name-$version.jar"
done
for module in bcprov bcutil bcpg; do
    cp="$cp:%{_datadir}/maven-repository/org/bouncycastle/$module-jdk18on/1.86/$module-jdk18on-1.86.jar"
done
mkdir -p build/bundles
for module in core metadata repository jarprocessor artifact.repository metadata.repository publisher; do
    name=org.eclipse.equinox.p2.$module
    jar="$PWD/build/bundles/$name.jar"
    %{bundle_tools}/build-bundle "bundles/$name" "$jar" --release 17 --classpath "$cp" --nested-classpath %{_datadir}/java/javapackages-bootstrap/ant.jar
    cp="$cp:$jar"
done
printf '%%s\n' "$cp" > build/classpath

%install
%{bundle_tools}/install-bundles %{buildroot} %{_datadir} %{name} build/bundles \
    %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7}

%check
cp="$(cat build/classpath):%{_datadir}/java/javapackages-bootstrap/junit.jar:%{_datadir}/java/javapackages-bootstrap/hamcrest-core.jar"
# Load and run the JAR processor task from its original PDE nested library.
mkdir -p build/ant-check/payload
(cd build/ant-check && jar xf ../bundles/org.eclipse.equinox.p2.jarprocessor.jar lib/jarprocessor-ant.jar)
echo 'p2 archive' > build/ant-check/payload/readme
jar --create --file build/ant-check/example.jar -C build/ant-check/payload .
cat > build/ant-check/build.xml <<'EOF'
<project default="test">
  <taskdef name="jarprocessor" classname="org.eclipse.equinox.internal.p2.jarprocessor.ant.JarProcessorTask"/>
  <target name="test"><jarprocessor jar="example.jar"/></target>
  <target name="missing-alias"><jarprocessor jar="example.jar" sign="true"/></target>
</project>
EOF
ant_cp="%{_datadir}/java/javapackages-bootstrap/ant.jar:%{_datadir}/java/javapackages-bootstrap/ant-launcher.jar:$cp:$PWD/build/ant-check/lib/jarprocessor-ant.jar"
java -cp "$ant_cp" org.apache.tools.ant.Main -f build/ant-check/build.xml test
if java -cp "$ant_cp" org.apache.tools.ant.Main -f build/ant-check/build.xml missing-alias > build/ant-check/missing-alias.log 2>&1; then exit 1; fi
grep -F 'Alias must be set' build/ant-check/missing-alias.log
# Verify the upstream p2 metadata, repository and publisher suites.
tests=bundles/org.eclipse.equinox.p2.tests/src/org/eclipse/equinox/p2/tests/omniVersion
mkdir -p build/tests
javac --release 17 -cp "$cp" -d build/tests "$tests"/*.java
java -cp "build/tests:$cp" org.junit.runner.JUnitCore org.eclipse.equinox.p2.tests.omniVersion.AllTests
cat > build/PublishVersion.java <<'JAVA'
import org.eclipse.equinox.p2.metadata.Version;
import org.eclipse.equinox.p2.publisher.actions.VersionAdvice;

class PublishVersion {
    public static void main(String[] args) {
        Version value = Version.create("1.2.3");
        VersionAdvice advice = new VersionAdvice();
        advice.setVersion("bundle", "org.openruyi.test", value);
        if (!value.equals(advice.getVersion("bundle", "org.openruyi.test"))) {
            throw new AssertionError("Publisher lost the supplied bundle version");
        }
    }
}
JAVA
java -cp "$cp" build/PublishVersion.java
framework=%{platform_repo}/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar
osgi=%{_datadir}/maven-repository/org/osgi
bundles=("$osgi/org.osgi.util.function/1.2.0/org.osgi.util.function-1.2.0.jar" \
    "$osgi/org.osgi.util.promise/1.3.0/org.osgi.util.promise-1.3.0.jar" \
    "$osgi/org.osgi.service.component/1.5.1/org.osgi.service.component-1.5.1.jar" \
    %{_datadir}/maven-repository/org/apache/felix/org.apache.felix.scr/2.2.18/org.apache.felix.scr-2.2.18.jar \
    %{platform_repo}/org.eclipse.equinox.common/3.20.300/org.eclipse.equinox.common-3.20.300.jar \
    %{platform_repo}/org.eclipse.core.jobs/3.15.700/org.eclipse.core.jobs-3.15.700.jar \
    "$osgi/org.osgi.service.prefs/1.1.2/org.osgi.service.prefs-1.1.2.jar")
for coordinate in org.eclipse.equinox.registry/3.12.600 org.eclipse.equinox.preferences/3.12.100 org.eclipse.equinox.app/1.7.600 \
    org.eclipse.equinox.security/1.4.700 org.eclipse.core.contenttype/3.9.800 org.eclipse.core.runtime/3.34.200; do
    name=${coordinate%%/*}
    version=${coordinate##*/}
    bundles+=("%{platform_repo}/$coordinate/$name-$version.jar")
done
for module in bcprov bcutil bcpg; do
    bundles+=("%{_datadir}/maven-repository/org/bouncycastle/$module-jdk18on/1.86/$module-jdk18on-1.86.jar")
done
java -cp "$framework" %{SOURCE8} "$PWD/build/runtime" "${bundles[@]}" \
    %{_datadir}/maven-repository/org/tukaani/xz/1.12/xz-1.12.jar \
    build/bundles/org.eclipse.equinox.p2.{core,metadata,repository,jarprocessor,artifact.repository,metadata.repository,publisher}.jar

%files
%doc README.md
%license LICENSE NOTICE
%{_datadir}/maven-metadata/eclipse-equinox-p2.xml
%{platform_repo}/org.eclipse.equinox.p2.*/

%changelog
%autochangelog
