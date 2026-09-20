# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name multimap
%global full_version 0.10.1
%global pkgname multimap-0.10

Name:           rust-multimap-0.10
Version:        0.10.1
Release:        %autorelease
Summary:        Rust crate "multimap"
License:        MIT OR Apache-2.0
URL:            https://github.com/havarnov/multimap
#!RemoteAsset:  sha256:1d87ecb2933e8aeadb3e3a02b828fed80a7528047e68b4f424523a0981a3a084
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "multimap"

%package     -n %{name}+serde
Summary:        Multimap implementation - feature "serde" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde-impl) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust multimap crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "serde_impl" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
