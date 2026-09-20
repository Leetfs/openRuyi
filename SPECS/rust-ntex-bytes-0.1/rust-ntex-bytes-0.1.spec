# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ntex-bytes
%global full_version 0.1.31
%global pkgname ntex-bytes-0.1

Name:           rust-ntex-bytes-0.1
Version:        0.1.31
Release:        %autorelease
Summary:        Rust crate "ntex-bytes"
License:        MIT OR Apache-2.0
URL:            https://github.com/ntex-rs/ntex
#!RemoteAsset:  sha256:da68b58d622475c69e4f19e33d12f90b4acaff1939f134e09e9318ad8bc6fa74
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(futures-core-0.3/alloc) >= 0.3.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ntex-bytes"

%package     -n %{name}+simdutf8
Summary:        Types and traits for working with bytes (bytes crate fork) - feature "simdutf8" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(simdutf8-0.1/default) >= 0.1.5
Provides:       crate(%{pkgname}/simd) = %{version}
Provides:       crate(%{pkgname}/simdutf8) = %{version}

%description -n %{name}+simdutf8
This metapackage enables feature "simdutf8" for the Rust ntex-bytes crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "simd" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
