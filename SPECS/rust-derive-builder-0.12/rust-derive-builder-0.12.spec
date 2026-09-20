# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name derive_builder
%global full_version 0.12.0
%global pkgname derive-builder-0.12

Name:           rust-derive-builder-0.12
Version:        0.12.0
Release:        %autorelease
Summary:        Rust crate "derive_builder"
License:        MIT OR Apache-2.0
URL:            https://github.com/colin-kiegel/rust-derive-builder
#!RemoteAsset:  sha256:8d67778784b508018359cbc8696edb3db78160bab2c2a28ba7f56ef6932997f8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(derive-builder-macro-0.12/default) >= 0.12.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "derive_builder"

%package     -n %{name}+clippy
Summary:        Rust macro to automatically implement the builder pattern for arbitrary structs - feature "clippy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(derive-builder-macro-0.12/clippy) >= 0.12.0
Provides:       crate(%{pkgname}/clippy) = %{version}

%description -n %{name}+clippy
This metapackage enables feature "clippy" for the Rust derive_builder crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
