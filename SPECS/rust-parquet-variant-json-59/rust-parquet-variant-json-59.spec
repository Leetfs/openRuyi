# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name parquet-variant-json
%global full_version 59.2.0
%global pkgname parquet-variant-json-59

Name:           rust-parquet-variant-json-59
Version:        59.2.0
Release:        %autorelease
Summary:        Rust crate "parquet-variant-json"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:fb19dfe1bd24c17addd761ba4f7000f615e2fa12525871c7baa835dbb3d7f147
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-schema-59/default) >= 59.2.0
Requires:       crate(base64-0.23/default) >= 0.23.0
Requires:       crate(chrono-0.4/clock) >= 0.4.40
Requires:       crate(parquet-variant-59/default) >= 59.2.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(uuid-1/default) >= 1.18.0
Requires:       crate(uuid-1/js) >= 1.18.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "parquet-variant-json"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
