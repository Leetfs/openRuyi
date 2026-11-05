# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global upstream_version 1.5.7-24

Name:           zstd-jni
Version:        1.5.7.24
Release:        %autorelease
Summary:        Zstandard compression bindings for Java
License:        BSD-2-Clause
URL:            https://github.com/luben/zstd-jni
VCS:            git:https://github.com/luben/zstd-jni.git
#!RemoteAsset:  sha256:b360090aadb4f60256215cdc48678ba0e2b2fd0e3c8f4a72465d1918b2f772f7
Source0:        %{url}/archive/refs/tags/v%{upstream_version}.tar.gz#/%{name}-%{upstream_version}.tar.gz

BuildRequires:  java-25-openjdk-devel
BuildRequires:  jetbrains-annotations
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconf
BuildRequires:  binutils

%description
Zstd JNI supplies byte-array, direct-buffer and streaming Java access to
Zstandard compression. The native binding uses the system zstd library.
The multi-release JAR also includes the upstream Foreign Function and
Memory API implementation for Java 22 and later.

%prep
%autosetup -n %{name}-%{upstream_version}
# The binding must compile against the same public headers as the system library.
rm src/main/native/zstd.h src/main/native/zstd_errors.h src/main/native/zdict.h

%build
mkdir classes java22
cat > src/main/java/com/github/luben/zstd/util/ZstdVersion.java <<'JAVA'
package com.github.luben.zstd.util;
public class ZstdVersion {
    public static final String VERSION = "%{upstream_version}";
}
JAVA
find src/main/java -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -cp %{_datadir}/java/jetbrains-annotations.jar -d classes @sources.list
find src/main/java22 -name '*.java' | sort > java22.list
javac --release 22 -encoding UTF-8 -cp classes:%{_datadir}/java/jetbrains-annotations.jar -d java22 @java22.list
cat > zstd.mf <<MANIFEST
Manifest-Version: 1.0
Automatic-Module-Name: com.github.luben.zstd_jni

MANIFEST
jar --create --file zstd-jni.jar --manifest zstd.mf -C classes . --release 22 -C java22 .
%{__cc} %{build_cflags} -std=c99 -fPIC -shared %{build_ldflags} \
    -Wl,-soname,libzstd-jni-%{upstream_version}.so -Wl,-z,defs \
    -I%{_libdir}/jvm/java-25-openjdk/include \
    -I%{_libdir}/jvm/java-25-openjdk/include/linux \
    src/main/native/*.c $(pkg-config --cflags --libs libzstd) -pthread \
    -o libzstd-jni-%{upstream_version}.so

%install
install -Dpm644 zstd-jni.jar %{buildroot}%{_datadir}/java/zstd-jni.jar
install -Dpm755 libzstd-jni-%{upstream_version}.so %{buildroot}%{_libdir}/libzstd-jni-%{upstream_version}.so

%check
# Confirm that the JNI binding links to the system compression library.
readelf -d libzstd-jni-%{upstream_version}.so | grep 'Shared library: \[libzstd.so.1\]'
# Exercise both multi-release implementations with arrays, direct buffers and streams.
# The upstream SBT suite requires ScalaTest and ScalaCheck.
cat > ZstdCheck.java <<'JAVA'
import com.github.luben.zstd.*;
import java.io.*;
import java.nio.ByteBuffer;
import java.util.Arrays;
class ZstdCheck {
    public static void main(String[] args) throws Exception {
        byte[] source=new byte[128*1024];
        for (int i=0;i<source.length;i++) source[i]=(byte)(i*31);
        byte[] packed=Zstd.compress(source,3);
        if (!Arrays.equals(source,Zstd.decompress(packed,source.length)))
            throw new AssertionError("array round trip");
        ByteArrayOutputStream bytes=new ByteArrayOutputStream();
        try (ZstdOutputStream out=new ZstdOutputStream(bytes)) { out.write(source); }
        try (ZstdInputStream in=new ZstdInputStream(new ByteArrayInputStream(bytes.toByteArray()))) {
            if (!Arrays.equals(source,in.readAllBytes())) throw new AssertionError("stream round trip");
        }
        ByteBuffer input=ByteBuffer.allocateDirect(source.length);
        input.put(source).flip();
        ByteBuffer compressed=ByteBuffer.allocateDirect((int)Zstd.compressBound(source.length));
        Zstd.compress(compressed,input,3);
        compressed.flip();
        ByteBuffer restored=ByteBuffer.allocateDirect(source.length);
        Zstd.decompress(restored,compressed);
        restored.flip();
        byte[] result=new byte[restored.remaining()]; restored.get(result);
        if (!Arrays.equals(source,result)) throw new AssertionError("direct buffer round trip");
        boolean rejected=false;
        try (ZstdDictDecompress invalid=new ZstdDictDecompress(new byte[8],-1,4)) {}
        catch (IllegalArgumentException expected) { rejected=true; }
        if (!rejected) throw new AssertionError("dictionary bounds");
        System.out.println("Zstd arrays, streams, buffers and dictionary bounds passed");
    }
}
JAVA
javac -cp zstd-jni.jar ZstdCheck.java
java --enable-native-access=ALL-UNNAMED -Djava.library.path="$PWD" -cp .:zstd-jni.jar ZstdCheck
java --enable-native-access=ALL-UNNAMED -Xcheck:jni -Djdk.util.jar.enableMultiRelease=false \
    -Djava.library.path="$PWD" -cp .:zstd-jni.jar ZstdCheck

%files
%license LICENSE
%doc README.md
%{_datadir}/java/zstd-jni.jar
%{_libdir}/libzstd-jni-%{upstream_version}.so

%changelog
%autochangelog
