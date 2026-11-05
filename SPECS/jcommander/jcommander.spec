# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jcommander
Version:        1.83
Release:        %autorelease
Summary:        Parse annotated Java command-line options
License:        Apache-2.0
URL:            https://jcommander.org/
VCS:            git:https://github.com/cbeust/jcommander.git
#!RemoteAsset:  sha256:1dc01ee67c0f0aa506f7221204b72522e127edfa74f461a123ccdb4ec708f42c
Source0:        https://github.com/cbeust/jcommander/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel

%description
JCommander maps command-line arguments to annotated Java fields. It
handles type conversion, required arguments and nested commands.

%prep
%autosetup
# The distribution includes build tools. Compile the library from its Java sources.
find . -type f -name '*.jar' -delete

%build
mkdir -p classes module
find src/main/java -name '*.java' | sort > sources.list
javac --release 8 -encoding UTF-8 -d classes @sources.list
javac --release 9 --patch-module com.beust.jcommander=classes -d module module-info.java
jar --create --file jcommander.jar -C classes . --release 9 -C module module-info.class

%install
install -Dpm644 jcommander.jar %{buildroot}%{_datadir}/java/jcommander.jar

%check
cat > Parse.java <<'JAVA'
import com.beust.jcommander.JCommander;
import com.beust.jcommander.Parameter;
import com.beust.jcommander.ParameterException;
class Parse {
    @Parameter(names = "--jobs", required = true) int jobs;
    public static void main(String[] args) {
        Parse options = new Parse();
        JCommander parser = JCommander.newBuilder().addObject(options).build();
        parser.parse("--jobs", "3");
        if (options.jobs != 3) throw new AssertionError("Integer conversion");
        try {
            parser.parse("--unknown");
            throw new AssertionError("Accepted an unknown option");
        } catch (ParameterException expected) {}
    }
}
JAVA
javac --release 8 -cp jcommander.jar Parse.java
java -cp .:jcommander.jar Parse
jar --describe-module --file jcommander.jar --release 9 | grep -F com.beust.jcommander

%files
%license license.txt notice.md
%{_datadir}/java/jcommander.jar

%changelog
%autochangelog
