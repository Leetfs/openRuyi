# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global maven_version 1.5.7-6
%global repo %{_datadir}/maven-repository/com/github/luben/zstd-jni/%{maven_version}
Name:           zstd-jni
Version:        1.5.7.6
Release:        %autorelease
Summary:        Java bindings for Zstandard compression
License:        BSD-2-Clause
URL:            https://github.com/luben/zstd-jni
VCS:            git:https://github.com/luben/zstd-jni
#!RemoteAsset:  sha256:ff3a5989d1e0f0b51aa3087e276080be97679d0ace64c6f9c195116a5fcd6d28
Source0:        https://github.com/luben/zstd-jni/archive/refs/tags/v%{maven_version}.tar.gz?/zstd-jni-%{maven_version}.tar.gz
#!RemoteAsset:  sha256:794d9b995ed59165c54243dcc73fe9483d7fe1af7fb80fcd89a5ae5b693f3eb7
Source1:        https://maven-central.storage-download.googleapis.com/maven2/com/github/luben/zstd-jni/%{maven_version}/zstd-jni-%{maven_version}.pom
Source2:        CheckZstd.java
Patch0:         0001-use-system-zstd-trainer.patch
BuildRequires:  gcc
BuildRequires:  java-25-openjdk-devel
BuildRequires:  pkgconfig(libzstd) >= 1.5.7
Provides:       mvn(com.github.luben:zstd-jni) == %{maven_version}
Requires:       java-25-openjdk
Requires:       zstd >= 1.5.7

%description
Java APIs for Zstandard compression, streaming and dictionary training.
The native bindings use the distribution's shared Zstandard library.

%prep
%autosetup -p1 -n zstd-jni-%{maven_version}
test "$(cat version)" = "%{maven_version}"

%build
%set_build_flags
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
mkdir -p target/{classes,generated/com/github/luben/zstd/util}
# Generate the version class with the upstream build.sbt source-generator format.
printf 'package com.github.luben.zstd.util;\npublic class ZstdVersion { public static final String VERSION = "%%s"; }\n' \
    '%{maven_version}' > target/generated/com/github/luben/zstd/util/ZstdVersion.java
find src/main/java target/generated -name '*.java' | sort > target/sources
javac --release 8 -g -proc:none -d target/classes @target/sources
gcc $CFLAGS -fPIC -fvisibility=hidden -DZSTD_MULTITHREAD=1 -shared $LDFLAGS -Wl,-z,defs \
    -Wl,--version-script="$PWD/libzstd-jni.so.map" \
    -I"$JAVA_HOME/include" -I"$JAVA_HOME/include/linux" src/main/native/jni*.c \
    -o target/libzstd-jni-%{maven_version}.so $(pkg-config --cflags --libs libzstd) -lpthread
meta=target/classes/META-INF/maven/com.github.luben/zstd-jni
mkdir -p "$meta"
cp %{SOURCE1} "$meta/pom.xml"
printf 'groupId=com.github.luben\nartifactId=zstd-jni\nversion=%%s\n' '%{maven_version}' > "$meta/pom.properties"
cp LICENSE target/classes/META-INF/
jar cf target/zstd-jni-%{maven_version}.jar -C target/classes .

%install
install -Dm755 target/libzstd-jni-%{maven_version}.so %{buildroot}%{_libdir}/libzstd-jni-%{maven_version}.so
install -Dm644 target/zstd-jni-%{maven_version}.jar %{buildroot}%{repo}/zstd-jni-%{maven_version}.jar
install -m644 %{SOURCE1} %{buildroot}%{repo}/zstd-jni-%{maven_version}.pom
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
<artifact><groupId>com.github.luben</groupId><artifactId>zstd-jni</artifactId><version>%{maven_version}</version><extension>jar</extension><path>%{repo}/zstd-jni-%{maven_version}.jar</path><compatVersions><version>%{maven_version}</version></compatVersions></artifact>
<artifact><groupId>com.github.luben</groupId><artifactId>zstd-jni</artifactId><version>%{maven_version}</version><extension>pom</extension><path>%{repo}/zstd-jni-%{maven_version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{maven_version}</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
mkdir target/tests
javac --release 17 -cp target/zstd-jni-%{maven_version}.jar -d target/tests %{SOURCE2}
# Exercise the JNI APIs and upstream compressed fixtures on the target architecture.
java --enable-native-access=ALL-UNNAMED -Djava.library.path="$PWD/target" \
    -cp target/tests:target/zstd-jni-%{maven_version}.jar CheckZstd "$PWD/src/test/resources"
readelf -d target/libzstd-jni-%{maven_version}.so | grep -F 'Shared library: [libzstd.so.1]'

%files
%license LICENSE
%{_libdir}/libzstd-jni-%{maven_version}.so
%{repo}/
%{_datadir}/maven-metadata/zstd-jni.xml

%changelog
%autochangelog
