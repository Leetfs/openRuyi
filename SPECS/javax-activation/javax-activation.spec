# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           javax-activation
Version:        1.2.2
Release:        %autorelease
Summary:        Data handlers and MIME type registry for Java
License:        BSD-3-Clause
URL:            https://jakarta.ee/specifications/activation/1.2/
VCS:            git:https://github.com/jakartaee/jaf-api
#!RemoteAsset:  sha256:6d2322271bf6fb00d5505317973b8797064d72390c1389906b72fc8a21636a01
Source0:        https://github.com/jakartaee/jaf-api/archive/refs/tags/%{version}.tar.gz#/javax-activation-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel

%description
The JavaBeans Activation Framework provides the javax.activation API,
content handlers and a MIME type registry for Java applications.

%prep
%autosetup -n jaf-api-%{version}

%build
mkdir classes
find activation/src/main/java -name '*.java' ! -name module-info.java | sort > java.sources
javac --release 8 -encoding UTF-8 -d classes @java.sources
javac --release 9 --patch-module jakarta.activation=classes -d classes activation/src/main/java/module-info.java
cp -rp activation/src/main/resources/. classes/
jar --create --file javax-activation.jar -C classes .

%install
install -Dpm644 javax-activation.jar %{buildroot}%{_datadir}/java/javax-activation.jar

%check
cat > ActivationSmoke.java <<'JAVA'
import java.io.*;
import java.util.Arrays;
import javax.activation.*;
public class ActivationSmoke {
    public static void main(String[] args) throws Exception {
        byte[] content = {0, 42, -1};
        DataSource binary = new DataSource() {
            public String getContentType() { return "application/octet-stream"; }
            public String getName() { return "report.bin"; }
            public InputStream getInputStream() { return new ByteArrayInputStream(content); }
            public OutputStream getOutputStream() throws IOException { throw new IOException("read-only"); }
        };
        DataHandler handler = new DataHandler(binary);
        ByteArrayOutputStream destination = new ByteArrayOutputStream();
        handler.writeTo(destination);
        if (!Arrays.equals(content, destination.toByteArray())
                || !new MimetypesFileTypeMap().getContentType("report.html").equals("text/html"))
            throw new AssertionError("Data handler or MIME type map");
    }
}
JAVA
javac -cp javax-activation.jar ActivationSmoke.java
java -cp .:javax-activation.jar ActivationSmoke
jar --describe-module --file javax-activation.jar | grep -F 'exports javax.activation'

%files
%license LICENSE.md NOTICE.md
%{_datadir}/java/javax-activation.jar

%changelog
%autochangelog
