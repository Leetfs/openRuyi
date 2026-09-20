# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows_aarch64_msvc
%global full_version 0.32.0
%global pkgname windows-aarch64-msvc-0.32

Name:           rust-windows-aarch64-msvc-0.32
Version:        0.32.0
Release:        %autorelease
Summary:        Rust crate "windows_aarch64_msvc"
License:        MIT OR Apache-2.0
URL:            FIXME
#!RemoteAsset:  sha256:d8e92753b1c443191654ec532f14c199742964a061be25d77d7a96f09db20bf5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "windows_aarch64_msvc"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
