# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-row
%global full_version 59.3.0
%global pkgname arrow-row-59

Name:           rust-arrow-row-59
Version:        59.3.0
Release:        %autorelease
Summary:        Rust crate "arrow-row"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:f4c6425032e28266e3fc4ff680805e57e670d6ea92473043f3e65b7ed6ac79f2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-array-59/default) >= 59.3.0
Requires:       crate(arrow-buffer-59/default) >= 59.3.0
Requires:       crate(arrow-data-59/default) >= 59.3.0
Requires:       crate(arrow-schema-59/default) >= 59.3.0
Requires:       crate(half-2) >= 2.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "arrow-row"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
