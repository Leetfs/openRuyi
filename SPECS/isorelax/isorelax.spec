# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           isorelax
Version:        20041111
Release:        %autorelease
Summary:        Java interfaces for XML schema verification
License:        MIT
URL:            https://iso-relax.sourceforge.net/
VCS:            https://sourceforge.net/p/iso-relax/code/
#!RemoteAsset:  sha256:2fce4a64611737ecd52d5a5b816f572722602b62d2851b74279e7ccc2fab1476
Source0:        https://downloads.sourceforge.net/project/iso-relax/package/2004_11_11/%{name}.%{version}.zip
# The release-20050331 tag supplies the JAXP 1.3 factory methods.
# https://sourceforge.net/p/iso-relax/code/
Patch1000:      1000-build-with-jaxp-1.3.patch
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  java-25-openjdk-devel
BuildRequires:  unzip

%description
ISO RELAX defines the Java API for RELAX Verifiers (JARV). XML validators
use it to compile schemas, create verifiers and pass SAX events to a
validation engine. The library also provides JAXP and Ant adapters.

%prep
%setup -q -c -T
# The release ZIP contains the original Java sources in a separate archive.
unzip -q %{SOURCE0} COPYING.txt src.zip
unzip -q src.zip
sed -i 's/\r$//' org/iso_relax/jaxp/ValidatingDocumentBuilderFactory.java
%patch -P 1000 -p1

%build
mkdir classes
find jp org -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -cp %{_datadir}/ant/lib/ant.jar -d classes @sources.list
jar --create --file isorelax.jar -C classes . jp/gr/xml/relax/lib

%install
install -Dpm644 isorelax.jar %{buildroot}%{_datadir}/java/isorelax.jar

%check
mkdir checks
cat > checks/CheckFactory.java <<'JAVA'
import java.io.StringReader;
import javax.xml.parsers.ParserConfigurationException;
import org.iso_relax.jaxp.ValidatingDocumentBuilderFactory;
import org.w3c.dom.Document;
import org.xml.sax.InputSource;

class CheckFactory {
    public static void main(String[] args) throws Exception {
        ValidatingDocumentBuilderFactory factory = new ValidatingDocumentBuilderFactory(() -> null);
        factory.setValidating(false);
        factory.setNamespaceAware(true);
        Document doc = factory.newDocumentBuilder().parse(
            new InputSource(new StringReader("<item xmlns='urn:example'/>")));
        if (!"urn:example".equals(doc.getDocumentElement().getNamespaceURI()))
            throw new AssertionError("Namespace setting did not reach the parser");
        try {
            factory.getFeature("urn:unknown-feature");
            throw new AssertionError("Unknown parser feature was accepted");
        } catch (ParserConfigurationException expected) {
        }
        if (CheckFactory.class.getResource("/jp/gr/xml/relax/lib/relaxCore.dtd") == null)
            throw new AssertionError("Missing RELAX Core grammar");
    }
}
JAVA
(cd checks && java -cp ../isorelax.jar CheckFactory.java)

%files
%license COPYING.txt
%{_datadir}/java/isorelax.jar

%changelog
%autochangelog
