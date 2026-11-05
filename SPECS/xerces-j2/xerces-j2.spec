# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xerces-j2
Version:        2.12.2
Release:        %autorelease
Summary:        Apache Xerces XML parser and schema validator for Java
License:        Apache-2.0 AND W3C
URL:            https://xerces.apache.org/xerces2-j/
VCS:            git:https://github.com/apache/xerces2-j.git
#!RemoteAsset:  sha256:6dd1ebd4c88e935c182375346cd7365514bd8dd2ad2f30f0d0b05257bab34ee8
Source0:        https://archive.apache.org/dist/xerces/j/source/Xerces-J-src.%{version}.tar.gz
# Use standard Ant and the XML APIs supplied by the system JDK.
# https://github.com/apache/xerces2-j/blob/trunk/build.xml
Patch2000:      2000-build-with-standard-ant-and-jdk-xml-apis.patch
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  java-25-openjdk-devel
BuildRequires:  xml-commons-resolver
Requires:       xml-commons-resolver

%description
Xerces parses XML documents and validates namespaces, DTDs and XML
Schemas. It implements the Java APIs for XML processing and exposes the
Xerces Native Interface for applications that configure their own parsers.

%prep
%autosetup -N -n xerces-%{lua:print((rpm.expand("%{version}"):gsub("[.]", "_")))}
sed -i 's/\r$//' build.xml
%patch -P 2000 -p1

%build
ant -nouserlib -Dtools.dir=%{_datadir}/java -Djar.resolver=xml-resolver.jar jar
# The catalog resolver is a separate distribution JAR.
printf 'Class-Path: xml-resolver.jar\n' > system-classpath.mf
jar --update --file build/xercesImpl.jar --manifest system-classpath.mf

%install
install -Dpm644 build/xercesImpl.jar %{buildroot}%{_datadir}/java/xercesImpl.jar

%check
# Validate the upstream sample against its schema, then reject an invalid root.
cat > SchemaCheck.java <<'JAVA'
import java.io.File;
import java.io.StringReader;
import javax.xml.transform.stream.StreamSource;
import javax.xml.validation.Schema;
import org.apache.xerces.jaxp.validation.XMLSchemaFactory;
import org.xml.sax.SAXException;
class SchemaCheck {
    public static void main(String[] args) throws Exception {
        Schema schema = new XMLSchemaFactory().newSchema(new File("data/personal.xsd"));
        schema.newValidator().validate(new StreamSource(new File("data/personal-schema.xml")));
        try {
            schema.newValidator().validate(new StreamSource(new StringReader("<unknown/>")));
            throw new AssertionError("Accepted an undeclared root");
        } catch (SAXException expected) {}
    }
}
JAVA
javac --release 11 -cp build/xercesImpl.jar SchemaCheck.java
java -cp .:build/xercesImpl.jar:%{_datadir}/java/xml-resolver.jar SchemaCheck

%files
%license LICENSE NOTICE LICENSE.DOM-software.html
%{_datadir}/java/xercesImpl.jar

%changelog
%autochangelog
