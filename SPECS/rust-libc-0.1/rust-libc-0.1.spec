# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libc
%global full_version 0.1.1
%global pkgname libc-0.1

Name:           rust-libc-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "libc"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/libc
#!RemoteAsset:  sha256:a2b2cedc8d50557005b2a6bb62e0f56b00f1aaaa2c4d3c67e9fe538b0c33d368
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/cargo-build) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "libc"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
