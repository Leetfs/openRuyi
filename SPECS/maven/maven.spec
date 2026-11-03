# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global upstream_revision 2bdd9fddda4b155ebf8000e807eb73fd829a51d5
%global bootstrap_mvn %{_libexecdir}/javapackages-bootstrap/mvn
%global repo_dir %{_datadir}/maven-repository
%global _local_file_attrs maven_runtime
%global __maven_runtime_path ^%{_datadir}/maven/bin/m2[.]conf$
%global __maven_runtime_requires %{_bindir}/cat %{_builddir}/%{buildsubdir}/runtime-requires

Name:           maven
Version:        3.9.16
Release:        %autorelease
Summary:        Build and project management tool for Java
License:        Apache-2.0
URL:            https://maven.apache.org/
VCS:            git:https://github.com/apache/maven
#!RemoteAsset:  sha256:f7031b091ad75a226a06a0c092cbf05860dcfc16d140e6da997e6c6b62dbd03c
Source0:        https://archive.apache.org/dist/maven/maven-3/%{version}/source/apache-maven-%{version}-src.tar.gz
Source1:        install-libraries.py
Patch2000:      2000-Accept-the-source-revision-in-archive-builds.patch
Patch2001:      2001-Use-Java-assertions-in-Java-tests.patch
Patch2002:      2002-Invoke-Logback-via-reflection.patch
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin) == 3.6.2
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:) == 48
BuildRequires:  mvn(org.codehaus.mojo:extra-enforcer-rules) == 1.11.0
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api) == 1.9.27
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-connector-basic) == 1.9.27
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-impl) == 1.9.27
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-transport-file) == 1.9.27
BuildRequires:  mvn(org.codehaus.mojo:animal-sniffer-maven-plugin) == 1.27
BuildRequires:  mvn(org.codehaus.mojo.signature:java18:signature) == 1.0
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing) == 2.1.0
BuildRequires:  mvn(org.powermock:powermock-reflect) == 2.0.9
BuildRequires:  mvn(org.slf4j:slf4j-api) == 1.7.36
BuildRequires:  python3
BuildRequires:  xmlstarlet

Provides:       mvn(org.apache.maven:maven-artifact) == %{version}
Provides:       mvn(org.apache.maven:maven-builder-support) == %{version}
Provides:       mvn(org.apache.maven:maven-compat) == %{version}
Provides:       mvn(org.apache.maven:maven-core) == %{version}
Provides:       mvn(org.apache.maven:maven-embedder) == %{version}
Provides:       mvn(org.apache.maven:maven-model) == %{version}
Provides:       mvn(org.apache.maven:maven-model-builder) == %{version}
Provides:       mvn(org.apache.maven:maven-plugin-api) == %{version}
Provides:       mvn(org.apache.maven:maven-repository-metadata) == %{version}
Provides:       mvn(org.apache.maven:maven-resolver-provider) == %{version}
Provides:       mvn(org.apache.maven:maven-settings) == %{version}
Provides:       mvn(org.apache.maven:maven-settings-builder) == %{version}
Provides:       mvn(org.apache.maven:maven-slf4j-provider) == %{version}
Provides:       mvn(org.apache.maven:maven:pom:) == %{version}

Requires:       java-25-openjdk
Requires:       mvn(org.apache.maven:maven-parent:pom:) == 48

%description
Apache Maven builds Java projects using a project object model. It
resolves dependencies and runs the plugins bound to each stage of the
project lifecycle.

%package        distribution
Summary:        Source-built Apache Maven distribution for integration tests
Provides:       mvn(org.apache.maven:apache-maven:tar.gz:bin) == %{version}
Provides:       mvn(org.apache.maven:apache-maven:pom:) == %{version}
Requires:       %{name} = %{version}-%{release}

%description    distribution
The Apache Maven distribution archive lets integration tests unpack
and start the same Maven release in an isolated directory.

%prep
%autosetup -n apache-maven-%{version} -p1
# The Embedder loads Logback only when that SLF4J binding is selected.
for pom in pom.xml maven-embedder/pom.xml; do
    xmlstarlet ed -P -L -N m=http://maven.apache.org/POM/4.0.0 \
        -d '//m:dependency[m:groupId="ch.qos.logback" and m:artifactId="logback-classic"]' "$pom"
done
cp pom.xml consumer.pom
# The release parent binds formatting and license-header checks to source processing.
# Build the Java artifacts with the offline bootstrap plugins.
python3 - <<'PARENT'
from pathlib import Path
from xml.etree import ElementTree as ET

path = Path("pom.xml")
namespace = "http://maven.apache.org/POM/4.0.0"
ET.register_namespace("", namespace)
def tag(name):
    return "{" + namespace + "}" + name
model = ET.parse(path)
plugins = model.getroot().find(tag("build") + "/" + tag("plugins"))
assert plugins is not None
for group, name, check in [
    ("org.apache.maven.plugins", "maven-checkstyle-plugin", "checkstyle-check"),
    ("org.apache.rat", "apache-rat-plugin", "rat-check"),
]:
    plugin = ET.SubElement(plugins, tag("plugin"))
    ET.SubElement(plugin, tag("groupId")).text = group
    ET.SubElement(plugin, tag("artifactId")).text = name
    execution = ET.SubElement(ET.SubElement(plugin, tag("executions")), tag("execution"))
    ET.SubElement(execution, tag("id")).text = check
    ET.SubElement(execution, tag("phase")).text = "none"
# Use the installed bytecode rule in the same Enforcer execution as the parent.
management = model.getroot().find(tag("build") + "/" + tag("pluginManagement") + "/" + tag("plugins"))
assert management is not None
enforcer = next((p for p in management.findall(tag("plugin"))
                 if p.findtext(tag("artifactId")) == "maven-enforcer-plugin"), None)
if enforcer is None:
    enforcer = ET.SubElement(management, tag("plugin"))
    ET.SubElement(enforcer, tag("artifactId")).text = "maven-enforcer-plugin"
dependencies = enforcer.find(tag("dependencies"))
if dependencies is None:
    dependencies = ET.SubElement(enforcer, tag("dependencies"))
dep = ET.SubElement(dependencies, tag("dependency"))
ET.SubElement(dep, tag("groupId")).text = "org.codehaus.mojo"
ET.SubElement(dep, tag("artifactId")).text = "extra-enforcer-rules"
ET.SubElement(dep, tag("version")).text = "1.11.0"
model.write(path, encoding="utf-8", xml_declaration=True)
PARENT
mkdir -p .xmvn local-repository
if test -d %{repo_dir}; then
    cp -as %{repo_dir}/. local-repository/
fi
cat > .xmvn/configuration.xml <<EOF
<configuration>
  <resolverSettings>
    <metadataRepositories>
      <repository>%{_datadir}/maven-metadata</repository>
      <repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
    </metadataRepositories>
  </resolverSettings>
</configuration>
EOF

%build
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
%{bootstrap_mvn} --batch-mode --offline -P!java17+ -DbuildNumber=%{upstream_revision} -Dmaven.repo.local="$PWD/local-repository" \
    -DskipTests package
mkdir distribution
tar -xf apache-maven/target/apache-maven-%{version}-bin.tar.gz --strip-components=1 -C distribution
test -x distribution/bin/mvn

%install
install -d %{buildroot}%{_datadir}/%{name}/bin %{buildroot}%{_bindir} %{buildroot}%{_sysconfdir}
install -m755 distribution/bin/mvn distribution/bin/mvnDebug %{buildroot}%{_datadir}/%{name}/bin
install -m644 distribution/bin/m2.conf %{buildroot}%{_datadir}/%{name}/bin
cp -a distribution/conf %{buildroot}%{_sysconfdir}/%{name}
ln -s %{_sysconfdir}/%{name} %{buildroot}%{_datadir}/%{name}/conf
ln -s %{_datadir}/%{name}/bin/mvn %{buildroot}%{_bindir}/mvn
ln -s %{_datadir}/%{name}/bin/mvnDebug %{buildroot}%{_bindir}/mvnDebug
python3 %{SOURCE1} %{buildroot} %{_datadir} %{version}

# Preserve the installed parent model without the build-only check overrides.
install -m644 consumer.pom %{buildroot}%{repo_dir}/org/apache/maven/maven/%{version}/maven-%{version}.pom

archive_dir=%{repo_dir}/org/apache/maven/apache-maven/%{version}
archive=apache-maven-%{version}
install -Dm644 apache-maven/target/$archive-bin.tar.gz "%{buildroot}$archive_dir/$archive-bin.tar.gz"
install -m644 apache-maven/pom.xml "%{buildroot}$archive_dir/$archive.pom"
cat > %{buildroot}%{_datadir}/maven-metadata/maven-distribution.xml <<EOF
<metadata><artifacts>
<artifact><groupId>org.apache.maven</groupId><artifactId>apache-maven</artifactId><version>%{version}</version><extension>tar.gz</extension><classifier>bin</classifier><path>$archive_dir/$archive-bin.tar.gz</path><compatVersions><version>%{version}</version></compatVersions></artifact>
<artifact><groupId>org.apache.maven</groupId><artifactId>apache-maven</artifactId><version>%{version}</version><extension>pom</extension><path>$archive_dir/$archive.pom</path><properties><xmvn.resolver.disableEffectivePom>true</xmvn.resolver.disableEffectivePom></properties><compatVersions><version>%{version}</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
%{bootstrap_mvn} --batch-mode --offline -P!java17+ -DbuildNumber=%{upstream_revision} -Dmaven.repo.local="$PWD/local-repository" verify
python3 - <<'PYCODE'
from pathlib import Path
from zipfile import ZipFile

range_request = "org/eclipse/aether/resolution/VersionRangeRequest.class"
resolver_apis = []
providers = []
for jar in Path("distribution/lib").glob("*.jar"):
    with ZipFile(jar) as archive:
        if range_request in archive.namelist():
            resolver_apis.append(jar.name)
        if "org/slf4j/impl/StaticLoggerBinder.class" in archive.namelist():
            providers.append(jar.name)
assert resolver_apis == ["maven-resolver-api-1.9.27.jar"], resolver_apis
assert providers == ["maven-slf4j-provider-%{version}.jar"], providers
PYCODE
distribution/bin/mvn --version | grep -F 'Apache Maven %{version} (%{upstream_revision}'
mkdir -p target/cli-smoke
cat > target/cli-smoke/pom.xml <<'EOF'
<project><modelVersion>4.0.0</modelVersion><groupId>org.openruyi.test</groupId>
<artifactId>logging</artifactId><version>1</version></project>
EOF
distribution/bin/mvn --batch-mode --offline -X -f target/cli-smoke/pom.xml validate > target/cli-smoke/debug.log 2>&1
grep -F '[DEBUG]' target/cli-smoke/debug.log > /dev/null
grep -F 'BUILD SUCCESS' target/cli-smoke/debug.log
# The core resolver reads this local parent range before the validate phase.
range_dir="$PWD/target/cli-smoke/repo/org/openruyi/test/range-parent"
mkdir -p "$range_dir/1.1"
cat > "$range_dir/1.1/range-parent-1.1.pom" <<'EOF'
<project><modelVersion>4.0.0</modelVersion><groupId>org.openruyi.test</groupId>
<artifactId>range-parent</artifactId><version>1.1</version><packaging>pom</packaging></project>
EOF
cat > "$range_dir/maven-metadata-local.xml" <<'EOF'
<metadata><groupId>org.openruyi.test</groupId><artifactId>range-parent</artifactId>
<versioning><versions><version>1.1</version></versions></versioning></metadata>
EOF
cat > target/cli-smoke/pom.xml <<'EOF'
<project><modelVersion>4.0.0</modelVersion>
<parent><groupId>org.openruyi.test</groupId><artifactId>range-parent</artifactId>
<version>[1,2)</version><relativePath/></parent><artifactId>range-consumer</artifactId><version>1</version></project>
EOF
distribution/bin/mvn --batch-mode --offline -Dmaven.repo.local="$PWD/target/cli-smoke/repo" -f target/cli-smoke/pom.xml validate


# Resolve the bin classifier through Maven and execute the distribution it unpacks.
mkdir -p target/distribution-check/{.xmvn,repo}
cd target/distribution-check
cp -as %{buildroot}%{repo_dir}/. repo/
sed 's|<path>%{repo_dir}|<path>%{buildroot}%{repo_dir}|g' %{buildroot}%{_datadir}/maven-metadata/maven-distribution.xml > .xmvn/distribution.xml
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
<repository>$PWD/.xmvn/distribution.xml</repository><repository>%{_datadir}/maven-metadata</repository>
<repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
cat > pom.xml <<EOF
<project><modelVersion>4.0.0</modelVersion><groupId>org.openruyi.check</groupId><artifactId>maven-distribution-check</artifactId><version>1</version>
<dependencies><dependency><groupId>org.apache.maven</groupId><artifactId>apache-maven</artifactId><version>%{version}</version><type>tar.gz</type><classifier>bin</classifier><scope>provided</scope></dependency></dependencies></project>
EOF
%{bootstrap_mvn} -B -o -Dmaven.repo.local="$PWD/repo" -DincludeArtifactIds=apache-maven -DoutputDirectory="$PWD/unpacked" org.apache.maven.plugins:maven-dependency-plugin:unpack-dependencies
test -x unpacked/apache-maven-%{version}/bin/mvn
unpacked/apache-maven-%{version}/bin/mvn --version | grep -F 'Apache Maven %{version} (%{upstream_revision}'

%files
%doc README.md DEPENDENCIES
%license LICENSE NOTICE
%config(noreplace) %{_sysconfdir}/%{name}/
%{_bindir}/mvn
%{_bindir}/mvnDebug
%{_datadir}/%{name}/
%{_datadir}/maven-metadata/maven.xml
%{repo_dir}/org/apache/maven/

%exclude %{repo_dir}/org/apache/maven/apache-maven/

%files distribution
%license LICENSE NOTICE
%{_datadir}/maven-metadata/maven-distribution.xml
%{repo_dir}/org/apache/maven/apache-maven/

%changelog
%autochangelog
