# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global repo_dir %{_datadir}/maven-repository
%define build_mvn %{_libexecdir}/javapackages-bootstrap/mvn --batch-mode --offline -Dmaven.compiler.release=8 -DparsedVersion.osgiVersion=%{version} -Dmaven.repo.local="$PWD/local-repository"

Name:           slf4j
Version:        1.7.36
Release:        %autorelease
Summary:        Java logging API for SLF4J 1.7 applications
License:        MIT
URL:            https://www.slf4j.org/
VCS:            git:https://github.com/qos-ch/slf4j
#!RemoteAsset:  sha256:a2deaffa191c81abbf830d4060eb84129f31b9b3b945b7791344e8875b595286
Source0:        https://github.com/qos-ch/slf4j/archive/refs/tags/v_%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  xmlstarlet
Provides:       mvn(org.slf4j:slf4j-api) == %{version}

%description
SLF4J provides a common logging interface for Java applications. At
runtime an application selects a binding to supply its logging backend.

%prep
%autosetup -n slf4j-v_%{version}
# The SSH wagon publishes the SLF4J website.
xmlstarlet ed -P -L -N m=http://maven.apache.org/POM/4.0.0 \
    -d '/m:project/m:build/m:extensions/m:extension[m:artifactId="wagon-ssh"]' pom.xml
mkdir -p .xmvn local-repository
if test -d %{repo_dir}; then cp -as %{repo_dir}/. local-repository/; fi
cat > .xmvn/configuration.xml <<EOF
<configuration>
  <repositories><repository><id>install</id><type>maven</type>
    <properties><root>usr/share/maven-repository</root></properties>
  </repository></repositories>
  <installerSettings><metadataDir>usr/share/maven-metadata</metadataDir></installerSettings>
  <artifactManagement><rule><artifactGlob/>
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
%{build_mvn} -pl slf4j-api org.apache.maven.plugins:maven-resources-plugin:resources \
    org.apache.maven.plugins:maven-compiler-plugin:compile
# The upstream process-classes execution removes the compile-time binding stubs.
rm -f slf4j-api/target/classes/org/slf4j/impl/*.class
%{build_mvn} -pl slf4j-api org.apache.maven.plugins:maven-jar-plugin:jar \
    org.fedoraproject.xmvn:xmvn-mojo:install

%install
%{_libexecdir}/javapackages-bootstrap/xmvn-install -R "$PWD/.xmvn-reactor" -d %{buildroot} -n %{name}

%check
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
%{build_mvn} -pl slf4j-api org.apache.maven.plugins:maven-resources-plugin:testResources \
    org.apache.maven.plugins:maven-compiler-plugin:testCompile
jar=%{buildroot}%{repo_dir}/org/slf4j/slf4j-api/%{version}/slf4j-api-%{version}.jar
# NoBindingTest needs a class path without the bootstrap test runner's SLF4J binding.
(
    cd slf4j-api
    cp="target/test-classes:$jar:%{_datadir}/java/javapackages-bootstrap/junit.jar:%{_datadir}/java/javapackages-bootstrap/hamcrest-core.jar"
    # The binding modules subclass this abstract initialization fixture.
    find target/test-classes -type f \
        \( -name 'Test*.class' -o -name '*Test.class' -o -name '*Tests.class' -o -name '*TestCase.class' \) \
        ! -name '*$*' ! -name 'AllTest.class' ! -name 'PackageTest.class' ! -name 'MultithreadedInitializationTest.class' \
        | sed 's|^target/test-classes/||; s|/|.|g; s|[.]class$||' | sort > target/junit-classes
    grep -Fx org.slf4j.NoBindingTest target/junit-classes
    while IFS= read -r suite; do
        %{_bindir}/java -cp "$cp" org.junit.runner.JUnitCore "$suite" || exit 1
    done < target/junit-classes
)
%{_bindir}/jar tf "$jar" > api-files
grep -Fx 'org/slf4j/LoggerFactory.class' api-files
if grep -E '^org/slf4j/impl/.*[.]class$' api-files; then exit 1; fi

%files
%doc README.md
%license LICENSE.txt
%{_datadir}/maven-metadata/slf4j.xml
%{repo_dir}/org/slf4j/slf4j-api/

%changelog
%autochangelog
