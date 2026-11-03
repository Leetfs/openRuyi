# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global platform_repo %{_datadir}/maven-repository/org/eclipse/platform
%global bundle_tools %{_libexecdir}/eclipse-equinox
%global bundle org.eclipse.e4.ui.workbench3
%global swt_version 3.133.0

Name:           eclipse-e4-workbench3
Version:        0.18.0
Release:        %autorelease
Summary:        Eclipse workbench test harness and diagnostics API
License:        EPL-2.0
URL:            https://eclipse.dev/eclipse/
VCS:            git:https://github.com/eclipse-platform/eclipse.platform.ui
#!RemoteAsset:  sha256:ae951404e00e81d269ec787cc5329f81872cd777240e2da719dc69acb2adec15
Source0:        https://github.com/eclipse-platform/eclipse.platform.ui/archive/refs/tags/R4_39.tar.gz
#!RemoteAsset:  sha256:9e62027b4ec261a63247dfe3c798a7af80fa2345dce1600dd743f19281377a9b
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/%{bundle}/%{version}/%{bundle}-%{version}.pom
BuildArch:      noarch

BuildRequires:  eclipse-equinox-build >= 4.39
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.core.runtime) == 3.34.200
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.swt) == %{swt_version}
Provides:       mvn(org.eclipse.platform:org.eclipse.e4.ui.workbench3) == %{version}
Requires:       eclipse-core-runtime >= 4.39
Requires:       eclipse-swt >= %{swt_version}

%description
These workbench compatibility interfaces connect a UI test harness to the
Eclipse application. The bundle also provides timeout and screenshot
diagnostics for workbench tests.

%prep
%autosetup -n eclipse.platform.ui-R4_39

%build
mkdir -p build/bundles
set -- %{platform_repo}/org.eclipse.swt.gtk.linux.*/%{swt_version}/*.jar
test "$#" = 1 && test -f "$1"
cp="$1"
for coordinate in org.eclipse.osgi/3.24.100 org.eclipse.equinox.common/3.20.300 org.eclipse.equinox.registry/3.12.600 org.eclipse.core.runtime/3.34.200 org.eclipse.swt/%{swt_version}; do
    name=${coordinate%%/*}; version=${coordinate##*/}
    cp="$cp:%{platform_repo}/$coordinate/$name-$version.jar"
done
%{bundle_tools}/build-bundle bundles/%{bundle} "$PWD/build/bundles/%{bundle}.jar" --release 17 --classpath "$cp"
printf '%%s\n' "$cp" > build/classpath

%install
%{bundle_tools}/install-bundles %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1}

%check
cat > build/Bridge.java <<'EOF'
import org.eclipse.ui.testing.ITestHarness;
import org.eclipse.ui.testing.TestableObject;
class Bridge {
    public static void main(String[] args) {
        var target = new TestableObject();
        int[] calls = {0};
        ITestHarness harness = () -> calls[0]++;
        target.setTestHarness(harness);
        if (target.getTestHarness() != harness) throw new AssertionError("Harness identity");
        target.testingStarting();
        target.runTest(() -> target.getTestHarness().runTests());
        target.testingFinished();
        if (calls[0] != 1) throw new AssertionError("Test callback");
    }
}
EOF
java -ea -cp "build/bundles/%{bundle}.jar:$(cat build/classpath)" build/Bridge.java

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/eclipse-e4-workbench3.xml
%{platform_repo}/%{bundle}/

%changelog
%autochangelog
