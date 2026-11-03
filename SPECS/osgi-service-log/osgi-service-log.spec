# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bundle org.osgi.service.log
%global repo_dir %{_datadir}/maven-repository/org/osgi/%{bundle}/%{version}
%global central https://maven-central.storage-download.googleapis.com/maven2/org/osgi/%{bundle}/%{version}

Name:           osgi-service-log
Version:        1.3.0
Release:        %autorelease
Summary:        OSGi Log Service 1.3 API
License:        Apache-2.0
URL:            https://docs.osgi.org/
VCS:            git:https://github.com/osgi/osgi
#!RemoteAsset:  sha256:201b5923d38cc5c09f2a0aea5a27029f7338dd9040b1ff235591b3dfc0904980
Source0:        %{central}/%{bundle}-%{version}-sources.jar
#!RemoteAsset:  sha256:21c2950c1092fdb38ec084586b8ef5a54e5d1d0495f54a8247e02ebaed44328b
Source1:        %{central}/%{bundle}-%{version}.pom
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.osgi) == 3.24.100
BuildRequires:  unzip
Provides:       mvn(org.osgi:org.osgi.service.log) == %{version}
Requires:       eclipse-equinox >= 4.39

%description
The OSGi Log Service 1.3 interfaces let bundles write log entries and
receive log events. This API supports libraries implementing the
four logging methods defined by version 1.3.

%prep
%setup -q -c -T
unzip -q %{SOURCE0} 'org/*' LICENSE

%build
framework=%{_datadir}/maven-repository/org/eclipse/platform/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar
mkdir -p build/classes/META-INF build/classes/OSGI-OPT/src
javac --release 8 -encoding UTF-8 -cp "$framework" -d build/classes org/osgi/service/log/*.java
install -m644 LICENSE build/classes/META-INF/
install -m644 org/osgi/service/log/packageinfo build/classes/org/osgi/service/log/
cp -r org build/classes/OSGI-OPT/src/
cat > build/MANIFEST.MF <<EOF
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-SymbolicName: %{bundle}
Bundle-Version: %{version}
Bundle-Name: OSGi Log Service
Bundle-License: Apache-2.0
Export-Package: %{bundle};version="1.3";uses:="org.osgi.framework"
Import-Package: org.osgi.framework;version="[1.3,2)"
Require-Capability: osgi.ee;filter:="(&(osgi.ee=JavaSE)(version=1.8))"

EOF
jar --create --file build/%{bundle}.jar --manifest build/MANIFEST.MF -C build/classes .

%install
install -Dm644 build/%{bundle}.jar %{buildroot}%{repo_dir}/%{bundle}-%{version}.jar
install -m644 %{SOURCE1} %{buildroot}%{repo_dir}/%{bundle}-%{version}.pom
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>org.osgi</groupId><artifactId>%{bundle}</artifactId><version>%{version}</version>
    <path>%{repo_dir}/%{bundle}-%{version}.jar</path></artifact>
  <artifact><groupId>org.osgi</groupId><artifactId>%{bundle}</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{repo_dir}/%{bundle}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
framework=%{_datadir}/maven-repository/org/eclipse/platform/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar
jar=%{buildroot}%{repo_dir}/%{bundle}-%{version}.jar
cat > build/LoggingBackend.java <<'JAVA'
import org.osgi.framework.ServiceReference;
import org.osgi.service.log.LogService;

class LoggingBackend implements LogService {
    String last;
    public void log(int level, String message) { last = message; }
    public void log(int level, String message, Throwable error) { log(level, message); }
    public void log(ServiceReference ref, int level, String message) { log(level, message); }
    public void log(ServiceReference ref, int level, String message, Throwable error) { log(level, message); }
    public static void main(String[] args) {
        LoggingBackend backend = new LoggingBackend();
        LogService service = backend;
        service.log(null, LogService.LOG_INFO, "artifact found", null);
        if (!"artifact found".equals(backend.last)) throw new AssertionError();
    }
}
JAVA
javac --release 8 -cp "$jar:$framework" -d build build/LoggingBackend.java
java -cp "build:$jar:$framework" LoggingBackend

%files
%license LICENSE
%{_datadir}/maven-metadata/osgi-service-log.xml
%{repo_dir}/

%changelog
%autochangelog
