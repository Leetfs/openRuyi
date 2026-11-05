# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           commons-codec
Version:        1.23.0
Release:        %autorelease
Summary:        Encoders, decoders and digest utilities for Java
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://commons.apache.org/proper/commons-codec/
VCS:            git:https://github.com/apache/commons-codec.git
#!RemoteAsset:  sha256:24283dd892485465d6988a2e8ff5d6ea36ea8d35bff4afa07dfef20b8557939c
Source0:        https://downloads.apache.org/commons/codec/source/commons-codec-%{version}-src.tar.gz
# PureJavaCrc32C retains the Intel BSD-licensed implementation from Hadoop.
#!RemoteAsset:  sha256:2e8eb7f0de6c0df20e1b120e36e21518163109931f5278418975bac447b4b151
Source1:        https://raw.githubusercontent.com/apache/hadoop/rel/release-3.4.2/licenses/LICENSE-slicing-by-8.txt
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel

Requires:       java-25-openjdk-headless

%description
Commons Codec provides binary-to-text encodings, message digests, hashes
and phonetic encoders, including Base64, hexadecimal and XXHash32.

%prep
%autosetup -n commons-codec-%{version}-src
find . -type f -name '*.jar' -delete
cp %{SOURCE1} LICENSE-slicing-by-8.txt

%build
# Compile the library without resolving Maven plugins or downloading artifacts.
mkdir classes
find src/main/java -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -d classes @sources.list
cp -a src/main/resources/. classes/
cat > library.mf <<MANIFEST
Manifest-Version: 1.0
Implementation-Version: %{version}

MANIFEST
jar --create --file commons-codec.jar --manifest library.mf -C classes .

%install
install -Dpm644 commons-codec.jar %{buildroot}%{_datadir}/java/commons-codec.jar

%check
# Check RFC encoding/digest vectors and the streaming hash used by Compress.
# The separate upstream suite uses JUnit Jupiter and optional test extensions.
cat > CheckCodec.java <<'JAVA'
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import org.apache.commons.codec.binary.*;
import org.apache.commons.codec.digest.*;
import org.apache.commons.codec.language.Soundex;
import org.apache.commons.codec.language.bm.BeiderMorseEncoder;
public class CheckCodec {
    public static void main(String[] args) throws Exception {
        byte[] data = "foobar".getBytes(StandardCharsets.US_ASCII);
        if (!Base64.encodeBase64String(data).equals("Zm9vYmFy")
                || !Arrays.equals(data, Base64.decodeBase64("Zm9vYmFy"))
                || !Hex.encodeHexString(data).equals("666f6f626172"))
            throw new AssertionError("RFC 4648 encoding vectors");
        if (!DigestUtils.sha256Hex("abc").equals(
                "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"))
            throw new AssertionError("SHA-256 vector");
        byte[] key = new byte[20]; Arrays.fill(key, (byte) 11);
        if (!new HmacUtils(HmacAlgorithms.HMAC_SHA_256, key).hmacHex("Hi There").equals(
                "b0344c61d8db38535ca8afceaf0bf12b881dc200c9833da726e9376c2e32cff7"))
            throw new AssertionError("RFC 4231 HMAC vector");
        XXHash32 hash = new XXHash32();
        if (hash.getValue() != 0x02cc5d05L) throw new AssertionError("Empty XXHash32");
        byte[] abc = "abc".getBytes(StandardCharsets.US_ASCII);
        hash.update(abc, 0, 1); hash.update(abc, 1, 2);
        if (hash.getValue() != 0x32d153ffL) throw new AssertionError("Streaming XXHash32");
        if (!Soundex.US_ENGLISH.soundex("Robert").equals("R163")
                || new BeiderMorseEncoder().encode("Renault").isEmpty())
            throw new AssertionError("Phonetic encoders and their dictionaries");
    }
}
JAVA
javac --release 8 -cp commons-codec.jar CheckCodec.java
java -cp .:commons-codec.jar CheckCodec

%files
%license LICENSE.txt NOTICE.txt LICENSE-slicing-by-8.txt
%doc RELEASE-NOTES.txt
%{_datadir}/java/commons-codec.jar

%changelog
%autochangelog
