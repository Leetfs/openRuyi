# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global maven_repo %{_datadir}/maven-repository
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
Name:           bndtools-api
Version:        7.2.1
Release:        %autorelease
Summary:        Bndtools Eclipse API and version control ignore services
License:        Apache-2.0 OR EPL-2.0
URL:            https://bndtools.org/
VCS:            git:https://github.com/bndtools/bnd
#!RemoteAsset:  sha256:69b3775c7520143e79079bb1781aa25bf24a3fd6c82dd6507a821966210e4c34
Source0:        https://github.com/bndtools/bnd/archive/refs/tags/%{version}.tar.gz?/bnd-%{version}.tar.gz
#!RemoteAsset:  sha256:841e3f826bc057a4af676c82ebd8dc84043eab4967c7e8707a6381cd5f31d8ba
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/bndtools/bndtools.api/%{version}/bndtools.api-%{version}.pom
#!RemoteAsset:  sha256:8db1228f9355fa57bb27f3c3bd2cb0bff17b26dacc87b83917c734f6897df3b1
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/bndtools/org.bndtools.versioncontrol.ignores.manager/%{version}/org.bndtools.versioncontrol.ignores.manager-%{version}.pom
Source3:        BuildBndBundle.java
Source4:        IgnoreApiCheck.java
BuildArch:      noarch
BuildRequires:  eclipse-core-resources
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.osgi:org.osgi.service.component.annotations) == 1.5.1
Provides:       mvn(org.bndtools:bndtools.api) == %{version}
Provides:       mvn(org.bndtools:org.bndtools.versioncontrol.ignores.manager) == %{version}
Requires:       eclipse-core-resources
Requires:       javapackages-bootstrap

%description
The Bndtools API integrates bnd build projects with Eclipse resources.
The ignore manager exposes the service used by PDE to maintain version
control ignore rules for generated files.

%prep
%autosetup -n bnd-%{version}

%build
mkdir -p build/{tools,bundles}
cp=$(find %{maven_repo}/org/eclipse/platform -name '*.jar' ! -name '*-sources.jar' -printf '%%p:')
for n in osgi.core osgi.cmpn osgi.annotation biz.aQute.bndlib aQute.libg slf4j-api; do cp="$cp:%{bootstrap_java}/$n.jar"; done
javac --release 17 -proc:none -cp "$cp" -d build/tools %{SOURCE3}
find %{maven_repo}/org/eclipse/platform -name '*.jar' ! -name '*-sources.jar' | sort > build/analyzer-inputs
for n in osgi.core osgi.cmpn osgi.annotation biz.aQute.bndlib aQute.libg slf4j-api; do echo "%{bootstrap_java}/$n.jar" >> build/analyzer-inputs; done
for name in bndtools.api org.bndtools.versioncontrol.ignores.manager; do
    classes="$PWD/build/$name"; mkdir -p "$classes/OSGI-OPT/src"
    (cd "$name/src"; find . -type f \( -name '*.java' -o -name packageinfo \) -exec cp --parents '{}' "$classes/OSGI-OPT/src/" \;)
    if test "$name" = bndtools.api; then
        # These packages are included by the upstream conditionalpackage instruction.
        (cd aQute.libg/src; for f in aQute/lib/hex/{Hex.java,packageinfo} aQute/lib/strings/{Strings.java,package-info.java} aQute/libg/qtokens/{QuotedTokenizer.java,package-info.java}; do cp --parents "$f" "$classes/OSGI-OPT/src/"; done)
        mkdir -p "$classes/aQute/lib/hex"; cp aQute.libg/src/aQute/lib/hex/packageinfo "$classes/aQute/lib/hex/"
    fi
    find "$classes/OSGI-OPT/src" -name '*.java' | sort > build/sources
    javac --release 17 -encoding UTF-8 -proc:none -cp "$cp" -d "$classes" @build/sources
    java -cp "build/tools:$cp" BuildBndBundle "$name" "$classes" "build/bundles/$name.jar" build/analyzer-inputs
    echo "$PWD/build/bundles/$name.jar" >> build/analyzer-inputs
    cp="$PWD/build/bundles/$name.jar:$cp"
done
printf '%%s\n' "$cp" > build/classpath

%install
%{_libexecdir}/eclipse-equinox/install-bundles --qualifier 202601121903 %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1} %{SOURCE2}

%check
cp=$(cat build/classpath)
javac --release 17 -proc:none -cp "$cp" -d build/tools %{SOURCE4}
java -cp "build/tools:$cp" IgnoreApiCheck
jar tf build/bundles/org.bndtools.versioncontrol.ignores.manager.jar | grep -Fx OSGI-INF/org.bndtools.versioncontrol.ignores.manager.VersionControlIgnoresManagerImpl.xml

%files
%license LICENSE
%{_datadir}/maven-metadata/bndtools-api.xml
%{maven_repo}/org/bndtools/bndtools.api/
%{maven_repo}/org/bndtools/org.bndtools.versioncontrol.ignores.manager/

%changelog
%autochangelog
