# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows_x86_64_gnu
%global full_version 0.32.0
%global pkgname windows-x86-64-gnu-0.32

Name:           rust-windows-x86-64-gnu-0.32
Version:        0.32.0
Release:        %autorelease
Summary:        Rust crate "windows_x86_64_gnu"
License:        MIT OR Apache-2.0
URL:            FIXME
#!RemoteAsset:  sha256:c912b12f7454c6620635bbff3450962753834be2a594819bd5e945af18ec64bc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "windows_x86_64_gnu"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
