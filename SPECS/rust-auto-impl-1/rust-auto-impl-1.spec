# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name auto_impl
%global full_version 1.3.0
%global pkgname auto-impl-1

Name:           rust-auto-impl-1
Version:        1.3.0
Release:        %autorelease
Summary:        Rust crate "auto_impl"
License:        MIT OR Apache-2.0
URL:            https://github.com/auto-impl-rs/auto_impl/
#!RemoteAsset:  sha256:ffdcb70bdbc4d478427380519163274ac86e52916e10f0a8889adf0f96d3fee7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/default) >= 2.0.117
Requires:       crate(syn-2/full) >= 2.0.117
Requires:       crate(syn-2/visit) >= 2.0.117
Requires:       crate(syn-2/visit-mut) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "auto_impl"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
