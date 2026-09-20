# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unic-ucd-common
%global full_version 0.9.0
%global pkgname unic-ucd-common-0.9

Name:           rust-unic-ucd-common-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "unic-ucd-common"
License:        MIT OR Apache-2.0
URL:            https://github.com/open-i18n/rust-unic/
#!RemoteAsset:  sha256:e9b78b910beafa1aae5c59bf00877c6cece1c5db28a1241ad801e86cecdff4ad
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unic-char-property-0.9/default) >= 0.9.0
Requires:       crate(unic-char-range-0.9/default) >= 0.9.0
Requires:       crate(unic-ucd-version-0.9/default) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "unic-ucd-common"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
