# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           commons-beanutils
Version:        1.11.0
Release:        %autorelease
Summary:        JavaBean property inspection and conversion
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-beanutils/
VCS:            git:https://github.com/apache/commons-beanutils.git
#!RemoteAsset:  sha256:28cace1c5f454f6b17bc7d0175aab79fe85799b4fd56b16bb4683dabd2c84cc7
Source0:        https://downloads.apache.org/commons/beanutils/source/commons-beanutils-%{version}-src.tar.gz
# Downstream use of the existing JUnit 4 runner for the enum security regression.
# https://github.com/apache/commons-beanutils/blob/BEANUTILS_1_11_0/src/test/java/org/apache/commons/beanutils/bugs/EnumDeclaringClassTest.java
Patch2000:      2000-run-enum-security-tests-with-junit4.patch
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  commons-collections3
BuildRequires:  slf4j-jcl
BuildRequires:  junit4
BuildRequires:  slf4j-jdk14

Requires:       java-25-openjdk-headless
Requires:       commons-collections3
Requires:       slf4j-jcl

%description
BeanUtils provides reflection and conversion utilities for reading and
writing JavaBean properties, including nested, indexed and mapped values.

%prep
%autosetup -n commons-beanutils-%{version}-src -p1
find . -type f -name '*.jar' -delete

%build
# Compile the library without resolving Maven plugins or downloading artifacts.
mkdir classes
find src/main/java -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -cp "%{_datadir}/java/commons-collections3.jar:%{_datadir}/java/jcl-over-slf4j.jar" -d classes @sources.list
cat > library.mf <<MANIFEST
Manifest-Version: 1.0
Implementation-Version: %{version}
Class-Path: commons-collections3.jar jcl-over-slf4j.jar

MANIFEST
jar --create --file commons-beanutils.jar --manifest library.mf -C classes .

%install
install -Dpm644 commons-beanutils.jar %{buildroot}%{_datadir}/java/commons-beanutils.jar

%check
# Run the upstream JUnit tests against the system dependencies.
mkdir test-classes
find src/test/java -name '*.java' | sort > tests.list
deps=commons-beanutils.jar:%{_datadir}/java/commons-collections3.jar:%{_datadir}/java/jcl-over-slf4j.jar:%{_datadir}/java/slf4j-jdk14.jar:%{_datadir}/java/junit4.jar:%{_datadir}/java/hamcrest1.3/hamcrest-core.jar
javac --release 8 -encoding UTF-8 -cp "$deps" -d test-classes @tests.list
tests=$(find src/test/java -type f \( -name '*Test.java' -o -name '*TestCase.java' \) \
    ! -name 'Abstract*.java' | sed 's|^src/test/java/||;s|/|.|g;s|\.java$||' | sort)
java -cp "test-classes:$deps" org.junit.runner.JUnitCore $tests

%files
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt
%{_datadir}/java/commons-beanutils.jar

%changelog
%autochangelog
