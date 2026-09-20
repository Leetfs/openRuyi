# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sct
%global full_version 0.7.0
%global pkgname sct-0.7

Name:           rust-sct-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "sct"
License:        Apache-2.0 OR ISC OR MIT
URL:            https://github.com/ctz/sct.rs
#!RemoteAsset:  sha256:d53dcdb7c9f8158937a7981b48accfd39a43af418591a5d008c7b22b5e1b7ca4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ring-0.16/default) >= 0.16.20
Requires:       crate(untrusted-0.7/default) >= 0.7.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sct"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
