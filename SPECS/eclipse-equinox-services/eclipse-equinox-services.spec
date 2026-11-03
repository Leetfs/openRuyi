# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global platform_repo %{_datadir}/maven-repository/org/eclipse/platform
%global bundle_tools %{_libexecdir}/eclipse-equinox
%global prefs_api %{_datadir}/maven-repository/org/osgi/org.osgi.service.prefs/1.1.2/org.osgi.service.prefs-1.1.2.jar

Name:           eclipse-equinox-services
Version:        4.39
Release:        %autorelease
Summary:        Eclipse extension registry, preferences, applications and secure storage
License:        EPL-2.0 AND Apache-2.0
URL:            https://equinox.eclipseprojects.io/
VCS:            git:https://github.com/eclipse-equinox/equinox
#!RemoteAsset:  sha256:02519719c894588cf12930d66064422ddd875688e53e6679e133b71694fac5ea
Source0:        https://github.com/eclipse-equinox/equinox/archive/refs/tags/R4_39.tar.gz
#!RemoteAsset:  sha256:2b08376fa819bb9437bc70ca24ceb0f0db44de013feb717dbe699a294fb63127
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.registry/3.12.600/org.eclipse.equinox.registry-3.12.600.pom
#!RemoteAsset:  sha256:218c625a85b0e50414e9d191285614b6b2fea9ff7fd132132a6e0f9324333196
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.preferences/3.12.100/org.eclipse.equinox.preferences-3.12.100.pom
#!RemoteAsset:  sha256:71986751a6a7e6e272309b3a66ac921943e995096a5c8808d42e9a0cc251d5e8
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.app/1.7.600/org.eclipse.equinox.app-1.7.600.pom
#!RemoteAsset:  sha256:09ff2411d315eb1f97d460eaf8feb73229f651bfa09fa26885336d686764b93d
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.security/1.4.700/org.eclipse.equinox.security-1.4.700.pom
Source5:        ServicesCheck.java
#!RemoteAsset:  sha256:c79ebccb5fc9576fdfbe60e6ff8e6c263f8e08219cb85f4e10878fee01f7cd6c
Source6:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.concurrent/1.3.400/org.eclipse.equinox.concurrent-1.3.400.pom
#!RemoteAsset:  sha256:eb21464acffd766f24c9017f4cfb6571d706571425d87cb87b25c5fc4b5eb30f
Source7:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.osgi.compatibility.state/1.3.0/org.eclipse.osgi.compatibility.state-1.3.0.pom
BuildArch:      noarch

BuildRequires:  eclipse-equinox-build == %{version}
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.core.jobs) == 3.15.700
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.common) == 3.20.300
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.osgi) == 3.24.100
BuildRequires:  mvn(org.osgi:org.osgi.service.prefs) == 1.1.2
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.registry) == 3.12.600
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.preferences) == 3.12.100
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.app) == 1.7.600
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.security) == 1.4.700
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.concurrent) == 1.3.400
Provides:       mvn(org.eclipse.platform:org.eclipse.osgi.compatibility.state) == 1.3.0
Requires:       eclipse-core-jobs >= 3.15.700
Requires:       eclipse-equinox >= %{version}
Requires:       osgi-service-prefs >= 1.1.2

%description
These Equinox bundles manage extension points, discover Eclipse applications,
persist user and system preferences, and encode and protect stored credentials.

%prep
%autosetup -n equinox-R4_39

%build
framework=%{platform_repo}/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar
common=%{platform_repo}/org.eclipse.equinox.common/3.20.300/org.eclipse.equinox.common-3.20.300.jar
jobs=%{platform_repo}/org.eclipse.core.jobs/3.15.700/org.eclipse.core.jobs-3.15.700.jar
cp="$framework:$common:$jobs:%{prefs_api}:%{_datadir}/java/javapackages-bootstrap/osgi.cmpn.jar"
for service in registry preferences app security; do
    name=org.eclipse.equinox.$service
    jar="$PWD/build/bundles/$name.jar"
    %{bundle_tools}/build-bundle "bundles/$name" "$jar" --release 17 --classpath "$cp"
    cp="$cp:$jar"
done
for name in org.eclipse.equinox.concurrent org.eclipse.osgi.compatibility.state; do
    jar="$PWD/build/bundles/$name.jar"
    %{bundle_tools}/build-bundle "bundles/$name" "$jar" --release 17 --classpath "$cp"
    cp="$cp:$jar"
done
printf '%%s\n' "$cp" > build/classpath

%install
%{bundle_tools}/install-bundles %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE6} %{SOURCE7}

%check
cp="$(cat build/classpath):%{_datadir}/java/javapackages-bootstrap/junit.jar:%{_datadir}/java/javapackages-bootstrap/hamcrest-core.jar"
prefs=bundles/org.eclipse.equinox.preferences.tests/src/org/eclipse/equinox/preferences/tests
security=bundles/org.eclipse.equinox.security.tests/src/org/eclipse/equinox/internal/security/tests/storage
mkdir -p build/tests
javac --release 17 -cp "$cp" -d build/tests "$prefs/PreferenceMetadataTest.java" "$prefs/OsgiPreferenceMetadataStoreTest.java" \
    "$security/Base64Test.java" "$security/DetectPBECiphersTest.java"
cp %{_datadir}/java/javapackages-bootstrap/{junit,hamcrest-core}.jar build/tests/
cat > build/tests.MF <<'EOF'
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-SymbolicName: org.openruyi.equinox.tests
Bundle-Version: 1.0.0
Bundle-ClassPath: .,junit.jar,hamcrest-core.jar
Require-Bundle: org.eclipse.equinox.preferences,org.eclipse.equinox.security

EOF
jar --create --file build/tests.jar --manifest build/tests.MF -C build/tests .
framework=%{platform_repo}/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar
common=%{platform_repo}/org.eclipse.equinox.common/3.20.300/org.eclipse.equinox.common-3.20.300.jar
jobs=%{platform_repo}/org.eclipse.core.jobs/3.15.700/org.eclipse.core.jobs-3.15.700.jar
java -cp "$framework" %{SOURCE5} "$PWD/build/runtime-test" build/tests.jar "$common" "$jobs" %{prefs_api} \
    build/bundles/org.eclipse.equinox.{registry,preferences,app,security}.jar

# Run a future and add a bundle description to the resolver state.
cat > build/FutureAndState.java <<'EOF'
import java.util.Hashtable;
import org.eclipse.equinox.concurrent.future.ImmediateExecutor;
import org.eclipse.osgi.internal.resolver.StateObjectFactoryImpl;
import org.osgi.framework.Constants;
class FutureAndState {
    public static void main(String[] args) throws Exception {
        if (new ImmediateExecutor().execute(monitor -> 7, null).get() != 7) throw new AssertionError("Future result");
        var factory = new StateObjectFactoryImpl();
        var state = factory.createState(false);
        var headers = new Hashtable<String, String>();
        headers.put(Constants.BUNDLE_MANIFESTVERSION, "2");
        headers.put(Constants.BUNDLE_SYMBOLICNAME, "org.openruyi.state.check");
        headers.put(Constants.BUNDLE_VERSION, "1.2.3");
        var bundle = factory.createBundleDescription(state, headers, "memory:/state-check", 7);
        if (!state.addBundle(bundle) || state.getBundle(7) != bundle) throw new AssertionError("Resolver state");
    }
}
EOF
java -ea -cp "$cp" build/FutureAndState.java

%files
%doc README.md
%license LICENSE NOTICE bundles/org.eclipse.equinox.app/about_files/LICENSE-2.0.txt
%{_datadir}/maven-metadata/eclipse-equinox-services.xml
%{platform_repo}/org.eclipse.equinox.registry/
%{platform_repo}/org.eclipse.equinox.preferences/
%{platform_repo}/org.eclipse.equinox.app/
%{platform_repo}/org.eclipse.equinox.security/

%{platform_repo}/org.eclipse.equinox.concurrent/
%{platform_repo}/org.eclipse.osgi.compatibility.state/

%changelog
%autochangelog
