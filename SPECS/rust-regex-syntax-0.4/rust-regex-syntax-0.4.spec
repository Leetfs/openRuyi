# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name regex-syntax
%global full_version 0.4.0
%global pkgname regex-syntax-0.4

Name:           rust-regex-syntax-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "regex-syntax"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/regex
#!RemoteAsset:  sha256:2f9191b1f57603095f105d317e375d19b1c9c5c3185ea9633a99a6dcbed04457
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "regex-syntax"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
