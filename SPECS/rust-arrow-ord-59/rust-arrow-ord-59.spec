# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-ord
%global full_version 59.3.0
%global pkgname arrow-ord-59

Name:           rust-arrow-ord-59
Version:        59.3.0
Release:        %autorelease
Summary:        Rust crate "arrow-ord"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:2c900759f3bd8354fd4196bc4403eee846894dc2adf66b4225472006a0bf18c5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-array-59/default) >= 59.3.0
Requires:       crate(arrow-buffer-59/default) >= 59.3.0
Requires:       crate(arrow-data-59/default) >= 59.3.0
Requires:       crate(arrow-schema-59/default) >= 59.3.0
Requires:       crate(arrow-select-59/default) >= 59.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "arrow-ord"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
