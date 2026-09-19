# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond valgrind 0

Name:           jq
Version:        1.8.2
Release:        %autorelease
Summary:        A lightweight and flexible command-line JSON processor
License:        MIT AND ICU AND CC-BY-3.0
URL:            https://jqlang.org/
VCS:            git:https://github.com/jqlang/jq
#!RemoteAsset:  sha256:71b8d6e8f5fe81f6c6d0d110e3892251f6ce76ed095abd315e26e6e1193af3af
Source0:        https://github.com/jqlang/jq/releases/download/jq-%{version}/jq-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  chrpath
BuildRequires:  pkgconfig(oniguruma)
%if %{with valgrind}
BuildRequires:  valgrind
%endif
BuildRequires:  tzdata

%description
jq is a lightweight and flexible command-line JSON processor.
You can use it to slice and filter and map and transform structured data.
It is written in portable C, and it has zero runtime dependencies.
It can mangle the data format that you have into the one that you want.

%package        devel
Summary:        Development files for jq
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for jq.

%package        help
Summary:        Documentation and man pages for jq
BuildArch:      noarch

%description    help
Documentation (README, NEWS) and the jq(1) man page.

%install -a
chrpath -d %{buildroot}%{_bindir}/%{name}

%files
%license %{_docdir}/jq/COPYING
%doc %{_docdir}/jq/AUTHORS
%{_bindir}/jq
%{_libdir}/libjq.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/libjq.so
%{_libdir}/pkgconfig/libjq.pc

%files help
%doc %{_docdir}/jq/README.md
%doc %{_docdir}/jq/NEWS.md
%{_mandir}/man1/jq.1*

%changelog
%autochangelog
