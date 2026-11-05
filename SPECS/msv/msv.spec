# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           msv
Version:        2022.7
Release:        %autorelease
Summary:        Validate XML documents against multiple schema languages
License:        Apache-2.0 AND BSD-3-Clause AND BSD-3-Clause-Sun
URL:            https://github.com/xmlark/msv
VCS:            git:https://github.com/xmlark/msv.git
#!RemoteAsset:  sha256:8b1279458c32580f17116bcd0af87ec583279bfa00276248f180118cdc823e3e
Source0:        https://github.com/xmlark/msv/archive/refs/tags/msv-%{version}.tar.gz#/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  isorelax
BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4
BuildRequires:  relaxng-datatype
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-resolver
Requires:       %{name}-xsdlib = %{version}-%{release}
Requires:       isorelax
Requires:       java-25-openjdk-headless
Requires:       xerces-j2
Requires:       xml-commons-resolver

%description
The Multi-Schema XML Validator reads RELAX NG, W3C XML Schema and other
schema languages. It provides a command-line validator and a JARV
implementation for applications that validate XML through Java.

%package        xsdlib
Summary:        XML Schema datatype library for Java
License:        Apache-1.1 AND BSD-3-Clause AND BSD-3-Clause-Sun
Requires:       relaxng-datatype

%description    xsdlib
The datatype library provides XML Schema simple types, facets and
regular expressions. RELAX NG processors can discover it through the
datatype library service interface.

%prep
%autosetup -n msv-msv-%{version}
cp -p %{SOURCE1} Apache-2.0.txt
# The Oracle BSD notice is distributed as a full header in each module.
sed -n '1,/^ \*\//p' msv/src/main/java/com/sun/msv/util/LightStack.java | sed '1d;$d;s/^ \* \{0,1\}//' > Oracle-BSD.txt

%build
mkdir -p build/xsd build/core
cp=%{_datadir}/java/relaxngDatatype.jar:%{_datadir}/java/xercesImpl.jar
find xsdlib/src/main/java -name '*.java' | sort > xsd.list
javac --release 8 -encoding UTF-8 -cp "$cp" -d build/xsd @xsd.list
jar --create --file xsdlib.jar -C build/xsd . -C xsdlib/src/main/resources .
cp=$cp:xsdlib.jar:%{_datadir}/java/isorelax.jar:%{_datadir}/java/xml-resolver.jar
find msv/src/main/java -name '*.java' | sort > core.list
javac --release 8 -encoding UTF-8 -cp "$cp" -d build/core @core.list
printf 'Main-Class: com.sun.msv.driver.textui.Driver\nClass-Path: xsdlib.jar isorelax.jar relaxngDatatype.jar xercesImpl.jar xml-resolver.jar\n' > manifest.mf
mkdir -p build/core/META-INF/services
echo com.sun.msv.verifier.jarv.FactoryLoaderImpl > build/core/META-INF/services/org.iso_relax.verifier.VerifierFactoryLoader
jar --create --file msv-core.jar --manifest manifest.mf -C build/core . -C msv/src/main/resources .

%install
install -Dpm644 msv-core.jar %{buildroot}%{_datadir}/java/msv-core.jar
install -Dpm644 xsdlib.jar %{buildroot}%{_datadir}/java/xsdlib.jar
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/msv <<'SH'
#!/bin/sh
exec java -jar %{_datadir}/java/msv-core.jar "$@"
SH
chmod 0755 %{buildroot}%{_bindir}/msv

%check
cp=msv-core.jar:xsdlib.jar:%{_datadir}/java/relaxngDatatype.jar:%{_datadir}/java/isorelax.jar:%{_datadir}/java/xercesImpl.jar:%{_datadir}/java/xml-resolver.jar
mkdir tests
testcp=$cp:%{_datadir}/java/junit4.jar
javac --release 8 -cp "$testcp" -sourcepath msv/src/test/java:xsdlib/src/test/java -d tests \
    xsdlib/src/test/java/com/sun/msv/datatype/xsd/{AnyURITypeTest,WhiteSpaceProcessorTest}.java \
    msv/src/test/java/com/sun/msv/util/StringPairTest.java \
    msv/src/test/java/com/sun/msv/verifier/identity/IDConstraintCheckerTest.java
java -cp "tests:$testcp" org.junit.runner.JUnitCore \
    com.sun.msv.datatype.xsd.AnyURITypeTest com.sun.msv.datatype.xsd.WhiteSpaceProcessorTest \
    com.sun.msv.util.StringPairTest com.sun.msv.verifier.identity.IDConstraintCheckerTest
echo '<element name="item" xmlns="http://relaxng.org/ns/structure/1.0"><empty/></element>' > schema.rng
echo '<item/>' > good.xml
echo '<wrong/>' > bad.xml
java -cp "$cp" com.sun.msv.driver.textui.Driver schema.rng good.xml
if java -cp "$cp" com.sun.msv.driver.textui.Driver schema.rng bad.xml > errors.log; then
    exit 1
fi
grep -F 'the document is NOT valid' errors.log

%files
%license docs/core/license.txt Oracle-BSD.txt Apache-2.0.txt
%{_bindir}/msv
%{_datadir}/java/msv-core.jar

%files xsdlib
%license docs/xsdlib/license.txt docs/xsdlib/Apache-LICENSE-1.1.txt Oracle-BSD.txt
%{_datadir}/java/xsdlib.jar

%changelog
%autochangelog
