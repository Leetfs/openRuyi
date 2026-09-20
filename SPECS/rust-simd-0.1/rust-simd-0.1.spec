# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name simd
%global full_version 0.1.0
%global pkgname simd-0.1

Name:           rust-simd-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "simd"
License:        MIT OR Apache-2.0
URL:            https://github.com/huonw/simd
#!RemoteAsset:  sha256:e76c201f9f97660550e0900babb7c43f76f910d78d859dfc5dde496ee1de189e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/doc) = %{version}

%description
Source code for takopackized Rust crate "simd"

%package     -n %{name}+serde
Summary:        `simd` offers limited cross-platform access to SIMD instructions on CPUs, as well as raw interfaces to platform-specific instructions - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust simd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-macros
Summary:        `simd` offers limited cross-platform access to SIMD instructions on CPUs, as well as raw interfaces to platform-specific instructions - feature "serde_macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-macros-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/serde-macros) = %{version}

%description -n %{name}+serde-macros
This metapackage enables feature "serde_macros" for the Rust simd crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
