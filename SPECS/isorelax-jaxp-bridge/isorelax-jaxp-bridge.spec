# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           isorelax-jaxp-bridge
Version:        1.1
Release:        %autorelease
Summary:        Use RELAX NG verifiers through the JAXP validation API
License:        MIT
URL:            https://www.jopendocument.org/
# VCS: No VCS link available
# ILM publishes the amended Java sources inside the bridge archive in its source distribution.
#!RemoteAsset:  sha256:3e3763aaf083e3c8ab10b34822fb9a06469659d709664ca5f9d1e424b7ec125d
Source0:        https://www.jopendocument.org/download/jOpenDocument-src-1.3b1.zip
#!RemoteAsset:  sha256:aee4aea8930332cbf380b96a45a40bc906119fa1e37b3dd4e340105f0a840290
Source1:        https://raw.githubusercontent.com/kohsuke/isorelax-jaxp-bridge/71b2f3cb6eba7d9068da2d6af15e3ae7bde7f552/LICENSE.txt
BuildArch:      noarch

BuildRequires:  isorelax
BuildRequires:  java-25-openjdk-devel
BuildRequires:  msv
BuildRequires:  unzip
Requires:       isorelax
Requires:       msv

%description
The bridge lets Java applications obtain a RELAX NG SchemaFactory, compile
schemas and validate XML through JAXP. This edition includes the service
registration and public factory class used by the ODF Toolkit.

%prep
%setup -q -c -T
unzip -q %{SOURCE0} lib/isorelax-jaxp-bridge-ILM.jar
# Extract sources and service metadata from the publisher's combined archive.
unzip -q lib/isorelax-jaxp-bridge-ILM.jar '*.java' META-INF/services/javax.xml.validation.SchemaFactory README
cp -p %{SOURCE1} LICENSE.txt

%build
mkdir classes
find org -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -cp %{_datadir}/java/isorelax.jar -d classes @sources.list
jar --create --file isorelax-jaxp-bridge.jar -C classes . META-INF/services/javax.xml.validation.SchemaFactory

%install
install -Dpm644 isorelax-jaxp-bridge.jar %{buildroot}%{_datadir}/java/isorelax-jaxp-bridge.jar

%check
mkdir checks
cat > checks/CheckBridge.java <<'JAVA'
import java.io.StringReader;
import javax.xml.XMLConstants;
import javax.xml.transform.stream.StreamSource;
import javax.xml.validation.Schema;
import javax.xml.validation.SchemaFactory;
import org.xml.sax.SAXException;

class CheckBridge {
    static StreamSource xml(String value) { return new StreamSource(new StringReader(value)); }
    public static void main(String[] args) throws Exception {
        SchemaFactory factory = SchemaFactory.newInstance(XMLConstants.RELAXNG_NS_URI);
        if (!factory.getClass().getName().equals("org.iso_relax.verifier.jaxp.validation.RELAXNGSchemaFactoryImpl"))
            throw new AssertionError(factory.getClass().getName());
        Schema schema = factory.newSchema(xml("<element xmlns='http://relaxng.org/ns/structure/1.0' name='item'><empty/></element>"));
        javax.xml.validation.Validator validator = schema.newValidator();
        validator.validate(xml("<item/>"));
        try {
            validator.validate(xml("<wrong/>"));
            throw new AssertionError("Default error handler accepted an invalid document");
        } catch (SAXException expected) {}
        validator = schema.newValidator();
        validator.setErrorHandler(new org.xml.sax.helpers.DefaultHandler() {
            @Override public void error(org.xml.sax.SAXParseException e) throws SAXException { throw e; }
        });
        validator.validate(xml("<item/>"));
        try {
            validator.validate(xml("<wrong/>"));
            throw new AssertionError("Accepted element outside the grammar");
        } catch (SAXException expected) { }
    }
}
JAVA
javac --release 8 checks/CheckBridge.java
java -cp checks:isorelax-jaxp-bridge.jar:%{_datadir}/java/isorelax.jar:%{_datadir}/java/msv-core.jar CheckBridge

%files
%license LICENSE.txt
%doc README
%{_datadir}/java/isorelax-jaxp-bridge.jar

%changelog
%autochangelog
