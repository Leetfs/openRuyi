# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bundle org.eclipse.jdt.annotation
%global repo_dir %{_datadir}/maven-repository/org/eclipse/jdt/%{bundle}/%{version}
%global revision 6725c16c24d94c83302346dc384bb915a0f2fe1a

Name:           eclipse-jdt-annotations
Version:        2.4.100
Release:        %autorelease
Summary:        Eclipse JDT nullness annotations and runtime checks
License:        EPL-2.0
URL:            https://eclipse.dev/jdt/
VCS:            git:https://github.com/eclipse-jdt/eclipse.jdt.core
#!RemoteAsset:  sha256:a650a17bb74381fb042318ea05483c5451f1aad78df30f67b51cb572007370d9
Source0:        https://github.com/eclipse-jdt/eclipse.jdt.core/archive/%{revision}.tar.gz
#!RemoteAsset:  sha256:7ea61aca8f70e07d8f1a0c166ae462fc5a81f12c26c3b081fc25d7d2cbb434ea
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/jdt/%{bundle}/%{version}/%{bundle}-%{version}.pom
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
Provides:       mvn(org.eclipse.jdt:org.eclipse.jdt.annotation) == %{version}
Requires:       java-25-openjdk

%description
JDT's annotations describe nullable and non-null Java types. The Checks
class enforces nullness contracts at runtime.

%prep
%autosetup -n eclipse.jdt.core-%{revision}

%build
mkdir -p build/classes
find %{bundle}/src -name '*.java' | sort > build/sources
javac --release 8 -encoding UTF-8 -d build/classes @build/sources
sed 's/^\(Bundle-Version: %{version}\)\.qualifier$/\1/' %{bundle}/META-INF/MANIFEST.MF > build/MANIFEST.MF
jar --create --file build/%{bundle}.jar --manifest build/MANIFEST.MF -C build/classes . \
    -C %{bundle} src -C %{bundle} bundle.properties -C %{bundle} about.html

%install
install -Dm644 build/%{bundle}.jar %{buildroot}%{repo_dir}/%{bundle}-%{version}.jar
install -m644 %{SOURCE1} %{buildroot}%{repo_dir}/%{bundle}-%{version}.pom
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>org.eclipse.jdt</groupId><artifactId>%{bundle}</artifactId><version>%{version}</version>
    <path>%{repo_dir}/%{bundle}-%{version}.jar</path></artifact>
  <artifact><groupId>org.eclipse.jdt</groupId><artifactId>%{bundle}</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{repo_dir}/%{bundle}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
jar=%{buildroot}%{repo_dir}/%{bundle}-%{version}.jar
cat > build/NullContract.java <<'JAVA'
import org.eclipse.jdt.annotation.Checks;
import org.eclipse.jdt.annotation.Nullable;

class NullContract {
    static @Nullable String maybe(boolean present) { return present ? "value" : null; }
    public static void main(String[] args) {
        if (!"value".equals(Checks.requireNonNull(maybe(true)))) throw new AssertionError();
        if (!"fallback".equals(Checks.nonNullElse(maybe(false), "fallback"))) throw new AssertionError();
        try {
            Checks.requireNonNull(maybe(false), "missing");
            throw new AssertionError("Null did not violate the contract");
        } catch (NullPointerException expected) {
            if (!"missing".equals(expected.getMessage())) throw expected;
        }
    }
}
JAVA
javac --release 8 -cp "$jar" -d build build/NullContract.java
javap -v -cp build NullContract > build/annotations
grep -F 'RuntimeInvisibleTypeAnnotations:' build/annotations
grep -F 'org.eclipse.jdt.annotation.Nullable' build/annotations
java -cp "build:$jar" NullContract

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/eclipse-jdt-annotations.xml
%{repo_dir}/

%changelog
%autochangelog
