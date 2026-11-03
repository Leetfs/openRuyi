# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global revision 09588723fd782c3ff2bb932723f37159552418f7
%global qualifier v20260704-1256
%global bundle_tools %{_libexecdir}/eclipse-equinox
%global mvnrepo %{_datadir}/maven-repository
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
%global common_version 2.46.0
%global ecore_version 2.43.0
%global change_version 2.18.0
%global xmi_version 2.41.0

Name:           eclipse-emf
Version:        2.47.0
Release:        %autorelease
Summary:        Eclipse Modeling Framework Ecore runtime
License:        EPL-2.0 AND Apache-1.1 AND Apache-2.0
URL:            https://eclipse.dev/emf/
VCS:            git:https://github.com/eclipse-emf/org.eclipse.emf
#!RemoteAsset:  sha256:c5b2312790a4162b5428915e40637a5d5528fe381cbbdd055acb3228412c4044
Source0:        https://github.com/eclipse-emf/org.eclipse.emf/archive/%{revision}.tar.gz
#!RemoteAsset:  sha256:53aac1e2c06766652a1a1772ba560e2e0c8b46af88788fe716cf843c65987c44
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/emf/org.eclipse.emf.common/%{common_version}/org.eclipse.emf.common-%{common_version}.pom
#!RemoteAsset:  sha256:47f1b9d3df3af7b56674aebccbc361f0473cccb46a16e19655d442df499b8a31
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/emf/org.eclipse.emf.ecore/%{ecore_version}/org.eclipse.emf.ecore-%{ecore_version}.pom
#!RemoteAsset:  sha256:e88925412013116c04e9a472cf2912948c6a95db9e0cd7436f6528a3939a923f
Source3:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/emf/org.eclipse.emf.ecore.change/%{change_version}/org.eclipse.emf.ecore.change-%{change_version}.pom
#!RemoteAsset:  sha256:09106c5b98ac92f6ea2278b90646fe65d155b8403211601a1bd2627662ad7005
Source4:        https://maven-central.storage-download.googleapis.com/maven2/org/eclipse/emf/org.eclipse.emf.ecore.xmi/%{xmi_version}/org.eclipse.emf.ecore.xmi-%{xmi_version}.pom
Source5:        EmfFramework.java
Source6:        EmfJUnit.java
Source7:        EmfModelCheck.java
Source8:        build-source-bundle.py
BuildArch:      noarch

BuildRequires:  eclipse-core-resources
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  python3
BuildRequires:  unzip
BuildRequires:  zip
Provides:       mvn(org.eclipse.emf:org.eclipse.emf.common) == %{common_version}
Provides:       mvn(org.eclipse.emf:org.eclipse.emf.ecore) == %{ecore_version}
Provides:       mvn(org.eclipse.emf:org.eclipse.emf.ecore.change) == %{change_version}
Provides:       mvn(org.eclipse.emf:org.eclipse.emf.ecore.xmi) == %{xmi_version}
Requires:       eclipse-equinox >= 4.39
Requires:       java-25-openjdk

%description
EMF represents structured data as Ecore models. These bundles provide its
common utilities, model runtime, change recorder and XMI serialization.

%prep
%autosetup -n org.eclipse.emf-%{revision}

%build
mkdir -p build/bundles
cp=$(find %{mvnrepo}/org/eclipse/platform %{mvnrepo}/org/osgi -name '*.jar' -printf '%%p:')
for item in common:%{common_version} ecore:%{ecore_version} ecore.change:%{change_version} ecore.xmi:%{xmi_version}; do
    name=org.eclipse.emf.${item%:*}; version=${item#*:}; module=plugins/$name
    manifest=$module/META-INF/MANIFEST.MF
    grep -Fx "Bundle-Version: $version.qualifier" "$manifest"
    sed -i "s/^Bundle-Version: .*/Bundle-Version: $version.%{qualifier}/" "$manifest"
    jar="$PWD/build/bundles/$name.jar"
    %{bundle_tools}/build-bundle "$module" "$jar" --release 8 --classpath "$cp"
    # PDE excludes Java documentation images and source model diagrams.
    if jar tf "$jar" | grep -Eq '(^|/)doc-files/|^model/.*[.](cat|ecorediag|mdl)$'; then
        zip -qd "$jar" '*/doc-files/*' 'model/*.cat' 'model/*.ecorediag' 'model/*.mdl'
    fi
    python3 %{SOURCE8} "$module" "$PWD/build/sources/$name.jar"
    cp="$jar:$cp"
done
printf '%%s\n' "$cp" > build/classpath

%install
%{bundle_tools}/install-bundles --qualifier %{qualifier} --sources build/sources %{buildroot} %{_datadir} %{name} build/bundles %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4}

%check
# Verify that the source attachments contain the original Java sources for each binary.
python3 - <<'PYSOURCES'
from pathlib import Path
from zipfile import ZipFile
for jar in Path("build/sources").glob("*.jar"):
    source = Path("plugins") / jar.stem / "src"
    originals = {f.relative_to(source).as_posix(): f.read_bytes() for f in source.rglob("*.java")}
    with ZipFile(jar) as archive:
        assert originals == {n: archive.read(n) for n in archive.namelist() if n.endswith(".java")}
        assert "OSGI-INF/l10n/bundle-src.properties" in archive.namelist()
PYSOURCES
# Run the upstream utility, Ecore and list change suites inside a live Equinox registry.
mkdir -p build/tests build/test-libs
src=tests/org.eclipse.emf.test.core/src
base=$src/org/eclipse/emf/test/core
find "$base/common/util" -name '*Test.java' | sort > build/tests.list
printf '%%s\n' "$base/change/ListDifferenceAnalyzerTest.java" "$base/ecore/EcoreTest.java" >> build/tests.list
cp="$(cat build/classpath):%{bootstrap_java}/*"
javac --release 17 -proc:none -encoding UTF-8 -cp "$cp" \
    -sourcepath "$src:tests/org.eclipse.emf.test.common/src:tests/org.eclipse.emf.test.models/src" \
    -d build/tests %{SOURCE6} @build/tests.list
sed "s#^$src/##;s#[.]java\$##;s#/#.#g" build/tests.list > build/test-classes
cp %{bootstrap_java}/{junit.jar,hamcrest-core.jar} build/test-libs/
cat > build/probe.mf <<'EOF'
Manifest-Version: 1.0
Bundle-ManifestVersion: 2
Bundle-SymbolicName: org.openruyi.emf.model.tests
Bundle-Version: 1.0.0
Bundle-ClassPath: .,junit.jar,hamcrest-core.jar
Require-Bundle: org.eclipse.emf.common,org.eclipse.emf.ecore,
 org.eclipse.emf.ecore.change,org.eclipse.emf.ecore.xmi,
 org.eclipse.core.runtime,org.eclipse.core.resources,org.eclipse.osgi
EOF
# The original GenModel capability and resource are also checked without a PDE target registry.
grep '^Provide-Capability:' tests/org.eclipse.emf.test.core/META-INF/MANIFEST.MF >> build/probe.mf
jar --create --file build/test.jar --manifest build/probe.mf -C build/tests . -C build/test-libs . -C tests/org.eclipse.emf.test.core model/ProvideCapability
system=%{mvnrepo}
platform=$system/org/eclipse/platform
set --
for n in org.osgi.util.function org.osgi.util.promise org.osgi.service.component org.osgi.service.prefs; do set -- "$@" "$system/org/osgi/$n"/*/*.jar; done
set -- "$@" "$system/org/apache/felix/org.apache.felix.scr"/*/*.jar
for n in org.eclipse.equinox.common org.eclipse.core.jobs org.eclipse.equinox.registry org.eclipse.equinox.preferences org.eclipse.equinox.app org.eclipse.core.contenttype org.eclipse.core.runtime; do
    set -- "$@" "$platform/$n"/*/*.jar
done
for n in jna jna-platform; do set -- "$@" "$system/net/java/dev/jna/$n"/*/*.jar; done
for n in org.eclipse.core.expressions org.eclipse.core.variables org.eclipse.ant.core org.eclipse.core.filesystem org.eclipse.core.resources; do set -- "$@" "$platform/$n"/*/*.jar; done
for n in common ecore ecore.xmi ecore.change; do set -- "$@" "build/bundles/org.eclipse.emf.$n.jar"; done
framework=$platform/org.eclipse.osgi/3.24.100/org.eclipse.osgi-3.24.100.jar
java -ea -cp "$framework" %{SOURCE5} "$@" build/test.jar

# Resolve XMI and Change transitively from installed Maven metadata with an empty cache.
mkdir -p build/consumer/{.mvn,.xmvn,metadata,src/main/java}
install -m644 %{SOURCE7} build/consumer/src/main/java/EmfModelCheck.java
cd build/consumer
for file in %{_datadir}/maven-metadata/*.xml; do
    test "$(basename "$file")" = %{name}.xml || ln -s "$file" metadata/
done
sed 's@<path>/@<path>%{buildroot}/@g' %{buildroot}%{_datadir}/maven-metadata/%{name}.xml > metadata/%{name}.xml
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
  <repository>$PWD/metadata</repository><repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
cat > pom.xml <<'EOF'
<project xmlns="http://maven.apache.org/POM/4.0.0"><modelVersion>4.0.0</modelVersion>
<groupId>org.openruyi.check</groupId><artifactId>emf-consumer</artifactId><version>1</version>
<properties><maven.compiler.release>17</maven.compiler.release></properties>
<dependencies>
<dependency><groupId>org.eclipse.emf</groupId><artifactId>org.eclipse.emf.ecore.change</artifactId><version>%{change_version}</version></dependency>
<dependency><groupId>org.eclipse.emf</groupId><artifactId>org.eclipse.emf.ecore.xmi</artifactId><version>%{xmi_version}</version></dependency>
</dependencies></project>
EOF
ext=%{_datadir}/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
plugin=$(unzip -p %{bootstrap_java}/maven-compiler-plugin.jar META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
test -n "$plugin"
mvn -B --offline -Dmaven.repo.local="$PWD/repository" "org.apache.maven.plugins:maven-compiler-plugin:$plugin:compile"
# Exercise generated and dynamic models, change undo/redo, and XMI save/load with the packaged bundles.
java -ea -cp "target/classes:$(cat ../classpath)" EmfModelCheck

%files
%license LICENSE NOTICE.md plugins/org.eclipse.emf.ecore/about.html
%{_datadir}/maven-metadata/eclipse-emf.xml
%{mvnrepo}/org/eclipse/emf/org.eclipse.emf.common/
%{mvnrepo}/org/eclipse/emf/org.eclipse.emf.ecore/
%{mvnrepo}/org/eclipse/emf/org.eclipse.emf.ecore.change/
%{mvnrepo}/org/eclipse/emf/org.eclipse.emf.ecore.xmi/

%changelog
%autochangelog
