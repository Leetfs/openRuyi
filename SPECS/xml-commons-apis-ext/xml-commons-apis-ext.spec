# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xml-commons-apis-ext
Version:        1.4.01
Release:        %autorelease
Summary:        SVG and SMIL DOM interfaces for Java
License:        W3C
URL:            https://xerces.apache.org/xml-commons/
VCS:            git:https://github.com/apache/xerces-j.git
#!RemoteAsset:  sha256:d34bd88dc89c5c1ed2545ec5c61e4606fc28beb200a6fecf8c3ed17694181866
Source0:        https://archive.apache.org/dist/xml/commons/source/xml-commons-external-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel

%description
The W3C SVG and SMIL interfaces extend the DOM interfaces provided by the
Java runtime. They are used by SVG document implementations and renderers.

%prep
%autosetup -c

%build
mkdir classes
find org/w3c/dom/svg org/w3c/dom/smil -name '*.java' | sort > sources.list
javac --release 11 --add-modules jdk.xml.dom -d classes @sources.list
jar --create --file xml-apis-ext.jar -C classes .

%install
install -Dpm644 xml-apis-ext.jar %{buildroot}%{_datadir}/java/xml-apis-ext.jar

%check
# Compile a consumer against both the SVG type hierarchy and the runtime's CSS DOM.
cat > SvgTypes.java <<'JAVA'
import org.w3c.dom.Document;
import org.w3c.dom.svg.SVGDocument;
import org.w3c.dom.svg.SVGSVGElement;
import org.w3c.dom.css.ViewCSS;
import org.w3c.dom.smil.TimeEvent;
import org.w3c.dom.events.Event;
class SvgTypes {
    public static void main(String[] args) throws Exception {
        if (!Document.class.isAssignableFrom(SVGDocument.class)
                || !Event.class.isAssignableFrom(TimeEvent.class)
                || !ViewCSS.class.isAssignableFrom(SVGSVGElement.class)
                || SVGDocument.class.getMethod("getRootElement").getReturnType() != SVGSVGElement.class)
            throw new AssertionError("DOM API");
    }
}
JAVA
javac -cp xml-apis-ext.jar SvgTypes.java
java -cp .:xml-apis-ext.jar SvgTypes

%files
%license LICENSE.dom-software.txt NOTICE
%{_datadir}/java/xml-apis-ext.jar

%changelog
%autochangelog
