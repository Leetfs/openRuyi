# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name synstructure
%global full_version 0.6.0
%global pkgname synstructure-0.6

Name:           rust-synstructure-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "synstructure"
License:        MIT
URL:            https://github.com/mystor/synstructure
#!RemoteAsset:  sha256:51fa8ce41ed22c8dc2baa435a3c721b0d2b7e7dc6e5460822ea7689e6a640a22
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-0.3/default) >= 0.3.15
Requires:       crate(syn-0.11/default) >= 0.11.0
Requires:       crate(syn-0.11/visit) >= 0.11.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/simple-derive) = %{version}

%description
Source code for takopackized Rust crate "synstructure"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
