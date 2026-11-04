# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global tools_dir %{_libexecdir}/eclipse-equinox
%global maven_repo %{_datadir}/maven-repository
%global platform_repo %{maven_repo}/org/eclipse/platform
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap

Name:           eclipse-debug-core
Version:        4.39
Release:        %autorelease
Summary:        Eclipse debug and launch framework
License:        EPL-2.0
URL:            https://eclipse.dev/eclipse/
VCS:            git:https://github.com/eclipse-platform/eclipse.platform
#!RemoteAsset:  sha256:973e213b8f8abbbfe397ec12d3d43c2a31fa81231646f29c473fec877b6bbd53
Source0:        https://github.com/eclipse-platform/eclipse.platform/archive/refs/tags/R4_39.tar.gz
#!RemoteAsset:  sha256:e868ba5830d4d30a3adcb6e104ee74de2cf1a6b48b48a16f1f144a4a399c93d9
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.debug.core/3.23.200/org.eclipse.debug.core-3.23.200.pom
Source2:        core-test-bundles.sh
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  eclipse-core-resources
BuildRequires:  eclipse-equinox-build(framework-tests)
BuildRequires:  felix-scr
BuildRequires:  osgi-service-prefs
Provides:       mvn(org.eclipse.platform:org.eclipse.debug.core) == 3.23.200
Requires:       eclipse-core-resources

%description
The Eclipse Debug framework manages launch configurations, processes,
breakpoints and debugger events.

%prep
%autosetup -n eclipse.platform-R4_39

%build
mkdir -p build/bundles
cp=$(find %{platform_repo} -name '*.jar' ! -name '*-sources.jar' -printf '%%p:')
cp="$cp%{bootstrap_java}/osgi.cmpn.jar:%{bootstrap_java}/osgi.annotation.jar:%{bootstrap_java}/ant.jar:%{bootstrap_java}/ant-launcher.jar"
for dir in debug/org.eclipse.debug.core; do
    name=$(basename "$dir")
    jar="$PWD/build/bundles/$name.jar"
    %{tools_dir}/build-bundle "$dir" "$jar" --release 17 --classpath "$cp"
    cp="$jar:$cp"
done
printf '%%s\n' "$cp" > build/classpath

%install
%{tools_dir}/install-bundles %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1}

%check
cp=$(cat build/classpath)
mkdir -p build/tests
# Start the real debug services headlessly. The upstream extension opens the workbench for UI tests.
src=debug/org.eclipse.debug.tests/src/org/eclipse/debug/tests/launching
sed -e '/^import org.eclipse.debug.tests.DebugTestExtension;/d' -e '/^@ExtendWith(DebugTestExtension.class)/d' \
    -e 's|ArgumentsPrinter.class.getResource("/")|ArgumentsPrinter.class.getProtectionDomain().getCodeSource().getLocation()|' \
    "$src/ArgumentParsingTests.java" > build/ArgumentParsingTests.java
javac --release 17 -proc:none -cp "$cp:%{bootstrap_java}/*" -d build/tests %{tools_dir}/RunJupiter.java "$src/ArgumentsPrinter.java" build/ArgumentParsingTests.java
bash %{SOURCE2} > build/bundles.list
printf 'start %%s\n' "$PWD/build/bundles/org.eclipse.debug.core.jar" >> build/bundles.list
echo "$PWD/build/tests" > build/testpath
for n in junit-jupiter-api junit-jupiter-engine junit-platform-launcher junit-platform-engine junit-platform-commons opentest4j apiguardian-api assertj-core; do
    echo "%{bootstrap_java}/$n.jar" >> build/testpath
done
framework=%{platform_repo}/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar
java -cp "$framework" %{tools_dir}/RunFramework.java "$PWD/build/state" build/bundles.list org.eclipse.debug.core build/testpath RunJupiter org.eclipse.debug.tests.launching.ArgumentParsingTests

%files
%license LICENSE
%{_datadir}/maven-metadata/eclipse-debug-core.xml
%{platform_repo}/org.eclipse.debug.core/

%changelog
%autochangelog
