# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global doc_commit 1fc8c8d337c2c75b6b15b281f2c69e86110e475f

Name:           jing
Version:        20241231
Release:        %autorelease
Summary:        RELAX NG and Schematron validator for Java
License:        BSD-3-Clause AND ISO-permission AND Unicode-3.0
URL:            https://relaxng.org/jclark/jing.html
VCS:            git:https://github.com/relaxng/jing-trang.git
#!RemoteAsset:  sha256:d2c2e2f481ed36fc65d10969c53ba8535d51b7617b505dffcab1293e38b867e9
Source0:        https://github.com/relaxng/jing-trang/archive/refs/tags/V%{version}.tar.gz#/jing-trang-V%{version}.tar.gz
#!RemoteAsset:  sha256:3846c67ec9762188b2b1d66ccff8f4e7333f8e9e126e262d0c02797ef5e089df
Source1:        https://github.com/relaxng/relaxng.org/archive/%{doc_commit}.tar.gz#/relaxng.org-%{doc_commit}.tar.gz
#!RemoteAsset:  sha256:e7a93b009565cfce55919a381437ac4db883e9da2126fa28b91d12732bc53d96
Source2:        https://www.unicode.org/license.txt#/Unicode-LICENSE.txt
# Downstream offline build using the standalone datatype API and TestNG Ant task.
# https://github.com/relaxng/jing-trang/blob/V20241231/build.xsl
Patch2000:      2000-use-system-libraries-in-offline-ant-builds.patch
# Downstream compatibility with the configured net.sf.saxon transformer.
# https://github.com/relaxng/jing-trang/blob/V20241231/test/saxon.xsl
Patch2001:      2001-generate-test-fixtures-with-xslt-2.patch
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  isorelax
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javacc
BuildRequires:  relaxng-datatype
BuildRequires:  saxon-he
BuildRequires:  testng-ant
BuildRequires:  xalan-j2-interpretive
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-resolver

Requires:       isorelax
Requires:       java-25-openjdk-headless
Requires:       relaxng-datatype
Requires:       saxon-he
Requires:       xalan-j2-interpretive
Requires:       xerces-j2
Requires:       xml-commons-resolver

%description
Jing validates XML documents against RELAX NG schemas in XML or compact
syntax. It also supports Schematron, NVDL and W3C XML Schema through its
Java API, Ant task and command-line interface.

%prep
%autosetup -n jing-trang-%{version} -p1
# The upstream build copies this pinned submodule into its documentation tree.
tar -xf %{SOURCE1} --strip-components=1 -C relaxng.org
find . -type f -name '*.jar' -delete
# The standalone datatype package supplies these interfaces during compilation.
rm -rf mod/datatype/src/main/org
for pair in saxon9:saxon-he resolver:xml-resolver \
    xalan:xalan serializer:serializer xercesImpl:xercesImpl \
    isorelax:isorelax javacc:javacc relaxngDatatype:relaxngDatatype \
    testng:testng testng-ant:testng-ant; do
    ln -s %{_datadir}/java/"${pair#*:}".jar lib/"${pair%%:*}".jar
done
ln -s %{_datadir}/ant/lib/ant.jar lib/ant.jar
cp %{SOURCE2} Unicode-LICENSE.txt
sed -n '1,4s/^# *//p' \
    mod/schematron/src/main/com/thaiopensource/validate/schematron/resources/iso-schematron.rnc \
    > ISO-PERMISSION.txt

%build
ant modbuild
ant -f modbuild.xml -Dlib.dir="$PWD/lib" jing-jar

%install
install -Dpm644 build/jing.jar %{buildroot}%{_datadir}/java/jing.jar
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/jing <<'SH'
#!/bin/sh
exec java -jar /usr/share/java/jing.jar "$@"
SH
chmod 755 %{buildroot}%{_bindir}/jing

%check
# Resolve the installed manifest names while exercising the upstream test suite.
for jar in saxon-he xalan serializer xercesImpl isorelax xml-resolver relaxngDatatype; do
    ln -s %{_datadir}/java/"$jar".jar build/"$jar".jar
done
ant -f modbuild.xml -Dlib.dir="$PWD/lib" test
# The installed validator must use the external datatype API and reject bad XML.
if jar tf build/jing.jar | grep -q '^org/relaxng/datatype/'; then
    echo 'Bundled datatype classes remain in jing.jar'
    exit 1
fi
cat > check.rnc <<'RNC'
start = element answer { xsd:integer }
RNC
echo '<answer>42</answer>' > valid.xml
echo '<answer>not-an-integer</answer>' > invalid.xml
java -jar build/jing.jar -c check.rnc valid.xml
if java -jar build/jing.jar -c check.rnc invalid.xml; then
    echo 'Accepted XML that violates the schema'
    exit 1
fi

%files
%license copying.txt ISO-PERMISSION.txt Unicode-LICENSE.txt
%doc README.adoc
%{_bindir}/jing
%{_datadir}/java/jing.jar

%changelog
%autochangelog
