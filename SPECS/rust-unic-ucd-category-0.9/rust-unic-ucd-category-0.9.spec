# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unic-ucd-category
%global full_version 0.9.0
%global pkgname unic-ucd-category-0.9

Name:           rust-unic-ucd-category-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "unic-ucd-category"
License:        MIT OR Apache-2.0
URL:            https://github.com/open-i18n/rust-unic/
#!RemoteAsset:  sha256:1b8d4591f5fcfe1bd4453baaf803c40e1b1e69ff8455c47620440b46efef91c0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(matches-0.1/default) >= 0.1.0
Requires:       crate(unic-char-property-0.9/default) >= 0.9.0
Requires:       crate(unic-char-range-0.9/default) >= 0.9.0
Requires:       crate(unic-ucd-version-0.9/default) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "unic-ucd-category"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
