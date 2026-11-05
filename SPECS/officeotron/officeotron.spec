# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit 81b91b821b019937b4bfb3f15efd88fa17da9985

Name:           officeotron
Version:        0.8.8
Release:        %autorelease
Summary:        Office Open XML document validator
License:        MPL-1.1 AND LicenseRef-openRuyi-ECMA-Text AND CC-BY-3.0 AND W3C-19980720
URL:            https://git.libreoffice.org/officeotron
VCS:            git:https://git.libreoffice.org/officeotron
#!RemoteAsset:  git+https://git.libreoffice.org/officeotron#%{commit}
#!CreateArchive
Source0:        officeotron-%{version}.tar.gz
#!RemoteAsset:  sha256:f849fc26a7a99981611a3a370e83078deb617d12a45776d6c4cada4d338be469
Source1:        https://www.mozilla.org/media/MPL/1.1/index.0c5913925d40.txt#/MPL-1.1.txt
#!RemoteAsset:  sha256:652933d8a76844f74d72107eed9c45dd7c44c0482be7a0e928b2dde6f1f4fd5e
Source2:        https://ecma-international.org/wp-content/uploads/Ecma_text_copyright_policy_version_1.pdf#/ECMA-Text.pdf
#!RemoteAsset:  sha256:e6bc9e9c474700b708f568bac9e5a8a9bcb2b1dad53442f5ba449fcb848b8e76
Source3:        https://creativecommons.org/licenses/by/3.0/legalcode.txt#/CC-BY-3.0.txt
#!RemoteAsset:  sha256:d4eedcb04dc16687b6d56b49ed06e1b55f599b8bd8e518af9773d1b7d2cf5c76
Source4:        https://www.w3.org/Consortium/Legal/copyright-software-19980720#/W3C-19980720.html
Source5:        schema-licenses.md
# Downstream fix for an independently packaged logging provider.
# https://git.libreoffice.org/officeotron/+/81b91b821b019937b4bfb3f15efd88fa17da9985/src/org/probatron/officeotron/Driver.java
Patch2000:      2000-report-the-application-version.patch
# Downstream inclusion of the W3C software license's required attribution.
# https://www.w3.org/Consortium/Legal/copyright-software-19980720
Patch2001:      2001-include-w3c-schema-attribution.patch
# Downstream test fixes for implicit namespaces and a non-counting mock report.
# https://git.libreoffice.org/officeotron/+/81b91b821b019937b4bfb3f15efd88fa17da9985/src/org/probatron/officeotron/
Patch2002:      2002-correct-the-validation-test-fixtures.patch
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  jing
BuildRequires:  junit4
BuildRequires:  slf4j-jdk14
BuildRequires:  slf4j-log4j
BuildRequires:  xerces-j2
BuildRequires:  zipspy

Requires:       java-25-openjdk-headless
Requires:       jing
Requires:       slf4j-jdk14
Requires:       slf4j-log4j
Requires:       xerces-j2
Requires:       zipspy

%description
Officeotron checks Office Open XML documents for package integrity and
schema conformance. This package provides the command-line validator
used to check document exports, with separately packaged Java libraries.

%prep
%autosetup -N
# Normalize upstream CRLF files before applying the source patches.
sed -i 's/\r$//' src/org/probatron/officeotron/Driver.java \
    etc/schema/others/xml.xsd etc/schema/others/XMLSchema.dtd \
    etc/schema/others/datatypes.dtd
sed -i 's/\r$//' src/org/probatron/officeotron/MceXmlFilterTest.java \
    src/org/probatron/officeotron/OOXMLValidationSessionTest.java
%autopatch -p1
find . -type f -name '*.jar' -delete
cp %{SOURCE1} MPL-1.1.txt
cp %{SOURCE2} ECMA-Text.pdf
cp %{SOURCE3} CC-BY-3.0.txt
cp %{SOURCE4} W3C-19980720.html
cp %{SOURCE5} schema-licenses.md

%build
# The upstream Ant application target also compiles the servlet and embeds
# third-party JARs. Compile the command-line entry point and its actual imports.
mkdir classes
deps=%{_datadir}/java/jing.jar:%{_datadir}/java/zipspy.jar:%{_datadir}/java/log4j-over-slf4j.jar
javac --release 8 -encoding UTF-8 -cp "$deps" -sourcepath src \
    -d classes src/org/probatron/officeotron/Driver.java
cp -a etc/schema classes/
find classes/schema -type f ! -name '*.xsd' ! -name '*.dtd' -delete
# Embed attribution with the schema resources as well as installing the licenses.
cp schema-licenses.md classes/schema/
cat > officeotron.mf <<MANIFEST
Manifest-Version: 1.0
Main-Class: org.probatron.officeotron.Driver
Implementation-Version: %{version}
Class-Path: jing.jar zipspy.jar log4j-over-slf4j.jar slf4j-jdk14.jar
  xercesImpl.jar

MANIFEST
jar --create --file officeotron.jar --manifest officeotron.mf -C classes .

%install
install -Dpm644 officeotron.jar %{buildroot}%{_datadir}/java/officeotron.jar
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/officeotron <<'SH'
#!/bin/sh
exec java -jar /usr/share/java/officeotron.jar "$@"
SH
chmod 755 %{buildroot}%{_bindir}/officeotron

%check
# Run all four upstream JUnit test classes using the packaged libraries.
deps=officeotron.jar:%{_datadir}/java/jing.jar:%{_datadir}/java/zipspy.jar:%{_datadir}/java/log4j-over-slf4j.jar:%{_datadir}/java/slf4j-jdk14.jar:%{_datadir}/java/xercesImpl.jar:%{_datadir}/java/junit4.jar:%{_datadir}/java/hamcrest1.3/hamcrest-core.jar
mkdir test-classes
find src -name '*Test.java' | sort > tests.list
javac --release 8 -encoding UTF-8 -cp "$deps" -d test-classes @tests.list
tests=$(sed -e 's|^src/||' -e 's|/|.|g' -e 's|\.java$||' tests.list)
java -cp "test-classes:$deps" org.junit.runner.JUnitCore $tests
# Check the installed JAR manifest, version and valid/invalid OOXML fixtures.
for jar in jing zipspy log4j-over-slf4j slf4j-jdk14 xercesImpl; do
    ln -s %{_datadir}/java/"$jar".jar "$jar".jar
done
test "$(java -jar officeotron.jar --version)" = "%{version}"
for doc in Book1.xlsx Presentation1.pptx; do
    java -jar officeotron.jar --errors-only "etc/test-data/$doc" > "$doc.log" 2>&1
    if grep -E 'ERROR|Exception|SEVERE' "$doc.log"; then
        exit 1
    fi
done
# Upstream returns zero on validation errors; check the diagnostic itself.
java -jar officeotron.jar --errors-only etc/test-data/maria.xlsx > invalid.log 2>&1
grep -E "ERROR.*cvc-complex-type.*foo" invalid.log

%files
%license MPL-1.1.txt ECMA-Text.pdf CC-BY-3.0.txt W3C-19980720.html schema-licenses.md
%{_bindir}/officeotron
%{_datadir}/java/officeotron.jar

%changelog
%autochangelog
