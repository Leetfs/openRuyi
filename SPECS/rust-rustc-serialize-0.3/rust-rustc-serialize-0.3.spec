# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustc-serialize
%global full_version 0.3.16
%global pkgname rustc-serialize-0.3

Name:           rust-rustc-serialize-0.3
Version:        0.3.16
Release:        %autorelease
Summary:        Rust crate "rustc-serialize"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/rustc-serialize
#!RemoteAsset:  sha256:1a48546a64cae47d06885e9bccadb99d0547d877a94c5167fa451ea33a484456
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Also includes support for hex, base64, and json encoding and decoding.
Source code for takopackized Rust crate "rustc-serialize"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
