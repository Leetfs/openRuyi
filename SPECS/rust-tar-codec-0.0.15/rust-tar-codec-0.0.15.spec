# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tar-codec
%global full_version 0.0.15
%global pkgname tar-codec-0.0.15

Name:           rust-tar-codec-0.0.15
Version:        0.0.15
Release:        %autorelease
Summary:        Rust crate "tar-codec"
License:        MIT OR Apache-2.0
URL:            https://github.com/astral-sh/astral-codec
#!RemoteAsset:  sha256:b9dad615e50d181afea4bafea23dacb8e33ed52dde06503813570634b932d467
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(archive-trait-0.0.15/default) >= 0.0.15
Requires:       crate(tar-framing-0.0.15/default) >= 0.0.15
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/io-util) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tar-codec"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
