# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_cbor
%global full_version 0.11.2
%global pkgname serde-cbor-0.11

Name:           rust-serde-cbor-0.11
Version:        0.11.2
Release:        %autorelease
Summary:        Rust crate "serde_cbor"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyfisch/cbor
#!RemoteAsset:  sha256:2bef2ebfde456fb76bbcf9f59315333decc4fda0b2b44b420243c11e0f5ec1f5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(half-1/default) >= 1.2.0
Requires:       crate(serde-1) >= 1.0.14

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/tags) = %{version}
Provides:       crate(%{pkgname}/unsealed-read-write) = %{version}

%description
Source code for takopackized Rust crate "serde_cbor"

%package     -n %{name}+alloc
Summary:        CBOR support for serde - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.14
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust serde_cbor crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        CBOR support for serde - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/std) >= 1.0.14
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust serde_cbor crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
