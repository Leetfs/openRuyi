# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global fragment org.eclipse.swt.gtk.linux.%{_arch}
%global platform_repo %{_datadir}/maven-repository/org/eclipse/platform
%global bundle_tools %{_libexecdir}/eclipse-equinox

Name:           eclipse-swt
Version:        3.133.0
Release:        %autorelease
Summary:        Eclipse Standard Widget Toolkit for GTK
License:        EPL-2.0 AND LGPL-2.1-only AND BSD-2-Clause AND MPL-1.1 AND IJG AND MIT
URL:            https://eclipse.dev/eclipse/swt/
VCS:            git:https://github.com/eclipse-platform/eclipse.platform.swt
#!RemoteAsset:  sha256:e3e940abd9d5c50604d32ccb1a689383aff16f60de03548735594c17d443cc4c
Source0:        https://github.com/eclipse-platform/eclipse.platform.swt/archive/refs/tags/R4_39.tar.gz
#!RemoteAsset:  sha256:5d2feb51ee47a06ff1035240bd9709d6c67dec1b988f633ad054236904c50cf3
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.swt/%{version}/org.eclipse.swt-%{version}.pom
#!RemoteAsset:  sha256:4d25efe45b1fa04ae9417e927c9653a3c7c4fa27d9e585cdc4242edf8e93a47b
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.swt.gtk.linux.x86_64/%{version}/org.eclipse.swt.gtk.linux.x86_64-%{version}.pom
#!RemoteAsset:  sha256:196da9f347541c32ead5636db67409399323fcadab5942900ac1ae08ea2244e3
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.swt.gtk.linux.riscv64/%{version}/org.eclipse.swt.gtk.linux.riscv64-%{version}.pom
Source4:        SwtSmoke.java
# SwtTestUtil references the release test harness to capture UI timeouts.
#!RemoteAsset:  sha256:6eeb81196d1ff967e7ed764c80be720fdac357933ad8a51a0ae4ba0c40bd1f9c
Source5:        https://raw.githubusercontent.com/eclipse-platform/eclipse.platform.releng.aggregator/cbf8d407306aad17ec8e2426995a164318c5a408/eclipse.platform.releng/bundles/org.eclipse.test/src/org/eclipse/test/Screenshots.java
#!RemoteAsset:  sha256:4e1d08b6e2561697d2d6cac611c344358649d7eec832f33588d22e3deb070d20
Source6:        https://raw.githubusercontent.com/eclipse-platform/eclipse.platform.releng.aggregator/cbf8d407306aad17ec8e2426995a164318c5a408/eclipse.platform.releng/bundles/org.eclipse.test/src/org/eclipse/test/AwtScreenshot.java

BuildRequires:  dbus-tools
BuildRequires:  eclipse-equinox-build >= 4.39
BuildRequires:  gcc
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  make
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.core.runtime) == 3.34.200
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  unzip
BuildRequires:  xorg-server-xvfb
BuildRequires:  zip
Provides:       mvn(org.eclipse.platform:org.eclipse.swt) == %{version}
Provides:       mvn(org.eclipse.platform:%{fragment}) == %{version}
Requires:       glu
Requires:       gtk3
Requires:       java-25-openjdk

%description
SWT is the widget toolkit used by Eclipse. This build includes its GTK 3
and X11 integration, Java widgets, graphics, accessibility, drag and drop,
printing and OpenGL APIs.

%prep
%autosetup -n eclipse.platform.swt-R4_39
fragment=binaries/%{fragment}
find "$fragment" -maxdepth 1 -name 'libswt-*.so' -delete
test -z "$(find "$fragment" -name '*.so' -print -quit)"

%build
%set_build_flags
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
export SWT_JAVA_HOME="$JAVA_HOME" OUTPUT_DIR="$PWD/binaries/%{fragment}"
mkdir -p build/bundles build/host/META-INF
(cd bundles/org.eclipse.swt && java -Dws=gtk build-scripts/CollectSources.java -nativeSources native && sh native/build.sh -gtk3 install)
test -s "$OUTPUT_DIR"/libswt-gtk-*.so
test -s "$OUTPUT_DIR"/libswt-pi3-gtk-*.so

host=bundles/org.eclipse.swt
cp -a "$host"/{META-INF,about.html,about_files,plugin.properties} build/host/
sed 's/^Bundle-Version: %{version}\.qualifier$/Bundle-Version: %{version}/' "$host/META-INF/MANIFEST.MF" > build/host.mf
jar --create --file build/bundles/org.eclipse.swt.jar --manifest build/host.mf -C build/host .
jar="$PWD/build/bundles/%{fragment}.jar"
%{bundle_tools}/build-bundle "$OUTPUT_DIR" "$jar" --release 17 --classpath .
# The fragment's PDE bin.excludes omits the source-only JNI library directory.
if jar tf "$jar" | grep -q '^library/'; then zip -qd "$jar" 'library/*'; fi

%install
%ifarch x86_64
model=%{SOURCE2}
%endif
%ifarch riscv64
model=%{SOURCE3}
%endif
%{bundle_tools}/install-bundles %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1} "$model"

%check
host=build/bundles/org.eclipse.swt.jar
fragment=build/bundles/%{fragment}.jar
jar tf "$fragment" | grep -Fx 'org/eclipse/swt/widgets/Display.class'
if jar tf "$fragment" | grep -q '^library/'; then exit 1; fi
for lib in binaries/%{fragment}/libswt-*.so; do
    unzip -p "$fragment" "$(basename "$lib")" | cmp - "$lib"
done
junit=
for lib in junit-platform-launcher junit-platform-engine junit-platform-commons junit-jupiter-api junit-jupiter-engine apiguardian-api opentest4j; do
    junit="$junit:%{_datadir}/java/javapackages-bootstrap/$lib.jar"
done
tests='tests/org.eclipse.swt.tests/JUnit Tests'
mkdir -p build/tests
classes=
for name in Point Rectangle RGB PaletteData; do
    file=Test_org_eclipse_swt_graphics_$name
    printf '"%%s"\n' "$tests/org/eclipse/swt/tests/junit/$file.java" >> build/test-sources
    classes="$classes org.eclipse.swt.tests.junit.$file"
done
support="%{_datadir}/java/javapackages-bootstrap/junit.jar:%{platform_repo}/org.eclipse.core.runtime/3.34.200/org.eclipse.core.runtime-3.34.200.jar"
javac --release 17 -encoding UTF-8 -cp "$host:$fragment:$support$junit" -sourcepath "$tests" -d build/tests %{SOURCE5} %{SOURCE6} @build/test-sources
java -ea -cp "build/tests:$host:$fragment:$support$junit" %{bundle_tools}/RunJupiter.java $classes

# Resolve the SWT host as a normal Maven dependency, including its native profile.
mkdir -p build/consumer/{.mvn,.xmvn,metadata,src/main/java}
cp %{SOURCE4} build/consumer/src/main/java/
cd build/consumer
for file in %{_datadir}/maven-metadata/*.xml; do
    test "$(basename "$file")" = %{name}.xml || ln -s "$file" metadata/
done
sed 's@<path>/@<path>%{buildroot}/@g' %{buildroot}%{_datadir}/maven-metadata/%{name}.xml > metadata/%{name}.xml
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
  <repository>$PWD/metadata</repository><repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
cat > pom.xml <<'EOF'
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
  <groupId>org.openruyi.check</groupId><artifactId>swt-consumer</artifactId><version>1</version>
  <properties><maven.compiler.release>17</maven.compiler.release></properties>
  <dependencies><dependency><groupId>org.eclipse.platform</groupId><artifactId>org.eclipse.swt</artifactId><version>%{version}</version></dependency></dependencies>
</project>
EOF
ext=%{_datadir}/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
plugin=$(unzip -p %{_datadir}/java/javapackages-bootstrap/maven-compiler-plugin.jar META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
test -n "$plugin"
mvn -B --offline -Dmaven.repo.local="$PWD/repository" "org.apache.maven.plugins:maven-compiler-plugin:$plugin:compile"
cd ../..
export XDG_RUNTIME_DIR="$PWD/build/runtime"
mkdir -m700 "$XDG_RUNTIME_DIR"
Xvfb -displayfd 3 -screen 0 1024x768x24 -nolisten tcp 3>build/display >build/xvfb.log 2>&1 &
server=$!
trap 'kill "$server" 2>/dev/null || :' EXIT
for i in $(seq 1 60); do test ! -s build/display || break; kill -0 "$server"; sleep 0.2; done
test -s build/display
export DISPLAY=:$(cat build/display) SWT_GTK3=1 GDK_BACKEND=x11
timeout 60 dbus-run-session -- java -cp "build/consumer/target/classes:$host:$fragment" SwtSmoke

%files
%license LICENSE NOTICE binaries/legal_files/gtk.linux/about.html binaries/legal_files/gtk.linux/about_files/
%{_datadir}/maven-metadata/eclipse-swt.xml
%{platform_repo}/org.eclipse.swt/
%{platform_repo}/%{fragment}/

%changelog
%autochangelog
