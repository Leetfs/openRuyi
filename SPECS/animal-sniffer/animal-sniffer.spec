# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository
%global jpb_mvn %{_libexecdir}/javapackages-bootstrap/mvn
%define build_mvn %{jpb_mvn} --batch-mode --offline -Dmaven.repo.local="$PWD/local-repository" -pl :animal-sniffer-maven-plugin -am

Name:           animal-sniffer
Version:        1.27
Release:        %autorelease
Summary:        Check Java API compatibility against a reference signature
License:        MIT
URL:            https://www.mojohaus.org/animal-sniffer/
VCS:            git:https://github.com/mojohaus/animal-sniffer
#!RemoteAsset:  sha256:7145769e73889649a8e470858ecd077e37da8b6424c2274a6ca287a3edd3f7bc
Source0:        https://github.com/mojohaus/animal-sniffer/archive/refs/tags/animal-sniffer-%{version}.tar.gz
Source1:        check-plugin.sh
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
Provides:       mvn(org.codehaus.mojo:animal-sniffer-maven-plugin) == %{version}
Provides:       mvn(org.codehaus.mojo:animal-sniffer) == %{version}
Provides:       mvn(org.codehaus.mojo:animal-sniffer-annotations) == %{version}
Provides:       mvn(org.codehaus.mojo:java-boot-classpath-detector) == %{version}
Requires:       javapackages-bootstrap

%description
Animal Sniffer examines compiled Java classes for references to methods
and fields that are unavailable in a reference API. The Maven plugin
checks project classes during the build.

%prep
%autosetup -n animal-sniffer-animal-sniffer-%{version}
mkdir -p local-repository .xmvn
if test -d %{repo_dir}; then
    cp -as %{repo_dir}/. local-repository/
fi
cat > .xmvn/configuration.xml <<EOF
<configuration>
  <repositories><repository>
    <id>install</id><type>maven</type>
    <properties><root>usr/share/maven-repository</root></properties>
  </repository></repositories>
  <installerSettings><metadataDir>usr/share/maven-metadata</metadataDir></installerSettings>
  <artifactManagement><rule>
    <artifactGlob/><versions><version>%{version}</version><version>SYSTEM</version></versions>
  </rule></artifactManagement>
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
%{build_mvn} \
    org.apache.maven.plugins:maven-resources-plugin:resources \
    org.apache.maven.plugins:maven-compiler-plugin:compile \
    org.apache.maven.plugins:maven-plugin-plugin:descriptor \
    org.apache.maven.plugins:maven-jar-plugin:jar \
    org.fedoraproject.xmvn:xmvn-mojo:install

%install
%{_libexecdir}/javapackages-bootstrap/xmvn-install -R "$PWD/.xmvn-reactor" -d %{buildroot} -n %{name}
# The parent reactor selects a JAR when the jar goal is invoked explicitly.
install -pm644 pom.xml %{buildroot}%{repo_dir}/org/codehaus/mojo/animal-sniffer-parent/%{version}/animal-sniffer-parent-%{version}.pom

%check
cmp pom.xml %{buildroot}%{repo_dir}/org/codehaus/mojo/animal-sniffer-parent/%{version}/animal-sniffer-parent-%{version}.pom
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
cp -a --remove-destination %{buildroot}%{repo_dir}/. local-repository/
%{build_mvn} \
    org.apache.maven.plugins:maven-resources-plugin:testResources \
    org.apache.maven.plugins:maven-compiler-plugin:testCompile \
    org.apache.maven.plugins:maven-surefire-plugin:test
test -s animal-sniffer/target/surefire-reports/TEST-org.codehaus.mojo.animal_sniffer.SignatureCheckerTest.xml
jar tf animal-sniffer-maven-plugin/target/animal-sniffer-maven-plugin-%{version}.jar | grep -Fx META-INF/maven/plugin.xml

sh %{SOURCE1} %{buildroot} %{jpb_mvn} %{version}

%files
%doc README.md
%license LICENSE
%{_datadir}/maven-metadata/animal-sniffer.xml
%{repo_dir}/org/codehaus/mojo/animal-sniffer/
%{repo_dir}/org/codehaus/mojo/animal-sniffer-annotations/
%{repo_dir}/org/codehaus/mojo/animal-sniffer-maven-plugin/
%{repo_dir}/org/codehaus/mojo/animal-sniffer-parent/
%{repo_dir}/org/codehaus/mojo/java-boot-classpath-detector/

%changelog
%autochangelog
