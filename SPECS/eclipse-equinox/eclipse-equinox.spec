# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global osgi_version 3.24.100
%global common_version 3.20.300
%global platform_repo %{_datadir}/maven-repository/org/eclipse/platform
%global bundle_tools %{_libexecdir}/eclipse-equinox

Name:           eclipse-equinox
Version:        4.39
Release:        %autorelease
Summary:        Eclipse Equinox OSGi framework and common runtime
License:        EPL-2.0 AND Apache-2.0
URL:            https://equinox.eclipseprojects.io/
VCS:            git:https://github.com/eclipse-equinox/equinox
#!RemoteAsset:  sha256:02519719c894588cf12930d66064422ddd875688e53e6679e133b71694fac5ea
Source0:        https://github.com/eclipse-equinox/equinox/archive/refs/tags/R4_39.tar.gz
#!RemoteAsset:  sha256:f94e22f5036629cc73ec0338d7e0b9c05c7683bd13678c166bca7f7c87e6fa81
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.osgi/%{osgi_version}/org.eclipse.osgi-%{osgi_version}.pom
# Published project model from Maven Central.
# https://repo.maven.apache.org/maven2/org/eclipse/platform/org.eclipse.equinox.common/3.20.300/org.eclipse.equinox.common-3.20.300.pom
Source2:        org.eclipse.equinox.common-%{common_version}.pom
#!RemoteAsset:  sha256:eb7a1d713eb919b146787629e22e4c975cb701f529a65d4d7e0fcd417558bf1c
Source3:        https://raw.githubusercontent.com/openRuyi-Project/openRuyi/4a77554c97ed3cb8134b682c245646fde8810999/LICENSES/MulanPSL-2.0.txt
Source4:        build-bundle.py
Source5:        install-bundles.py
Source6:        FrameworkCheck.java
Source7:        GenerateComponents.java
Source8:        RunJupiter.java
#!RemoteAsset:  sha256:12f66041680d6bf40084a17503f879bde9d806a83a38fe10c5749f215f544114
Source9:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.launcher/1.7.100/org.eclipse.equinox.launcher-1.7.100.pom
Source10:       RunFramework.java
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.eclipse.pde:org.eclipse.pde.api.tools.annotations) == 1.4.0
BuildRequires:  python3
BuildRequires:  unzip
Provides:       mvn(org.eclipse.platform:org.eclipse.osgi) == %{osgi_version}
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.common) == %{common_version}
Requires:       java-25-openjdk

%description
Equinox runs OSGi bundles and manages their class loaders, services and
lifecycle. The Common bundle supplies paths, status objects and progress
monitors shared by Eclipse components.

%package        build
Summary:        Build and install Eclipse bundles from PDE metadata
Provides:       eclipse-equinox-build(nested-jars)
Provides:       eclipse-equinox-build(nested-only-bundles)
Provides:       eclipse-equinox-build(framework-tests)
Provides:       eclipse-equinox-build(source-bundles)
Provides:       eclipse-equinox-build(parent-models)
License:        MulanPSL-2.0
Requires:       java-25-openjdk-devel
Requires:       javapackages-bootstrap
Requires:       python3

%description    build
These tools compile bundle sources, preserve OSGi manifests and install
the resulting JARs with their published Maven project models.

%package        launcher
Summary:        Java launcher for Equinox applications
License:        EPL-2.0
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.launcher) == 1.7.100
Requires:       %{name} = %{version}-%{release}

%description    launcher
The launcher starts the Equinox framework with Eclipse application defaults
and loads framework extensions from the installation.

%prep
%autosetup -n equinox-R4_39
echo '00bb3ffef4f5ff0aff95768819896fc58d64c62b4a90473ad27884e8fd2f8852  %{SOURCE2}' | sha256sum -c -
mkdir -p build/j9-src build/j9-api build/bundles
# The upstream OpenJ9 archive includes the Java sources for its compile-time hooks.
unzip -q bundles/org.eclipse.osgi/osgi/j9stubs.jar '*.java' -d build/j9-src
cp %{SOURCE3} MulanPSL-2.0.txt

%build
pde=%{_datadir}/maven-repository/org/eclipse/pde/org.eclipse.pde.api.tools.annotations/1.4.0/org.eclipse.pde.api.tools.annotations-1.4.0.jar
find build/j9-src -name '*.java' | sort > build/j9-sources
javac --release 8 -d build/j9-api @build/j9-sources
%{_bindir}/python3 %{SOURCE4} bundles/org.eclipse.osgi build/bundles/org.eclipse.osgi.jar --release 8 \
    --classpath "$pde:build/j9-api:%{_datadir}/java/javapackages-bootstrap/osgi.annotation.jar"
%{_bindir}/python3 %{SOURCE4} bundles/org.eclipse.equinox.common build/bundles/org.eclipse.equinox.common.jar --release 17 \
    --classpath "build/bundles/org.eclipse.osgi.jar:%{_datadir}/java/javapackages-bootstrap/osgi.cmpn.jar"

%{_bindir}/python3 %{SOURCE4} bundles/org.eclipse.equinox.launcher build/bundles/org.eclipse.equinox.launcher.jar --release 17 --classpath .

%install
%{_bindir}/python3 %{SOURCE5} %{buildroot} %{_datadir} %{name}-launcher build/bundles %{SOURCE9}
%{_bindir}/python3 %{SOURCE5} %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1} %{SOURCE2}
install -Dm755 %{SOURCE4} %{buildroot}%{bundle_tools}/build-bundle
install -Dm755 %{SOURCE5} %{buildroot}%{bundle_tools}/install-bundles
install -Dm644 %{SOURCE7} %{buildroot}%{bundle_tools}/GenerateComponents.java
install -Dm644 %{SOURCE8} %{buildroot}%{bundle_tools}/RunJupiter.java
install -Dm644 %{SOURCE10} %{buildroot}%{bundle_tools}/RunFramework.java

%check
framework=%{buildroot}%{platform_repo}/org.eclipse.osgi/%{osgi_version}/org.eclipse.osgi-%{osgi_version}.jar
common=%{buildroot}%{platform_repo}/org.eclipse.equinox.common/%{common_version}/org.eclipse.equinox.common-%{common_version}.jar
jar tf "$framework" > build/framework-contents
if grep -q '^com/ibm/oti/shared/' build/framework-contents; then exit 1; fi
java -cp "$framework" %{SOURCE6} "$common" "$PWD/build/framework-storage"
test_src=bundles/org.eclipse.equinox.common.tests/src
tests=$test_src/org/eclipse/equinox/common/tests
cp="$common:$framework:%{_datadir}/java/javapackages-bootstrap/junit.jar:%{_datadir}/java/javapackages-bootstrap/hamcrest-core.jar"
mkdir -p build/tests
javac --release 17 -cp "$cp" -sourcepath "$test_src" -d build/tests "$tests/TestProgressMonitor.java" "$tests/PathTest.java" \
    "$tests/SubProgressTest.java" "$tests/SubMonitorTest.java" "$tests/SubMonitorSmallTicksTest.java" "$tests/SliceProgressMonitorTest.java"
java -cp "build/tests:$cp" org.junit.runner.JUnitCore org.eclipse.equinox.common.tests.PathTest \
    org.eclipse.equinox.common.tests.SubProgressTest org.eclipse.equinox.common.tests.SubMonitorTest org.eclipse.equinox.common.tests.SubMonitorSmallTicksTest \
    org.eclipse.equinox.common.tests.SliceProgressMonitorTest

# Start the release launcher and initialize a fresh Equinox configuration.
mkdir -p build/launch/configuration
java -Dosgi.framework="file:$framework" -jar build/bundles/org.eclipse.equinox.launcher.jar -nosplash -consoleLog -initialize \
    -configuration "$PWD/build/launch/configuration" -data "$PWD/build/launch/workspace"
test -d build/launch/configuration/org.eclipse.osgi

# PDE Build and JDT Debug keep all Java classes in their nested bundle class path.
fixture="$PWD/build/nested-only"
mkdir -p "$fixture"/{src/demo,META-INF,check}
printf 'Manifest-Version: 1.0\nBundle-ManifestVersion: 2\nBundle-SymbolicName: org.openruyi.check.nested\nBundle-Version: 1.0.0.qualifier\nBundle-ClassPath: lib/model.jar\n' > "$fixture/META-INF/MANIFEST.MF"
printf 'bin.includes = META-INF/,lib/model.jar\nsource.lib/model.jar = src/\njars.compile.order = lib/model.jar\n' > "$fixture/build.properties"
echo 'package demo; public class Model {}' > "$fixture/src/demo/Model.java"
%{buildroot}%{_libexecdir}/eclipse-equinox/build-bundle "$fixture" "$fixture/example.jar" --release 17 --classpath "$fixture/src" --nested-classpath "$fixture/src"
(cd "$fixture/check"; jar xf ../example.jar lib/model.jar; jar tf lib/model.jar | grep -Fx demo/Model.class)
# Load the nested class through the installed bundle's real framework wiring.
cat > "$fixture/check/FrameworkSmoke.java" <<'EOF'
public class FrameworkSmoke {
    public static void main(String[] args) throws Exception {
        Class<?> model = Thread.currentThread().getContextClassLoader().loadClass("demo.Model");
        if (model.getDeclaredConstructor().newInstance().getClass() != model) throw new AssertionError();
    }
}
EOF
javac --release 17 -d "$fixture/check" "$fixture/check/FrameworkSmoke.java"
printf 'start %%s\n' "$fixture/example.jar" > "$fixture/bundles"
printf '%%s\n' "$fixture/check" > "$fixture/test-path"
java -cp build/bundles/org.eclipse.osgi.jar %{SOURCE10} "$fixture/state" "$fixture/bundles" org.openruyi.check.nested "$fixture/test-path" FrameworkSmoke

%files
%doc README.md
%license LICENSE NOTICE bundles/org.eclipse.osgi/container/src/about_files/LICENSE-2.0.txt
%{_datadir}/maven-metadata/eclipse-equinox.xml
%{platform_repo}/org.eclipse.osgi/
%{platform_repo}/org.eclipse.equinox.common/

%files build
%license MulanPSL-2.0.txt
%{bundle_tools}/

%files launcher
%license LICENSE NOTICE
%{_datadir}/maven-metadata/eclipse-equinox-launcher.xml
%{platform_repo}/org.eclipse.equinox.launcher/

%changelog
%autochangelog
