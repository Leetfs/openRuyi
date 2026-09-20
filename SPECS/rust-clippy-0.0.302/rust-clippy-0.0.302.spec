# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clippy
%global full_version 0.0.302
%global pkgname clippy-0.0.302

Name:           rust-clippy-0.0.302
Version:        0.0.302
Release:        %autorelease
Summary:        Rust crate "clippy"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang-nursery/rust-clippy
#!RemoteAsset:  sha256:d911ee15579a3f50880d8c1d59ef6e79f9533127a3bd342462f5d584f5e8c294
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(term-0.5) >= 0.5.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
This package contains the following binaries built from the Rust crate
"clippy":
- clippy

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
