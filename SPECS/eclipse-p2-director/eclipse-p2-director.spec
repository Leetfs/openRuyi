# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global platform_repo %{_datadir}/maven-repository/org/eclipse/platform
%global bundle_tools %{_libexecdir}/eclipse-equinox

Name:           eclipse-p2-director
Version:        4.39
Release:        %autorelease
Summary:        Eclipse provisioning planner, installation engine and command-line director
License:        EPL-2.0
URL:            https://equinox.eclipseprojects.io/p2/
VCS:            git:https://github.com/eclipse-equinox/p2
#!RemoteAsset:  sha256:b35991e28613e4ccb4a5aefc16b7aa6bd4885cfabeea63f671772727e490b7cc
Source0:        https://github.com/eclipse-equinox/p2/archive/refs/tags/R4_39.tar.gz?/p2-R4_39.tar.gz
#!RemoteAsset:  sha256:f0928678f0b81406246c8761a64dba00e8d38a8b96a97215b32aea6bea9c36e2
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.frameworkadmin/2.3.500/org.eclipse.equinox.frameworkadmin-2.3.500.pom
#!RemoteAsset:  sha256:ced5c7a2f0bf260ee7e93b57cd2ae0e1e26162f048c7642fcc297d322f3760d6
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.frameworkadmin.equinox/1.3.400/org.eclipse.equinox.frameworkadmin.equinox-1.3.400.pom
#!RemoteAsset:  sha256:d308ee787d506937e19099a0ffac94c22a667c9f3c3fe16ab5442593607c7719
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.p2.director/2.6.800/org.eclipse.equinox.p2.director-2.6.800.pom
#!RemoteAsset:  sha256:63d810c97192915ba01d068ff77fdb464db273fd4eeda4ce7aa300ec95e587a2
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.p2.director.app/1.3.900/org.eclipse.equinox.p2.director.app-1.3.900.pom
#!RemoteAsset:  sha256:7a71ae06ea1372eec436a4e1a79e17ca06042e4829b096ed12771ee4f1f4a321
Source5:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.p2.engine/2.11.0/org.eclipse.equinox.p2.engine-2.11.0.pom
#!RemoteAsset:  sha256:df621e02efefbad0079c62bc531f3d678c6971614b19980ade7ef1dcdd342b84
Source6:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.p2.garbagecollector/1.3.700/org.eclipse.equinox.p2.garbagecollector-1.3.700.pom
#!RemoteAsset:  sha256:70e7e7a3aeba8df5ace6ce23f0038081d1b07c891b0415b3e2ee97d88c4a8a6a
Source7:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.p2.publisher.eclipse/1.6.700/org.eclipse.equinox.p2.publisher.eclipse-1.6.700.pom
#!RemoteAsset:  sha256:868e2c87f75cb9acc97bf6983529361c39fd3b122e3513ce0e2e6183fd12064a
Source8:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.p2.repository.tools/2.4.900/org.eclipse.equinox.p2.repository.tools-2.4.900.pom
#!RemoteAsset:  sha256:2ba057d5fa0382c08bc5858e1bc2008f38fd3147c9f24c97cfde324e4516ff22
Source9:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.p2.touchpoint.eclipse/2.4.600/org.eclipse.equinox.p2.touchpoint.eclipse-2.4.600.pom
#!RemoteAsset:  sha256:821d6a3b0103bb9eaf4e7084d7d2d9dc98ed1dde03ac184174c4bd29f159e47b
Source10:       https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.p2.touchpoint.natives/1.5.800/org.eclipse.equinox.p2.touchpoint.natives-1.5.800.pom
#!RemoteAsset:  sha256:39fc44ad2906377a53c71613111259e00d276d36c77bd6d6c59de6b944a301b9
Source11:       https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.p2.updatesite/1.3.800/org.eclipse.equinox.p2.updatesite-1.3.800.pom
#!RemoteAsset:  sha256:fccc57d92b9dfdb64157a42885f9b56799abc019897995a34ed68aa55bf064d8
Source12:       https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.simpleconfigurator/1.5.700/org.eclipse.equinox.simpleconfigurator-1.5.700.pom
#!RemoteAsset:  sha256:d92b4f78a6dc99f5fda693ff7e90772032d8b9c9aeea9c994c5b0fe5a5846bd2
Source13:       https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.simpleconfigurator.manipulator/2.3.600/org.eclipse.equinox.simpleconfigurator.manipulator-2.3.600.pom
Source14:       check-director.sh
#!RemoteAsset:  sha256:6d15f036f03aebef1a83c6ff45fb0cfb42d081bc6cf1b7fb7fff0ba3237f03ed
Source15:       https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.equinox.p2.transport.ecf/1.4.600/org.eclipse.equinox.p2.transport.ecf-1.4.600.pom
BuildArch:      noarch

BuildRequires:  eclipse-equinox-build(nested-jars)
BuildRequires:  mvn(org.eclipse.ecf:org.eclipse.ecf.provider.filetransfer) == 3.3.100
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.launcher) == 1.7.100
BuildRequires:  javapackages-bootstrap
BuildRequires:  java-25-openjdk-devel
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.core.runtime) == 3.34.200
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.concurrent) == 1.3.400
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.p2.jarprocessor) == 1.3.600
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.p2.publisher) == 1.9.600
BuildRequires:  mvn(org.ow2.sat4j:org.ow2.sat4j.pb) == 2.3.6
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.frameworkadmin) == 2.3.500
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.frameworkadmin.equinox) == 1.3.400
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.p2.director) == 2.6.800
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.p2.director.app) == 1.3.900
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.p2.engine) == 2.11.0
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.p2.garbagecollector) == 1.3.700
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.p2.publisher.eclipse) == 1.6.700
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.p2.repository.tools) == 2.4.900
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.p2.touchpoint.eclipse) == 2.4.600
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.p2.touchpoint.natives) == 1.5.800
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.p2.updatesite) == 1.3.800
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.simpleconfigurator) == 1.5.700
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.simpleconfigurator.manipulator) == 2.3.600
Provides:       mvn(org.eclipse.platform:org.eclipse.equinox.p2.transport.ecf) == 1.4.600
Requires:       eclipse-ecf >= 3.13.0
Requires:       eclipse-equinox-p2 >= 4.38
Requires:       eclipse-equinox-services >= 4.39
Requires:       sat4j >= 2.3.6

%description
The p2 director computes installation plans, applies them to Eclipse profiles
and installs or removes features and their required bundles. This package also
provides the publisher, repository and configuration tools used by Tycho.

%prep
%autosetup -n p2-R4_39
mkdir -p build/classes build/bundles build/jarprocessor
cat > build/modules <<'MODULES'
org.eclipse.equinox.frameworkadmin
org.eclipse.equinox.frameworkadmin.equinox
org.eclipse.equinox.p2.director
org.eclipse.equinox.p2.director.app
org.eclipse.equinox.p2.engine
org.eclipse.equinox.p2.garbagecollector
org.eclipse.equinox.p2.publisher.eclipse
org.eclipse.equinox.p2.repository.tools
org.eclipse.equinox.p2.touchpoint.eclipse
org.eclipse.equinox.p2.touchpoint.natives
org.eclipse.equinox.p2.updatesite
org.eclipse.equinox.simpleconfigurator
org.eclipse.equinox.simpleconfigurator.manipulator
org.eclipse.equinox.p2.transport.ecf
MODULES

%build
# Compile the related planner, engine and publisher APIs together to resolve their cyclic imports.
base=$PWD
(cd build/jarprocessor && jar xf %{platform_repo}/org.eclipse.equinox.p2.jarprocessor/1.3.600/org.eclipse.equinox.p2.jarprocessor-1.3.600.jar lib/jarprocessor-ant.jar)
test -s build/jarprocessor/lib/jarprocessor-ant.jar
classpath=$(rpm -ql eclipse-equinox eclipse-equinox-services eclipse-core-jobs eclipse-core-runtime eclipse-equinox-p2 \
    bouncycastle eclipse-ecf eclipse-core-net jna sat4j xz-java | sed -n '/^\/usr\/share\/maven-repository\/.*[.]jar$/ { /-sources[.]jar$/!p; }' | sort -u | paste -sd:)
classpath="$classpath:%{_datadir}/java/javapackages-bootstrap/osgi.cmpn.jar:%{_datadir}/java/javapackages-bootstrap/osgi.annotation.jar:%{_datadir}/java/javapackages-bootstrap/ant.jar"
nested="$base/build/jarprocessor/lib/jarprocessor-ant.jar:%{_datadir}/java/javapackages-bootstrap/ant.jar"
while read -r name; do
    find "bundles/$name/src" -name '*.java' -print
    if test -d "bundles/$name/src_ant"; then find "bundles/$name/src_ant" -name '*.java' -print; fi
done < build/modules | sort > build/java-sources
javac --release 17 -proc:none -encoding UTF-8 -cp "$classpath:$nested" -d build/classes @build/java-sources
while read -r name; do
    %{bundle_tools}/build-bundle "bundles/$name" "build/bundles/$name.jar" --release 17 \
        --classpath "$base/build/classes:$classpath" --nested-classpath "$nested"
done < build/modules

%install
%{bundle_tools}/install-bundles %{buildroot} %{_datadir} %{name} build/bundles \
    %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} \
    %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE15}

%check
# Verify the Ant tasks declared by the director, publisher and repository tools.
for task in org.eclipse.equinox.p2.director.app:ant_tasks/director-ant.jar \
    org.eclipse.equinox.p2.publisher.eclipse:ant_tasks/pdepublishing-ant.jar \
    org.eclipse.equinox.p2.repository.tools:lib/repository-tools-ant.jar; do
    jar tf "build/bundles/${task%%:*}.jar" | grep -Fx "${task#*:}"
done
# Start the provisioning services and install and uninstall the upstream feature and its required plugin.
framework=%{platform_repo}/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar
osgi=%{_datadir}/maven-repository/org/osgi
bundles=("$osgi/org.osgi.util.function/1.2.0/org.osgi.util.function-1.2.0.jar" \
    "$osgi/org.osgi.util.promise/1.3.0/org.osgi.util.promise-1.3.0.jar" \
    "$osgi/org.osgi.service.component/1.5.1/org.osgi.service.component-1.5.1.jar" \
    %{_datadir}/maven-repository/org/apache/felix/org.apache.felix.scr/2.2.18/org.apache.felix.scr-2.2.18.jar \
    %{platform_repo}/org.eclipse.equinox.common/3.20.300/org.eclipse.equinox.common-3.20.300.jar \
    %{platform_repo}/org.eclipse.core.jobs/3.15.700/org.eclipse.core.jobs-3.15.700.jar \
    "$osgi/org.osgi.service.prefs/1.1.2/org.osgi.service.prefs-1.1.2.jar")
for coordinate in org.eclipse.equinox.registry/3.12.600 org.eclipse.equinox.preferences/3.12.100 org.eclipse.equinox.app/1.7.600 \
    org.eclipse.equinox.security/1.4.700 org.eclipse.core.contenttype/3.9.800 org.eclipse.core.runtime/3.34.200; do
    name=${coordinate%%/*}
    version=${coordinate##*/}
    bundles+=("%{platform_repo}/$coordinate/$name-$version.jar")
done
for module in bcprov bcutil bcpg; do
    bundles+=("%{_datadir}/maven-repository/org/bouncycastle/$module-jdk18on/1.86/$module-jdk18on-1.86.jar")
done

platform=%{platform_repo}
repo=%{_datadir}/maven-repository
for coord in org.eclipse.equinox.concurrent/1.3.400 org.eclipse.osgi.compatibility.state/1.3.0; do
    bundles+=("$platform/$coord/${coord%%/*}-${coord##*/}.jar")
done
bundles+=("$repo/org/tukaani/xz/1.12/xz-1.12.jar")
for name in core metadata repository jarprocessor artifact.repository metadata.repository publisher; do
    binary=("$platform/org.eclipse.equinox.p2.$name"/*/org.eclipse.equinox.p2.$name-[0-9]*.jar)
    test "${#binary[@]}" = 1
    bundles+=("${binary[0]}")
done
for mod in core pb; do
    bundles+=("$repo/org/ow2/sat4j/org.ow2.sat4j.$mod/2.3.6/org.ow2.sat4j.$mod-2.3.6.jar")
done
for name in jna jna-platform; do
    bundles+=("$repo/net/java/dev/jna/$name/5.18.1/$name-5.18.1.jar")
done
bundles+=("$platform/org.eclipse.core.net/1.5.800/org.eclipse.core.net-1.5.800.jar")
for coord in org.eclipse.ecf.identity/3.10.0 org.eclipse.ecf/3.13.0 org.eclipse.ecf.filetransfer/5.1.103 org.eclipse.ecf.provider.filetransfer/3.3.100; do
    bundles+=("$repo/org/eclipse/ecf/$coord/${coord%%/*}-${coord##*/}.jar")
done
bash %{SOURCE14} %{platform_repo}/org.eclipse.equinox.launcher/1.7.100/org.eclipse.equinox.launcher-1.7.100.jar "$framework" bundles/org.eclipse.equinox.p2.tests/testData/reconciler/basicRepo "${bundles[@]}" build/bundles/*.jar

%files
%license LICENSE NOTICE
%doc README.md
%{_datadir}/maven-metadata/eclipse-p2-director.xml
%{platform_repo}/org.eclipse.equinox.frameworkadmin/
%{platform_repo}/org.eclipse.equinox.frameworkadmin.equinox/
%{platform_repo}/org.eclipse.equinox.p2.director/
%{platform_repo}/org.eclipse.equinox.p2.director.app/
%{platform_repo}/org.eclipse.equinox.p2.engine/
%{platform_repo}/org.eclipse.equinox.p2.garbagecollector/
%{platform_repo}/org.eclipse.equinox.p2.publisher.eclipse/
%{platform_repo}/org.eclipse.equinox.p2.repository.tools/
%{platform_repo}/org.eclipse.equinox.p2.touchpoint.eclipse/
%{platform_repo}/org.eclipse.equinox.p2.touchpoint.natives/
%{platform_repo}/org.eclipse.equinox.p2.updatesite/
%{platform_repo}/org.eclipse.equinox.simpleconfigurator/
%{platform_repo}/org.eclipse.equinox.simpleconfigurator.manipulator/

%{platform_repo}/org.eclipse.equinox.p2.transport.ecf/

%changelog
%autochangelog
