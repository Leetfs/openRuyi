# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           javax-mail
Version:        1.6.7
Release:        %autorelease
Summary:        JavaMail API and mail protocol implementation
License:        EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://jakarta.ee/specifications/mail/1.6/
VCS:            git:https://github.com/jakartaee/mail-api
#!RemoteAsset:  sha256:9188bc218a7a9586f41766ba79453fa26e2cc01304b74b2a9e80974f63f4c31c
Source0:        https://github.com/jakartaee/mail-api/archive/refs/tags/%{version}.tar.gz#/javax-mail-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javax-activation
# Upstream logging tests exercise a SecurityManager on JDK 17.
BuildRequires:  java-17-openjdk-headless
BuildRequires:  junit4
Requires:       javax-activation

%description
JavaMail reads and writes MIME messages and supplies implementations of the
SMTP, IMAP and POP3 protocols in the javax.mail namespace.

%prep
%autosetup -n mail-api-%{version}

%build
mkdir -p classes generated/javax/mail
sed 's/[$]{mail[.]version}/%{version}/g' mail/src/main/resources/javax/mail/Version.java > generated/javax/mail/Version.java
find mail/src/main/java generated -name '*.java' ! -name module-info.java | sort > java.sources
javac --release 8 -encoding UTF-8 -cp %{_datadir}/java/javax-activation.jar -d classes @java.sources
javac --release 9 --module-path %{_datadir}/java/javax-activation.jar --patch-module jakarta.mail=classes \
    -d classes mail/src/main/java/module-info.java
cp -rp mail/src/main/resources/META-INF classes/
rm classes/META-INF/MANIFEST.MF
printf 'Class-Path: javax-activation.jar\n' > mail.mf
jar --create --file javax-mail.jar --manifest mail.mf -C classes .

%install
install -Dpm644 javax-mail.jar %{buildroot}%{_datadir}/java/javax-mail.jar

%check
cat > MailSmoke.java <<'JAVA'
import java.io.*;
import java.util.*;
import javax.activation.*;
import javax.mail.*;
import javax.mail.internet.*;
import javax.mail.util.ByteArrayDataSource;
public class MailSmoke {
    public static void main(String[] args) throws Exception {
        Session session = Session.getInstance(new Properties());
        MimeMessage message = new MimeMessage(session);
        MimeBodyPart attached = new MimeBodyPart();
        attached.setDataHandler(new DataHandler(new ByteArrayDataSource(new byte[] {0, 1, 42, -1}, "application/octet-stream")));
        attached.setFileName("report.bin");
        MimeMultipart contents = new MimeMultipart();
        contents.addBodyPart(attached);
        message.setSubject("Report 42", "UTF-8");
        message.setContent(contents);
        ByteArrayOutputStream wire = new ByteArrayOutputStream();
        message.writeTo(wire);
        MimeMessage copy = new MimeMessage(session, new ByteArrayInputStream(wire.toByteArray()));
        BodyPart restored = ((Multipart) copy.getContent()).getBodyPart(0);
        if (!copy.getSubject().equals("Report 42") || !restored.getFileName().equals("report.bin")
                || !Arrays.equals(restored.getInputStream().readAllBytes(), new byte[] {0, 1, 42, -1}))
            throw new AssertionError("MIME round trip");
        if (!session.getTransport("smtp").getClass().getName().equals("com.sun.mail.smtp.SMTPTransport"))
            throw new AssertionError("SMTP provider");
        System.out.println("MIME attachment and default SMTP provider passed");
    }
}
JAVA
cp=javax-mail.jar:%{_datadir}/java/javax-activation.jar
javac -cp "$cp" MailSmoke.java
java -cp ".:$cp" MailSmoke
jar --describe-module --file javax-mail.jar | grep -F 'exports javax.mail.internet'

# Match the POM's Surefire include patterns, resources and assertion settings.
mkdir classes-test
find mail/src/test/java -name '*.java' | sort > test.sources
tests_cp=$cp:%{_datadir}/java/junit4.jar:%{_datadir}/java/hamcrest1.3/hamcrest-core.jar
javac --release 8 -encoding UTF-8 -cp "$tests_cp" -d classes-test @test.sources
cp -rp mail/src/test/resources/. classes-test/
# The logging suite checks an unresolvable random hostname. Keep loopback
# protocols available and make the unknown-host check independent of DNS.
printf '127.0.0.1 localhost %%s\n::1 ip6-localhost\n' "$(uname -n)" > test-hosts
classes=$(sed -n '/Test[.]java$/p; /TestSuite[.]java$/p' test.sources |
    sed 's|^mail/src/test/java/||;s|/|.|g;s|[.]java$||')
test -n "$classes"
%{_prefix}/lib64/jvm/java-17-openjdk/bin/java -ea -Djava.awt.headless=true -Djdk.net.hosts.file="$PWD/test-hosts" \
    -cp "$PWD/classes-test:$tests_cp" org.junit.runner.JUnitCore $classes > upstream-tests.log 2>&1 ||
    { tail -100 upstream-tests.log; exit 1; }
tail -4 upstream-tests.log


%files
%license LICENSE.md NOTICE.md
%{_datadir}/java/javax-mail.jar

%changelog
%autochangelog
