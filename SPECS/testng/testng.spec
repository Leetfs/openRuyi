# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           testng
Version:        7.12.0
Release:        %autorelease
Summary:        Annotation-based testing framework for Java
License:        Apache-2.0
URL:            https://testng.org/
VCS:            git:https://github.com/testng-team/testng.git
#!RemoteAsset:  sha256:0983e3e7593b87ccb65ef9470034b310d05fbc638386e7b82b0d97676c19e008
Source0:        https://github.com/testng-team/testng/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Downstream integration with the system JavaScript library.
# https://github.com/testng-team/testng/blob/7.12.0/testng-core/src/main/java/org/testng/reporters/jq/Main.java
Patch2000:      2000-use-system-jquery-for-reports.patch
BuildArch:      noarch

BuildRequires:  guice
BuildRequires:  java-25-openjdk-devel
BuildRequires:  jcommander
BuildRequires:  jquery3
BuildRequires:  jsr305
BuildRequires:  slf4j-jdk14
BuildRequires:  snakeyaml

Requires:       guice
Requires:       java-25-openjdk-headless
Requires:       jcommander
Requires:       jquery3
Requires:       jsr305
Requires:       slf4j-jdk14
Requires:       snakeyaml

%description
TestNG runs Java tests described by annotations or XML suites. It supports
parameterized tests, dependent methods, injected fixtures and XML and HTML
reports. Its command-line runner is available as the testng command.

%prep
%autosetup -p1
find . -type f -name '*.jar' -delete
rm testng-core/src/main/resources/org/testng/jquery-3.6.0.min.js

%build
mkdir classes
find testng-api/src/main/java testng-asserts/src/main/java \
    testng-collections/src/main/java testng-core-api/src/main/java \
    testng-reflection-utils/src/main/java testng-runner-api/src/main/java \
    testng-core/src/main/java -name '*.java' ! -name module-info.java | sort > sources.list
deps=%{_datadir}/java/guice.jar:%{_datadir}/java/jcommander.jar:%{_datadir}/java/slf4j-api.jar:%{_datadir}/java/jsr305.jar:%{_datadir}/java/snakeyaml.jar
javac --release 17 -encoding UTF-8 -cp "$deps" -d classes @sources.list
cp -a testng-core/src/main/resources/. classes/
cat > testng.mf <<MANIFEST
Manifest-Version: 1.0
Main-Class: org.testng.TestNG
Implementation-Version: %{version}
Automatic-Module-Name: org.testng
Class-Path: guice.jar jcommander.jar slf4j-api.jar slf4j-jdk14.jar
  jsr305.jar snakeyaml.jar

MANIFEST
jar --create --file testng.jar --manifest testng.mf -C classes .

%install
install -Dpm644 testng.jar %{buildroot}%{_datadir}/java/testng.jar
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/testng <<'SH'
#!/bin/sh
exec java -cp "/usr/share/java/testng.jar${CLASSPATH:+:$CLASSPATH}" org.testng.TestNG "$@"
SH
chmod 755 %{buildroot}%{_bindir}/testng

%check
# Exercise injection, data providers, dependencies and the default HTML reports.
mkdir checks
cat > checks/FrameworkCheck.java <<'JAVA'
import org.testng.Assert;
import org.testng.annotations.*;
import com.google.inject.*;

@org.testng.annotations.Guice(modules = FrameworkCheck.Bindings.class)
public class FrameworkCheck {
    public static class Bindings extends AbstractModule {
        protected void configure() { bind(Integer.class).toInstance(42); }
    }
    @Inject Integer value;
    @DataProvider(name = "values")
    public Object[][] values() { return new Object[][] { {21}, {21} }; }
    @Test(dataProvider = "values")
    public void injected(int half) { Assert.assertEquals(half * 2, value.intValue()); }
    @Test(dependsOnMethods = "injected")
    public void dependent() { Assert.assertNotNull(value); }
    @Test(expectedExceptions = IllegalArgumentException.class)
    public void expectedFailure() { throw new IllegalArgumentException("expected"); }
}
JAVA
cat > checks/FailureCheck.java <<'JAVA'
import org.testng.Assert;
import org.testng.annotations.Test;
public class FailureCheck {
    @Test public void fails() { Assert.fail("intentional negative control"); }
}
JAVA
deps=testng.jar:%{_datadir}/java/guice.jar:%{_datadir}/java/jcommander.jar:%{_datadir}/java/slf4j-api.jar:%{_datadir}/java/slf4j-jdk14.jar:%{_datadir}/java/jsr305.jar:%{_datadir}/java/snakeyaml.jar
javac --release 17 -cp "$deps" checks/*.java
# Exercise the installed launcher with caller-supplied test classes.
sed "s|/usr/share/java/testng.jar|$PWD/testng.jar|" \
    %{buildroot}%{_bindir}/testng > testng-check
jar --create --file passing-tests.jar -C checks FrameworkCheck.class \
    -C checks 'FrameworkCheck$Bindings.class'
CLASSPATH="$PWD/passing-tests.jar:$deps" sh ./testng-check -testjar "$PWD/passing-tests.jar" -d "passing report"
test -s "passing report/index.html"
grep -F 'total="4"' "passing report/testng-results.xml"
cmp %{_datadir}/javascript/jquery3/jquery.js "passing report/jquery-3.6.0.min.js"
# Confirm that a failing test is reflected in both the status and XML report.
if CLASSPATH="checks:$deps" sh ./testng-check -testclass FailureCheck -d "failing report"; then
    echo 'Accepted the failing control test'
    exit 1
else
    test "$?" -eq 1
fi
grep -F 'failed="1"' "failing report/testng-results.xml"

%files
%license LICENSE.txt
%{_bindir}/testng
%{_datadir}/java/testng.jar

%changelog
%autochangelog
