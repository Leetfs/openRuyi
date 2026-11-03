# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global release_tag R4_41
%global qualifier v20260828-1142
%global jdk_home %{_libdir}/jvm/java-25-openjdk
%global sdk_dir products/eclipse-sdk/target/products/org.eclipse.sdk.ide/linux/gtk/%{_arch}/eclipse

Name:           eclipse
Version:        4.41
Release:        %autorelease
Summary:        Eclipse integrated development environment
License:        EPL-2.0 AND Apache-1.1 AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT AND EPL-1.0 AND 0BSD AND LGPL-2.1-only AND MPL-1.1 AND IJG
URL:            https://eclipse.dev/eclipse/
VCS:            git:https://github.com/eclipse-platform/eclipse.platform.releng.aggregator
#!RemoteAsset:  sha256:f43b389cc2edf029a344f22f9819876347712105da18d3c088d189cdadd73ec1
Source0:        https://github.com/eclipse-platform/eclipse.platform.releng.aggregator/archive/%{release_tag}.tar.gz
#!RemoteAsset:  sha256:3a1c32a79cd22f34d173820b55aebebe83eb7aa29486caa4a319de6226c7bba5
Source1:        https://github.com/eclipse-jdt/eclipse.jdt/archive/406480b02685764dac31ac122f009dab2209246d.tar.gz
#!RemoteAsset:  sha256:a650a17bb74381fb042318ea05483c5451f1aad78df30f67b51cb572007370d9
Source2:        https://github.com/eclipse-jdt/eclipse.jdt.core/archive/6725c16c24d94c83302346dc384bb915a0f2fe1a.tar.gz
#!RemoteAsset:  sha256:18e97aa0bc2c6efa791dcabc6e144c07d966c483cd4660482f44ad1d9a1db15c
Source3:        https://github.com/eclipse-jdt/eclipse.jdt.core.binaries/archive/ea1e2ac218341566a643bd5ec445b73a7c675215.tar.gz
#!RemoteAsset:  sha256:b546ced88f3238e332f9c032c58a013742568c58bd721790e30b87ef8572c764
Source4:        https://github.com/eclipse-jdt/eclipse.jdt.debug/archive/4906ab36a3b6ff2d18c6330380fb502eca24ae1c.tar.gz
#!RemoteAsset:  sha256:22120eedfe525bbf0eeed48faa6709bbca8f8566b1d690d225b53bf33e525d82
Source5:        https://github.com/eclipse-jdt/eclipse.jdt.ui/archive/54bd63e6453a7eb5db0bfc1d60f17e9568095619.tar.gz
#!RemoteAsset:  sha256:186f9d2318bf6db2c454e4107af3b07f546131071b6f7de076e137fe789ba778
Source6:        https://github.com/eclipse-pde/eclipse.pde/archive/ae968850a6a6d94f0f68b4ebae11e04302c36111.tar.gz
#!RemoteAsset:  sha256:d9af7400b71ad805c5cd4f9d99a49c0d09cd2346e9d128d375daf4b89d8561d3
Source7:        https://github.com/eclipse-platform/eclipse.platform/archive/2fa8a8026334c9104e825bf5259f12ee8baebf26.tar.gz
#!RemoteAsset:  sha256:ae2e39059b21195d41c37f7f74272e6f7b3fc82988466306086a9a50f5596c83
Source8:        https://github.com/eclipse-platform/eclipse.platform.swt/archive/3e3b24b4691c4f18a7d5e22653fe28d4c47385d7.tar.gz
#!RemoteAsset:  sha256:d9c7a54906f3dcdc7a9b6f3194f879509a157cc384f659f926b0a114bc558eaa
Source9:        https://github.com/eclipse-platform/eclipse.platform.ui/archive/f0ef795ed3148ad7aec4157c78f5ea9c8b7f3380.tar.gz
#!RemoteAsset:  sha256:6e2382b5480c13b5777abe5c5cc493896ab3014065cec2fe659969b75a96de2e
Source10:       https://github.com/eclipse-equinox/equinox/archive/12022c26e62ce76e376f6f9b22001b9aa0f969a7.tar.gz
#!RemoteAsset:  sha256:d46e4984766553a863e52be25ef1ffa80f02649a3d4cb43d579bf884d29dff88
Source11:       https://github.com/eclipse-equinox/equinox.binaries/archive/c23e26d74804f6d20a6a4c825e02c461dabf4402.tar.gz
#!RemoteAsset:  sha256:892214b411a05a22dfac035c56c8b8691e4425146eaab9d4ae4409beb9237978
Source12:       https://github.com/eclipse-equinox/p2/archive/529df3a3aa0257a89af007b4714066f9db552e33.tar.gz
Source13:       eclipse.desktop
Source14:       prepare-sdk-maven.py

BuildRequires:  dbus-tools
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  make
BuildRequires:  maven >= 3.9.12
BuildRequires:  mvn(org.eclipse.tycho:tycho-build) == 5.0.3
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin) == 3.2.0
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin) == 3.8.0
BuildRequires:  mvn(org.apache.maven.plugins:maven-clean-plugin) == 3.5.0
BuildRequires:  mvn(org.apache.maven.plugins:maven-resources-plugin) == 3.5.0
BuildRequires:  mvn(org.apache.maven.plugins:maven-install-plugin) == 3.1.1
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin) == 3.15.0
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin) == 3.5.0
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin) == 3.6.1
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin) == 3.5.6
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin) == 3.6.1
BuildRequires:  mvn(org.eclipse.jdt:ecj) == 3.45.0
BuildRequires:  python3
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  xmlstarlet
BuildRequires:  xorg-server-xvfb
Requires:       gtk3
Requires:       java-25-openjdk

%description
The Eclipse SDK includes the Eclipse workbench, Java Development Tools and
Plug-in Development Environment. It can edit, build and debug Java
applications and develop extensions for the Eclipse platform.

%prep
%autosetup -n eclipse.platform.releng.aggregator-%{release_tag}
unpack_module() {
    mkdir -p "$2"
    tar -xf "$1" --strip-components=1 -C "$2"
}
unpack_module %{SOURCE1} eclipse.jdt
unpack_module %{SOURCE2} eclipse.jdt.core
unpack_module %{SOURCE3} eclipse.jdt.core.binaries
unpack_module %{SOURCE4} eclipse.jdt.debug
unpack_module %{SOURCE5} eclipse.jdt.ui
unpack_module %{SOURCE6} eclipse.pde
unpack_module %{SOURCE7} eclipse.platform
unpack_module %{SOURCE8} eclipse.platform.swt
unpack_module %{SOURCE9} eclipse.platform.ui
unpack_module %{SOURCE10} equinox
unpack_module %{SOURCE11} equinox.binaries
unpack_module %{SOURCE12} equinox.p2

# Tycho normally materializes products for all architectures in the parent POM.
xmlstarlet ed -P -L -N m=http://maven.apache.org/POM/4.0.0 \
    -d "//m:environments/m:environment[m:os!='linux' or m:ws!='gtk' or m:arch!='%{_arch}']" \
    eclipse-platform-parent/pom.xml
cat >> .mvn/maven.config <<EOF
--batch-mode
--offline
--no-transfer-progress
-Dmaven.repo.local=$PWD/maven-repository
-DforceContextQualifier=%{qualifier}
-Dtycho.baseline=disable
-Dtycho.baseline.replace=none
-DcompilerBaselineMode=disable
-DcompilerBaselineReplace=none
EOF
mkdir -p maven-repository .xmvn
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
  <repository>%{_datadir}/maven-metadata</repository>
  <repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
cp -as %{_datadir}/maven-repository/. maven-repository/

%build
%set_build_flags
export JAVA_HOME=%{jdk_home}
export PATH="$JAVA_HOME/bin:$PATH"
python3 %{SOURCE14}
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=$(cat .mvn/openruyi-extension/sdk-classpath)"
export BINARIES_DIR="$PWD/equinox.binaries"
launcher=equinox/features/org.eclipse.equinox.executable.feature/library/gtk
sh "$launcher/build.sh" -os linux -ws gtk -arch %{_arch} -java "$JAVA_HOME" install

%ifarch x86_64
# This platform feature ships the Unix and bulk Linux filesystem JNI libraries.
resources=eclipse.platform/resources/bundles
native=$resources/org.eclipse.core.filesystem/natives/unix
fragment=$resources/org.eclipse.core.filesystem.linux.x86_64/os/linux/x86_64
for dir in linux fastlinux; do
    make -C "$native/$dir" core OPT_FLAGS="$CFLAGS $LDFLAGS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"
done
install -m755 "$native/linux/libunixfile_1_0_0.so" "$native/fastlinux/libfastlinuxfile_1_0_0.so" "$fragment/"
%endif

export SWT_JAVA_HOME="$JAVA_HOME"
export OUTPUT_DIR="$PWD/eclipse.platform.swt/binaries/org.eclipse.swt.gtk.linux.%{_arch}"
# The upstream fragment contains binaries from the release builds.
rm -f "$OUTPUT_DIR"/libswt-*.so
(
    cd eclipse.platform.swt/bundles/org.eclipse.swt
    java -Dws=gtk build-scripts/CollectSources.java -nativeSources native
    sh native/build.sh -gtk3 install
)
test -f "$OUTPUT_DIR"/libswt-pi3-gtk-*.so
mvn -DskipTests package
test -x %{sdk_dir}/eclipse

%install
install -d %{buildroot}%{_libdir} %{buildroot}%{_bindir}
cp -a %{sdk_dir} %{buildroot}%{_libdir}/eclipse
ln -s %{_libdir}/eclipse/eclipse %{buildroot}%{_bindir}/eclipse
install -Dm644 products/icons/eclipse.xpm %{buildroot}%{_datadir}/pixmaps/eclipse.xpm
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE13}

%check
export JAVA_HOME=%{jdk_home}
export PATH="$JAVA_HOME/bin:$PATH"
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=$(cat .mvn/openruyi-extension/sdk-classpath)"
export GDK_BACKEND=x11
export DISPLAY=:77
Xvfb "$DISPLAY" -screen 0 1280x1024x24 -nolisten tcp &
xpid=$!
trap 'kill "$xpid" 2>/dev/null || :' EXIT
for attempt in $(seq 1 50); do
    test -S /tmp/.X11-unix/X77 && break
    kill -0 "$xpid" || exit 1
    sleep 0.1
done
test -S /tmp/.X11-unix/X77
dbus-run-session -- mvn verify
%ifarch x86_64
set -- %{buildroot}%{_libdir}/eclipse/plugins/org.eclipse.core.filesystem.linux.x86_64_*.jar
test "$#" -eq 1
test -f "$1"
mkdir -p filesystem-check
(cd filesystem-check && jar xf "$1" os/linux/x86_64)
native=eclipse.platform/resources/bundles/org.eclipse.core.filesystem/natives/unix
cmp "$native/linux/libunixfile_1_0_0.so" filesystem-check/os/linux/x86_64/libunixfile_1_0_0.so
cmp "$native/fastlinux/libfastlinuxfile_1_0_0.so" filesystem-check/os/linux/x86_64/libfastlinuxfile_1_0_0.so
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/eclipse.desktop

%files
%doc README.md
%license LICENSE NOTICE
%{_bindir}/eclipse
%{_libdir}/eclipse/
%{_datadir}/applications/eclipse.desktop
%{_datadir}/pixmaps/eclipse.xpm

%changelog
%autochangelog
