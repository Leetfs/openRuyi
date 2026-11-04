# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global upstream_version %{version}-GA
%global artifact_dir %{_datadir}/maven-repository/org/javassist/javassist/%{upstream_version}
%global bootstrap_java %{_datadir}/java/javapackages-bootstrap
Name:           javassist
Version:        3.27.0
Release:        %autorelease
Summary:        Java class file inspection and bytecode transformation
License:        MPL-1.1 OR LGPL-2.1-or-later OR Apache-2.0
URL:            https://www.javassist.org/
VCS:            git:https://github.com/jboss-javassist/javassist
#!RemoteAsset:  sha256:52b68060a587f0ab883aba14cddecaef6f1675b3ea5ff50f20f513cd267b5b2a
Source0:        https://github.com/jboss-javassist/javassist/archive/refs/tags/rel_3_27_0_ga.tar.gz?/javassist-%{upstream_version}.tar.gz
Source1:        BuildJavassist.java
Patch1:         0001-Preserve-unnamed-method-parameters.patch
BuildArch:      noarch
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javapackages-bootstrap
Provides:       mvn(org.javassist:javassist) == %{upstream_version}
Requires:       java-25-openjdk

%description
Javassist reads and writes Java class files. Its compiler and bytecode
APIs support runtime instrumentation, class loaders and dynamic proxies.

%prep
%autosetup -p1 -n javassist-rel_3_27_0_ga
rm javassist.jar
# The inner-class compiler test originally used the RMI activation API removed in Java 17.
for f in src/test/test2/Inner.java src/test/javassist/JvstTest2.java; do
    grep -F 'java.rmi.activation.ActivationGroupDesc.CommandEnvironment' "$f"
    sed -i -e 's/java.rmi.activation.ActivationGroupDesc.CommandEnvironment/java.util.AbstractMap.SimpleEntry/g' \
        -e 's/java.rmi.activation.ActivationGroupDesc/java.util.AbstractMap.SimpleImmutableEntry/g' "$f"
done
# Date.getYear retains the same Deprecated attribute after Thread.suspend was removed.
sed -i '/void testDeprecatedAttribute()/,/getDeclaredMethod("toString")/{
    s/java.lang.Thread/java.util.Date/
    s/getDeclaredMethod("suspend")/getDeclaredMethod("getYear")/
}' src/test/javassist/bytecode/BytecodeTest.java

%build
mkdir -p target/classes/META-INF/maven/org.javassist/javassist
cp pom.xml target/classes/META-INF/maven/org.javassist/javassist/
find src/main -name '*.java' | sort > target/sources
# The two debugger utilities compile against JDI and the JDK Attach API.
javac -source 8 -target 8 -g -proc:none -encoding UTF-8 -d target/classes @target/sources
java -cp '%{bootstrap_java}/*' %{SOURCE1} target/classes javassist.jar

%install
mkdir -p %{buildroot}%{artifact_dir} %{buildroot}%{_datadir}/maven-metadata
install -m644 javassist.jar %{buildroot}%{artifact_dir}/javassist-%{upstream_version}.jar
install -m644 pom.xml %{buildroot}%{artifact_dir}/javassist-%{upstream_version}.pom
cat > %{buildroot}%{_datadir}/maven-metadata/javassist.xml <<EOF
<metadata><artifacts>
 <artifact><groupId>org.javassist</groupId><artifactId>javassist</artifactId><version>%{upstream_version}</version><extension>jar</extension>
 <path>%{artifact_dir}/javassist-%{upstream_version}.jar</path><compatVersions><version>%{upstream_version}</version><version>SYSTEM</version></compatVersions></artifact>
 <artifact><groupId>org.javassist</groupId><artifactId>javassist</artifactId><version>%{upstream_version}</version><extension>pom</extension>
 <path>%{artifact_dir}/javassist-%{upstream_version}.pom</path><compatVersions><version>%{upstream_version}</version><version>SYSTEM</version></compatVersions></artifact>
</artifacts></metadata>
EOF

%check
mkdir -p target/{test-classes,runtest} target/fixture-src/{com/test,org/ow2/jonas/empty} target/fixture-classes
# The archive lookup tests use a named empty class and an archive that can be deleted.
echo 'package com.test; public class Test {}' > target/fixture-src/com/test/Test.java
echo 'package org.ow2.jonas.empty; public class Empty {}' > target/fixture-src/org/ow2/jonas/empty/Empty.java
javac --release 8 -d target/fixture-classes target/fixture-src/com/test/Test.java target/fixture-src/org/ow2/jonas/empty/Empty.java
jar cf target/test-classes/simple.jar -C target/fixture-classes com/test/Test.class
jar cf target/test-classes/empty.jar -C target/fixture-classes org/ow2/jonas/empty/Empty.class
base=$PWD
cp="$base/javassist.jar:%{bootstrap_java}/junit.jar:%{bootstrap_java}/hamcrest-core.jar"
javac --release 21 -d target/test-classes src/test/fixtures/Java21InnerClassWithoutParameters.java
find src/test -name '*.java' ! -path 'src/test/fixtures/*' | sort > target/test-sources
javac --release 11 -g -parameters -proc:none -encoding UTF-8 -cp "$cp" -d target/test-classes @target/test-sources
cd target/runtest
java -Xmx768m --add-opens=java.base/java.lang=ALL-UNNAMED -Djdk.attach.allowAttachSelf=true -XX:+EnableDynamicAgentLoading \
    -cp "$base/target/test-classes:$base/target/classes:$cp" junit.textui.TestRunner javassist.JvstTest

%files
%license License.html
%doc README.md
%{_datadir}/maven-metadata/javassist.xml
%{artifact_dir}/

%changelog
%autochangelog
