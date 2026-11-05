# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xalan-j2-interpretive
Version:        2.7.3
Release:        %autorelease
Summary:        Apache Xalan interpretive XSLT processor for Java
License:        Apache-2.0 AND W3C
URL:            https://xalan.apache.org/xalan-j/
VCS:            git:https://gitbox.apache.org/repos/asf/xalan-java.git
#!RemoteAsset:  sha256:638453194b6eb68f07f8d6becb14ff849913d3e93991fb866994badb94556456
Source0:        https://archive.apache.org/dist/xalan/xalan-j/source/xalan-j_2_7_3-src.tar.gz
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  java-25-openjdk-devel
BuildRequires:  xerces-j2
Requires:       xerces-j2

%description
Apache Xalan interprets XSLT 1.0 stylesheets and XPath expressions in
Java applications. It provides a JAXP transformer factory and the
serializer that writes the transformed document.

%prep
%setup -q -n xalan-j_2_7_3
# Keep the Ant build on the system class path, including its XML parser.
find . -type f -name '*.jar' -delete

%build
ant -nouserlib -lib %{_datadir}/java/xercesImpl.jar \
    -Dparser.jar=%{_datadir}/java/xercesImpl.jar -Dbuild.sysclasspath=only \
    -Dcompiler.source=11 -Dcompiler.target=11 xalan-interpretive.jar

%install
install -Dpm644 build/xalan.jar %{buildroot}%{_datadir}/java/xalan.jar
install -Dpm644 build/serializer.jar %{buildroot}%{_datadir}/java/serializer.jar

%check
# Transform Apache's sample input with the interpreter and its serializer.
java -cp build/xalan.jar:build/serializer.jar:%{_datadir}/java/xercesImpl.jar \
    org.apache.xalan.xslt.Process -IN samples/SimpleTransform/foo.xml \
    -XSL samples/SimpleTransform/foo.xsl -OUT result.xml
grep -F '<out>Hello</out>' result.xml

%files
%license LICENSE.txt NOTICE.txt
%{_datadir}/java/serializer.jar
%{_datadir}/java/xalan.jar

%changelog
%autochangelog
