# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name syntex
%global full_version 0.39.0
%global pkgname syntex-0.39

Name:           rust-syntex-0.39
Version:        0.39.0
Release:        %autorelease
Summary:        Rust crate "syntex"
License:        MIT OR Apache-2.0
URL:            https://github.com/erickt/rust-syntex
#!RemoteAsset:  sha256:8cdab48fb1d177756cac40894a2f12ee8e37beadb0d220855343093af7411cbd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(syntex-errors-0.39/default) >= 0.39.0
Requires:       crate(syntex-syntax-0.39/default) >= 0.39.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "syntex"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
