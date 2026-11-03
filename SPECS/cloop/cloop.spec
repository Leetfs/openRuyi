# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit 05a4d28642afce2e8efe43e312aada3f2abb70fa

Name:           cloop
Version:        0^20260725git05a4d28
Release:        %autorelease
Summary:        Cross-language interface definition compiler
License:        LicenseRef-IDPL-1.0
URL:            https://github.com/asfernandes/cloop
#!RemoteAsset:  sha256:3934d00a9dedd7110e2d174a736aaec6c67c1e52d0ade552d98f1288e4eb21d0
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
#!RemoteAsset:  sha256:cbe82df6d443ea5d96ac97c469db517b1b8ea785ce18cacb7c21d196c1e7c0ce
Source1:        https://raw.githubusercontent.com/FirebirdSQL/firebird/v3.0.14/doc/license/IDPL.txt
BuildSystem:    cmake

BuildOption(prep):  -n %{name}-%{commit}

BuildRequires:  cmake >= 3.16
BuildRequires:  gcc-c++

%description
CLoop generates language bindings from an interface definition. Its
backends include C, C++ and Pascal.

%prep -a
cp -p %{SOURCE1} IDPL.txt

%install
install -Dpm 0755 %{_vpath_builddir}/bin/cloop %{buildroot}%{_bindir}/cloop

%check
# Run the C and C++ clients against both shared implementations of the upstream calculator interface.
for test in c cpp; do
    for implementation in c cpp; do
        %{_vpath_builddir}/bin/test1-$test "$PWD/%{_vpath_builddir}/lib/test1-$implementation.so"
    done
done

%files
%license IDPL.txt
%{_bindir}/cloop

%changelog
%autochangelog
