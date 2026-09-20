# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name widestring
%global full_version 0.5.0
%global pkgname widestring-0.5

Name:           rust-widestring-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "widestring"
License:        MIT OR Apache-2.0
URL:            https://github.com/starkat99/widestring-rs
#!RemoteAsset:  sha256:15be6395051be4e41efeee975b7561b8c602ba30204bfa35fefa0f85582075b6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Both `u16` and `u32` string types are provided, including support for UTF-16 and UTF-32, malformed encoding, C-style strings, etc.
Source code for takopackized Rust crate "widestring"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
