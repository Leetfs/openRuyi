# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global platform_repo %{_datadir}/maven-repository/org/eclipse/platform
%global bundle_tools %{_libexecdir}/eclipse-equinox

Name:           eclipse-text
Version:        4.39
Release:        %autorelease
Summary:        Eclipse text models, edit operations and command framework
License:        EPL-2.0
URL:            https://eclipse.dev/eclipse/
VCS:            git:https://github.com/eclipse-platform/eclipse.platform.ui
#!RemoteAsset:  sha256:ae951404e00e81d269ec787cc5329f81872cd777240e2da719dc69acb2adec15
Source0:        https://github.com/eclipse-platform/eclipse.platform.ui/archive/refs/tags/R4_39.tar.gz
# Published Maven model: https://repo.maven.apache.org/maven2/org/eclipse/platform/org.eclipse.core.commands/3.12.500/org.eclipse.core.commands-3.12.500.pom
Source1:        org.eclipse.core.commands-3.12.500.pom
# Published Maven model: https://repo.maven.apache.org/maven2/org/eclipse/platform/org.eclipse.text/3.14.600/org.eclipse.text-3.14.600.pom
Source2:        org.eclipse.text-3.14.600.pom
# Keep the annotation snapshot test independent of HashMap iteration order.
Patch2000:      2000-Test-annotation-snapshots-without-assuming-hash-order.patch
BuildArch:      noarch

BuildRequires:  eclipse-equinox-build >= %{version}
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.core.runtime) == 3.34.200
BuildRequires:  mvn(org.eclipse.platform:org.eclipse.equinox.preferences) == 3.12.100
BuildRequires:  mvn(org.osgi:org.osgi.service.prefs) == 1.1.2
Provides:       mvn(org.eclipse.platform:org.eclipse.core.commands) == 3.12.500
Provides:       mvn(org.eclipse.platform:org.eclipse.text) == 3.14.600
Requires:       eclipse-core-runtime >= %{version}

%description
Eclipse Text provides documents, line tracking, text edits, undo and
projection models for editors and other tools. Eclipse Core Commands
defines command handlers, parameters and execution events.

%prep
%autosetup -n eclipse.platform.ui-R4_39 -p1
echo 'c83fb8b7475ceb600d7e28f1c327c68e1cd26851dec8410ab619fff56d7b4a82  %{SOURCE1}' | sha256sum --check --status
echo '7a3ff04136efd159fca4dd10124da2743f9f48550deec85f4784d30f1648431d  %{SOURCE2}' | sha256sum --check --status

%build
mkdir -p build/bundles
cp=%{_datadir}/maven-repository/org/osgi/org.osgi.service.prefs/1.1.2/org.osgi.service.prefs-1.1.2.jar
for coordinate in org.eclipse.osgi/3.24.100 org.eclipse.equinox.common/3.20.300 org.eclipse.core.jobs/3.15.700 org.eclipse.equinox.registry/3.12.600 org.eclipse.equinox.preferences/3.12.100 org.eclipse.core.runtime/3.34.200; do
    name=${coordinate%%/*}
    version=${coordinate##*/}
    cp="$cp:%{platform_repo}/$coordinate/$name-$version.jar"
done
for name in org.eclipse.core.commands org.eclipse.text; do
    jar="$PWD/build/bundles/$name.jar"
    %{bundle_tools}/build-bundle "bundles/$name" "$jar" --release 17 --classpath "$cp"
    cp="$jar:$cp"
done
printf '%%s\n' "$cp" > build/classpath

%install
%{bundle_tools}/install-bundles %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1} %{SOURCE2}

%check
cp=$(cat build/classpath)
for library in junit-platform-launcher junit-platform-engine junit-platform-commons junit-platform-suite-api junit-jupiter-api junit-jupiter-engine apiguardian-api opentest4j; do
    cp="$cp:%{_datadir}/java/javapackages-bootstrap/$library.jar"
done
testdir=tests/org.eclipse.text.tests
mkdir -p build/tests
find "$testdir/src" "$testdir/projection" -name '*.java' | sort > build/test-sources
javac --release 17 -encoding UTF-8 -cp "$cp" -d build/tests @build/test-sources
classes=$(sed -e 's@^.*org/eclipse/@org/eclipse/@' -e 's@\.java$@@' -e 's@/@.@g' build/test-sources)
testcp="build/tests:$testdir/src:$testdir/projection:$cp"
java -ea -cp "$testcp" %{bundle_tools}/RunJupiter.java $classes
for hash in 1 2 3; do
    java -ea -XX:+UnlockExperimentalVMOptions -XX:hashCode=$hash -cp "$testcp" \
        %{bundle_tools}/RunJupiter.java org.eclipse.text.tests.Bug401391Test
done

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/eclipse-text.xml
%{platform_repo}/org.eclipse.core.commands/
%{platform_repo}/org.eclipse.text/

%changelog
%autochangelog
