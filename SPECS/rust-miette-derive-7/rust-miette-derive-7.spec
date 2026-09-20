# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name miette-derive
%global full_version 7.6.0
%global pkgname miette-derive-7

Name:           rust-miette-derive-7
Version:        7.6.0
Release:        %autorelease
Summary:        Rust crate "miette-derive"
License:        Apache-2.0
URL:            https://github.com/zkat/miette
#!RemoteAsset:  sha256:db5b29714e950dbb20d5e6f74f9dcec4edbcc1067bb7f8ed198c097b8c1a818b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/default) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Like `thiserror` for Diagnostics.
Source code for takopackized Rust crate "miette-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
