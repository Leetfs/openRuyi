# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name backtrace-ext
%global full_version 0.2.1
%global pkgname backtrace-ext-0.2

Name:           rust-backtrace-ext-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "backtrace-ext"
License:        MIT OR Apache-2.0
URL:            https://github.com/gankra/backtrace-ext
#!RemoteAsset:  sha256:537beee3be4a18fb023b570f80e3ae28003db9167a751266b259926e25539d50
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(backtrace-0.3/default) >= 0.3.61

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "backtrace-ext"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
