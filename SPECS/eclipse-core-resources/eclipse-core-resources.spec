# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global platform_repo %{_datadir}/maven-repository/org/eclipse/platform
%global osgi_repo %{_datadir}/maven-repository/org/osgi
%global jna_repo %{_datadir}/maven-repository/net/java/dev/jna
%global bundle_tools %{_libexecdir}/eclipse-equinox
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap

Name:           eclipse-core-resources
Version:        4.39
Release:        %autorelease
Summary:        Eclipse workspace, filesystem and build task support
License:        EPL-2.0
URL:            https://eclipse.dev/eclipse/
VCS:            git:https://github.com/eclipse-platform/eclipse.platform
#!RemoteAsset:  sha256:973e213b8f8abbbfe397ec12d3d43c2a31fa81231646f29c473fec877b6bbd53
Source0:        https://github.com/eclipse-platform/eclipse.platform/archive/refs/tags/R4_39.tar.gz
#!RemoteAsset:  sha256:d4ab3b85b254387957457c1f46b7001b5a90a898c5222c5020a0790e51616a50
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.core.expressions/3.9.500/org.eclipse.core.expressions-3.9.500.pom
#!RemoteAsset:  sha256:6857ecb38a96fae4851a62af11685d87f9435000a1ac98f086072082fe9ef094
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.core.variables/3.6.700/org.eclipse.core.variables-3.6.700.pom
#!RemoteAsset:  sha256:3655a432e1044a750e2d7db6fd4d183ad7fd16bdd41d0938292980a6acdc846c
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.ant.core/3.7.800/org.eclipse.ant.core-3.7.800.pom
#!RemoteAsset:  sha256:b1003cfaef0137e633c1386bcc57db0a5e587a59b5171e567ba530cfabbf8cc5
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.core.filesystem/1.11.400/org.eclipse.core.filesystem-1.11.400.pom
#!RemoteAsset:  sha256:08f6539df4a538caa0d07b1d7b6b4726c0e9724e86587eaa3172b1d11007f1f8
Source5:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.core.resources/3.23.200/org.eclipse.core.resources-3.23.200.pom
Source6:        ResourcesProbe.java

BuildRequires:  eclipse-equinox-build >= %{version}
BuildRequires:  gcc
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(net.java.dev.jna:jna) == 5.18.1
BuildRequires:  mvn(net.java.dev.jna:jna-platform) == 5.18.1
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.core.runtime) == 3.34.200
BuildRequires:  mvn(org.osgi:org.osgi.service.component.annotations) == 1.5.1
Provides:       mvn(org.eclipse.platform:org.eclipse.ant.core) == 3.7.800
Provides:       mvn(org.eclipse.platform:org.eclipse.core.expressions) == 3.9.500
Provides:       mvn(org.eclipse.platform:org.eclipse.core.filesystem) == 1.11.400
Provides:       mvn(org.eclipse.platform:org.eclipse.core.resources) == 3.23.200
Provides:       mvn(org.eclipse.platform:org.eclipse.core.variables) == 3.6.700
Requires:       eclipse-core-runtime >= %{version}
Requires:       mvn(net.java.dev.jna:jna) == 5.18.1
Requires:       mvn(net.java.dev.jna:jna-platform) == 5.18.1

%description
Eclipse Resources manages workspace projects, files and change notifications.
The filesystem bundle and Unix native library provide file attributes and
symbolic link support. The package includes the expression and variable
services and integrations for Ant workspace tasks.

%prep
%autosetup -n eclipse.platform-R4_39

%build
%set_build_flags
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
mkdir -p build/bundles
native=resources/bundles/org.eclipse.core.filesystem/natives/unix
%{__cc} $CFLAGS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -fPIC -I"$JAVA_HOME/include" -I"$JAVA_HOME/include/linux" \
    -c "$native/unixfile.c" -o build/unixfile.o
%{__cc} $LDFLAGS -shared -Wl,-soname,libunixfile_1_0_0.so -o build/libunixfile_1_0_0.so build/unixfile.o -lc

cp="%{bootstrap_java}/ant.jar:%{bootstrap_java}/ant-launcher.jar:%{bootstrap_java}/osgi.annotation.jar"
cp="$cp:%{osgi_repo}/org.osgi.service.component.annotations/1.5.1/org.osgi.service.component.annotations-1.5.1.jar"
cp="$cp:%{osgi_repo}/org.osgi.service.prefs/1.1.2/org.osgi.service.prefs-1.1.2.jar"
for name in jna jna-platform; do cp="$cp:%{jna_repo}/$name/5.18.1/$name-5.18.1.jar"; done
for coordinate in org.eclipse.osgi/3.24.100 org.eclipse.equinox.common/3.20.300 org.eclipse.core.jobs/3.15.700 org.eclipse.equinox.registry/3.12.600 org.eclipse.equinox.preferences/3.12.100 org.eclipse.equinox.app/1.7.600 org.eclipse.core.contenttype/3.9.800 org.eclipse.core.runtime/3.34.200; do
    name=${coordinate%%/*}
    version=${coordinate##*/}
    cp="$cp:%{platform_repo}/$coordinate/$name-$version.jar"
done
for module in runtime/bundles/org.eclipse.core.expressions debug/org.eclipse.core.variables ant/org.eclipse.ant.core resources/bundles/org.eclipse.core.filesystem resources/bundles/org.eclipse.core.resources; do
    name=$(basename "$module")
    jar="$PWD/build/bundles/$name.jar"
    %{bundle_tools}/build-bundle "$module" "$jar" --release 17 --classpath "$cp"
    cp="$jar:$cp"
    case "$name" in
        org.eclipse.ant.core) inner=lib/antsupportlib.jar ;;
        org.eclipse.core.resources) inner=ant_tasks/resources-ant.jar ;;
        *) continue ;;
    esac
    classes="$PWD/build/$name-ant"
    mkdir -p "$classes" "$module/$(dirname "$inner")"
    find "$module/src_ant" -name '*.java' | sort > build/ant-sources
    javac --release 17 -encoding UTF-8 -cp "$cp" -d "$classes" @build/ant-sources
    (cd "$module/src_ant" && find . -type f ! -name '*.java' -exec cp --parents -t "$classes" '{}' +)
    if test -f "$classes/META-INF/MANIFEST.MF"; then
        jar --create --file "$module/$inner" --manifest "$classes/META-INF/MANIFEST.MF" -C "$classes" .
    else
        jar --create --file "$module/$inner" -C "$classes" .
    fi
    jar --update --file "$jar" -C "$module" "$inner"
done
printf '%%s\n' "$cp" > build/classpath

%install
%{bundle_tools}/install-bundles %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5}
install -Dm755 build/libunixfile_1_0_0.so %{buildroot}%{_libdir}/libunixfile_1_0_0.so

%check
cp=$(cat build/classpath)
junit=
for lib in junit-platform-launcher junit-platform-engine junit-platform-commons junit-jupiter-api junit-jupiter-engine apiguardian-api opentest4j assertj-core; do
    junit="$junit:%{bootstrap_java}/$lib.jar"
done
tests=runtime/tests/org.eclipse.core.expressions.tests/src
mkdir -p build/tests
find "$tests" \( -name CountExpressionTest.java -o -name ExpressionInfoTests.java \) | sort > build/test-sources
javac --release 17 -encoding UTF-8 -cp "$cp$junit" -sourcepath "$tests" -d build/tests @build/test-sources
mkdir -p build/launcher
javac --release 17 -encoding UTF-8 -cp "$cp$junit" -d build/launcher %{SOURCE6} %{bundle_tools}/RunJupiter.java
cat > build/probe.mf <<'EOF'
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-SymbolicName: org.openruyi.workspace.check
Bundle-Version: 1.0.0
Bundle-Activator: ResourcesProbe
Require-Bundle: org.eclipse.core.resources,org.eclipse.core.filesystem,
 org.eclipse.core.runtime,org.eclipse.osgi
EOF
jar --create --file build/probe.jar --manifest build/probe.mf -C build/launcher ResourcesProbe.class
platform="%{platform_repo}"
osgi="%{osgi_repo}"
bundles=
for coordinate in org.osgi.util.function/1.2.0 org.osgi.util.promise/1.3.0 org.osgi.service.component/1.5.1 org.osgi.service.prefs/1.1.2; do
    name=${coordinate%%/*}; version=${coordinate##*/}
    bundles="$bundles $osgi/$coordinate/$name-$version.jar"
done
bundles="$bundles %{_datadir}/maven-repository/org/apache/felix/org.apache.felix.scr/2.2.18/org.apache.felix.scr-2.2.18.jar"
for coordinate in org.eclipse.equinox.common/3.20.300 org.eclipse.core.jobs/3.15.700 org.eclipse.equinox.registry/3.12.600 org.eclipse.equinox.preferences/3.12.100 org.eclipse.equinox.app/1.7.600 org.eclipse.core.contenttype/3.9.800 org.eclipse.core.runtime/3.34.200; do
    name=${coordinate%%/*}; version=${coordinate##*/}
    bundles="$bundles $platform/$coordinate/$name-$version.jar"
done
for name in jna jna-platform; do bundles="$bundles %{jna_repo}/$name/5.18.1/$name-5.18.1.jar"; done
for name in org.eclipse.core.expressions org.eclipse.core.variables org.eclipse.ant.core org.eclipse.core.filesystem org.eclipse.core.resources; do bundles="$bundles build/bundles/$name.jar"; done
java -ea -Djava.library.path="%{buildroot}%{_libdir}" -cp "build/launcher:$platform/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar$junit" \
    ResourcesFramework build/osgi build/tests $bundles build/probe.jar

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/eclipse-core-resources.xml
%{_libdir}/libunixfile_1_0_0.so
%{platform_repo}/org.eclipse.ant.core/
%{platform_repo}/org.eclipse.core.expressions/
%{platform_repo}/org.eclipse.core.filesystem/
%{platform_repo}/org.eclipse.core.resources/
%{platform_repo}/org.eclipse.core.variables/

%changelog
%autochangelog
