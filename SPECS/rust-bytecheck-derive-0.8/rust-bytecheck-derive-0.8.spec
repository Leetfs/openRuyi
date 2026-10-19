# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bytecheck_derive
%global full_version 0.8.3
%global pkgname bytecheck-derive-0.8

Name:           rust-bytecheck-derive-0.8
Version:        0.8.3
Release:        %autorelease
Summary:        Rust crate "bytecheck_derive"
License:        MIT
URL:            https://github.com/rkyv/bytecheck
#!RemoteAsset:  sha256:46d07918caa9eeaaf06b7873925c53a61daac173539b4f7715090745e44e4e69
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1) >= 1.0.0
Requires:       crate(quote-1) >= 1.0.0
Requires:       crate(syn-3/clone-impls) >= 3.0.0
Requires:       crate(syn-3/derive) >= 3.0.0
Requires:       crate(syn-3/full) >= 3.0.0
Requires:       crate(syn-3/parsing) >= 3.0.0
Requires:       crate(syn-3/printing) >= 3.0.0
Requires:       crate(syn-3/proc-macro) >= 3.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "bytecheck_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
