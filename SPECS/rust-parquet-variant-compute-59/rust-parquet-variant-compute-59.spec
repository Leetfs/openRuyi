# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name parquet-variant-compute
%global full_version 59.2.0
%global pkgname parquet-variant-compute-59

Name:           rust-parquet-variant-compute-59
Version:        59.2.0
Release:        %autorelease
Summary:        Rust crate "parquet-variant-compute"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:ba4d3de89dab8d1aaaf601ae8d71bd07ea88cfca9efc1df5815b982c30f631e1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-59/canonical-extension-types) >= 59.2.0
Requires:       crate(arrow-schema-59/default) >= 59.2.0
Requires:       crate(chrono-0.4/clock) >= 0.4.40
Requires:       crate(half-2) >= 2.1.0
Requires:       crate(indexmap-2/default) >= 2.10.0
Requires:       crate(parquet-variant-59/default) >= 59.2.0
Requires:       crate(parquet-variant-json-59/default) >= 59.2.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(uuid-1/default) >= 1.18.0
Requires:       crate(uuid-1/js) >= 1.18.0
Requires:       crate(uuid-1/v4) >= 1.18.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "parquet-variant-compute"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
