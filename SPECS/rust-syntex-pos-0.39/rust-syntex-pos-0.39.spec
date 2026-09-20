# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name syntex_pos
%global full_version 0.39.0
%global pkgname syntex-pos-0.39

Name:           rust-syntex-pos-0.39
Version:        0.39.0
Release:        %autorelease
Summary:        Rust crate "syntex_pos"
License:        MIT OR Apache-2.0
URL:            https://github.com/serde-rs/syntex
#!RemoteAsset:  sha256:f0e5253631b0329f46ebcae63c2db016d4c8171eaa940610cc894f45617ebe92
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustc-serialize-0.3/default) >= 0.3.16

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "syntex_pos"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
