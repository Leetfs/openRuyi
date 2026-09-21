# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hexf-parse
%global full_version 0.2.1
%global pkgname hexf-parse-0.2

Name:           rust-hexf-parse-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "hexf-parse"
License:        CC0-1.0
URL:            https://github.com/lifthrasiir/hexf
#!RemoteAsset:  sha256:dfa686283ad6dd069f105e5ab091b04c62850d3e4cf5d67debad1933f55023df
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "hexf-parse"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
