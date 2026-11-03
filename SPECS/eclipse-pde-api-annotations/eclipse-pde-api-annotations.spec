# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bundle org.eclipse.pde.api.tools.annotations
%global repo_dir %{_datadir}/maven-repository/org/eclipse/pde/%{bundle}/%{version}

Name:           eclipse-pde-api-annotations
Version:        1.4.0
Release:        %autorelease
Summary:        Eclipse API Tools annotations for Java code
License:        EPL-2.0
URL:            https://eclipse.dev/pde/
VCS:            git:https://github.com/eclipse-pde/eclipse.pde
#!RemoteAsset:  sha256:99c7d83f50ebffe9dc596ce06ebfec84367b7d3175cf673ad7110a66efc268d7
Source0:        https://github.com/eclipse-pde/eclipse.pde/archive/refs/tags/R4_38.tar.gz
#!RemoteAsset:  sha256:a9455db63c01dee5df4659e65f86ca320722466c27290227a997b8203e122627
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/pde/%{bundle}/%{version}/%{bundle}-%{version}.pom
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
Provides:       mvn(org.eclipse.pde:org.eclipse.pde.api.tools.annotations) == %{version}

%description
Eclipse API Tools annotations mark Java types, methods and constructors
whose use is restricted by the API contract. They are retained in Java
class files for tools that check API compatibility.

%prep
%autosetup -n eclipse.pde-R4_38

%build
bundle=apitools/%{bundle}
mkdir -p build/classes
find "$bundle/src" -name '*.java' | sort > build/sources
javac --release 8 -d build/classes @build/sources
sed 's/^Bundle-Version: %{version}[.]qualifier/Bundle-Version: %{version}/' "$bundle/META-INF/MANIFEST.MF" > build/MANIFEST.MF
cp -a "$bundle/OSGI-INF" "$bundle/about.html" build/classes/
jar --create --file build/%{bundle}.jar --manifest build/MANIFEST.MF -C build/classes .

%install
install -Dm644 build/%{bundle}.jar %{buildroot}%{repo_dir}/%{bundle}-%{version}.jar
install -m644 %{SOURCE1} %{buildroot}%{repo_dir}/%{bundle}-%{version}.pom
install -d %{buildroot}%{_datadir}/maven-metadata
cat > %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<EOF
<metadata><artifacts>
  <artifact><groupId>org.eclipse.pde</groupId><artifactId>%{bundle}</artifactId><version>%{version}</version>
    <path>%{repo_dir}/%{bundle}-%{version}.jar</path></artifact>
  <artifact><groupId>org.eclipse.pde</groupId><artifactId>%{bundle}</artifactId><version>%{version}</version><extension>pom</extension>
    <path>%{repo_dir}/%{bundle}-%{version}.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties></artifact>
</artifacts></metadata>
EOF

%check
jar=%{buildroot}%{repo_dir}/%{bundle}-%{version}.jar
cat > build/ApiContract.java <<'JAVA'
import org.eclipse.pde.api.tools.annotations.NoImplement;

@NoImplement public interface ApiContract {}
JAVA
javac --release 8 -cp "$jar" -d build build/ApiContract.java
javap -v -cp build ApiContract > build/contract.txt
grep -F 'RuntimeInvisibleAnnotations:' build/contract.txt
grep -F org.eclipse.pde.api.tools.annotations.NoImplement build/contract.txt
cat > build/InvalidUsage.java <<'JAVA'
import org.eclipse.pde.api.tools.annotations.NoImplement;

class InvalidUsage { @NoImplement void method() {} }
JAVA
if javac -J-Duser.language=en --release 8 -cp "$jar" -d build build/InvalidUsage.java > build/rejected.log 2>&1; then exit 1; fi
grep -F 'annotation interface not applicable' build/rejected.log

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/eclipse-pde-api-annotations.xml
%{repo_dir}/

%changelog
%autochangelog
