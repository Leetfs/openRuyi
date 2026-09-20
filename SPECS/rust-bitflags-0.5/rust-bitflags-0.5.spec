# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bitflags
%global full_version 0.5.0
%global pkgname bitflags-0.5

Name:           rust-bitflags-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "bitflags"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/bitflags
#!RemoteAsset:  sha256:4f67931368edf3a9a51d29886d245f1c3db2f1ef0dcc9e35ff70341b78c10d23
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/assignment-operators) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-std) = %{version}

%description
Source code for takopackized Rust crate "bitflags"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
