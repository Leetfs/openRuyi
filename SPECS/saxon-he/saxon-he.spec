# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global         saxon_commit 45924081b69cabf8e55baafcfb1833f7c544b823

Name:           saxon-he
Version:        10.9
Release:        %autorelease
Summary:        Saxon Home Edition XSLT and XQuery processor
License:        MPL-2.0-no-copyleft-exception AND BSD-3-Clause AND X11 AND Unicode-DFS-2015
URL:            https://www.saxonica.com/
VCS:            git:https://github.com/Saxonica/Saxon-HE.git
#!RemoteAsset:  sha256:5d44af4dd64f76afe0c899ab4414fca9c5f4009641c544d61bc7ff31e4e49010
Source0:        https://raw.githubusercontent.com/Saxonica/Saxon-HE/%{saxon_commit}/10/source/saxon10-9source.zip
# Saxonica distributes the full license notices separately from the Java source ZIP.
#!RemoteAsset:  sha256:9b596a71042a6bd04d31e404dfda11f4cd45459907e745ac645b861919a763dd
Source1:        https://raw.githubusercontent.com/Saxonica/Saxon-HE/%{saxon_commit}/10/Java/SaxonHE10-9J.zip
# Downstream fix for the ErrorListener set on SAXTransformerFactory.
# https://github.com/Saxonica/Saxon-HE/tree/main/10/source
Patch2000:      2000-preserve-the-sax-templates-error-listener.patch
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  unzip
BuildRequires:  xml-commons-resolver
Requires:       xml-commons-resolver

%description
Saxon Home Edition compiles and executes XSLT stylesheets and XQuery
expressions. It includes the Java transformation and XPath APIs used by
XML applications, with DOM, SAX and StAX support.

%prep
%setup -q -c -T
unzip -q %{SOURCE0}
unzip -q %{SOURCE1} notices/LICENSE.txt notices/THAI.txt notices/JAMESCLARK.txt notices/UNICODE.txt
# The source files exist after the ZIP has been unpacked.
%patch -P 2000 -p1

%build
mkdir -p classes/META-INF/services
# Build the standard Java processor. Gizmo and the external tree-model bridges
# have separate optional line-editing and object-model libraries.
find net -name '*.java' ! -path '*/option/axiom/*' ! -path '*/option/dom4j/*' \
    ! -path '*/option/jdom2/*' ! -path '*/option/xom/*' \
    ! -path '*/gizmo/*' ! -name Gizmo.java | sort > sources.list
javac --release 11 -encoding UTF-8 -cp %{_datadir}/java/xml-resolver.jar -d classes @sources.list
cp -pr net/sf/saxon/data classes/net/sf/saxon/
echo net.sf.saxon.TransformerFactoryImpl > classes/META-INF/services/javax.xml.transform.TransformerFactory
printf 'Main-Class: net.sf.saxon.Transform\nClass-Path: xml-resolver.jar\n' > manifest.mf
jar --create --file saxon-he.jar --manifest manifest.mf -C classes .

%install
install -Dpm644 saxon-he.jar %{buildroot}%{_datadir}/java/saxon-he.jar

%check
cp=saxon-he.jar:%{_datadir}/java/xml-resolver.jar
java -cp "$cp" net.sf.saxon.Query '-qs:sum((1, 2, 3))' > query.xml
grep -F '>6' query.xml
cat > transform.xsl <<'XSL'
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">
  <xsl:template match="/">
    <result><xsl:value-of select="upper-case(/*)"/></result>
  </xsl:template>
</xsl:stylesheet>
XSL
echo '<input>ready</input>' > input.xml
java -cp "$cp" net.sf.saxon.Transform -s:input.xml -xsl:transform.xsl -o:result.xml
grep -F '<result>READY</result>' result.xml

# SAX stylesheet compilation must report errors to the caller's listener.
cat > CheckTemplates.java <<'JAVA'
import java.io.*;
import javax.xml.parsers.SAXParserFactory;
import javax.xml.transform.*;
import javax.xml.transform.sax.*;
import javax.xml.transform.stream.*;
import org.xml.sax.*;
public class CheckTemplates {
    static class Errors implements ErrorListener {
        int count;
        public void warning(TransformerException e) {}
        public void error(TransformerException e) { count++; }
        public void fatalError(TransformerException e) { count++; }
    }
    static TemplatesHandler handler(String stylesheet, Errors errors) throws Exception {
        SAXTransformerFactory factory = new net.sf.saxon.TransformerFactoryImpl();
        factory.setErrorListener(errors);
        TemplatesHandler handler = factory.newTemplatesHandler();
        handler.setSystemId("file:/stylesheet.xsl");
        SAXParserFactory parser = SAXParserFactory.newInstance();
        parser.setNamespaceAware(true);
        XMLReader reader = parser.newSAXParser().getXMLReader();
        reader.setContentHandler(handler);
        reader.parse(new InputSource(new StringReader(stylesheet)));
        return handler;
    }
    public static void main(String[] args) throws Exception {
        String start = "<xsl:stylesheet version='2.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>";
        Errors valid = new Errors();
        Templates good = handler(start + "<xsl:output method='text'/><xsl:template match='/'>42</xsl:template></xsl:stylesheet>", valid).getTemplates();
        StringWriter result = new StringWriter();
        good.newTransformer().transform(new StreamSource(new StringReader("<root/>")), new StreamResult(result));
        if (valid.count != 0 || !"42".equals(result.toString())) throw new AssertionError("Valid transform");
        Errors invalid = new Errors();
        boolean rejected = false;
        try {
            Templates bad = handler(start + "<xsl:template match='foo bar'/></xsl:stylesheet>", invalid).getTemplates();
            rejected = bad == null;
        } catch (IllegalStateException expected) { rejected = true; }
        if (!rejected || invalid.count == 0) throw new AssertionError("Missing caller error notification");
        System.out.println("SAX TemplatesHandler valid transform and caller error notification passed");
    }
}
JAVA
javac --release 11 -cp "$cp" CheckTemplates.java
java -cp ".:$cp" CheckTemplates

%files
%license notices/LICENSE.txt notices/THAI.txt notices/JAMESCLARK.txt notices/UNICODE.txt
%{_datadir}/java/saxon-he.jar

%changelog
%autochangelog
