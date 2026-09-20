# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name syntex_errors
%global full_version 0.39.0
%global pkgname syntex-errors-0.39

Name:           rust-syntex-errors-0.39
Version:        0.39.0
Release:        %autorelease
Summary:        Rust crate "syntex_errors"
License:        MIT OR Apache-2.0
URL:            https://github.com/serde-rs/syntex
#!RemoteAsset:  sha256:7b2b48e32b90ebbd428cfbcb768fa2b798b6869100bd5980f433eb9c0aab14d0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.13
Requires:       crate(log-0.3/default) >= 0.3.3
Requires:       crate(rustc-serialize-0.3/default) >= 0.3.16
Requires:       crate(syntex-pos-0.39/default) >= 0.39.0
Requires:       crate(term-0.4/default) >= 0.4.4
Requires:       crate(unicode-xid-0.0.3/default) >= 0.0.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "syntex_errors"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
