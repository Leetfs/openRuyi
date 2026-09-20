# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dissimilar
%global full_version 1.0.11
%global pkgname dissimilar-1

Name:           rust-dissimilar-1
Version:        1.0.11
Release:        %autorelease
Summary:        Rust crate "dissimilar"
License:        Apache-2.0
URL:            https://github.com/dtolnay/dissimilar
#!RemoteAsset:  sha256:aeda16ab4059c5fd2a83f2b9c9e9c981327b18aa8e3b313f7e6563799d4f093e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dissimilar"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
