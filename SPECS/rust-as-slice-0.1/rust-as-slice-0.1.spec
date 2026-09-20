# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name as-slice
%global full_version 0.1.0
%global pkgname as-slice-0.1

Name:           rust-as-slice-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "as-slice"
License:        MIT OR Apache-2.0
URL:            https://github.com/japaric/as-slice
#!RemoteAsset:  sha256:293dac66b274fab06f95e7efb05ec439a6b70136081ea522d270bc351ae5bb27
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(generic-array-0.12/default) >= 0.12.0
Requires:       crate(stable-deref-trait-1) >= 1.1.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "as-slice"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
