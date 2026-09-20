# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name derive_builder_core
%global full_version 0.12.0
%global pkgname derive-builder-core-0.12

Name:           rust-derive-builder-core-0.12
Version:        0.12.0
Release:        %autorelease
Summary:        Rust crate "derive_builder_core"
License:        MIT OR Apache-2.0
URL:            https://github.com/colin-kiegel/rust-derive-builder
#!RemoteAsset:  sha256:c11bdc11a0c47bc7d37d582b5285da6849c96681023680b906673c5707af7b0f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(darling-0.14/default) >= 0.14.0
Requires:       crate(proc-macro2-1/default) >= 1.0.37
Requires:       crate(quote-1/default) >= 1.0.18
Requires:       crate(syn-1/default) >= 1.0.91
Requires:       crate(syn-1/extra-traits) >= 1.0.91
Requires:       crate(syn-1/full) >= 1.0.91

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/clippy) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "derive_builder_core"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
