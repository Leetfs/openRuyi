# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows-future
%global full_version 0.2.1
%global pkgname windows-future-0.2

Name:           rust-windows-future-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "windows-future"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:fc6a41e98427b19fe4b73c550f060b59fa592d7d686537eebf9385621bfbad8e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-core-0.61) >= 0.61.1
Requires:       crate(windows-link-0.1) >= 0.1.1
Requires:       crate(windows-threading-0.1) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "windows-future"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
