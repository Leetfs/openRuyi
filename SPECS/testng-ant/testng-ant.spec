# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           testng-ant
Version:        1.0.0
Release:        %autorelease
Summary:        Apache Ant task for running TestNG suites
License:        Apache-2.0
URL:            https://testng-team.github.io/testng-ant/
VCS:            git:https://github.com/testng-team/testng-ant.git
#!RemoteAsset:  sha256:97177e81a1b23c8b94f39c2cb924f6f49c910781a74d52e16a3970b36c8ff0e6
Source0:        https://github.com/testng-team/testng-ant/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Downstream fix for whitespace in forked TestNG arguments.
# https://github.com/testng-team/testng-ant/blob/v1.0.0/src/main/java/org/testng/TestNGAntTask.java
Patch2000:      2000-preserve-forked-argument-boundaries.patch
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  java-25-openjdk-devel
BuildRequires:  testng >= 7.10.2

Requires:       ant
Requires:       java-25-openjdk-headless
Requires:       testng >= 7.10.2

%description
This Ant task runs TestNG tests from Ant build files and exposes suite selection,
forked execution and failure handling through standard Ant attributes.

%prep
%autosetup -p1
find . -type f -name '*.jar' -delete

%build
mkdir classes
find src/main/java -name '*.java' | sort > sources.list
javac --release 11 -encoding UTF-8 \
    -cp %{_datadir}/ant/lib/ant.jar:%{_datadir}/java/testng.jar \
    -d classes @sources.list
cat > testng-ant.mf <<MANIFEST
Manifest-Version: 1.0
Implementation-Version: %{version}
Class-Path: file:/usr/share/java/testng.jar
  file:/usr/share/ant/lib/ant.jar

MANIFEST
jar --create --file testng-ant.jar --manifest testng-ant.mf -C classes .

%install
install -Dpm644 testng-ant.jar %{buildroot}%{_datadir}/java/testng-ant.jar
mkdir -p %{buildroot}%{_datadir}/ant/lib
ln -s ../../java/testng-ant.jar %{buildroot}%{_datadir}/ant/lib/testng-ant.jar

%check
# Run a forked suite with the default spaced test name and spaced output paths.
# This directly covers argument transport through the Ant task and Java launcher.
mkdir -p 'check classes'
cat > 'check classes/Passing.java' <<'JAVA'
import org.testng.Assert;
import org.testng.annotations.Test;
public class Passing {
    @Test public void pass() { Assert.assertEquals(21 * 2, 42); }
}
JAVA
cat > 'check classes/Failing.java' <<'JAVA'
import org.testng.Assert;
import org.testng.annotations.Test;
public class Failing {
    @Test public void fail() { Assert.fail("intentional negative control"); }
}
JAVA
javac --release 17 -cp %{_datadir}/java/testng.jar 'check classes/'*.java
cat > checks.xml <<'XML'
<project default="passing">
  <path id="tests">
    <pathelement location="testng-ant.jar"/>
    <pathelement location="%{_datadir}/java/testng.jar"/>
    <pathelement location="check classes"/>
  </path>
  <taskdef name="testng" classname="org.testng.TestNGAntTask" classpathref="tests"/>
  <target name="passing">
    <testng classpathref="tests" outputdir="passing report" haltonfailure="true">
      <classfileset dir="check classes" includes="Passing.class"/>
    </testng>
  </target>
  <target name="failing">
    <testng classpathref="tests" outputdir="failing report" haltonfailure="true">
      <classfileset dir="check classes" includes="Failing.class"/>
    </testng>
  </target>
</project>
XML
ant -f checks.xml passing
test -s 'passing report/index.html'
grep -F 'total="1" passed="1" failed="0"' 'passing report/testng-results.xml'
# Ant must fail when the forked test reports an assertion failure.
if ant -f checks.xml failing; then
    echo 'Ant accepted the failing control test'
    exit 1
fi
grep -F 'failed="1"' 'failing report/testng-results.xml'

%files
%license LICENSE
%{_datadir}/java/testng-ant.jar
%{_datadir}/ant/lib/testng-ant.jar

%changelog
%autochangelog
