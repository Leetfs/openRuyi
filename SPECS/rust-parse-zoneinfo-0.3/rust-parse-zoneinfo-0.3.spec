# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name parse-zoneinfo
%global full_version 0.3.1
%global pkgname parse-zoneinfo-0.3

Name:           rust-parse-zoneinfo-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "parse-zoneinfo"
License:        MIT
URL:            https://github.com/chronotope/chrono-tz
#!RemoteAsset:  sha256:1f2a05b18d44e2957b88f96ba460715e295bc1d7510468a2f3d3b44535d26c24
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(regex-1/std) >= 1.3.1
Requires:       crate(regex-1/unicode-perl) >= 1.3.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "parse-zoneinfo"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
