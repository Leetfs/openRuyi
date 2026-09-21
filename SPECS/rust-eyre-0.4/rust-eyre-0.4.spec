# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name eyre
%global full_version 0.4.3
%global pkgname eyre-0.4

Name:           rust-eyre-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "eyre"
License:        MIT OR Apache-2.0
URL:            https://github.com/yaahc/eyre
#!RemoteAsset:  sha256:e9e412cbea04ea7af520b2f4d4ac1677ce546027a7237d8a40b494e34e1e0e31
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(indenter-0.3/default) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "eyre"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
