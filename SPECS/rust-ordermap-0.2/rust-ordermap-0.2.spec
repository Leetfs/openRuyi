# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ordermap
%global full_version 0.2.2
%global pkgname ordermap-0.2

Name:           rust-ordermap-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "ordermap"
License:        Apache-2.0 OR MIT
URL:            https://github.com/bluss/ordermap
#!RemoteAsset:  sha256:7572f7abe8ede2869180fff59e9004700c91b46c2e361774fb88f68b6137badb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/test-debug) = %{version}
Provides:       crate(%{pkgname}/test-low-transition-point) = %{version}

%description
Source code for takopackized Rust crate "ordermap"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
