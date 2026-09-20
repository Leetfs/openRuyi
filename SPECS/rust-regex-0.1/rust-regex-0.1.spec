# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name regex
%global full_version 0.1.0
%global pkgname regex-0.1

Name:           rust-regex-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "regex"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/regex
#!RemoteAsset:  sha256:f0ff1ca641d3c9a2c30464dac30183a8b91cdcc959d616961be020cdea6255c5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "regex"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
