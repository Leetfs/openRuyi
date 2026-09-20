# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name scopeguard
%global full_version 0.3.0
%global pkgname scopeguard-0.3

Name:           rust-scopeguard-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "scopeguard"
License:        MIT OR Apache-2.0
URL:            https://github.com/bluss/scopeguard
#!RemoteAsset:  sha256:ce108ea69fbd2c47dd2e75806bd7fc14bd58e73c7720544879449088f730716d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/use-std) = %{version}

%description
Defines the macros `defer!` and `defer_on_unwind!`; the latter only runs if the scope is extited through unwinding on panic.
Source code for takopackized Rust crate "scopeguard"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
