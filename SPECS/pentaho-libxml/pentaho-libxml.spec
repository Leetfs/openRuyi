# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global lo_version 26.8.2.2

Name:           pentaho-libxml
Version:        1.1.7
Release:        %autorelease
Summary:        XML utilities for Pentaho Reporting
License:        LGPL-2.1-only
URL:            https://github.com/pentaho/pentaho-reporting
#!RemoteAsset:  sha256:7d2797fe9f79a77009721e3f14fa4a1dec17a6d706bdc93f85f1f01d124fab66
Source0:        https://downloads.sourceforge.net/project/jfreereport/02.%20Libraries/%{version}-stable/libxml-%{version}.zip
# Applied by the LibreOffice external project for this source release.
#!RemoteAsset:  sha256:8980ba27dc14ba20a9f78ccf3c5612dbafdb7add66a95e75a0501bfddd82e765
Patch0:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/common_build.patch
# LibreOffice upstream patch.
#!RemoteAsset:  sha256:f91491cca52b71b83a94ceaa50ab86fec11737a87725007eb30f40024b0b3dc5
Patch1:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/libxml-1.1.3-remove-commons-logging.patch.1
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4
BuildRequires:  unzip
BuildRequires:  pentaho-libbase
BuildRequires:  pentaho-libloader
Requires:       pentaho-libbase
Requires:       pentaho-libloader

%description
LibXml supports XML namespaces, configuration and writing escaped report content.

%prep
%autosetup -N -c
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete
sed -i 's/\r$//' common_build.xml
%patch -P 0 -p2
%patch -P 1 -p1
mkdir -p lib
ln -s %{_datadir}/java/libbase.jar lib/libbase.jar
ln -s %{_datadir}/java/libloader.jar lib/libloader.jar

%build
ant -nouserlib -f build.xml -Dbuild.label=%{version} \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
    -Dantcontrib.available=true -Dbuild.id=10682 -Dproject.revision=%{version} \
    -Dlibbase.jar=%{_datadir}/java/libbase.jar \
    -Dlibloader.jar=%{_datadir}/java/libloader.jar jar
printf 'Class-Path: libbase.jar libloader.jar\n' > system-jars.mf
jar --update --file dist/libxml-%{version}.jar --manifest system-jars.mf

%install
install -Dpm644 dist/libxml-%{version}.jar %{buildroot}%{_datadir}/java/libxml.jar

%check
# Exercise the installed interfaces, resource lookup and archive content.
cat > Smoke.java <<'JAVA'
import java.io.StringWriter;
import org.pentaho.reporting.libraries.base.config.DefaultConfiguration;
import org.pentaho.reporting.libraries.xmlns.writer.DefaultTagDescription;
import org.pentaho.reporting.libraries.xmlns.writer.XmlWriterSupport;
class Smoke {
    public static void main(String[] args) throws Exception {
        DefaultTagDescription tags=new DefaultTagDescription(new DefaultConfiguration(),"report.");
        if(!tags.hasCData("urn:report", "text")) throw new AssertionError("Mixed content default");
        tags.addTagDefinition("urn:report","rows",false);
        if(tags.hasCData("urn:report","rows")) throw new AssertionError("Element-only content");
        StringWriter writer=new StringWriter();
        new XmlWriterSupport().writeTextNormalized(writer,"<report>&",false);
        if(!writer.toString().equals("&lt;report&gt;&amp;")) throw new AssertionError(writer.toString());
    }
}
JAVA
cp=dist/libxml-%{version}.jar:%{_datadir}/java/libbase.jar:%{_datadir}/java/libloader.jar
javac -cp "$cp" Smoke.java
java -Djava.awt.headless=true -cp ".:$cp" Smoke
# Run XML encoding; Smoke covers the canonical mixed-content default and explicit element-only tags.
mkdir classes-test
find test -name '*.java' | sort > test.sources
tc=$cp:%{_datadir}/java/junit4.jar
javac --release 8 -encoding UTF-8 -cp "$tc" -d classes-test @test.sources
java -Djava.awt.headless=true -cp "classes-test:test:$tc" org.junit.runner.JUnitCore \
    org.pentaho.reporting.libraries.xmlns.writer.XmlWriterSupportTest

%files
%license licence-LGPL.txt
%doc README.txt
%{_datadir}/java/libxml.jar

%changelog
%autochangelog
