# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hashbrown
%global full_version 0.1.0
%global pkgname hashbrown-0.1

Name:           rust-hashbrown-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "hashbrown"
License:        Apache-2.0 OR MIT
URL:            https://github.com/Amanieu/hashbrown
#!RemoteAsset:  sha256:38799f5c6a3fbd412bdc8d8647108a3e5b8031823210db000968556be358bf64
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1) >= 1.0.0
Requires:       crate(scopeguard-0.3) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "hashbrown"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
