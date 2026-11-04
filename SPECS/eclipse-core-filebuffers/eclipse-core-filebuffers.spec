# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global tools_dir %{_libexecdir}/eclipse-equinox
%global maven_repo %{_datadir}/maven-repository
%global platform_repo %{maven_repo}/org/eclipse/platform
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap

Name:           eclipse-core-filebuffers
Version:        4.39
Release:        %autorelease
Summary:        Eclipse file buffers
License:        EPL-2.0
URL:            https://eclipse.dev/eclipse/
VCS:            git:https://github.com/eclipse-platform/eclipse.platform.ui
#!RemoteAsset:  sha256:ae951404e00e81d269ec787cc5329f81872cd777240e2da719dc69acb2adec15
Source0:        https://github.com/eclipse-platform/eclipse.platform.ui/archive/refs/tags/R4_39.tar.gz
#!RemoteAsset:  sha256:3df0de64fb06a9111290bbb088fa2498972036d42588bf47c6ef72f55acf4aea
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/platform/org.eclipse.core.filebuffers/3.8.500/org.eclipse.core.filebuffers-3.8.500.pom
Source2:        FileBufferCheck.java
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  eclipse-core-resources
BuildRequires:  eclipse-text
Provides:       mvn(org.eclipse.platform:org.eclipse.core.filebuffers) == 3.8.500
Requires:       eclipse-core-resources
Requires:       eclipse-text

%description
The file buffer manager connects Eclipse text documents to workspace and
external files and applies text edits to their contents.

%prep
%autosetup -n eclipse.platform.ui-R4_39

%build
mkdir -p build/bundles
cp=$(find %{platform_repo} -name '*.jar' ! -name '*-sources.jar' -printf '%%p:')
cp="$cp%{bootstrap_java}/osgi.cmpn.jar:%{bootstrap_java}/osgi.annotation.jar:%{bootstrap_java}/ant.jar:%{bootstrap_java}/ant-launcher.jar"
for dir in bundles/org.eclipse.core.filebuffers; do
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
javac --release 17 -proc:none -cp "$cp" -d build/tests %{SOURCE2}
java -cp "build/tests:$cp" FileBufferCheck

%files
%license LICENSE
%{_datadir}/maven-metadata/eclipse-core-filebuffers.xml
%{platform_repo}/org.eclipse.core.filebuffers/

%changelog
%autochangelog
