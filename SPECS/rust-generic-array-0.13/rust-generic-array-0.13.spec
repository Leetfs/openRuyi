# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name generic-array
%global full_version 0.13.0
%global pkgname generic-array-0.13

Name:           rust-generic-array-0.13
Version:        0.13.0
Release:        %autorelease
Summary:        Rust crate "generic-array"
License:        MIT
URL:            https://github.com/fizyk20/generic-array.git
#!RemoteAsset:  sha256:1d3904420fad470d07ec9e4dbac00c2dc46765d3c4eb6cd1d9bb4d9c8a09c5f6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(typenum-1/default) >= 1.10.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "generic-array"

%package     -n %{name}+serde
Summary:        Generic types implementing functionality of arrays - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
