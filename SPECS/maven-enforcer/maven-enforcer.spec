# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bootstrap_mvn %{_libexecdir}/javapackages-bootstrap/mvn
%global repo_dir %{_datadir}/maven-repository

Name:           maven-enforcer
Version:        3.6.2
Release:        %autorelease
Summary:        Enforce build rules in Maven projects
License:        Apache-2.0
URL:            https://maven.apache.org/enforcer/
VCS:            git:https://github.com/apache/maven-enforcer
#!RemoteAsset:  sha256:9fe2f4619e24307f0ee76e33214f4ab58625e9ec8f8dc4d68298f8ea6d8268b1
Source0:        https://github.com/apache/maven-enforcer/archive/refs/tags/enforcer-%{version}.tar.gz
Source1:        check-plugin.sh
#!RemoteAsset:  sha256:0d57ede12bd32258035361a8569bdcc3ecaab53ca4620052b47e337b45897c15
Source2:        https://github.com/apache/maven-enforcer/archive/refs/tags/enforcer-3.6.1.tar.gz
BuildArch:      noarch

# https://github.com/apache/maven-enforcer/blob/enforcer-3.6.2/enforcer-rules/pom.xml
Patch2000:      2000-use-beanshell-2.1.1.patch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  mvn(org.apache-extras.beanshell:bsh) == 2.1.1
BuildRequires:  mvn(org.mockito:mockito-junit-jupiter) == 4.11.0
Provides:       mvn(org.apache.maven.plugins:maven-enforcer-plugin) == %{version}
Provides:       mvn(org.apache.maven.enforcer:enforcer-api) == %{version}
Provides:       mvn(org.apache.maven.plugins:maven-enforcer-plugin) == 3.6.1
Provides:       mvn(org.apache.maven.enforcer:enforcer-api) == 3.6.1
Requires:       mvn(org.apache-extras.beanshell:bsh) == 2.1.1

%description
Apache Maven Enforcer evaluates build rules, including Maven and JDK
version requirements, dependency convergence and restrictions on the
artifacts allowed in a project.

%prep
%autosetup -p1 -n maven-enforcer-enforcer-%{version}
mkdir compat
tar -xf %{SOURCE2} -C compat --strip-components=1
(cd compat && patch -p1 < %{PATCH2000})
mkdir -p .xmvn local-repository
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

mkdir -p compat/{.xmvn,local-repository}
cp -as %{repo_dir}/. compat/local-repository/
sed -e 's|<version>%{version}</version><version>SYSTEM</version>|<version>3.6.1</version>|' .xmvn/configuration.xml > compat/.xmvn/configuration.xml

%build
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
base=$PWD
for tree in . compat; do
    cd "$base/$tree"
# The parent binds Enforcer to validate. Invoke the compilation goals directly
# so that the plugin can be built before its own first execution.
%{bootstrap_mvn} --batch-mode --offline -Dmaven.repo.local="$PWD/local-repository" \
    org.apache.maven.plugins:maven-resources-plugin:resources \
    org.apache.maven.plugins:maven-compiler-plugin:compile \
    org.eclipse.sisu:sisu-maven-plugin:main-index \
    org.apache.maven.plugins:maven-plugin-plugin:descriptor \
    org.apache.maven.plugins:maven-jar-plugin:jar \
    org.fedoraproject.xmvn:xmvn-mojo:install

done

%install
%{_libexecdir}/javapackages-bootstrap/xmvn-install -R "$PWD/.xmvn-reactor" -d %{buildroot} -n %{name}
(cd compat && %{_libexecdir}/javapackages-bootstrap/xmvn-install -R "$PWD/.xmvn-reactor" -d %{buildroot} -n %{name}-3.6.1)
install -pm644 compat/pom.xml %{buildroot}%{repo_dir}/org/apache/maven/enforcer/enforcer/3.6.1/enforcer-3.6.1.pom
# The parent reactor selects a JAR when the jar goal is invoked explicitly.
install -pm644 pom.xml %{buildroot}%{repo_dir}/org/apache/maven/enforcer/enforcer/%{version}/enforcer-%{version}.pom

%check
base=$PWD
for tree in . compat; do
    cd "$base/$tree"
    version=%{version}
    metadata=maven-enforcer
    if test "$tree" = compat; then version=3.6.1; metadata=maven-enforcer-3.6.1; fi
cmp pom.xml %{buildroot}%{repo_dir}/org/apache/maven/enforcer/enforcer/$version/enforcer-$version.pom
cp -a --remove-destination %{buildroot}%{repo_dir}/. local-repository/
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
%{bootstrap_mvn} --batch-mode --offline -Dmaven.repo.local="$PWD/local-repository" \
    org.apache.maven.plugins:maven-resources-plugin:testResources \
    org.apache.maven.plugins:maven-compiler-plugin:testCompile \
    org.apache.maven.plugins:maven-surefire-plugin:test
jar tf maven-enforcer-plugin/target/maven-enforcer-plugin-$version.jar | grep -Fx META-INF/maven/plugin.xml

sh %{SOURCE1} %{buildroot} %{bootstrap_mvn} "$version" "$metadata"
done

%files
%doc README.md
%license LICENSE NOTICE
%{_datadir}/maven-metadata/maven-enforcer.xml
%{_datadir}/maven-metadata/maven-enforcer-3.6.1.xml
%{repo_dir}/org/apache/maven/enforcer/
%{repo_dir}/org/apache/maven/extensions/maven-enforcer-extension/
%{repo_dir}/org/apache/maven/plugins/maven-enforcer-plugin/

%changelog
%autochangelog
