# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global modules maven-resolver-api,maven-resolver-spi,maven-resolver-test-util,maven-resolver-util,maven-resolver-named-locks,maven-resolver-impl,maven-resolver-connector-basic,maven-resolver-transport-file
%global repo_dir %{_datadir}/maven-repository
%define build_mvn %{_libexecdir}/javapackages-bootstrap/mvn --batch-mode --offline -Dmaven.repo.local="$PWD/local-repository"

Name:           maven-resolver
Version:        1.9.27
Release:        %autorelease
Summary:        Apache Maven artifact resolution libraries
License:        Apache-2.0
URL:            https://maven.apache.org/resolver/
VCS:            git:https://github.com/apache/maven-resolver
#!RemoteAsset:  sha256:dfead7be16788159b5f44b0b6842627f23901b48ea8cd26eade2083926d78ba6
Source0:        https://archive.apache.org/dist/maven/resolver/maven-resolver-%{version}-source-release.zip
Source1:        prepare-bundles.py
Patch2000:      2000-Generate-bundle-manifests-with-Felix.patch
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.mockito:mockito-core) == 4.11.0
BuildRequires:  python3
BuildRequires:  unzip
Provides:       mvn(org.apache.maven.resolver:maven-resolver-api) == %{version}
Provides:       mvn(org.apache.maven.resolver:maven-resolver-impl) == %{version}
Provides:       mvn(org.apache.maven.resolver:maven-resolver-connector-basic) == %{version}
Provides:       mvn(org.apache.maven.resolver:maven-resolver-transport-file) == %{version}
Provides:       mvn(org.apache.maven.resolver:maven-resolver-named-locks) == %{version}
Provides:       mvn(org.apache.maven.resolver:maven-resolver-spi) == %{version}
Provides:       mvn(org.apache.maven.resolver:maven-resolver-util) == %{version}
Requires:       javapackages-bootstrap

%description
Maven Resolver collects dependency graphs and resolves artifacts from Maven
repositories. These libraries provide the API, service interfaces, named
locks, utilities and the repository system implementation.

%prep
%autosetup -p1
%{_bindir}/python3 %{SOURCE1} %{modules}
mkdir -p .xmvn local-repository
if test -d %{repo_dir}; then cp -as %{repo_dir}/. local-repository/; fi
cat > .xmvn/configuration.xml <<EOF
<configuration>
  <repositories><repository><id>install</id><type>maven</type>
    <properties><root>usr/share/maven-repository</root></properties>
  </repository></repositories>
  <installerSettings><metadataDir>usr/share/maven-metadata</metadataDir></installerSettings>
  <artifactManagement><rule>
    <artifactGlob><artifactId>maven-resolver-test-util</artifactId></artifactGlob>
    <targetPackage>__noinstall</targetPackage>
  </rule><rule><artifactGlob/>
    <versions><version>%{version}</version></versions>
  </rule></artifactManagement>
  <resolverSettings><metadataRepositories>
    <repository>%{_datadir}/maven-metadata</repository>
    <repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
  </metadataRepositories></resolverSettings>
</configuration>
EOF

%build
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
%{build_mvn} -pl %{modules} org.apache.maven.plugins:maven-resources-plugin:resources \
    org.apache.maven.plugins:maven-compiler-plugin:compile \
    org.eclipse.sisu:sisu-maven-plugin:main-index \
    org.apache.felix:maven-bundle-plugin:manifest \
    org.apache.maven.plugins:maven-jar-plugin:jar \
    org.fedoraproject.xmvn:xmvn-mojo:install

%install
%{_libexecdir}/javapackages-bootstrap/xmvn-install -R "$PWD/.xmvn-reactor" -d %{buildroot} -n %{name}

%check
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
%{build_mvn} -pl %{modules} org.apache.maven.plugins:maven-jar-plugin:jar \
    org.apache.maven.plugins:maven-resources-plugin:testResources \
    org.apache.maven.plugins:maven-compiler-plugin:testCompile \
    org.eclipse.sisu:sisu-maven-plugin:test-index \
    org.apache.maven.plugins:maven-surefire-plugin:test
test -s maven-resolver-api/target/surefire-reports/TEST-org.eclipse.aether.DefaultRepositorySystemSessionTest.xml
test -s maven-resolver-impl/target/surefire-reports/TEST-org.eclipse.aether.internal.impl.DefaultTrackingFileManagerTest.xml
impl=%{buildroot}%{repo_dir}/org/apache/maven/resolver/maven-resolver-impl/%{version}/maven-resolver-impl-%{version}.jar
unzip -p "$impl" META-INF/sisu/javax.inject.Named | grep -Fx org.eclipse.aether.internal.impl.DefaultTrackingFileManager
jar=%{buildroot}%{repo_dir}/org/apache/maven/resolver/maven-resolver-api/%{version}/maven-resolver-api-%{version}.jar
unzip -p "$jar" META-INF/MANIFEST.MF | grep -F 'Automatic-Module-Name: org.apache.maven.resolver'
unzip -p "$jar" META-INF/MANIFEST.MF | grep -F 'Export-Package: org.eclipse.aether;'
cat > TestNature.java <<'JAVA'
import org.eclipse.aether.metadata.Metadata.Nature;
import org.eclipse.aether.resolution.VersionRangeRequest;

class TestNature {
    public static void main(String[] args) {
        VersionRangeRequest request = new VersionRangeRequest();
        if (request.getNature() != Nature.RELEASE_OR_SNAPSHOT
                || request.setNature(Nature.RELEASE).getNature() != Nature.RELEASE) {
            throw new AssertionError("Incorrect version range nature");
        }
    }
}
JAVA
%{_bindir}/java -cp "$jar" TestNature.java

# A connector or transport must not shadow the version range API loaded by Maven.
for module in maven-resolver-connector-basic maven-resolver-transport-file; do
    jar="%{buildroot}%{repo_dir}/org/apache/maven/resolver/$module/%{version}/$module-%{version}.jar"
    test -s "$jar"
    if jar tf "$jar" | grep -Fx 'org/eclipse/aether/resolution/VersionRangeRequest.class'; then exit 1; fi
    test -n "$(find "$module/target/surefire-reports" -name 'TEST-*.xml' -print -quit)"
done
javap -classpath maven-resolver-api/target/maven-resolver-api-%{version}.jar org.eclipse.aether.resolution.VersionRangeRequest | grep -F ' getNature()'

%files
%doc README.md
%license LICENSE NOTICE
%{_datadir}/maven-metadata/maven-resolver.xml
%{repo_dir}/org/apache/maven/resolver/maven-resolver-api/
%{repo_dir}/org/apache/maven/resolver/maven-resolver-connector-basic/
%{repo_dir}/org/apache/maven/resolver/maven-resolver-transport-file/
%{repo_dir}/org/apache/maven/resolver/maven-resolver-impl/
%{repo_dir}/org/apache/maven/resolver/maven-resolver-named-locks/
%{repo_dir}/org/apache/maven/resolver/maven-resolver-spi/
%{repo_dir}/org/apache/maven/resolver/maven-resolver-util/

%changelog
%autochangelog
