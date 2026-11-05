# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           commons-compress
Version:        1.28.0
Release:        %autorelease
Summary:        Java archive and compression stream library
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-compress/
VCS:            git:https://github.com/apache/commons-compress.git
#!RemoteAsset:  sha256:5c870fa454221b24c81d10a28031a9183d55f2baab92c160ecc985e51a387662
Source0:        https://downloads.apache.org/commons/compress/source/commons-compress-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  commons-io
BuildRequires:  commons-lang3
BuildRequires:  commons-codec
BuildRequires:  objectweb-asm
BuildRequires:  xz-java
BuildRequires:  brotli-java
BuildRequires:  zstd-jni

Requires:       commons-io
Requires:       commons-lang3
Requires:       commons-codec
Requires:       objectweb-asm
Requires:       xz-java
Requires:       brotli-java
Requires:       zstd-jni

%description
Apache Commons Compress reads and writes archive and compression formats,
including ZIP, TAR, CPIO, BZip2, XZ, Brotli and Zstandard. The external
compression backends are supplied by separate system packages.

%prep
%autosetup -n commons-compress-%{version}-src

%build
deps=%{_datadir}/java/commons-codec.jar:%{_datadir}/java/brotli-dec.jar:%{_datadir}/java/zstd-jni.jar
for artifact in commons-io/commons-io org/apache/commons/commons-lang3 org/ow2/asm/asm org/tukaani/xz; do
    jar=$(find %{_datadir}/maven-repository/"$artifact" -name '*.jar' -print -quit)
    test -n "$jar"
    deps="$deps:$jar"
done
printf '%s\n' "$deps" > dependencies.classpath
mkdir classes
find src/main/java -name '*.java' ! -name module-info.java | sort > sources.list
javac --release 8 -encoding UTF-8 -cp "$deps" -d classes @sources.list
cp -a src/main/resources/. classes/
cat > compress.mf <<MANIFEST
Manifest-Version: 1.0
Automatic-Module-Name: org.apache.commons.compress

MANIFEST
jar --create --file commons-compress.jar --manifest compress.mf -C classes .

%install
install -Dpm644 commons-compress.jar %{buildroot}%{_datadir}/java/commons-compress.jar

%check
# Exercise ZIP entry handling and the built-in and packaged compression backends.
# The full upstream suite also requires JUnit Jupiter, Mockito and generated fixtures.
cat > CompressCheck.java <<'JAVA'
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import org.apache.commons.compress.archivers.zip.*;
import org.apache.commons.compress.compressors.*;
class CompressCheck {
    public static void main(String[] args) throws Exception {
        byte[] data="OpenDocument package compression\n".repeat(1000).getBytes(StandardCharsets.UTF_8);
        ByteArrayOutputStream zipped=new ByteArrayOutputStream();
        try (ZipArchiveOutputStream out=new ZipArchiveOutputStream(zipped)) {
            out.putArchiveEntry(new ZipArchiveEntry("content.xml"));
            out.write(data); out.closeArchiveEntry();
        }
        try (ZipArchiveInputStream in=new ZipArchiveInputStream(new ByteArrayInputStream(zipped.toByteArray()))) {
            if (!"content.xml".equals(in.getNextEntry().getName()) || !Arrays.equals(data,in.readAllBytes())
                || in.getNextEntry()!=null) throw new AssertionError("ZIP entry round trip");
        }
        CompressorStreamFactory factory=new CompressorStreamFactory();
        for (String format : new String[]{"gz","bzip2","xz","zstd","snappy-framed","lz4-framed"}) {
            ByteArrayOutputStream bytes=new ByteArrayOutputStream();
            try (OutputStream out=factory.createCompressorOutputStream(format,bytes)) { out.write(data); }
            try (InputStream in=factory.createCompressorInputStream(format,new ByteArrayInputStream(bytes.toByteArray()))) {
                if (!Arrays.equals(data,in.readAllBytes())) throw new AssertionError(format);
            }
        }
        System.out.println("ZIP and six compression backend round trips passed");
    }
}
JAVA
deps="commons-compress.jar:$(cat dependencies.classpath)"
javac -cp "$deps" CompressCheck.java
java --enable-native-access=ALL-UNNAMED -cp ".:$deps" CompressCheck

%files
%license LICENSE.txt NOTICE.txt
%doc README.md
%{_datadir}/java/commons-compress.jar

%changelog
%autochangelog
