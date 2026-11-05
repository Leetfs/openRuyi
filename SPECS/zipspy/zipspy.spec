# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           zipspy
Version:        0.1.0
Release:        %autorelease
Summary:        Inspect ZIP headers and directory records in document containers
License:        MPL-1.1
URL:            https://code.google.com/archive/p/zipspy/
# VCS: No VCS link available
#!RemoteAsset:  sha256:42b01e7fec44b001874881ee45a8d6fe5f7928993263fafc24f6c9fed9b92c6e
Source0:        https://storage.googleapis.com/google-code-archive-source/v2/code.google.com/%{name}/source-archive.zip#/%{name}-%{version}.zip
#!RemoteAsset:  sha256:f849fc26a7a99981611a3a370e83078deb617d12a45776d6c4cada4d338be469
Source1:        https://www.mozilla.org/media/MPL/1.1/index.0c5913925d40.txt#/MPL-1.1.txt
# The archived workbook contains fifteen local and central ZIP headers.
# https://code.google.com/archive/p/zipspy/source/default/source
Patch2000:      2000-correct-test-workbook-entry-count.patch
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4
BuildRequires:  slf4j-log4j
BuildRequires:  slf4j-jdk14
BuildRequires:  unzip
Requires:       slf4j-log4j

%description
ZipSpy reads local file headers and central directory records from ZIP
archives. Document validators use it to check the structure of OOXML and
other ZIP-based formats and report discrepancies between the two records.

%prep
%setup -q -c -T
# Extract the original sources and test workbook from the archived Subversion trunk.
unzip -q %{SOURCE0} 'zipspy/trunk/src/*.java' 'zipspy/trunk/etc/testdata/maria.xlsx'
ziptest=zipspy/trunk/src/org/xmlopen/zipspy/ZipArchiveTest.java
sed -i 's/\r$//' "$ziptest"
%patch -P 2000 -p1
cp -p %{SOURCE1} MPL-1.1.txt

%build
mkdir classes
find zipspy/trunk/src -name '*.java' ! -name '*Test.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -cp %{_datadir}/java/log4j-over-slf4j.jar -d classes @sources.list
printf 'Main-Class: org.xmlopen.zipspy.Driver\nClass-Path: log4j-over-slf4j.jar\n' > manifest.mf
jar --create --file zipspy.jar --manifest manifest.mf -C classes .

%install
install -Dpm644 zipspy.jar %{buildroot}%{_datadir}/java/zipspy.jar

%check
# Run upstream's ZIP header and central-directory assertions on the XLSX fixture.
cp=$PWD/zipspy.jar:%{_datadir}/java/log4j-over-slf4j.jar:%{_datadir}/java/slf4j-jdk14.jar:%{_datadir}/java/junit4.jar
mkdir tests
javac --release 8 -encoding UTF-8 -cp "$cp" -d tests zipspy/trunk/src/org/xmlopen/zipspy/ZipArchiveTest.java
(cd zipspy/trunk && java -cp "$OLDPWD/tests:$cp" org.junit.runner.JUnitCore org.xmlopen.zipspy.ZipArchiveTest)

%files
%license MPL-1.1.txt
%{_datadir}/java/zipspy.jar

%changelog
%autochangelog
