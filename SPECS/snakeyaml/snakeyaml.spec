# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           snakeyaml
Version:        2.7
Release:        %autorelease
Summary:        Parse and emit YAML documents in Java
License:        Apache-2.0
URL:            https://codeberg.org/snakeyaml/snakeyaml
VCS:            git:https://codeberg.org/snakeyaml/snakeyaml.git
#!RemoteAsset:  sha256:a011107dd64e2b606b93f9d367b84f6209388450d6d13204fa4ab9bbd3980aad
Source0:        https://codeberg.org/snakeyaml/snakeyaml/archive/snakeyaml-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4

%description
SnakeYAML reads YAML streams into Java objects and writes Java values as
YAML. Applications can also consume parser events or work directly with
the YAML representation graph.

%prep
%autosetup -n snakeyaml

%build
mkdir -p classes module
find src/main/java -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -d classes @sources.list
find src/main/java9 -name '*.java' | sort > module.list
javac --release 9 --patch-module org.yaml.snakeyaml=classes -d module @module.list
jar --create --file snakeyaml.jar -C classes . --release 9 -C module .

%install
install -Dpm644 snakeyaml.jar %{buildroot}%{_datadir}/java/snakeyaml.jar

%check
mkdir tests
cp=snakeyaml.jar:%{_datadir}/java/junit4.jar
javac --release 8 -encoding UTF-8 -cp "$cp" -sourcepath src/test/java -d tests \
    src/test/java/org/yaml/snakeyaml/{Chapter2_2Test,Chapter2_3Test,YamlComposeTest,YamlParseTest,InputOutputExceptionTest}.java
java -cp "tests:src/test/resources:$cp" org.junit.runner.JUnitCore \
    org.yaml.snakeyaml.Chapter2_2Test org.yaml.snakeyaml.Chapter2_3Test \
    org.yaml.snakeyaml.YamlComposeTest org.yaml.snakeyaml.YamlParseTest org.yaml.snakeyaml.InputOutputExceptionTest

%files
%license LICENSE.txt
%{_datadir}/java/snakeyaml.jar

%changelog
%autochangelog
