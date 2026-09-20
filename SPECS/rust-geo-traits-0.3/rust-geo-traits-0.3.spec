# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name geo-traits
%global full_version 0.3.0
%global pkgname geo-traits-0.3

Name:           rust-geo-traits-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "geo-traits"
License:        MIT OR Apache-2.0
URL:            https://github.com/georust/geo
#!RemoteAsset:  sha256:2e7c353d12a704ccfab1ba8bfb1a7fe6cb18b665bf89d37f4f7890edcd260206
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "geo-traits"

%package     -n %{name}+geo-types
Summary:        Geospatial traits - feature "geo-types" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(geo-types-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/geo-types) = %{version}

%description -n %{name}+geo-types
This metapackage enables feature "geo-types" for the Rust geo-traits crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
