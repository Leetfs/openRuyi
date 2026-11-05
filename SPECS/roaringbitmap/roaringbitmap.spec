# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           roaringbitmap
Version:        1.6.28
Release:        %autorelease
Summary:        Compressed integer bitmap collections for Java
License:        Apache-2.0
URL:            https://github.com/RoaringBitmap/RoaringBitmap
VCS:            git:https://github.com/RoaringBitmap/RoaringBitmap.git
#!RemoteAsset:  sha256:363474beb5b4ae59646dc6725135433a7a62ea637b23b3d4f902fc53acf7261b
Source0:        https://github.com/RoaringBitmap/RoaringBitmap/archive/refs/tags/%{version}.tar.gz#/roaringbitmap-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel

%description
RoaringBitmap provides compressed integer sets with efficient set
operations, iteration and portable serialization for indexes.

%prep
%autosetup -n RoaringBitmap-%{version}

%build
mkdir classes java11
find roaringbitmap/src/main/java -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -d classes @sources.list
find roaringbitmap/src/java11/java -name '*.java' | sort > java11.list
javac --release 11 -encoding UTF-8 -cp classes -d java11 @java11.list
jar --create --file roaringbitmap.jar -C classes . --release 11 -C java11 .

%install
install -Dpm644 roaringbitmap.jar %{buildroot}%{_datadir}/java/roaringbitmap.jar

%check
# Check set intersection, unsigned values, cloning and serialized round trips.
# The full upstream suite requires JUnit Jupiter and parameterized test support.
cat > BitmapCheck.java <<'JAVA'
import java.io.*;
import org.roaringbitmap.RoaringBitmap;
class BitmapCheck {
    public static void main(String[] args) throws Exception {
        RoaringBitmap a=RoaringBitmap.bitmapOf(1,2,65536,-2);
        RoaringBitmap b=RoaringBitmap.bitmapOf(2,65536,1000);
        RoaringBitmap intersection=RoaringBitmap.and(a,b);
        if (!intersection.equals(RoaringBitmap.bitmapOf(2,65536)))
            throw new AssertionError("intersection");
        RoaringBitmap copy=a.clone(); copy.add(999);
        if (a.contains(999) || !a.contains(-2) || a.getCardinality()!=4)
            throw new AssertionError("clone or unsigned values");
        ByteArrayOutputStream bytes=new ByteArrayOutputStream();
        a.serialize(new DataOutputStream(bytes));
        RoaringBitmap restored=new RoaringBitmap();
        restored.deserialize(new DataInputStream(new ByteArrayInputStream(bytes.toByteArray())));
        if (!restored.equals(a) || restored.select(3)!=-2 || restored.rankLong(65536)!=3)
            throw new AssertionError("serialization or rank");
    }
}
JAVA
javac -cp roaringbitmap.jar BitmapCheck.java
java -cp .:roaringbitmap.jar BitmapCheck

%files
%license LICENSE LICENSE-2.0.txt
%doc README.md
%{_datadir}/java/roaringbitmap.jar

%changelog
%autochangelog
