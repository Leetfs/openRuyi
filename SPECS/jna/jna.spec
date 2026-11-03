# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bootstrap_java %{_datadir}/java/javapackages-bootstrap

Name:           jna
Version:        5.18.1
Release:        %autorelease
Summary:        Java access to native libraries
License:        Apache-2.0 OR LGPL-2.1-or-later
URL:            https://github.com/java-native-access/jna
VCS:            git:https://github.com/java-native-access/jna
#!RemoteAsset:  sha256:9af4d468a8b94def8c08761780766e919a0806d636b4c2ac55be0afe94cb8bb9
Source0:        https://github.com/java-native-access/jna/archive/refs/tags/%{version}.tar.gz
#!RemoteAsset:  sha256:98b62ae6ff280d747fb359fc42e48fed113d45bc3729a823dc30b8308a806645
Source1:        https://maven-central.storage-download.googleapis.com/maven2/net/java/dev/jna/jna/%{version}/jna-%{version}.pom
#!RemoteAsset:  sha256:39d538a9599a4474770838865ed42cfa3e6b3d13086cb1e577b8bb43148d1a65
Source2:        https://maven-central.storage-download.googleapis.com/maven2/net/java/dev/jna/jna-platform/%{version}/jna-platform-%{version}.pom
Source3:        JnaCheck.java
# Use the JUnit Platform scanner in the structure field order tests.
Patch2000:      2000-Discover-Structure-subclasses-with-the-JUnit-Platform.patch
# RISC-V passes floating-point unions through the integer argument registers.
Patch2001:      2001-Pass-floating-union-storage-in-integer-registers-on-RISC-V.patch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  binutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(x11)
BuildRequires:  python3
BuildRequires:  unzip
Provides:       mvn(net.java.dev.jna:jna) == %{version}
Provides:       mvn(net.java.dev.jna:jna-platform) == %{version}
Requires:       java-25-openjdk
Requires:       libffi

%description
Java Native Access calls native shared libraries and exposes their data
structures and callbacks to Java. The platform module provides mappings
for operating system APIs.

%prep
%autosetup -n jna-%{version} -p1
# Remove released Java bytecode and native libraries from upstream's build inputs.
find lib dist -type f \( -name '*.jar' -o -name '*.class' -o -name '*.aar' -o -name '*.so' -o -name '*.dll' -o -name '*.dylib' \) -delete
ln -s %{bootstrap_java}/ant.jar lib/ant.jar
ln -s %{bootstrap_java}/asm.jar lib/asm-8.0.1.jar
ln -s %{bootstrap_java}/junit.jar lib/junit.jar
ln -s %{bootstrap_java}/hamcrest-core.jar lib/hamcrest-core-1.3.jar
# JNI is loaded by its public library name, independent of the RPM build directory.
python3 - <<'PY'
from pathlib import Path
import xml.etree.ElementTree as E
makefile = Path("native/Makefile")
rules = makefile.read_text()
assert "-Wl,-soname,$@" in rules
makefile.write_text(rules.replace("-Wl,-soname,$@", "-Wl,-soname,$(notdir $@)"))
p=Path('build.xml'); tree=E.parse(p); native='linux-' + {'x86_64':'x86-64','i686':'x86'}.get('%{_arch}', '%{_arch}')
for parent in tree.iter():
    for item in list(parent):
        # Clover is only copied for an optional Java Web Start coverage archive.
        if item.tag == "copy" and item.get("file") == "lib/clover.jar" and item.get("todir") == "${build}/jws":
            parent.remove(item)
            continue
        archive=item.get('src','')
        if item.tag=='zipfileset' and archive.startswith('${lib.native}/') and archive!='${lib.native}/'+native+'.jar':
            parent.remove(item)
        if item.tag=='attribute' and item.get('name')=='Bundle-NativeCode':
            choices=[clause.strip() for clause in item.get('value').split(',') if '/'+native+'/' in clause]
            assert choices, native
            item.set('value',','.join(choices))
tree.write(p,encoding='utf-8',xml_declaration=True)
# The platform target selects Win32 CryptoAPI tests only on Windows.
# Its javac task otherwise compiles Crypt32Test with Windows-only PKIX fixtures on Linux.
platform = Path("contrib/platform/build.xml")
model = E.parse(platform)
target = next(item for item in model.findall("target") if item.get("name") == "compile-tests")
compiler = target.find(".//javac")
assert compiler is not None
E.SubElement(compiler, "exclude", {"name": "com/sun/jna/platform/win32/Crypt32Test.java"})
model.write(platform, encoding="utf-8", xml_declaration=True)
PY

%build
%set_build_flags
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
%{_libexecdir}/javapackages-bootstrap/ant -Dbuild-native=true -Ddynlink.native=true -Dcflags_extra.native="$CFLAGS" jar platform-jar

%install
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/maven-repository/net/java/dev/jna/jna/%{version}/jna-%{version}.pom
install -m644 build/jna.jar %{buildroot}%{_datadir}/maven-repository/net/java/dev/jna/jna/%{version}/jna-%{version}.jar
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/maven-repository/net/java/dev/jna/jna-platform/%{version}/jna-platform-%{version}.pom
install -m644 contrib/platform/dist/jna-platform.jar %{buildroot}%{_datadir}/maven-repository/net/java/dev/jna/jna-platform/%{version}/jna-platform-%{version}.jar
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>net.java.dev.jna</groupId><artifactId>jna</artifactId><version>%{version}</version><extension>jar</extension>
    <path>%{_datadir}/maven-repository/net/java/dev/jna/jna/%{version}/jna-%{version}.jar</path></artifact>
  <artifact><groupId>net.java.dev.jna</groupId><artifactId>jna</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/net/java/dev/jna/jna/%{version}/jna-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
  <artifact><groupId>net.java.dev.jna</groupId><artifactId>jna-platform</artifactId><version>%{version}</version><extension>jar</extension>
    <path>%{_datadir}/maven-repository/net/java/dev/jna/jna-platform/%{version}/jna-platform-%{version}.jar</path></artifact>
  <artifact><groupId>net.java.dev.jna</groupId><artifactId>jna-platform</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{_datadir}/maven-repository/net/java/dev/jna/jna-platform/%{version}/jna-platform-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
# Check the source-built JNI library, libc calls, and proxy/direct argument marshalling.
%set_build_flags
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
case "%{_arch}" in
    x86_64) native=linux-x86-64 ;;
    i686) native=linux-x86 ;;
    *) native=linux-%{_arch} ;;
esac
unzip -p build/jna.jar "com/sun/jna/$native/libjnidispatch.so" > build/checked-native.so
cmp "build/native-$native/libjnidispatch.so" build/checked-native.so
readelf -d build/checked-native.so | grep -F 'Library soname: [libjnidispatch.so]'
readelf -d build/checked-native.so | grep -F 'Shared library: [libffi.so.'
test "$(jar tf build/jna.jar | grep -Ec '/(libjnidispatch\.(so|dylib|a)|jnidispatch\.dll)$')" -eq 1
java -ea -cp 'build/jna.jar:contrib/platform/dist/jna-platform.jar' %{SOURCE3}
ln -s %{bootstrap_java}/junit-platform-commons.jar %{bootstrap_java}/apiguardian-api.jar lib/test/
%{_libexecdir}/javapackages-bootstrap/ant -Dbuild-native=true -Ddynlink.native=true -Dcflags_extra.native="$CFLAGS" \
    -lib '%{bootstrap_java}/ant-junit.jar:%{bootstrap_java}/ant-junit4.jar:%{bootstrap_java}/junit.jar:%{bootstrap_java}/hamcrest-core.jar' test test-platform

%files
%license LICENSE AL2.0 LGPL2.1
%{_datadir}/maven-metadata/jna.xml
%{_datadir}/maven-repository/net/java/dev/jna/jna/
%{_datadir}/maven-repository/net/java/dev/jna/jna-platform/

%changelog
%autochangelog
