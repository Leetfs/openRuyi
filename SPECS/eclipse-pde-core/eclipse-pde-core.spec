# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global revision 33d7ebb8f2c10fdf0189b094f127cf3e9d0bd894
%global repo %{_datadir}/maven-repository
%global platform %{repo}/org/eclipse/platform
%global tools %{_libexecdir}/eclipse-equinox
Name:           eclipse-pde-core
Version:        3.21.200
Release:        %autorelease
Summary:        Eclipse plug-in development environment and build tools
License:        EPL-2.0
URL:            https://eclipse.dev/pde/
VCS:            git:https://github.com/eclipse-pde/eclipse.pde
#!RemoteAsset:  sha256:50ef79d90ceb107ef64446b9ee78f8f44310fcfd42c0d2eb9adb62e86cf2b87f
Source0:        https://github.com/eclipse-pde/eclipse.pde/archive/%{revision}.tar.gz?/pde-%{revision}.tar.gz
#!RemoteAsset:  sha256:5d649bf2f9b3fc54ced126a1ac1a76715baa4d7127e1268c61b34efd6f20df40
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/pde/org.eclipse.pde.core/%{version}/org.eclipse.pde.core-%{version}.pom
#!RemoteAsset:  sha256:5680bdef7e6337ef468e3f3f34cfa8438ef0f317f0b1172f2f30b3908a904ac2
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/pde/org.eclipse.pde.build/3.12.900/org.eclipse.pde.build-3.12.900.pom
Source3:        PdeTargetCheck.java
Source4:        pde-test-bundles.py
#!RemoteAsset:  sha256:d0aa7a7039a5d58b0040e1635824a0739580a4d59773a611607895ae53f36fbe
Source5:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/pde/org.eclipse.pde.api.tools/1.3.1100/org.eclipse.pde.api.tools-1.3.1100.pom
Source6:        PdeApiDescription.java
Source7:        check-api-tools.sh
BuildArch:      noarch
BuildRequires:  bndtools-api
BuildRequires:  eclipse-core-filebuffers
BuildRequires:  eclipse-e4-core
BuildRequires:  eclipse-equinox-build(framework-tests)
BuildRequires:  eclipse-equinox-build(nested-only-bundles)
BuildRequires:  eclipse-jdt-debug
BuildRequires:  eclipse-p2-director
BuildRequires:  eclipse-team-core
BuildRequires:  felix-scr
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.bndlib) == 7.2.3
BuildRequires:  mvn(org.eclipse.jdt:ecj) == 3.45.0
BuildRequires:  mvn(org.ow2.asm:asm-tree) == 9.10.1
BuildRequires:  python3
BuildRequires:  slf4j-jdk14
BuildRequires:  unzip
Provides:       mvn(org.eclipse.pde:org.eclipse.pde.core) == %{version}
Provides:       mvn(org.eclipse.pde:org.eclipse.pde.build) == 3.12.900
Requires:       bndtools-api
Requires:       eclipse-core-filebuffers
Requires:       eclipse-e4-core
Requires:       eclipse-jdt-debug
Requires:       eclipse-p2-director
Requires:       eclipse-team-core
Requires:       mvn(biz.aQute.bnd:biz.aQute.bndlib) == 7.2.3
Requires:       slf4j-jdk14

%description
Eclipse PDE provides models for plug-ins, features and target platforms.
PDE Build and its Ant tasks assemble Eclipse bundles and products.

%package     -n eclipse-pde-apitools
Version:        1.3.1100
Summary:        Eclipse PDE API analysis and Ant tasks
Provides:       mvn(org.eclipse.pde:org.eclipse.pde.api.tools) == 1.3.1100
Requires:       eclipse-pde-core
Requires:       mvn(org.eclipse.jdt:ecj) == 3.45.0
Requires:       mvn(org.ow2.asm:asm-tree) == 9.10.1

%description -n eclipse-pde-apitools
Eclipse PDE API Tools analyzes Java API signatures and enforces restrictions
declared in plug-ins. Its Ant tasks generate API descriptions for builds.

%prep
%autosetup -n eclipse.pde-%{revision}

%build
mkdir -p build/{bundles,classpath}
cp=$(find %{repo}/biz/aQute/bnd %{repo}/org/bndtools %{repo}/org/eclipse/{platform,jdt} %{repo}/org/osgi -name '*.jar' ! -name '*-sources.jar' -printf '%%p:')
cp="$cp%{_datadir}/java/javapackages-bootstrap/ant.jar:%{_datadir}/java/javapackages-bootstrap/ant-launcher.jar:%{_datadir}/java/javapackages-bootstrap/aQute.libg.jar"
for path in \
    "org/eclipse/platform/org.eclipse.equinox.p2.jarprocessor/1.3.600/org.eclipse.equinox.p2.jarprocessor-1.3.600.jar lib/jarprocessor-ant.jar" \
    "org/eclipse/platform/org.eclipse.equinox.p2.repository.tools/2.4.900/org.eclipse.equinox.p2.repository.tools-2.4.900.jar lib/repository-tools-ant.jar" \
    "org/eclipse/jdt/org.eclipse.jdt.debug/3.25.100/org.eclipse.jdt.debug-3.25.100.jar jdimodel.jar"; do
    read -r artifact nested <<< "$path"
    file="$PWD/build/classpath/$(basename "$nested")"
    unzip -p "%{repo}/$artifact" "$nested" > "$file"
    cp="$file:$cp"
done
jar=build/bundles/org.eclipse.pde.build.jar
%{tools}/build-bundle build/org.eclipse.pde.build "$jar" --release 17 --classpath "$cp" --nested-classpath "$cp"
cp="$PWD/$jar:$cp"
for nested in pdebuild.jar lib/pdebuild-ant.jar; do
    file="$PWD/build/classpath/$(basename "$nested")"
    unzip -p "$jar" "$nested" > "$file"
    cp="$file:$cp"
done
%{tools}/build-bundle ui/org.eclipse.pde.core build/bundles/org.eclipse.pde.core.jar --release 17 --classpath "$cp"
printf '%%s\n' "$cp" > build/compiler-classpath
api=apitools/org.eclipse.pde.api.tools
sed -i 's/^Bundle-Version: 1.3.1100.qualifier/Bundle-Version: 1.3.1100.v20260212-1922/' "$api/META-INF/MANIFEST.MF"
# This script is excluded from the binary by the upstream build.properties.
rm "$api/scripts/buildApiToolsAntSupportJar.xml"
ecj=%{repo}/org/eclipse/jdt/ecj/3.45.0/ecj-3.45.0.jar
asm=%{repo}/org/ow2/asm
api_cp="$ecj:$asm/asm/9.10.1/asm-9.10.1.jar:$asm/asm-tree/9.10.1/asm-tree-9.10.1.jar:$PWD/build/bundles/org.eclipse.pde.core.jar:$cp"
%{tools}/build-bundle "$api" build/bundles/org.eclipse.pde.api.tools.jar --release 17 --classpath "$api_cp" --nested-classpath "$api_cp"


%install
%{tools}/install-bundles %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1} %{SOURCE2}

%{tools}/install-bundles --qualifier v20260212-1922 %{buildroot} %{_datadir} eclipse-pde-apitools build/bundles %{SOURCE5}

%check
mkdir -p build/{tests,feature,state}
cp="build/bundles/org.eclipse.pde.core.jar:$(cat build/compiler-classpath)"
javac --release 17 -proc:none -cp "$cp" -d build/tests %{SOURCE3}
printf '%%s\n' '<feature id="org.openruyi.check" label="PDE target test" version="1.2.3"/>' > build/feature/feature.xml
python3 %{SOURCE4} %{repo} build/bundles > build/test-bundles
printf '%%s\n' "$PWD/build/tests" > build/test-path
framework=%{platform}/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar
java -cp "$framework" %{tools}/RunFramework.java "$PWD/build/state" build/test-bundles org.eclipse.pde.core build/test-path \
    PdeTargetCheck "$PWD/build/bundles/org.eclipse.pde.build.jar" "$PWD/build/feature"

bash %{SOURCE7} %{SOURCE6} "$framework"

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/eclipse-pde-core.xml
%{repo}/org/eclipse/pde/org.eclipse.pde.core/
%{repo}/org/eclipse/pde/org.eclipse.pde.build/

%files -n eclipse-pde-apitools
%license LICENSE NOTICE
%{_datadir}/maven-metadata/eclipse-pde-apitools.xml
%{repo}/org/eclipse/pde/org.eclipse.pde.api.tools/

%changelog
%autochangelog
