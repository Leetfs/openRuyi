# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uv-warnings
%global full_version 0.0.96
%global pkgname uv-warnings-0.0.96

Name:           rust-uv-warnings-0.0.96
Version:        0.0.96
Release:        %autorelease
Summary:        Rust crate "uv-warnings"
License:        MIT OR Apache-2.0
URL:            https://pypi.org/project/uv/
#!RemoteAsset:  sha256:0b820ba59ef64b4d464a08ee0b7ae67580f2b61c40ce5453149618a707ce23b8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstream-1/auto) >= 1.0.0
Requires:       crate(anstream-1/wincon) >= 1.0.0
Requires:       crate(owo-colors-4) >= 4.1.0
Requires:       crate(rustc-hash-2/std) >= 2.0.0
Requires:       crate(uv-errors-0.0.96/default) >= 0.0.96

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "uv-warnings"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
