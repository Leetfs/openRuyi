# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ptr_meta_derive
%global full_version 0.3.2
%global pkgname ptr-meta-derive-0.3

Name:           rust-ptr-meta-derive-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "ptr_meta_derive"
License:        MIT
URL:            https://github.com/rkyv/ptr_meta
#!RemoteAsset:  sha256:1c8d9ca532f185d5d4db7a7c9d51420b452168ea1c2b913953281bd6fe1fcbd0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/proc-macro) >= 1.0.0
Requires:       crate(quote-1/proc-macro) >= 1.0.0
Requires:       crate(syn-3/clone-impls) >= 3.0.0
Requires:       crate(syn-3/derive) >= 3.0.0
Requires:       crate(syn-3/full) >= 3.0.0
Requires:       crate(syn-3/parsing) >= 3.0.0
Requires:       crate(syn-3/printing) >= 3.0.0
Requires:       crate(syn-3/proc-macro) >= 3.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ptr_meta_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
