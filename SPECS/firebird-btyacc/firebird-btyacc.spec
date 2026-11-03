# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global build_number 33856-0

Name:           firebird-btyacc
Version:        3.0.14
Release:        %autorelease
Summary:        Backtracking SQL parser generator for Firebird
License:        LicenseRef-openRuyi-Public-Domain
URL:            https://github.com/FirebirdSQL/firebird
#!RemoteAsset:  sha256:dce3f26c0f015b3c40f36085f8cc21de58dd568e0f347fdd0fcc7942deda8cff
Source0:        %{url}/releases/download/v%{version}/Firebird-%{version}.%{build_number}.tar.bz2

# Downstream: retain private scratch streams while generating parser output.
# https://github.com/FirebirdSQL/firebird/blob/v3.0.14/extern/btyacc/main.c
Patch0:         2000-use-private-streams-for-parser-temporaries.patch

BuildRequires:  gcc
BuildRequires:  make

%description
Firebird's BtYacc generates separate SQL keyword and semantic type guards
and accepts the grammar extensions used by the Firebird SQL parser.

%prep
%autosetup -p1 -n Firebird-%{version}.%{build_number}

%build
%make_build -C extern/btyacc CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"

%install
install -Dpm 0755 extern/btyacc/btyacc %{buildroot}%{_bindir}/%{name}

%check
# Generate the Firebird SQL parser and compare its token header with the released interface.
install -d -m 0700 grammar/tmp
cd grammar
sed -n '/%%type .*/p' ../src/dsql/parse.y > types.y
sed 's/%%type .*//' ../src/dsql/parse.y > y.y
TMPDIR="$PWD/tmp" ../extern/btyacc/btyacc -l -d -S ../src/dsql/btyacc_fb.ske y.y
cmp y_tab.h ../src/include/gen/parse.h
grep -q 'yyparse' y_tab.c

%files
%license extern/btyacc/README extern/btyacc/README.BYACC
%{_bindir}/firebird-btyacc

%changelog
%autochangelog
