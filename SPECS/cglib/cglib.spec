# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository
%global cglib_tag RELEASE_3_2_9
%define build_mvn %{_libexecdir}/javapackages-bootstrap/mvn --offline --batch-mode -Dmaven.repo.local="$PWD/local-repository" -Djava.version.source=8 -Djava.version.target=8 -pl :cglib -am

Name:           cglib
Version:        3.2.9
Release:        %autorelease
Summary:        Generate Java proxy and adapter classes at runtime
License:        Apache-2.0
URL:            https://github.com/cglib/cglib
VCS:            git:https://github.com/cglib/cglib
#!RemoteAsset:  sha256:3d87929c3fb933c833c691be1c1f996e7213025ca4a13e20790f36f9d16fac38
Source0:        https://github.com/cglib/cglib/archive/refs/tags/%{cglib_tag}.tar.gz
BuildArch:      noarch

# https://github.com/cglib/cglib/blob/RELEASE_3_2_9/pom.xml
Patch2000:      2000-align-transformer-test-bytecode-target.patch
# https://github.com/cglib/cglib/blob/RELEASE_3_2_9/cglib/src/main/java/net/sf/cglib/proxy/Enhancer.java
Patch2001:      2001-resolve-platform-proxy-interfaces.patch
# https://github.com/cglib/cglib/blob/RELEASE_3_2_9/cglib/src/test/java/net/sf/cglib/reflect/TestFastClass.java
Patch2002:      2002-check-present-bootstrap-methods.patch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom) == 7
Provides:       mvn(cglib:cglib) == %{version}
Requires:       javapackages-bootstrap

%description
CGLIB uses ASM to generate Java classes, implement interfaces and
intercept method calls. Its proxy classes support interception of calls
to concrete classes as well as interfaces.

%prep
%autosetup -p1 -n cglib-%{cglib_tag}
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
# The parent reactor selects a JAR when the jar goal is invoked explicitly.
install -pm644 pom.xml %{buildroot}%{repo_dir}/cglib/cglib-parent/%{version}/cglib-parent-%{version}.pom

%check
cmp pom.xml %{buildroot}%{repo_dir}/cglib/cglib-parent/%{version}/cglib-parent-%{version}.pom
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
cp -a --remove-destination %{buildroot}%{repo_dir}/. local-repository/
%{build_mvn} org.apache.maven.plugins:maven-resources-plugin:testResources \
    org.apache.maven.plugins:maven-compiler-plugin:testCompile
# CGLIB defines proxy classes through ClassLoader.defineClass on the test JVM.
java --add-opens=java.base/java.lang=ALL-UNNAMED -cp "cglib/target/test-classes:cglib/target/cglib-%{version}.jar:%{_datadir}/java/javapackages-bootstrap/*" \
    junit.textui.TestRunner net.sf.cglib.TestAll

%files
%doc README.md
%license LICENSE NOTICE
%{_datadir}/maven-metadata/cglib.xml
%{repo_dir}/cglib/cglib/
%{repo_dir}/cglib/cglib-parent/

%changelog
%autochangelog
