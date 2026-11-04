# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global tools_dir %{_libexecdir}/eclipse-equinox
%global maven_repo %{_datadir}/maven-repository
%global platform_repo %{maven_repo}/org/eclipse/platform
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap

Name:           eclipse-team-core
Version:        4.39
Release:        %autorelease
Summary:        Eclipse Team and resource comparison APIs
License:        EPL-2.0
URL:            https://eclipse.dev/eclipse/
VCS:            git:https://github.com/eclipse-platform/eclipse.platform
#!RemoteAsset:  sha256:973e213b8f8abbbfe397ec12d3d43c2a31fa81231646f29c473fec877b6bbd53
Source0:        https://github.com/eclipse-platform/eclipse.platform/archive/refs/tags/R4_39.tar.gz
#!RemoteAsset:  sha256:0eb3394a841d99815569d9f9204d8a19dfbbed1b24686f93c74c46617c48236e
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.compare.core/3.8.800/org.eclipse.compare.core-3.8.800.pom
#!RemoteAsset:  sha256:cd19a3e7feca3a45861b26c3ce4ea8946dfaba5019015d97dca3933ae0d47043
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.team.core/3.10.1000/org.eclipse.team.core-3.10.1000.pom
Source3:        LineFixtures.java
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  eclipse-core-resources
Provides:       mvn(org.eclipse.platform:org.eclipse.compare.core) == 3.8.800
Provides:       mvn(org.eclipse.platform:org.eclipse.team.core) == 3.10.1000
Requires:       eclipse-core-resources

%description
The Team API manages workspace synchronization and repository providers.
The Compare core supplies sequence differencing and three-way merge
ranges.

%prep
%autosetup -n eclipse.platform-R4_39

%build
mkdir -p build/bundles
cp=$(find %{platform_repo} -name '*.jar' ! -name '*-sources.jar' -printf '%%p:')
cp="$cp%{bootstrap_java}/osgi.cmpn.jar:%{bootstrap_java}/osgi.annotation.jar:%{bootstrap_java}/ant.jar:%{bootstrap_java}/ant-launcher.jar"
for dir in team/bundles/org.eclipse.compare.core team/bundles/org.eclipse.team.core; do
    name=$(basename "$dir")
    jar="$PWD/build/bundles/$name.jar"
    %{tools_dir}/build-bundle "$dir" "$jar" --release 17 --classpath "$cp"
    cp="$jar:$cp"
done
printf '%%s\n' "$cp" > build/classpath

%install
%{tools_dir}/install-bundles %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1} %{SOURCE2}

%check
cp=$(cat build/classpath)
mkdir -p build/tests
# Run the original three-way cases with the upstream stream comparator in this headless build.
test=team/tests/org.eclipse.compare.tests/src/org/eclipse/compare/tests/RangeDifferencerThreeWayDiffTest.java
sed -e 's/^package org.eclipse.compare.tests;/package org.eclipse.compare.internal.merge;/' \
    -e 's/import org.eclipse.compare.contentmergeviewer.ITokenComparator;/import org.eclipse.compare.rangedifferencer.IRangeComparator;/' \
    -e '/^import org.eclipse.compare.internal.DocLineComparator;/d' -e '/^import org.eclipse.jface.text.Document;/d' \
    -e 's/ITokenComparator /IRangeComparator /g' -e 's/new DocLineComparator(new Document(\([alr]\)), null, false)/LineFixtures.lines(\1)/g' \
    "$test" > build/RangeDifferencerThreeWayDiffTest.java
javac --release 17 -proc:none -cp "$cp:%{bootstrap_java}/*" -d build/tests %{tools_dir}/RunJupiter.java %{SOURCE3} \
    team/bundles/org.eclipse.compare/compare/org/eclipse/compare/internal/merge/LineComparator.java build/RangeDifferencerThreeWayDiffTest.java
java -cp "build/tests:$cp:%{bootstrap_java}/*" RunJupiter org.eclipse.compare.internal.merge.RangeDifferencerThreeWayDiffTest

%files
%license LICENSE
%{_datadir}/maven-metadata/eclipse-team-core.xml
%{platform_repo}/org.eclipse.compare.core/
%{platform_repo}/org.eclipse.team.core/

%changelog
%autochangelog
