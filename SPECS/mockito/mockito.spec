# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global jpb %{_datadir}/java/javapackages-bootstrap
%global repo_dir %{_datadir}/maven-repository/org/mockito

Name:           mockito
Version:        4.11.0
Release:        %autorelease
Summary:        Java mocking framework and JUnit Jupiter extension
License:        MIT AND Apache-2.0
URL:            https://site.mockito.org/
VCS:            git:https://github.com/mockito/mockito
#!RemoteAsset:  sha256:0c17a6016fb7cda11a42e3f938beb8f1bc7448fcc9f9d3f7c70d93f79e4d3a55
Source0:        https://github.com/mockito/mockito/archive/refs/tags/v%{version}.tar.gz
# https://repo.maven.apache.org/maven2/org/mockito/mockito-core/%{version}/mockito-core-%{version}.pom
Source1:        mockito-core-%{version}.pom
# https://repo.maven.apache.org/maven2/org/mockito/mockito-junit-jupiter/%{version}/mockito-junit-jupiter-%{version}.pom
Source2:        mockito-junit-jupiter-%{version}.pom
Source3:        RunJupiter.java
Source4:        install-modules.py
BuildArch:      noarch

# https://github.com/raphw/byte-buddy/blob/byte-buddy-1.17.7/byte-buddy-dep/pom.xml
Patch2000:      2000-use-system-byte-buddy-asm.patch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
BuildRequires:  python3
Provides:       mvn(org.mockito:mockito-core) == %{version}
Provides:       mvn(org.mockito:mockito-junit-jupiter) == %{version}
Requires:       javapackages-bootstrap

%description
Mockito creates test doubles, records method calls and verifies Java
application behavior. Its JUnit Jupiter extension initializes mocks for
test methods, constructors and fields.

%prep
%autosetup -p1
cp -p src/main/java/org/mockito/internal/util/concurrent/LICENSE LICENSE.concurrent
cp -p src/main/java/org/mockito/internal/matchers/apachecommons/commons-lang-license.txt LICENSE.commons

%build
mkdir -p classes/core classes/extension
find src/main/java -name '*.java' | sort > core-sources
cp="%{jpb}/byte-buddy.jar:%{jpb}/byte-buddy-agent.jar:%{jpb}/asm.jar:%{jpb}/asm-commons.jar:%{jpb}/objenesis.jar:%{jpb}/junit.jar:%{jpb}/hamcrest-core.jar:%{jpb}/opentest4j.jar"
javac -encoding UTF-8 -source 8 -target 8 -classpath "$cp" -d classes/core @core-sources
dispatch=classes/core/org/mockito/internal/creation/bytebuddy/inject
mv "$dispatch/MockMethodDispatcher.class" "$dispatch/MockMethodDispatcher.raw"
rm -f "$dispatch/package-info.class"
echo 'Automatic-Module-Name: org.mockito' > core.manifest
jar --create --file mockito-core-%{version}.jar --manifest core.manifest -C classes/core .
find subprojects/junit-jupiter/src/main/java -name '*.java' | sort > extension-sources
javac --release 8 -encoding UTF-8 -classpath "mockito-core-%{version}.jar:$cp:%{jpb}/junit-jupiter-api.jar:%{jpb}/junit-platform-commons.jar:%{jpb}/apiguardian-api.jar" \
    -d classes/extension @extension-sources
echo 'Automatic-Module-Name: org.mockito.junit.jupiter' > extension.manifest
jar --create --file mockito-junit-jupiter-%{version}.jar --manifest extension.manifest -C classes/extension .

%install
%{_bindir}/python3 %{SOURCE4} %{buildroot} %{_datadir} %{SOURCE1} %{SOURCE2}

%check
mkdir -p classes/tests
cp="$PWD/mockito-core-%{version}.jar:$PWD/mockito-junit-jupiter-%{version}.jar:%{jpb}/*"
find subprojects/junit-jupiter/src/test/java -name '*.java' | sort > test-sources
javac --release 8 -encoding UTF-8 -cp "$cp" -d classes/tests @test-sources %{SOURCE3}
java -cp "classes/tests:$cp" RunJupiter org.mockitousage.JunitJupiterTest \
    org.mockitousage.StrictnessTest org.mockitousage.MultiLevelNestedTest

mkdir -p consumer/.xmvn consumer/src/test/java
sed "s|<path>/usr/share/|<path>%{buildroot}/usr/share/|g" %{buildroot}%{_datadir}/maven-metadata/mockito.xml > consumer/.xmvn/mockito.xml
cat > consumer/.xmvn/configuration.xml <<EOF
<configuration><resolverSettings><metadataRepositories>
  <repository>$PWD/consumer/.xmvn/mockito.xml</repository>
  <repository>%{_datadir}/javapackages-bootstrap/maven-metadata</repository>
</metadataRepositories></resolverSettings></configuration>
EOF
cat > consumer/pom.xml <<EOF
<project><modelVersion>4.0.0</modelVersion>
  <groupId>org.openruyi.test</groupId><artifactId>mockito-consumer</artifactId><version>1</version>
  <properties><maven.compiler.release>8</maven.compiler.release></properties>
  <dependencies><dependency><groupId>org.mockito</groupId><artifactId>mockito-junit-jupiter</artifactId>
    <version>%{version}</version><scope>test</scope></dependency></dependencies>
</project>
EOF
cat > consumer/src/test/java/Consumer.java <<'EOF'
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)
class Consumer { @Mock Runnable callback; }
EOF
cd consumer
%{_libexecdir}/javapackages-bootstrap/mvn --offline --batch-mode -Dmaven.repo.local="$PWD/repository" org.apache.maven.plugins:maven-compiler-plugin:testCompile
test -s target/test-classes/Consumer.class

%files
%doc README.md
%license LICENSE LICENSE.concurrent LICENSE.commons
%{_datadir}/maven-metadata/mockito.xml
%{repo_dir}/mockito-core/
%{repo_dir}/mockito-junit-jupiter/

%changelog
%autochangelog
