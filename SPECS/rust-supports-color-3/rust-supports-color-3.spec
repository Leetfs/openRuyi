# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name supports-color
%global full_version 3.0.2
%global pkgname supports-color-3

Name:           rust-supports-color-3
Version:        3.0.2
Release:        %autorelease
Summary:        Rust crate "supports-color"
License:        Apache-2.0
URL:            https://github.com/zkat/supports-color
#!RemoteAsset:  sha256:c64fc7232dd8d2e4ac5ce4ef302b1d81e0b80d055b9d77c7c4f51f6aa4c867d6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(is-ci-1/default) >= 1.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "supports-color"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
