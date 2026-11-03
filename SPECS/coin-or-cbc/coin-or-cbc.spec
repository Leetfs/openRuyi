# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           coin-or-cbc
Version:        2.10.13
Release:        %autorelease
Summary:        COIN-OR mixed-integer linear programming solver
License:        EPL-2.0
URL:            https://github.com/coin-or/Cbc
#!RemoteAsset:  sha256:62fde44dcf6f3d05c5cd291d7435cdd1b7e8acd3c78ec481dd39fe49cbc40399
Source0:        %{url}/archive/refs/tags/releases/%{version}.tar.gz#/Cbc-%{version}.tar.gz
#!RemoteAsset:  sha256:f767969a308b6370c4fb2d2aea822d906c6531296dc565cb501b43d040034270
Source1:        https://raw.githubusercontent.com/coin-or-tools/Data-Sample/a75e56df8b3f44b09fcf7102546a3ca3cbf53a4f/exmip1.mps
BuildSystem:    autotools

BuildOption(prep):  -n Cbc-releases-%{version}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(coinutils)
BuildRequires:  pkgconfig(osi)
BuildRequires:  pkgconfig(cgl)
BuildRequires:  pkgconfig(clp)
BuildRequires:  pkgconfig(osi-clp)
BuildRequires:  pkgconfig(osi-unittests)

%description
Cbc solves mixed-integer programs using branch and cut. It includes a
command-line solver and an Osi adapter.

%package        devel
Summary:        Development files for Cbc
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for using Cbc.

# The release configure script predates the standard --docdir option.
%conf
CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" LDFLAGS="%{build_ldflags}" \
    ./configure --build=%{_build} --host=%{_host} --prefix=%{_prefix} --libdir=%{_libdir} --disable-static

%check -a
# Provide the exmip1 matrix used by the command-line solver check.
mkdir -p Data/Sample
install -pm 0644 %{SOURCE1} Data/Sample/exmip1.mps
# The OsiCbc integration suite reads externally distributed MIPLIB models.
%make_build -C Cbc/test gamstests ctests
# Verify that the packaged solver finds an optimum for that mixed-integer model.
Cbc/src/cbc Data/Sample/exmip1.mps -solve -solution cbc.solution
grep -q '^Optimal' cbc.solution

%files
%doc AUTHORS README.md
%license LICENSE
%{_bindir}/cbc*
%{_libdir}/libCbc*.so.*
%{_libdir}/libOsiCbc.so.*

%files devel
%{_includedir}/coin/
%{_libdir}/libCbc*.so
%{_libdir}/libOsiCbc.so
%{_libdir}/pkgconfig/cbc.pc
%{_libdir}/pkgconfig/osi-cbc.pc
%{_datadir}/coin/doc/Cbc/

%changelog
%autochangelog
