# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# LAPACK 3.12.1 intentionally retains the 3.12.0 shared-library version.
%global abi_version 3.12.0

Name:           lapack
Version:        3.12.1
Release:        %autorelease
Summary:        Reference implementation of BLAS and LAPACK
License:        BSD-3-Clause
URL:            https://www.netlib.org/lapack/
VCS:            git:https://github.com/Reference-LAPACK/lapack.git
#!RemoteAsset:  sha256:2ca6407a001a474d4d4d35f3a61550156050c48016d949f0da0529c0aa052422
Source0:        https://github.com/Reference-LAPACK/lapack/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=ON
BuildOption(conf):  -DCBLAS=ON
BuildOption(conf):  -DLAPACKE=ON

BuildRequires:  cmake
BuildRequires:  gcc-fortran
BuildRequires:  pkgconfig(python3)

%description
LAPACK provides Fortran routines for solving common numerical linear algebra
problems, including systems of equations, eigenvalue problems, and singular
value decompositions. This package also includes the reference BLAS library,
the CBLAS and LAPACKE C interfaces, and LAPACK's test matrix generator
library.

%package        devel
Summary:        Development files for LAPACK
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains headers, unversioned library links, pkg-config files,
and CMake metadata for developing software with BLAS, CBLAS, LAPACK, and
LAPACKE.

%files
%doc README.md
%license LICENSE
%{_libdir}/libblas.so.3*
%{_libdir}/libcblas.so.3*
%{_libdir}/liblapack.so.3*
%{_libdir}/liblapacke.so.3*
%{_libdir}/libtmglib.so.3*

%files devel
%{_includedir}/cblas*.h
%{_includedir}/lapack*.h
%{_libdir}/libblas.so
%{_libdir}/libcblas.so
%{_libdir}/liblapack.so
%{_libdir}/liblapacke.so
%{_libdir}/libtmglib.so
%{_libdir}/pkgconfig/blas.pc
%{_libdir}/pkgconfig/cblas.pc
%{_libdir}/pkgconfig/lapack.pc
%{_libdir}/pkgconfig/lapacke.pc
%{_libdir}/cmake/cblas-%{abi_version}/
%{_libdir}/cmake/lapack-%{abi_version}/
%{_libdir}/cmake/lapacke-%{abi_version}/

%changelog
%autochangelog
