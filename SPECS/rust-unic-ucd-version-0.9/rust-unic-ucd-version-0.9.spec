# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unic-ucd-version
%global full_version 0.9.0
%global pkgname unic-ucd-version-0.9

Name:           rust-unic-ucd-version-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "unic-ucd-version"
License:        MIT OR Apache-2.0
URL:            https://github.com/open-i18n/rust-unic/
#!RemoteAsset:  sha256:96bd2f2237fe450fcd0a1d2f5f4e91711124f7857ba2e964247776ebeeb7b0c4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unic-common-0.9/default) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "unic-ucd-version"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
