# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name darling_macro
%global full_version 0.14.0
%global pkgname darling-macro-0.14

Name:           rust-darling-macro-0.14
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "darling_macro"
License:        MIT
URL:            https://github.com/TedDriggs/darling
#!RemoteAsset:  sha256:64dd7e5a75a00cb6799ae9fbbfc3bba0134def6579a9e27564e72c839c837bed
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(darling-core-0.14/default) >= 0.14.0
Requires:       crate(quote-1/default) >= 1.0.18
Requires:       crate(syn-1/default) >= 1.0.91

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Use https://crates.io/crates/darling in your code.
Source code for takopackized Rust crate "darling_macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
