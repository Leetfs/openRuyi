# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name speedate
%global full_version 0.18.0
%global pkgname speedate-0.18

Name:           rust-speedate-0.18
Version:        0.18.0
Release:        %autorelease
Summary:        Rust crate "speedate"
License:        MIT
URL:            https://github.com/pydantic/speedate/
#!RemoteAsset:  sha256:da8f8c5f7f7ea2811a17f99bca4fec7f9ef0b0734713a5cbfc9baee203eba8eb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrayvec-0.7) >= 0.7.8
Requires:       crate(lexical-parse-float-1) >= 1.0.6
Requires:       crate(strum-0.28/derive) >= 0.28.0
Requires:       crate(strum-macros-0.28/default) >= 0.28.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "speedate"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
