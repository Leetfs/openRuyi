# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global lo_version 26.8.2.2

Name:           pentaho-librepository
Version:        1.1.6
Release:        %autorelease
Summary:        Report content repositories for Pentaho Reporting
License:        LGPL-2.1-only
URL:            https://github.com/pentaho/pentaho-reporting
#!RemoteAsset:  sha256:abe2c57ac12ba45d83563b02e240fa95d973376de2f720aab8fe11f2e621c095
Source0:        https://downloads.sourceforge.net/project/jfreereport/02.%20Libraries/%{version}-stable/librepository-%{version}.zip
# Upstream LibreOffice patches for this component.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/external/jfreereport/UnpackedTarball_jfreereport_librepository.mk
#!RemoteAsset:  sha256:8980ba27dc14ba20a9f78ccf3c5612dbafdb7add66a95e75a0501bfddd82e765
Patch0:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/common_build.patch
#!RemoteAsset:  sha256:e2e6b8604db5c3cb89db00e6680d371d55d41209bb21c13242a9074e5d7d2bc4
Patch1:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/librepository-1.1.6-deprecated.patch
#!RemoteAsset:  sha256:636d4b46ffb7f10cf2515907de8bdb6723b24a7c1264ab2ce82e9ef0d08d2ec6
Patch2:         https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/jfreereport/patches/librepository-1.1.3-remove-commons-logging.patch.1
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  java-25-openjdk-devel
BuildRequires:  unzip
BuildRequires:  pentaho-libbase
BuildRequires:  javax-activation
BuildRequires:  javax-mail
Requires:       pentaho-libbase
Requires:       javax-activation
Requires:       javax-mail

%description
LibRepository stores report content in file, ZIP, stream and MIME repositories.

%prep
%autosetup -N -c
# Build all classes from source, including the dependencies used by Ant.
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete
sed -i 's/\r$//' common_build.xml
%patch -P 0 -p2
%patch -P 1 -p2
%patch -P 2 -p1
mkdir -p lib
ln -s %{_datadir}/java/libbase.jar lib/libbase.jar
ln -s %{_datadir}/java/javax-activation.jar lib/javax-activation.jar
ln -s %{_datadir}/java/javax-mail.jar lib/javax-mail.jar

%build
ant -nouserlib -f build.xml -Dbuild.label=%{version} \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
    -Dantcontrib.available=true -Dbuild.id=10682 -Dproject.revision=%{version} jar
printf 'Class-Path: libbase.jar javax-activation.jar javax-mail.jar\n' > report-classpath.mf
jar --update --file dist/librepository-%{version}.jar --manifest report-classpath.mf

%install
install -Dpm644 dist/librepository-%{version}.jar %{buildroot}%{_datadir}/java/librepository.jar

%check
cat > Smoke.java <<'JAVA'
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.Properties;
import javax.mail.*;
import javax.mail.internet.*;
import org.pentaho.reporting.libraries.repository.*;
import org.pentaho.reporting.libraries.repository.email.EmailRepository;
class Smoke {
    public static void main(String[] args) throws Exception {
        Session session = Session.getInstance(new Properties());
        EmailRepository repository = new EmailRepository(new DefaultMimeRegistry(), session);
        ContentItem html = repository.getRoot().createItem("index.html");
        html.setAttribute(LibRepositoryBoot.REPOSITORY_DOMAIN, LibRepositoryBoot.CONTENT_TYPE, "text/html");
        try (OutputStream body = html.getOutputStream()) { body.write("<p>Report</p>".getBytes(StandardCharsets.UTF_8)); }
        ContentItem item = repository.getRoot().createItem("report.bin");
        item.setAttribute(LibRepositoryBoot.REPOSITORY_DOMAIN, LibRepositoryBoot.CONTENT_TYPE, "application/octet-stream");
        byte[] bytes = {0, 42, 65, -1};
        try (OutputStream out = item.getOutputStream()) { out.write(bytes); }
        MimeMessage mail = repository.getEmail();
        mail.setSubject("Report", StandardCharsets.UTF_8.name());
        ByteArrayOutputStream wire = new ByteArrayOutputStream();
        mail.writeTo(wire);
        MimeMessage copy = new MimeMessage(session, new ByteArrayInputStream(wire.toByteArray()));
        Multipart multipart = (Multipart) copy.getContent();
        if (multipart.getCount() != 2 || !Arrays.equals(bytes, multipart.getBodyPart(1).getInputStream().readAllBytes()))
            throw new AssertionError("Report attachment content");
    }
}
JAVA
javac -cp dist/librepository-%{version}.jar:%{_datadir}/java/libbase.jar:%{_datadir}/java/javax-activation.jar:%{_datadir}/java/javax-mail.jar Smoke.java
java -Djava.awt.headless=true -cp .:dist/librepository-%{version}.jar:%{_datadir}/java/libbase.jar:%{_datadir}/java/javax-activation.jar:%{_datadir}/java/javax-mail.jar Smoke

%files
%license licence-LGPL.txt
%doc README.txt
%{_datadir}/java/librepository.jar

%changelog
%autochangelog
