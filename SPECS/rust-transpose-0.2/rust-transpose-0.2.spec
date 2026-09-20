# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name transpose
%global full_version 0.2.3
%global pkgname transpose-0.2

Name:           rust-transpose-0.2
Version:        0.2.3
Release:        %autorelease
Summary:        Rust crate "transpose"
License:        MIT OR Apache-2.0
URL:            https://github.com/ejmahler/transpose
#!RemoteAsset:  sha256:1ad61aed86bc3faea4300c7aee358b4c6d0c8d6ccc36524c96e4c92ccf26e77e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-integer-0.1) >= 0.1.46
Requires:       crate(strength-reduce-0.2/default) >= 0.2.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "transpose"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
