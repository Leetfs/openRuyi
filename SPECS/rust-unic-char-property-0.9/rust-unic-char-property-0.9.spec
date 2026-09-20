# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unic-char-property
%global full_version 0.9.0
%global pkgname unic-char-property-0.9

Name:           rust-unic-char-property-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "unic-char-property"
License:        MIT OR Apache-2.0
URL:            https://github.com/open-i18n/rust-unic/
#!RemoteAsset:  sha256:a8c57a407d9b6fa02b4795eb81c5b6652060a15a7903ea981f3d723e6c0be221
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unic-char-range-0.9/default) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "unic-char-property"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
