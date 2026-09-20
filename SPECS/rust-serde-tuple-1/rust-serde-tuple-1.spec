# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_tuple
%global full_version 1.1.3
%global pkgname serde-tuple-1

Name:           rust-serde-tuple-1
Version:        1.1.3
Release:        %autorelease
Summary:        Rust crate "serde_tuple"
License:        MIT
URL:            https://github.com/kardeiz/serde_tuple
#!RemoteAsset:  sha256:6af196b9c06f0aa5555ab980c01a2527b0f67517da8d68b1731b9d4764846a6f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-tuple-macros-1/default) >= 1.1.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "serde_tuple"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
