# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           byaccj
Version:        1.15
Release:        %autorelease
Summary:        LALR parser generator with Java support
License:        LicenseRef-openRuyi-Public-Domain
URL:            https://byaccj.sourceforge.net/
#!RemoteAsset:  sha256:4d6ba21fa5bc4ec4b1be9eb6e6efbb367eb6df2577fd0eaff60be9c6614f6609
Source0:        https://downloads.sourceforge.net/%{name}/%{name}%{version}_src.tar.gz

BuildRequires:  gcc
BuildRequires:  java-25-openjdk-devel

%description
BYACC/J generates LALR parsers in Java or C from Berkeley Yacc grammars.
It adds Java semantic actions and parser classes to the Berkeley parser
generator.

%prep
%autosetup -n %{name}%{version}

%build
%set_build_flags
# The release Makefile hardcodes an i386 macOS SDK in its link rule.
%{__cc} $CPPFLAGS $CFLAGS -std=gnu17 -include unistd.h src/*.c $LDFLAGS -o byaccj

%install
install -Dm755 byaccj %{buildroot}%{_bindir}/byaccj
install -Dm644 src/yacc.1 %{buildroot}%{_mandir}/man1/byaccj.1

%check
mkdir regression
cd regression
../byaccj -J ../src/t.y
cat > Check.java <<'EOF'
import java.util.StringTokenizer;
class Check {
    public static void main(String[] args) {
        Parser parser = new Parser();
        parser.st = new StringTokenizer("2 + 3 * 4");
        if (parser.yyparse() != 0) throw new AssertionError("parse failed");
    }
}
EOF
javac Parser.java ParserVal.java Check.java
java Check | grep -Fx ' 14.0 '

%files
%doc docs/ACKNOWLEDGEMEN docs/tf.y src/new_features
%license src/no_warranty
%{_bindir}/byaccj
%{_mandir}/man1/byaccj.1*

%changelog
%autochangelog
