# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name memoffset
%global full_version 0.5.0
%global pkgname memoffset-0.5

Name:           rust-memoffset-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "memoffset"
License:        MIT
URL:            https://github.com/Gilnaa/memoffset
#!RemoteAsset:  sha256:dea4bf2ae5c6a9c64c2ba12b0c5a73b2e24d9aa205a1c3e1cdd7d0c0c1bfe3b2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustc-version-0.2) >= 0.2.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "memoffset"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
