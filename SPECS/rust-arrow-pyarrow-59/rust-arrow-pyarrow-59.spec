# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-pyarrow
%global full_version 59.3.0
%global pkgname arrow-pyarrow-59

Name:           rust-arrow-pyarrow-59
Version:        59.3.0
Release:        %autorelease
Summary:        Rust crate "arrow-pyarrow"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:801aed7e607dbcc60ed6359025383b27a490327d4282ba87a9a3b78e25959c9a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-array-59/default) >= 59.3.0
Requires:       crate(arrow-array-59/ffi) >= 59.3.0
Requires:       crate(arrow-data-59/default) >= 59.3.0
Requires:       crate(arrow-schema-59/default) >= 59.3.0
Requires:       crate(pyo3-0.29) >= 0.29.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "arrow-pyarrow"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
