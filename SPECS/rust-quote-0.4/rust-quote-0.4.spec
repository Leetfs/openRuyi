# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quote
%global full_version 0.4.0
%global pkgname quote-0.4

Name:           rust-quote-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "quote"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/quote
#!RemoteAsset:  sha256:d9588c006b2b46b884b49393cc875b25d9c6a0905eece0ac25fb43700d64f626
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "quote"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
