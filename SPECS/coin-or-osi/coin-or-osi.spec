# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           coin-or-osi
Version:        0.108.12
Release:        %autorelease
Summary:        COIN-OR solver interface
License:        EPL-2.0
URL:            https://github.com/coin-or/Osi
#!RemoteAsset:  sha256:1d80d0b4275f2e1ceefc6dda66b8616e3a8c8b07a926ef4456db4a0d55249333
Source0:        %{url}/archive/refs/tags/releases/%{version}.tar.gz#/Osi-%{version}.tar.gz
#!RemoteAsset:  sha256:f767969a308b6370c4fb2d2aea822d906c6531296dc565cb501b43d040034270
Source1:        https://raw.githubusercontent.com/coin-or-tools/Data-Sample/a75e56df8b3f44b09fcf7102546a3ca3cbf53a4f/exmip1.mps
BuildSystem:    autotools

BuildOption(prep):  -n Osi-releases-%{version}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(coinutils)

%description
Osi defines a common C++ interface to linear programming solvers and
provides shared tests for validating solver implementations.

%package        devel
Summary:        Development files for Osi
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for using Osi.

# The release configure script predates the standard --docdir option.
%conf
CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" LDFLAGS="%{build_ldflags}" \
    ./configure --build=%{_build} --host=%{_host} --prefix=%{_prefix} --libdir=%{_libdir} --disable-static

%check -a
# Supply the exmip1 matrix used by the Osi interface tests before running the upstream test target.
mkdir -p Data/Sample
install -pm 0644 %{SOURCE1} Data/Sample/exmip1.mps
%make_build test

%files
%doc README.md
%license LICENSE
%{_libdir}/libOsi.so.*
%{_libdir}/libOsiCommonTests.so.*

%files devel
%{_includedir}/coin/
%{_libdir}/libOsi.so
%{_libdir}/libOsiCommonTests.so
%{_libdir}/pkgconfig/osi.pc
%{_libdir}/pkgconfig/osi-unittests.pc
%{_datadir}/coin/doc/Osi/

%changelog
%autochangelog
