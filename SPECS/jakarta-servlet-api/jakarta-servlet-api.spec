# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global bundle_tools %{_libexecdir}/eclipse-equinox
%global jpb %{_datadir}/java/javapackages-bootstrap
Name:           jakarta-servlet-api
Version:        6.0.0
Release:        %autorelease
Summary:        Jakarta Servlet API for Java web containers
License:        EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://jakarta.ee/specifications/servlet/6.0/
VCS:            git:https://github.com/jakartaee/servlet
#!RemoteAsset:  sha256:350a1beacc8a626a1773ec8e2c4bc1824ac75de0c38a8f2c0b9128d6f9a30bd9
Source0:        https://github.com/jakartaee/servlet/archive/refs/tags/%{version}-RELEASE.tar.gz?/servlet-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  eclipse-equinox-build(source-bundles)
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven >= 3.9.9
BuildRequires:  mvn(org.eclipse.ee4j:project:pom:) == 1.0.7
BuildRequires:  unzip
Provides:       mvn(jakarta.servlet:jakarta.servlet-api) == %{version}
Requires:       java-25-openjdk
Requires:       mvn(org.eclipse.ee4j:project:pom:) == 1.0.7

%description
Jakarta Servlet defines the HTTP request, response, session and filtering
interfaces implemented by Java web containers.

%prep
%autosetup -n servlet-%{version}-RELEASE

%build
cd api
mkdir -p target/classes build/bundles .mvn .xmvn
find src/main/java -name '*.java' | sort > target/sources
javac --release 11 -encoding UTF-8 -proc:none -d target/classes @target/sources
cp -r src/main/resources/. target/classes/
(cd src/main/java; find . \( -name '*.properties' -o -name '*.html' \) -exec cp --parents '{}' ../../../target/classes/ \;)
mkdir -p target/classes/META-INF
install -m644 ../LICENSE.md ../NOTICE.md target/classes/META-INF/
cat > .xmvn/configuration.xml <<'EOF'
<configuration><resolverSettings><metadataRepositories><repository>/usr/share/maven-metadata</repository>
<repository>/usr/share/javapackages-bootstrap/maven-metadata</repository></metadataRepositories></resolverSettings></configuration>
EOF
plugin=$(unzip -p %{jpb}/maven-bundle-plugin.jar META-INF/maven/plugin.xml | sed -n '0,/<version>/s/.*<version>\([^<]*\)<.*/\1/p')
ext=%{_datadir}/javapackages-bootstrap/maven/lib/ext
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.ext.class.path=$ext/xmvn.jar:$ext/kojan-xml.jar"
mvn -B -o -Dmaven.repo.local="$PWD/target/repo" "org.apache.felix:maven-bundle-plugin:$plugin:manifest"
jar --create --file build/bundles/jakarta.servlet-api.jar --manifest target/classes/META-INF/MANIFEST.MF -C target/classes .

%install
%{bundle_tools}/install-bundles %{buildroot} %{_datadir} %{name} api/build/bundles api/pom.xml

%check
cd api
jar=build/bundles/jakarta.servlet-api.jar
jar --describe-module --file "$jar" | grep -F 'exports jakarta.servlet.http'
# Run all upstream Jupiter classes, including parameterized URL and HTTP method cases.
mkdir -p target/test-classes
find src/test/java -name '*.java' | sort > target/tests
javac --release 11 -proc:none -encoding UTF-8 -cp "$jar:%{jpb}/*" -d target/test-classes @target/tests
javac --release 17 -proc:none -cp '%{jpb}/*' -d target/test-classes %{bundle_tools}/RunJupiter.java
classes=$(find src/test/java -name '*Test.java' | sed 's|src/test/java/||;s|[.]java$||;s|/|.|g' | sort)
java -cp "target/test-classes:$jar:%{jpb}/*" RunJupiter $classes

%files
%license LICENSE.md NOTICE.md
%{_datadir}/maven-metadata/jakarta-servlet-api.xml
%{_datadir}/maven-repository/jakarta/servlet/jakarta.servlet-api/

%changelog
%autochangelog
