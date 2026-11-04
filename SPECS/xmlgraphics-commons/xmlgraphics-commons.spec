# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xmlgraphics-commons
Version:        2.12
Release:        %autorelease
Summary:        Shared image and graphics support for Apache XML Graphics
License:        Apache-2.0
URL:            https://xmlgraphics.apache.org/commons/
VCS:            git:https://github.com/apache/xmlgraphics-commons.git
#!RemoteAsset:  sha256:5d6e8ead658006746769a44ac6f0f8744cda1610a1573be037da6eb84c308f29
Source0:        https://archive.apache.org/dist/xmlgraphics/commons/source/xmlgraphics-commons-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  slf4j-jcl
BuildRequires:  slf4j-jdk14
Requires:       slf4j-jcl
Requires:       slf4j-jdk14

%description
XML Graphics Commons supplies color spaces, image loaders and writers,
Java2D drawing support and PostScript utilities.

%prep
%autosetup -n xmlgraphics-commons-%{version}

%build
mkdir classes
find src/main/java -name '*.java' | sort > sources.list
javac --release 11 -encoding UTF-8 -cp %{_datadir}/java/jcl-over-slf4j.jar -d classes @sources.list
cp -rp src/main/resources/. classes/
printf 'Class-Path: jcl-over-slf4j.jar slf4j-jdk14.jar\n' > manifest.mf
jar --create --file xmlgraphics-commons.jar --manifest manifest.mf -C classes .

%install
install -Dpm644 xmlgraphics-commons.jar %{buildroot}%{_datadir}/java/xmlgraphics-commons.jar

%check
# Verify SVG's sRGB color conversion through the graphics library.
cat > ColorCheck.java <<'JAVA'
import java.awt.Color;
import org.apache.xmlgraphics.java2d.color.ColorUtil;
class ColorCheck {
    public static void main(String[] args) {
        Color c = ColorUtil.toSRGBColor(new Color(224, 64, 32));
        if (c.getRGB() != 0xffe04020) throw new AssertionError("sRGB");
    }
}
JAVA
javac -cp xmlgraphics-commons.jar ColorCheck.java
java -Djava.awt.headless=true -cp .:xmlgraphics-commons.jar:%{_datadir}/java/jcl-over-slf4j.jar:%{_datadir}/java/slf4j-jdk14.jar ColorCheck

%files
%license LICENSE NOTICE
%{_datadir}/java/xmlgraphics-commons.jar

%changelog
%autochangelog
