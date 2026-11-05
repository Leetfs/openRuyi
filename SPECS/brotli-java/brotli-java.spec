# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit db24a98aed38a16de78cc05ca15cdd8dc2a0d92d

Name:           brotli-java
Version:        1.2.1
Release:        %autorelease
Summary:        Pure Java decoder for Brotli compressed streams
License:        MIT
URL:            https://github.com/google/brotli
VCS:            git:https://github.com/google/brotli.git
# The release archive excludes java/ through export-ignore; use the release commit.
#!RemoteAsset:  git+https://github.com/google/brotli.git#%{commit}
#!CreateArchive
Source0:        brotli-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4

Requires:       java-25-openjdk-headless

%description
This package provides the pure Java Brotli decoder, including the
BrotliInputStream API used by Apache Commons Compress.

%prep
%autosetup -n brotli-%{version}
find . -type f -name '*.jar' -delete

%build
# Compile the standalone decoder module, following its upstream Maven includes.
mkdir classes
find java/org/brotli/dec -maxdepth 1 -name '*.java' ! -name '*Test*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -d classes @sources.list
jar --create --file brotli-dec.jar -C classes .

%install
install -Dpm644 brotli-dec.jar %{buildroot}%{_datadir}/java/brotli-dec.jar

%check
# Run the decoder module's default upstream test set with assertions enabled.
# Its Maven build excludes SetDictionaryTest: that test requires a build without
# the embedded dictionary plus an external RFC_DICTIONARY file.
mkdir test-classes
find java/org/brotli/dec -maxdepth 1 -name '*Test*.java' ! -name SetDictionaryTest.java | sort > tests.list
deps=brotli-dec.jar:%{_datadir}/java/junit4.jar:%{_datadir}/java/hamcrest1.3/hamcrest-core.jar
javac --release 8 -encoding UTF-8 -cp "$deps" -d test-classes @tests.list
tests=$(find java/org/brotli/dec -maxdepth 1 -name '*Test.java' ! -name SetDictionaryTest.java \
    -printf 'org.brotli.dec.%f\n' | sed 's/\.java$//' | sort)
java -ea -DBROTLI_ENABLE_ASSERTS=true -cp "test-classes:$deps" org.junit.runner.JUnitCore $tests

%files
%license LICENSE
%doc README.md
%{_datadir}/java/brotli-dec.jar

%changelog
%autochangelog
