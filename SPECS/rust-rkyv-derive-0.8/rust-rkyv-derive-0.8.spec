# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rkyv_derive
%global full_version 0.8.18
%global pkgname rkyv-derive-0.8

Name:           rust-rkyv-derive-0.8
Version:        0.8.18
Release:        %autorelease
Summary:        Rust crate "rkyv_derive"
License:        MIT
URL:            https://github.com/rkyv/rkyv
#!RemoteAsset:  sha256:1c25ef604ac7dd839d44d64648952ea23c97866f124ff671b0ed2cf3ad9bb06e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/proc-macro) >= 1.0.0
Requires:       crate(quote-1/proc-macro) >= 1.0.0
Requires:       crate(syn-3/clone-impls) >= 3.0.0
Requires:       crate(syn-3/derive) >= 3.0.0
Requires:       crate(syn-3/parsing) >= 3.0.0
Requires:       crate(syn-3/printing) >= 3.0.0
Requires:       crate(syn-3/proc-macro) >= 3.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bytecheck) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rkyv_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
