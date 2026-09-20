# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hash32
%global full_version 0.1.0
%global pkgname hash32-0.1

Name:           rust-hash32-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "hash32"
License:        MIT OR Apache-2.0
URL:            https://github.com/japaric/hash32
#!RemoteAsset:  sha256:12d790435639c06a7b798af9e1e331ae245b7ef915b92f70a39b4cf8c00686af
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1) >= 1.2.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/const-fn) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "hash32"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
