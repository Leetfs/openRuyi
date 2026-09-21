# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unic-emoji-char
%global full_version 0.9.0
%global pkgname unic-emoji-char-0.9

Name:           rust-unic-emoji-char-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "unic-emoji-char"
License:        MIT OR Apache-2.0
URL:            https://github.com/open-i18n/rust-unic/
#!RemoteAsset:  sha256:0b07221e68897210270a38bde4babb655869637af0f69407f96053a34f76494d
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
Source code for takopackized Rust crate "unic-emoji-char"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
