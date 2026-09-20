# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name parquet-variant
%global full_version 59.2.0
%global pkgname parquet-variant-59

Name:           rust-parquet-variant-59
Version:        59.2.0
Release:        %autorelease
Summary:        Rust crate "parquet-variant"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:3f7e5fff3ed0c07514a7fb8bee3f2ea5a53f36939410ecac4a466620213539a8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-59/canonical-extension-types) >= 59.2.0
Requires:       crate(arrow-schema-59/default) >= 59.2.0
Requires:       crate(chrono-0.4/clock) >= 0.4.40
Requires:       crate(half-2) >= 2.1.0
Requires:       crate(indexmap-2/default) >= 2.10.0
Requires:       crate(num-traits-0.2) >= 0.2.0
Requires:       crate(uuid-1/default) >= 1.18.0
Requires:       crate(uuid-1/js) >= 1.18.0
Requires:       crate(uuid-1/v4) >= 1.18.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "parquet-variant"

%package     -n %{name}+simdutf8
Summary:        Apache Parquet Variant implementation in Rust - feature "simdutf8" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(simdutf8-0.1) >= 0.1.5
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/simdutf8) = %{version}

%description -n %{name}+simdutf8
This metapackage enables feature "simdutf8" for the Rust parquet-variant crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
