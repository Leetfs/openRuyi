# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name az
%global full_version 1.3.0
%global pkgname az-1

Name:           rust-az-1
Version:        1.3.0
Release:        %autorelease
Summary:        Rust crate "az"
License:        MIT OR Apache-2.0
URL:            https://gitlab.com/tspiteri/az
#!RemoteAsset:  sha256:be5eb007b7cacc6c660343e96f650fedf4b5a77512399eb952ca6642cf8d13f7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/fail-on-warnings) = %{version}
Provides:       crate(%{pkgname}/nightly-float) = %{version}

%description
Source code for takopackized Rust crate "az"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
