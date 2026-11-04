# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global qualifier v20201214
%global bundle_tools %{_libexecdir}/eclipse-equinox
%global mvnrepo %{_datadir}/maven-repository
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap

Name:           sat4j
Version:        2.3.6
Release:        %autorelease
Summary:        Boolean satisfiability and pseudo-Boolean solvers for Java
License:        (EPL-1.0 OR LGPL-2.1-or-later) AND MIT AND Apache-2.0
URL:            https://www.sat4j.org/
VCS:            git:https://gitlab.ow2.org/sat4j/sat4j
#!RemoteAsset:  sha256:1be61527a14491814013fdec677367ff7637dddd78a0e378711e75a93b8f513b
Source0:        https://gitlab.ow2.org/sat4j/sat4j/-/archive/2_3_6/sat4j-2_3_6.tar.gz
#!RemoteAsset:  sha256:0f8a1b116e760b8fe6389c51b84e4b07a70fc11082d4f936e453b583dd50b43b
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/ow2/ow2/1.5/ow2-1.5.pom
Source2:        prepare-tests.py
Source3:        SolverCheck.java
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source4:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  eclipse-equinox-build(parent-models)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap(pom-install)
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.mockito:mockito-core) == 4.11.0
BuildRequires:  python3
BuildRequires:  unzip
Provides:       mvn(org.ow2.sat4j:org.ow2.sat4j.core) == %{version}
Provides:       mvn(org.ow2.sat4j:org.ow2.sat4j.pb) == %{version}
Provides:       mvn(org.ow2.sat4j:org.ow2.sat4j.pom:pom:) == %{version}
Provides:       mvn(org.ow2:ow2:pom:) == 1.5
Requires:       java-25-openjdk

%description
SAT4J solves Boolean satisfiability and pseudo-Boolean constraints. Its core
and PB extensions are used by the Eclipse p2 provisioning planner.

%prep
%autosetup -n sat4j-2_3_6
cp org.sat4j.core/LICENSE.txt LICENSE-core.txt
cp org.sat4j.pb/LICENSE.txt LICENSE-pb.txt
cp %{SOURCE4} Apache-2.0.txt

%build
base=$PWD
cp=.
mkdir -p build/bundles build/sources
for module in core pb; do
    cd "$base/org.sat4j.$module"
    artifact=org.ow2.sat4j.$module
    mkdir -p target/classes
    find src/main/java -name '*.java' | sort > target/sources
    javac --release 8 -proc:none -encoding UTF-8 -cp "$cp" -d target/classes @target/sources
    cp -r src/main/resources/. target/classes/
    if test -f target/classes/sat4j.version; then echo '%{version}' > target/classes/sat4j.version; fi
    # Use the release qualifier in upstream's bundle exports and advertise the native Java target.
    sed -e 's/9[.]9[.]9[.]token/%{version}.%{qualifier}/g' \
        -e 's/^Bundle-RequiredExecutionEnvironment:.*/Bundle-RequiredExecutionEnvironment: JavaSE-1.8/' META-INF/MANIFEST.MF > target/manifest
    jar --create --file "target/$module.jar" --manifest target/manifest -C target/classes .
    cp "target/$module.jar" "$base/build/bundles/$artifact.jar"
    cp="$cp:$PWD/target/$module.jar"
    cat > target/source.mf <<EOF
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-SymbolicName: org.sat4j.$module.source
Bundle-Version: %{version}.%{qualifier}
Bundle-Name: SAT4J $module sources
Eclipse-SourceBundle: org.sat4j.$module;version="%{version}.%{qualifier}";roots:="."
EOF
    jar --create --file "$base/build/sources/$artifact.jar" --manifest target/source.mf -C src/main/java .
done

%install
%{_libexecdir}/javapackages-bootstrap/install-poms %{buildroot} %{_datadir} %{name}-parents pom.xml %{SOURCE1}
for module in core pb; do
    %{bundle_tools}/install-bundles --symbolic-name org.sat4j.$module --qualifier %{qualifier} --sources build/sources \
        %{buildroot} %{_datadir} %{name}-$module build/bundles org.sat4j.$module/pom.xml
done

%check
# Keep the release's Bug and Test selectors, benchmark directories, and timeout exclusions.
base=$PWD
ext=%{_datadir}/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
plugin=$(unzip -p %{bootstrap_java}/maven-surefire-plugin.jar META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
test -n "$plugin"
python3 %{SOURCE2} "$plugin"
for module in core pb; do
    cd "$base/org.sat4j.$module"
    mkdir -p target/test-classes .xmvn .mvn
    cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories><repository>%{_datadir}/maven-metadata</repository>
<repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository></metadataRepositories></resolverSettings></configuration>
EOF
    find src/test/java -name '*.java' | sort > target/test-sources
    javac --release 17 -proc:none -encoding UTF-8 -cp "target/classes:$base/org.sat4j.core/target/core.jar:%{bootstrap_java}/*" \
        -d target/test-classes @target/test-sources
    if test -d src/test/resources; then cp -r src/test/resources/. target/test-classes/; fi
    mvn -B --offline -f tests.pom -Dmaven.repo.local="$PWD/target/test-repo" -DfailIfNoTests=true "org.apache.maven.plugins:maven-surefire-plugin:$plugin:test"
done
# Solve a satisfiable formula and reject contradictory assumptions with the packaged libraries.
cd "$base"
java -ea -cp "build/bundles/org.ow2.sat4j.core.jar:build/bundles/org.ow2.sat4j.pb.jar" %{SOURCE3}

%files
%license LICENSE LICENSE-core.txt LICENSE-pb.txt Apache-2.0.txt
%{_datadir}/maven-metadata/sat4j-*.xml
%{mvnrepo}/org/ow2/sat4j/org.ow2.sat4j.core/
%{mvnrepo}/org/ow2/sat4j/org.ow2.sat4j.pb/
%{mvnrepo}/org/ow2/sat4j/org.ow2.sat4j.pom/
%{mvnrepo}/org/ow2/ow2/1.5/

%changelog
%autochangelog
