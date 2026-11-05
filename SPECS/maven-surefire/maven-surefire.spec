# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global mvn_opts -B -o -Dmaven.repo.local="$PWD/local-repository" -DskipITs -P!java17+ -pl :maven-failsafe-plugin,:common-java5 -am
%global xmvn_ext %{_datadir}/javapackages-bootstrap/maven/lib/ext
%global repo %{_datadir}/maven-repository

Name:           maven-surefire
Version:        3.5.5
Release:        %autorelease
Summary:        Maven test runners and fork protocol
License:        Apache-2.0
URL:            https://maven.apache.org/surefire/
VCS:            git:https://github.com/apache/maven-surefire
#!RemoteAsset:  sha256:87bd504e65ee537129bf4f510c8f0e741f14a8be32e830781cfca49d191c643b
Source0:        https://archive.apache.org/dist/maven/surefire/surefire-%{version}-source-release.zip
#!RemoteAsset:  sha256:0791c4b99b7bb6996015ed1017543a8b501659a1212fbc880bb61cd2ec87d3e2
Source1:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/maven-surefire-plugin/%{version}/maven-surefire-plugin-%{version}-sources.jar
#!RemoteAsset:  sha256:cac83dee50751a2a3c19f05ed12405c917b08120a152588f2d701ba440be4675
Source2:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/maven-failsafe-plugin/%{version}/maven-failsafe-plugin-%{version}-sources.jar
Source3:        configure-surefire.py
Source4:        install-surefire.py
Source5:        check-surefire.sh
Patch0:         0001-backport-junit-platform-reporter-test-expectations.patch
Patch1:         0002-select-jupiter-for-the-parameterized-container-test.patch
#!RemoteAsset:  sha256:d88607b2d4aa2c757ff4802f5b545e6730f665c13c9ae46183b84a0833427d9f
Source6:        https://archive.apache.org/dist/maven/surefire/surefire-3.5.6-source-release.zip
#!RemoteAsset:  sha256:01c35c5cac417077d987946a9d47411612abd6bf7ffbfa38b287dffa42abb32b
Source7:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/maven-surefire-plugin/3.5.6/maven-surefire-plugin-3.5.6-sources.jar
#!RemoteAsset:  sha256:a9398a51d9625caa9f21e4969b2ec811625b13c15207716b88f4bd1b9ed26be8
Source8:        https://maven-central.storage-download.googleapis.com/maven2/org/apache/maven/plugins/maven-failsafe-plugin/3.5.6/maven-failsafe-plugin-3.5.6-sources.jar
BuildArch:      noarch
BuildRequires:  java-25-openjdk-devel
BuildRequires:  unzip
BuildRequires:  python3
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin) == 3.6.1
BuildRequires:  mvn(org.jacoco:jacoco-maven-plugin) == 0.8.14
BuildRequires:  mvn(org.apache.maven.surefire:surefire-shadefire) == 3.5.2
BuildRequires:  mvn(org.powermock:powermock-reflect) == 2.0.9
BuildRequires:  mvn(org.powermock:powermock-core) == 2.0.9
BuildRequires:  mvn(org.powermock:powermock-api-mockito2) == 2.0.9
BuildRequires:  mvn(org.powermock:powermock-module-junit4) == 2.0.9
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api) == 5.12.2
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine) == 5.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-engine) == 1.12.2
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher) == 1.12.2
BuildRequires:  mvn(org.codehaus.mojo:extra-enforcer-rules) == 1.11.0
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin) == 3.6.2
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:) == 47
BuildRequires:  mvn(org.junit:junit-bom:pom:) == 5.12.2
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils) == 3.3.4
BuildRequires:  mvn(org.apache.maven.plugins:maven-resources-plugin) == 3.5.0
BuildRequires:  mvn(org.junit.vintage:junit-vintage-engine) == 5.12.2
BuildRequires:  mvn(org.apache.maven.surefire:surefire:pom:) == %{version}
Provides:       mvn(org.apache.maven.surefire:surefire-shared-utils) == %{version}
Provides:       mvn(org.apache.maven.surefire:surefire-logger-api) == %{version}
Provides:       mvn(org.apache.maven.surefire:surefire-api) == %{version}
Provides:       mvn(org.apache.maven.surefire:surefire-booter) == %{version}
Provides:       mvn(org.apache.maven.surefire:surefire-extensions-api) == %{version}
Provides:       mvn(org.apache.maven.surefire:surefire-extensions-spi) == %{version}
Provides:       mvn(org.apache.maven.surefire:surefire-providers:pom:) == %{version}
Provides:       mvn(org.apache.maven.surefire:common-java5) == %{version}
Provides:       mvn(org.apache.maven.surefire:surefire-junit-platform) == %{version}
Provides:       mvn(org.apache.maven.surefire:maven-surefire-common) == %{version}
Provides:       mvn(org.apache.maven.plugins:maven-surefire-plugin) == %{version}
Provides:       mvn(org.apache.maven.plugins:maven-failsafe-plugin) == %{version}
Provides:       mvn(org.apache.maven.surefire:surefire-shared-utils) == 3.5.6
Provides:       mvn(org.apache.maven.surefire:surefire-logger-api) == 3.5.6
Provides:       mvn(org.apache.maven.surefire:surefire-api) == 3.5.6
Provides:       mvn(org.apache.maven.surefire:surefire-booter) == 3.5.6
Provides:       mvn(org.apache.maven.surefire:surefire-extensions-api) == 3.5.6
Provides:       mvn(org.apache.maven.surefire:surefire-extensions-spi) == 3.5.6
Provides:       mvn(org.apache.maven.surefire:surefire-providers:pom:) == 3.5.6
Provides:       mvn(org.apache.maven.surefire:common-java5) == 3.5.6
Provides:       mvn(org.apache.maven.surefire:surefire-junit-platform) == 3.5.6
Provides:       mvn(org.apache.maven.surefire:maven-surefire-common) == 3.5.6
Provides:       mvn(org.apache.maven.plugins:maven-surefire-plugin) == 3.5.6
Provides:       mvn(org.apache.maven.plugins:maven-failsafe-plugin) == 3.5.6
Provides:       mvn(org.apache.maven.surefire:surefire:pom:) == 3.5.6
Requires:       javapackages-bootstrap
Requires:       maven >= 3.9.9
Requires:       mvn(org.apache.maven.surefire:surefire:pom:) == %{version}
Requires:       mvn(org.junit.platform:junit-platform-launcher) == 1.12.2

%description
Maven Surefire executes unit tests in forked Java processes. Failsafe
runs integration tests and verifies their reports. The package includes
the JUnit Platform provider, the fork protocol and the Maven plugins.

%prep
%autosetup -p1 -n surefire-%{version}
unzip -q %{SOURCE6}
(cd surefire-3.5.6 && patch -p1 < %{PATCH0} && patch -p1 < %{PATCH1})
base=$PWD
for tree in . surefire-3.5.6; do
    cd "$base/$tree"
    surefire_help=%{SOURCE1}
    failsafe_help=%{SOURCE2}
    if test "$tree" = surefire-3.5.6; then surefire_help=%{SOURCE7}; failsafe_help=%{SOURCE8}; fi
# The release source classifiers contain the generated Java sources for both help goals.
unzip -q "$surefire_help" 'org/apache/maven/plugins/maven_surefire_plugin/HelpMojo.java' -d maven-surefire-plugin/src/main/java
unzip -q "$failsafe_help" 'org/apache/maven/plugins/maven_failsafe_plugin/HelpMojo.java' -d maven-failsafe-plugin/src/main/java
python3 %{SOURCE3}
mkdir -p .xmvn local-repository
cat > .xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
<repository>%{_datadir}/maven-metadata</repository>
<repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
done

%build
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
mvn %{mvn_opts} -DskipTests package
(cd surefire-3.5.6 && mvn %{mvn_opts} -DskipTests package)

%install
python3 %{SOURCE4} %{SOURCE0} %{buildroot} %{_datadir} %{version}
(cd surefire-3.5.6 && python3 %{SOURCE4} %{SOURCE6} %{buildroot} %{_datadir} 3.5.6)

%check
export JAVA_HOME=$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=%{xmvn_ext}/xmvn.jar:%{xmvn_ext}/kojan-xml.jar"
mvn %{mvn_opts} package
bash %{SOURCE5} %{buildroot} %{version}
(cd surefire-3.5.6 && mvn %{mvn_opts} package && bash %{SOURCE5} %{buildroot} 3.5.6)

%files
%license LICENSE NOTICE
%{_datadir}/maven-metadata/maven-surefire.xml
%{repo}/org/apache/maven/surefire/surefire-shared-utils/%{version}/
%{repo}/org/apache/maven/surefire/surefire-logger-api/%{version}/
%{repo}/org/apache/maven/surefire/surefire-api/%{version}/
%{repo}/org/apache/maven/surefire/surefire-booter/%{version}/
%{repo}/org/apache/maven/surefire/surefire-extensions-api/%{version}/
%{repo}/org/apache/maven/surefire/surefire-extensions-spi/%{version}/
%{repo}/org/apache/maven/surefire/surefire-providers/%{version}/
%{repo}/org/apache/maven/surefire/common-java5/%{version}/
%{repo}/org/apache/maven/surefire/surefire-junit-platform/%{version}/
%{repo}/org/apache/maven/surefire/maven-surefire-common/%{version}/
%{repo}/org/apache/maven/plugins/maven-surefire-plugin/%{version}/
%{repo}/org/apache/maven/plugins/maven-failsafe-plugin/%{version}/
%{_datadir}/maven-metadata/maven-surefire-3.5.6.xml
%{repo}/org/apache/maven/surefire/surefire/3.5.6/
%{repo}/org/apache/maven/surefire/surefire-shared-utils/3.5.6/
%{repo}/org/apache/maven/surefire/surefire-logger-api/3.5.6/
%{repo}/org/apache/maven/surefire/surefire-api/3.5.6/
%{repo}/org/apache/maven/surefire/surefire-booter/3.5.6/
%{repo}/org/apache/maven/surefire/surefire-extensions-api/3.5.6/
%{repo}/org/apache/maven/surefire/surefire-extensions-spi/3.5.6/
%{repo}/org/apache/maven/surefire/surefire-providers/3.5.6/
%{repo}/org/apache/maven/surefire/common-java5/3.5.6/
%{repo}/org/apache/maven/surefire/surefire-junit-platform/3.5.6/
%{repo}/org/apache/maven/surefire/maven-surefire-common/3.5.6/
%{repo}/org/apache/maven/plugins/maven-surefire-plugin/3.5.6/
%{repo}/org/apache/maven/plugins/maven-failsafe-plugin/3.5.6/

%changelog
%autochangelog
