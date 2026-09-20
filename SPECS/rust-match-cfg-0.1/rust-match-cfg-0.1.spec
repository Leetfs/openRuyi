# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name match_cfg
%global full_version 0.1.0
%global pkgname match-cfg-0.1

Name:           rust-match-cfg-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "match_cfg"
License:        MIT OR Apache-2.0
URL:            https://github.com/gnzlbg/match_cfg
#!RemoteAsset:  sha256:ffbee8634e0d45d258acb448e7eaab3fce7a0a467395d4d9f228e3c1f01fb2e4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/use-core) = %{version}

%description
Structured like match statement, the first matching branch is the item that gets emitted.
Source code for takopackized Rust crate "match_cfg"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
