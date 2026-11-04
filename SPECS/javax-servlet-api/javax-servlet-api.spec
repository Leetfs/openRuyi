# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           javax-servlet-api
Version:        4.0.4
Release:        %autorelease
Summary:        Java Servlet 4 API for the javax namespace
License:        Apache-2.0 AND (EPL-2.0 OR (GPL-2.0-only WITH Classpath-exception-2.0))
URL:            https://jakarta.ee/specifications/servlet/4.0/
VCS:            git:https://github.com/jakartaee/servlet
#!RemoteAsset:  sha256:d050b4a8f1c7619f1f37c6c1cd2f41f71baa8822b98144dd00b38c46e27d4ec1
Source0:        https://github.com/jakartaee/servlet/archive/refs/tags/%{version}-RELEASE.tar.gz#/servlet-%{version}-RELEASE.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel

%description
This package supplies the javax.servlet and javax.servlet.http API
classes for building Java web applications that use Servlet 4.

%prep
%autosetup -n servlet-%{version}-RELEASE

%build
mkdir classes
find api/src/main/java -name '*.java' | sort > java-sources
javac --release 8 -encoding UTF-8 -d classes @java-sources
(cd api/src/main/java && find . -type f \( -name '*.properties' -o -name '*.html' \) -exec cp --parents {} "$OLDPWD/classes/" \;)
cat > servlet.mf <<'MANIFEST'
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-SymbolicName: jakarta.servlet-api
Bundle-Version: 4.0.0
Bundle-Description: Jakarta Servlet 4.0
Extension-Name: javax.servlet
Specification-Version: 4.0
Specification-Vendor: Eclipse Foundation
Implementation-Version: %{version}
Implementation-Vendor: Eclipse Foundation
Implementation-Vendor-Id: org.eclipse
Export-Package: javax.servlet;version="4.0.0",
 javax.servlet.annotation;version="4.0.0",
 javax.servlet.descriptor;version="4.0.0",
 javax.servlet.http;version="4.0.0"

MANIFEST
jar --create --file %{name}.jar --manifest servlet.mf -C classes .

%install
install -Dpm644 %{name}.jar %{buildroot}%{_datadir}/java/%{name}.jar

%check
cat > ServletCheck.java <<'JAVA'
import java.util.ResourceBundle;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
class ServletCheck extends HttpServlet {
    public static void main(String[] args) {
        Cookie cookie = new Cookie("session", "openRuyi");
        if (!"openRuyi".equals(cookie.getValue()))
            throw new AssertionError("Cookie value was not preserved");
        ResourceBundle.getBundle("javax.servlet.http.LocalStrings");
        if (!"4.0".equals(HttpServlet.class.getPackage().getSpecificationVersion()))
            throw new AssertionError("Missing Servlet 4 specification metadata");
    }
}
JAVA
javac -cp %{name}.jar ServletCheck.java
java -cp .:%{name}.jar ServletCheck

%files
%license LICENSE.md NOTICE.md
%{_datadir}/java/javax-servlet-api.jar

%changelog
%autochangelog
