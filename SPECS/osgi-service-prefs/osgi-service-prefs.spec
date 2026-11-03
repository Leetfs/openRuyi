# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bundle org.osgi.service.prefs
%global repo_dir %{_datadir}/maven-repository/org/osgi/%{bundle}/%{version}
%global central https://maven-central.storage-download.googleapis.com/maven2/org/osgi/%{bundle}/%{version}
%global revision db39ce672917cadce15aad14a33795cbed7e8791

Name:           osgi-service-prefs
Version:        1.1.2
Release:        %autorelease
Summary:        OSGi Preferences Service API
License:        Apache-2.0
URL:            https://docs.osgi.org/
VCS:            git:https://github.com/osgi/osgi
#!RemoteAsset:  sha256:53b22587dc722c9575aba521a82c10debcaec59e39ad28d4eb719017458a7721
Source0:        %{central}/%{bundle}-%{version}-sources.jar
#!RemoteAsset:  sha256:6ea483cea177e91310984c6452e694aa20801951b501f17cb9ba114328c2cc26
Source1:        %{central}/%{bundle}-%{version}.pom
#!RemoteAsset:  sha256:b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1
Source2:        https://raw.githubusercontent.com/osgi/osgi/%{revision}/LICENSE
#!RemoteAsset:  sha256:9095ce4629906ff31d2dc63d0b91194302463da2c3be0f8f714fdab77cd6b9ee
Source3:        https://raw.githubusercontent.com/osgi/osgi/%{revision}/NOTICE
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  unzip
Provides:       mvn(org.osgi:org.osgi.service.prefs) == %{version}
Requires:       java-25-openjdk

%description
The OSGi Preferences Service exposes hierarchical preference nodes and
separates system settings from user-specific settings.

%prep
%setup -q -c -T
unzip -q %{SOURCE0} 'org/*'
cp %{SOURCE2} LICENSE
cp %{SOURCE3} NOTICE

%build
mkdir -p build/classes/META-INF build/classes/OSGI-OPT/src
javac --release 8 -encoding UTF-8 -cp %{_datadir}/java/javapackages-bootstrap/osgi.annotation.jar \
    -d build/classes org/osgi/service/prefs/*.java
cp LICENSE NOTICE build/classes/META-INF/
cp -r org build/classes/OSGI-OPT/src/
cat > build/MANIFEST.MF <<EOF
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-SymbolicName: %{bundle}
Bundle-Version: %{version}
Bundle-Name: org.osgi:%{bundle}
Bundle-Vendor: Eclipse Foundation
Bundle-License: Apache-2.0
Automatic-Module-Name: %{bundle}
Export-Package: %{bundle};version="%{version}"
Require-Capability: osgi.ee;filter:="(&(osgi.ee=JavaSE/compact1)(version=1.8))"

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
jar=%{buildroot}%{repo_dir}/%{bundle}-%{version}.jar
cat > build/PreferencesContract.java <<'JAVA'
import java.util.jar.JarFile;
import org.osgi.service.prefs.BackingStoreException;
import org.osgi.service.prefs.Preferences;
import org.osgi.service.prefs.PreferencesService;

class PreferencesContract {
    public static void main(String[] args) throws Exception {
        if (PreferencesService.class.getMethod("getSystemPreferences").getReturnType() != Preferences.class
                || Preferences.class.getMethod("node", String.class).getReturnType() != Preferences.class) {
            throw new AssertionError("Incompatible preferences interfaces");
        }
        var cause = new IllegalStateException("storage offline");
        if (new BackingStoreException("write failed", cause).getCause() != cause) {
            throw new AssertionError("Backing store error lost its cause");
        }
        try (var archive = new JarFile(args[0])) {
            var fields = archive.getManifest().getMainAttributes();
            if (!"org.osgi.service.prefs".equals(fields.getValue("Bundle-SymbolicName"))
                    || !"org.osgi.service.prefs;version=\"1.1.2\"".equals(fields.getValue("Export-Package"))) {
                throw new AssertionError("Preferences package is missing its OSGi identity");
            }
        }
    }
}
JAVA
java -cp "$jar" build/PreferencesContract.java "$jar"

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/osgi-service-prefs.xml
%{repo_dir}/

%changelog
%autochangelog
