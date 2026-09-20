# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name humantime
%global full_version 1.1.0
%global pkgname humantime-1

Name:           rust-humantime-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "humantime"
License:        MIT OR Apache-2.0
URL:            https://github.com/tailhook/humantime
#!RemoteAsset:  sha256:5369e01a05e3404c421b5d6dcfea6ecf7d5e65eba8a275948151358cd8282042
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quick-error-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "humantime"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
