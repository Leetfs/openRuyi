# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name http-range-header
%global full_version 0.4.2
%global pkgname http-range-header-0.4

Name:           rust-http-range-header-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "http-range-header"
License:        MIT
URL:            https://github.com/MarcusGrass/parse-range-headers
#!RemoteAsset:  sha256:9171a2ea8a68358193d15dd5d70c1c10a2afc3e7e4c5bc92bc9f025cebd7359c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "http-range-header"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
