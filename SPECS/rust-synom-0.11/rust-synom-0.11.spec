# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name synom
%global full_version 0.11.0
%global pkgname synom-0.11

Name:           rust-synom-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "synom"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/syn
#!RemoteAsset:  sha256:8fece1853fb872b0acdc3ff88f37c474018e125ef81cd4cb8c0ca515746b62ed
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-xid-0.0.4/default) >= 0.0.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "synom"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
