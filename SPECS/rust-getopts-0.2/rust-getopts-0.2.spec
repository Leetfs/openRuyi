# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name getopts
%global full_version 0.2.0
%global pkgname getopts-0.2

Name:           rust-getopts-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "getopts"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/getopts
#!RemoteAsset:  sha256:d13e6fd53a993480767bad19a41b00b601790b1f9d6916f99e80e5f12e56fbfd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "getopts"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
