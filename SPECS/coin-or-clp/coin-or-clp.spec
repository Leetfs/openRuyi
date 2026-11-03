# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           coin-or-clp
Version:        1.17.11
Release:        %autorelease
Summary:        COIN-OR linear programming solver
License:        EPL-2.0
URL:            https://github.com/coin-or/Clp
#!RemoteAsset:  sha256:2c078e174dc1a7a308e091b6256fb34b4017897fc140ea707ba207b2913ea46d
Source0:        %{url}/archive/refs/tags/releases/%{version}.tar.gz#/Clp-%{version}.tar.gz
#!RemoteAsset:  sha256:f767969a308b6370c4fb2d2aea822d906c6531296dc565cb501b43d040034270
Source1:        https://raw.githubusercontent.com/coin-or-tools/Data-Sample/a75e56df8b3f44b09fcf7102546a3ca3cbf53a4f/exmip1.mps
BuildSystem:    autotools

BuildOption(prep):  -n Clp-releases-%{version}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(coinutils)
BuildRequires:  pkgconfig(osi)
BuildRequires:  pkgconfig(osi-unittests)

%description
Clp implements simplex and barrier methods for continuous linear
programs. It includes a command-line solver and an Osi adapter.

%package        devel
Summary:        Development files for Clp
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for using Clp.

# The release configure script predates the standard --docdir option.
%conf
CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" LDFLAGS="%{build_ldflags}" \
    ./configure --build=%{_build} --host=%{_host} --prefix=%{_prefix} --libdir=%{_libdir} --disable-static

%check -a
# Provide the exmip1 input for the offline solver tests.
mkdir -p Data/Sample
install -pm 0644 %{SOURCE1} Data/Sample/exmip1.mps
# The OsiClp integration tests additionally require the external MIPLIB p0033 instance.
(cd Clp/test && ../src/clp -unitTest)
# Solve the shipped MPS example and verify that the CLI reports an optimum.
Clp/src/clp Clp/examples/hello.mps -solve -solution hello.solution
grep -q '^Optimal' hello.solution

%files
%doc AUTHORS README.md
%license LICENSE
%{_bindir}/clp
%{_libdir}/libClp*.so.*
%{_libdir}/libOsiClp.so.*

%files devel
%{_includedir}/coin/
%{_libdir}/libClp*.so
%{_libdir}/libOsiClp.so
%{_libdir}/pkgconfig/clp.pc
%{_libdir}/pkgconfig/osi-clp.pc
%{_datadir}/coin/doc/Clp/

%changelog
%autochangelog
