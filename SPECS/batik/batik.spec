# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           batik
Version:        1.20
Release:        %autorelease
Summary:        SVG DOM, rendering and JavaScript toolkit
License:        Apache-2.0
URL:            https://xmlgraphics.apache.org/batik/
VCS:            git:https://github.com/apache/xmlgraphics-batik.git
#!RemoteAsset:  sha256:95d46a238ecbbe8abe1c2957b0bdf09bf7d60cb844fa23dec0cf7b35525bfd53
Source0:        https://archive.apache.org/dist/xmlgraphics/batik/source/batik-src-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  python3
BuildRequires:  java-sac
BuildRequires:  rhino
BuildRequires:  xml-commons-apis-ext
BuildRequires:  xmlgraphics-commons
Requires:       java-sac
Requires:       rhino
Requires:       xml-commons-apis-ext
Requires:       xmlgraphics-commons

%description
Batik parses SVG documents, builds their graphics trees, renders images and
provides the JavaScript integration used by SVG applications.

%prep
%autosetup -n batik-%{version}
# The source distribution carries library binaries. Use the system Java libraries.
find lib -type f -name '*.jar' -delete

%build
mkdir classes
# Follow batik-all's module order and the upstream Ant conditions on optional
# JACL and JPython interpreters. Rhino remains available for JavaScript.
python3 - <<'MODULES'
from pathlib import Path
from shutil import copyfile
from xml.etree import ElementTree as ET
root=ET.parse("batik-all/pom.xml")
deps=root.findall("./{*}dependencies/{*}dependency")
modules=[d.findtext("{*}artifactId") for d in deps if d.findtext("{*}artifactId").startswith("batik-")]
assert {"batik-bridge","batik-script","batik-dom"} <= set(modules)
sources=[]
for name in modules:
    module=Path(name)/"src/main"
    sources.extend(str(p) for p in sorted((module/"java").rglob("*.java"))
                   if "jpython" not in p.parts and "jacl" not in p.parts)
    resources=module/"resources"
    for p in sorted(resources.rglob("*")):
        if not p.is_file(): continue
        relative=p.relative_to(resources)
        dest=Path("classes")/relative
        dest.parent.mkdir(parents=True,exist_ok=True)
        if relative.parts[:2]==("META-INF","services"):
            with dest.open("ab") as f: f.write(p.read_bytes()+b"\n")
        elif not dest.exists():
            copyfile(p,dest)
Path("sources.list").write_text("\n".join(sources)+"\n")
MODULES
cp=%{_datadir}/java/xml-apis-ext.jar:%{_datadir}/java/xmlgraphics-commons.jar:%{_datadir}/java/js.jar:%{_datadir}/java/sac.jar
javac --release 11 --add-modules jdk.xml.dom -encoding UTF-8 -cp "$cp" -d classes @sources.list
printf 'Class-Path: xml-apis-ext.jar xmlgraphics-commons.jar js.jar sac.jar\n' > manifest.mf
jar --create --file batik-all.jar --manifest manifest.mf -C classes .

%install
install -Dpm644 batik-all.jar %{buildroot}%{_datadir}/java/batik-all.jar

%check
# Render a real SVG through the document loader, bridge and graphics tree.
cat > SvgRender.java <<'JAVA'
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.StringReader;
import org.apache.batik.anim.dom.SAXSVGDocumentFactory;
import org.apache.batik.bridge.*;
import org.apache.batik.gvt.GraphicsNode;
import org.w3c.dom.svg.SVGDocument;
class SvgRender {
 public static void main(String[] args) throws Exception {
  String source="<svg xmlns='http://www.w3.org/2000/svg' width='12' height='10'><rect x='2' y='1' width='7' height='6' style='fill:#e04020'/></svg>";
  SVGDocument doc=new SAXSVGDocumentFactory(null).createSVGDocument("file:///report.svg",new StringReader(source));
  BridgeContext context=new BridgeContext(new UserAgentAdapter());
  try {
   GraphicsNode node=new GVTBuilder().build(context,doc);
   BufferedImage image=new BufferedImage(12,10,BufferedImage.TYPE_INT_ARGB);
   Graphics2D g=image.createGraphics();try{node.paint(g);}finally{g.dispose();}
   if(image.getRGB(4,3)!=0xffe04020 || image.getRGB(0,0)!=0)throw new AssertionError("SVG fill and bounds");
  } finally {context.dispose();}
 }
}
JAVA
cp=batik-all.jar:%{_datadir}/java/xml-apis-ext.jar:%{_datadir}/java/xmlgraphics-commons.jar:%{_datadir}/java/js.jar:%{_datadir}/java/sac.jar
javac -cp "$cp" SvgRender.java
java -Djava.awt.headless=true -cp ".:$cp" SvgRender

%files
%license LICENSE NOTICE
%{_datadir}/java/batik-all.jar

%changelog
%autochangelog
