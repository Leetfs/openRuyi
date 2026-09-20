# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name parquet-geospatial
%global full_version 59.2.0
%global pkgname parquet-geospatial-59

Name:           rust-parquet-geospatial-59
Version:        59.2.0
Release:        %autorelease
Summary:        Rust crate "parquet-geospatial"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:0e3383d7e5a8e846863f12dc78a292e62510fd216a70023f5c327f1d833bf690
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-schema-59/default) >= 59.2.0
Requires:       crate(geo-traits-0.3/default) >= 0.3.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/std) >= 1.0.0
Requires:       crate(wkb-0.9/default) >= 0.9.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "parquet-geospatial"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
