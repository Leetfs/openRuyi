# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name enum-ordinalize-derive
%global full_version 4.3.2
%global pkgname enum-ordinalize-derive-4

Name:           rust-enum-ordinalize-derive-4
Version:        4.3.2
Release:        %autorelease
Summary:        Rust crate "enum-ordinalize-derive"
License:        MIT
URL:            https://magiclen.org/enum-ordinalize
#!RemoteAsset:  sha256:8ca9601fb2d62598ee17836250842873a413586e5d7ed88b356e38ddbb0ec631
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/default) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/traits) = %{version}

%description
Source code for takopackized Rust crate "enum-ordinalize-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
