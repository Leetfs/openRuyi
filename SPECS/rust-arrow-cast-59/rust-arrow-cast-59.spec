# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-cast
%global full_version 59.3.0
%global pkgname arrow-cast-59

Name:           rust-arrow-cast-59
Version:        59.3.0
Release:        %autorelease
Summary:        Rust crate "arrow-cast"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:635c9c635668ad26adf76cce8fb276c4be7cf06e63bd516de7da514f9680ee53
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-array-59/default) >= 59.3.0
Requires:       crate(arrow-buffer-59/default) >= 59.3.0
Requires:       crate(arrow-data-59/default) >= 59.3.0
Requires:       crate(arrow-ord-59/default) >= 59.3.0
Requires:       crate(arrow-schema-59/default) >= 59.3.0
Requires:       crate(arrow-select-59/default) >= 59.3.0
Requires:       crate(atoi-2/default) >= 2.0.0
Requires:       crate(base64-0.23/default) >= 0.23.0
Requires:       crate(chrono-0.4/clock) >= 0.4.40
Requires:       crate(half-2) >= 2.1.0
Requires:       crate(lexical-core-1/parse-floats) >= 1.0.0
Requires:       crate(lexical-core-1/parse-integers) >= 1.0.0
Requires:       crate(lexical-core-1/write-floats) >= 1.0.0
Requires:       crate(lexical-core-1/write-integers) >= 1.0.0
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Requires:       crate(ryu-1/default) >= 1.0.16

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/force-validate) = %{version}

%description
Source code for takopackized Rust crate "arrow-cast"

%package     -n %{name}+comfy-table
Summary:        Cast kernel and utilities for Apache Arrow - feature "comfy-table" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(comfy-table-7) >= 7.0.0
Provides:       crate(%{pkgname}/comfy-table) = %{version}
Provides:       crate(%{pkgname}/prettyprint) = %{version}

%description -n %{name}+comfy-table
This metapackage enables feature "comfy-table" for the Rust arrow-cast crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "prettyprint" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
