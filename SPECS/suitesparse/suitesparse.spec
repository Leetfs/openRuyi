# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           suitesparse
Version:        7.14.1
Release:        %autorelease
Summary:        Column ordering and configuration libraries from SuiteSparse
License:        BSD-3-Clause
URL:            https://github.com/DrTimothyAldenDavis/SuiteSparse
#!RemoteAsset:  sha256:81e560e1f74546df139edb765b3f5bc865866da23062312ffe8fd821063c8397
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/SuiteSparse-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(prep):  -n SuiteSparse-%{version}
BuildOption(conf):  -DSUITESPARSE_ENABLE_PROJECTS="suitesparse_config;colamd"
BuildOption(conf):  -DSUITESPARSE_REQUIRE_BLAS=OFF
BuildOption(conf):  -DBLA_VENDOR=Generic
BuildOption(conf):  -DBUILD_STATIC_LIBS=OFF
BuildOption(conf):  -DSUITESPARSE_DEMOS=ON

BuildRequires:  cmake
BuildRequires:  gcc

%description
SuiteSparse_config provides allocation, timing and version routines used
by sparse matrix libraries.

%package        colamd
Summary:        Column approximate minimum degree ordering for sparse matrices

%description    colamd
COLAMD orders sparse matrix columns to reduce fill during factorization.
Its C API includes routines for 32-bit and 64-bit indices.

%package        devel
Summary:        Headers and build metadata for SuiteSparse_config and COLAMD
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-colamd%{?_isa} = %{version}-%{release}

%description    devel
Headers, CMake modules and pkg-config metadata for building applications
against COLAMD and SuiteSparse_config.

%check -a
# Compare the 32-bit and 64-bit COLAMD ordering demos with their upstream reference output.
for demo in colamd_example colamd_l_example; do
    %{_vpath_builddir}/COLAMD/$demo > "$demo.out"
    diff -u "COLAMD/Demo/$demo.out" "$demo.out"
done

%files
%doc SuiteSparse_config/README.txt
%license LICENSE.txt
%{_libdir}/libsuitesparseconfig.so.*

%files colamd
%doc COLAMD/README.txt
%license COLAMD/Doc/License.txt
%{_libdir}/libcolamd.so.*

%files devel
%{_includedir}/suitesparse/
%{_libdir}/libsuitesparseconfig.so
%{_libdir}/libcolamd.so
%{_libdir}/cmake/
%{_libdir}/pkgconfig/

%changelog
%autochangelog
