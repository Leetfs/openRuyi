# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository
%define build_mvn %{_libexecdir}/javapackages-bootstrap/mvn --batch-mode --offline -Dmaven.repo.local="$PWD/local-repository"

Name:           plexus-testing
Version:        2.1.0
Release:        %autorelease
Summary:        JUnit Jupiter extension for testing Plexus components
License:        Apache-2.0
URL:            https://codehaus-plexus.github.io/plexus-testing/
VCS:            git:https://github.com/codehaus-plexus/plexus-testing
#!RemoteAsset:  sha256:a377c8e9d46b4ed077b58b33fcbd352079da0cbaaaab9bef39bead392c02e572
Source0:        https://github.com/codehaus-plexus/plexus-testing/archive/refs/tags/plexus-testing-%{version}.tar.gz
Patch0:         0001-close-plexus-resources-on-junit-5.12.patch
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.mockito:mockito-junit-jupiter) == 4.11.0
BuildRequires:  python3
Provides:       mvn(org.codehaus.plexus:plexus-testing) == %{version}
Requires:       javapackages-bootstrap

%description
Plexus Testing starts a component container for JUnit Jupiter tests. It
injects named services into test classes and supports custom container
bindings.

%prep
%autosetup -p1 -n plexus-testing-plexus-testing-%{version}
mkdir -p .xmvn local-repository
if test -d %{repo_dir}; then cp -as %{repo_dir}/. local-repository/; fi
cat > .xmvn/configuration.xml <<EOF
<configuration>
  <repositories><repository><id>install</id><type>maven</type>
    <properties><root>usr/share/maven-repository</root></properties>
  </repository></repositories>
  <installerSettings><metadataDir>usr/share/maven-metadata</metadataDir></installerSettings>
  <artifactManagement><rule><artifactGlob/>
    <versions><version>%{version}</version><version>SYSTEM</version></versions>
  </rule></artifactManagement>
  <resolverSettings><metadataRepositories>
    <repository>%{_datadir}/maven-metadata</repository>
    <repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
  </metadataRepositories></resolverSettings>
</configuration>
EOF

%build
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
%{build_mvn} org.apache.maven.plugins:maven-resources-plugin:resources \
    org.apache.maven.plugins:maven-compiler-plugin:compile \
    org.apache.maven.plugins:maven-jar-plugin:jar \
    org.fedoraproject.xmvn:xmvn-mojo:install

%install
%{_libexecdir}/javapackages-bootstrap/xmvn-install -R "$PWD/.xmvn-reactor" -d %{buildroot} -n %{name}

%check
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
%{build_mvn} org.apache.maven.plugins:maven-resources-plugin:testResources \
    org.apache.maven.plugins:maven-compiler-plugin:testCompile \
    org.apache.maven.plugins:maven-surefire-plugin:test
test -s target/surefire-reports/TEST-org.codehaus.plexus.testing.PlexusTestJavaxTest.xml
%{_bindir}/python3 - %{buildroot}%{_datadir}/maven-metadata/%{name}.xml <<'PY'
import sys
from xml.etree import ElementTree

metadata = ElementTree.parse(sys.argv[1])
guice = [d for d in metadata.iter("dependency")
         if d.findtext("groupId") == "com.google.inject" and d.findtext("artifactId") == "guice"]
assert guice and all(d.findtext("classifier") == "classes" for d in guice)
PY

%files
%doc README.md
%license LICENSE
%{_datadir}/maven-metadata/plexus-testing.xml
%{repo_dir}/org/codehaus/plexus/plexus-testing/

%changelog
%autochangelog
