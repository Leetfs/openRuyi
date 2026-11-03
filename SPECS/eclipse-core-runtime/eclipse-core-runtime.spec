# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global platform_repo %{_datadir}/maven-repository/org/eclipse/platform
%global bundle_tools %{_libexecdir}/eclipse-equinox

Name:           eclipse-core-runtime
Version:        4.39
Release:        %autorelease
Summary:        Eclipse Platform runtime and content type registry
License:        EPL-2.0
URL:            https://eclipse.dev/eclipse/
VCS:            git:https://github.com/eclipse-platform/eclipse.platform
#!RemoteAsset:  sha256:973e213b8f8abbbfe397ec12d3d43c2a31fa81231646f29c473fec877b6bbd53
Source0:        https://github.com/eclipse-platform/eclipse.platform/archive/refs/tags/R4_39.tar.gz
#!RemoteAsset:  sha256:bd9db45f7477248429c71cf8465702dabfb1520ce8534f9dc25d4178ebb5897b
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.core.contenttype/3.9.800/org.eclipse.core.contenttype-3.9.800.pom
#!RemoteAsset:  sha256:5547e14033f8051ae55f4a8387046c74093b52036cdc356ef69ea518eae7e6ec
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.core.runtime/3.34.200/org.eclipse.core.runtime-3.34.200.pom
Source3:        PlatformCheck.java
#!RemoteAsset:  sha256:a33d9d7bfe1d48d245052b3ee4ee18519698c5f1ae9a9bb511113fd538c784fe
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.core.net/1.5.800/org.eclipse.core.net-1.5.800.pom
Source5:        ProxyCheck.java
BuildArch:      noarch

BuildRequires:  eclipse-equinox-build >= %{version}
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(net.java.dev.jna:jna-platform) == 5.18.1
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.security) == 1.4.700
BuildRequires:  mvn(org.apache.felix:org.apache.felix.scr) == 2.2.18
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.core.jobs) == 3.15.700
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.app) == 1.7.600
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.common) == 3.20.300
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.registry) == 3.12.600
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.preferences) == 3.12.100
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.osgi) == 3.24.100
BuildRequires:  mvn(org.osgi:org.osgi.service.prefs) == 1.1.2
Provides:       mvn(org.eclipse.platform:org.eclipse.core.contenttype) == 3.9.800
Provides:       mvn(org.eclipse.platform:org.eclipse.core.runtime) == 3.34.200
Requires:       eclipse-core-jobs >= 3.15.700
Requires:       eclipse-equinox >= %{version}
Requires:       eclipse-equinox-services >= %{version}
Requires:       felix-scr >= 2.2.18

%description
The Eclipse Platform runtime connects plug-ins to the extension registry,
preferences and application services. Its content type registry identifies
files by name and content and selects the appropriate content describer.

%package     -n eclipse-core-net
Summary:        Eclipse network proxy service
Provides:       mvn(org.eclipse.platform:org.eclipse.core.net) == 1.5.800
Requires:       eclipse-equinox-services >= %{version}
Requires:       jna >= 5.18.1

%description -n eclipse-core-net
The Eclipse proxy service selects HTTP, HTTPS and SOCKS routes, reads
platform proxy settings and applies per-host bypass rules.

%prep
%autosetup -n eclipse.platform-R4_39

%build
cp="%{_datadir}/java/javapackages-bootstrap/osgi.cmpn.jar:%{_datadir}/maven-repository/org/osgi/org.osgi.service.prefs/1.1.2/org.osgi.service.prefs-1.1.2.jar"
for coordinate in org.eclipse.osgi/3.24.100 org.eclipse.equinox.common/3.20.300 org.eclipse.core.jobs/3.15.700 \
    org.eclipse.equinox.registry/3.12.600 org.eclipse.equinox.preferences/3.12.100 org.eclipse.equinox.app/1.7.600; do
    name=${coordinate%%/*}
    version=${coordinate##*/}
    cp="$cp:%{platform_repo}/$coordinate/$name-$version.jar"
done
for name in org.eclipse.core.contenttype org.eclipse.core.runtime; do
    jar="$PWD/build/bundles/$name.jar"
    %{bundle_tools}/build-bundle "runtime/bundles/$name" "$jar" --release 17 --classpath "$cp"
    cp="$cp:$jar"
done
jna=%{_datadir}/maven-repository/net/java/dev/jna
for name in jna jna-platform; do cp="$cp:$jna/$name/5.18.1/$name-5.18.1.jar"; done
security=%{platform_repo}/org.eclipse.equinox.security/1.4.700/org.eclipse.equinox.security-1.4.700.jar
%{bundle_tools}/build-bundle team/bundles/org.eclipse.core.net build/bundles/org.eclipse.core.net.jar --release 17 --classpath "$cp:$security"
cp="$cp:$security:$PWD/build/bundles/org.eclipse.core.net.jar"
printf '%%s\n' "$cp" > build/classpath

%install
%{bundle_tools}/install-bundles %{buildroot} %{_datadir} eclipse-core-net build/bundles %{SOURCE4}
%{bundle_tools}/install-bundles %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1} %{SOURCE2}

%check
cp=$(cat build/classpath)
junit=
for library in junit-platform-launcher junit-platform-engine junit-platform-commons junit-jupiter-api junit-jupiter-engine apiguardian-api opentest4j assertj-core; do
    junit="$junit:%{_datadir}/java/javapackages-bootstrap/$library.jar"
done
content=runtime/tests/org.eclipse.core.contenttype.tests/src/org/eclipse/core/internal/contenttype/tests
runtime=runtime/tests/org.eclipse.core.tests.runtime/src/org/eclipse/core/tests/internal/runtime
test_resources=build/tests/org/eclipse/core/tests/internal/runtime
mkdir -p "$test_resources" build/launcher
cp "$runtime"/{truststore.jks,keystore.p12} "$test_resources/"
javac --release 17 -cp "$cp$junit" -d build/tests "$content/XMLRootHandlerTest.java" "$content/UserContentTypeTest.java" \
    "$runtime/CollectionTrustManagerTest.java" "$runtime/KeyStoreUtilTest.java"
# Verify the proxy service selects a configured HTTP route and honors bypass rules.
javac --release 17 -cp "$cp" -d build/tests %{SOURCE5}
framework=%{platform_repo}/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar
javac --release 17 -cp "$framework$junit" -d build/launcher %{SOURCE3} %{bundle_tools}/RunJupiter.java
osgi=%{_datadir}/maven-repository/org/osgi
java -cp "build/launcher:$framework$junit" PlatformCheck "$PWD/build/state" "$PWD/build/tests" \
    "$osgi/org.osgi.util.function/1.2.0/org.osgi.util.function-1.2.0.jar" \
    "$osgi/org.osgi.util.promise/1.3.0/org.osgi.util.promise-1.3.0.jar" \
    "$osgi/org.osgi.service.component/1.5.1/org.osgi.service.component-1.5.1.jar" \
    %{_datadir}/maven-repository/org/apache/felix/org.apache.felix.scr/2.2.18/org.apache.felix.scr-2.2.18.jar \
    %{platform_repo}/org.eclipse.equinox.common/3.20.300/org.eclipse.equinox.common-3.20.300.jar \
    %{platform_repo}/org.eclipse.core.jobs/3.15.700/org.eclipse.core.jobs-3.15.700.jar \
    "$osgi/org.osgi.service.prefs/1.1.2/org.osgi.service.prefs-1.1.2.jar" \
    %{platform_repo}/org.eclipse.equinox.registry/3.12.600/org.eclipse.equinox.registry-3.12.600.jar \
    %{platform_repo}/org.eclipse.equinox.preferences/3.12.100/org.eclipse.equinox.preferences-3.12.100.jar \
    %{platform_repo}/org.eclipse.equinox.app/1.7.600/org.eclipse.equinox.app-1.7.600.jar \
    %{platform_repo}/org.eclipse.equinox.security/1.4.700/org.eclipse.equinox.security-1.4.700.jar \
    %{_datadir}/maven-repository/net/java/dev/jna/jna/5.18.1/jna-5.18.1.jar \
    %{_datadir}/maven-repository/net/java/dev/jna/jna-platform/5.18.1/jna-platform-5.18.1.jar \
    build/bundles/org.eclipse.core.contenttype.jar build/bundles/org.eclipse.core.runtime.jar build/bundles/org.eclipse.core.net.jar

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/eclipse-core-runtime.xml
%{platform_repo}/org.eclipse.core.contenttype/
%{platform_repo}/org.eclipse.core.runtime/

%files -n eclipse-core-net
%license LICENSE NOTICE
%{_datadir}/maven-metadata/eclipse-core-net.xml
%{platform_repo}/org.eclipse.core.net/

%changelog
%autochangelog
