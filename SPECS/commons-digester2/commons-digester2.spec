# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           commons-digester2
Version:        2.1
Release:        %autorelease
Summary:        XML to Java object mapping using Digester 2 APIs
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-digester/
VCS:            git:https://github.com/apache/commons-digester.git
#!RemoteAsset:  sha256:2713f07a6adec7e253d91f1fca70e658b93e1a63f1b6a36f4907a2b83088543f
Source0:        https://archive.apache.org/dist/commons/digester/source/commons-digester-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  commons-beanutils
BuildRequires:  slf4j-jcl
BuildRequires:  junit4
BuildRequires:  slf4j-jdk14

Requires:       java-25-openjdk-headless
Requires:       commons-beanutils
Requires:       slf4j-jcl

%description
Commons Digester builds Java object graphs from XML using configurable
rules. This package supplies the org.apache.commons.digester API used by
Commons Validator; Digester 3 uses a different Java package.

%prep
%autosetup -n commons-digester-%{version}-src
find . -type f -name '*.jar' -delete

%build
# Compile the library without resolving Maven plugins or downloading artifacts.
mkdir classes
find src/main/java -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -cp "%{_datadir}/java/commons-beanutils.jar:%{_datadir}/java/jcl-over-slf4j.jar" -d classes @sources.list
cp -a src/main/resources/. classes/
cat > library.mf <<MANIFEST
Manifest-Version: 1.0
Implementation-Version: %{version}
Class-Path: commons-beanutils.jar jcl-over-slf4j.jar

MANIFEST
jar --create --file commons-digester2.jar --manifest library.mf -C classes .

%install
install -Dpm644 commons-digester2.jar %{buildroot}%{_datadir}/java/commons-digester2.jar

%check
# Run the upstream JUnit tests against the system dependencies.
mkdir test-classes
find src/test/java -name '*.java' | sort > tests.list
deps=commons-digester2.jar:%{_datadir}/java/commons-beanutils.jar:%{_datadir}/java/jcl-over-slf4j.jar:%{_datadir}/java/slf4j-jdk14.jar:%{_datadir}/java/junit4.jar:%{_datadir}/java/hamcrest1.3/hamcrest-core.jar
javac --release 8 -encoding UTF-8 -cp "$deps" -d test-classes @tests.list
cp -a src/test/resources/. test-classes/
tests=$(find src/test/java -type f \( -name '*Test.java' -o -name '*TestCase.java' \) \
    ! -name 'Abstract*.java' | sed 's|^src/test/java/||;s|/|.|g;s|\.java$||' | sort)
java -cp "test-classes:$deps" org.junit.runner.JUnitCore $tests

%files
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt
%{_datadir}/java/commons-digester2.jar

%changelog
%autochangelog
