# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unreachable
%global full_version 0.1.0
%global pkgname unreachable-0.1

Name:           rust-unreachable-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "unreachable"
License:        MIT
URL:            https://github.com/reem/rust-unreachable.git
#!RemoteAsset:  sha256:ba6ca90cbc7fe966c80afab0e8677f09bc157da39eb5bd54084e0d0ce2433777
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(void-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "unreachable"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
