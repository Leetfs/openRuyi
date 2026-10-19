# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bytecheck
%global full_version 0.8.3
%global pkgname bytecheck-0.8

Name:           rust-bytecheck-0.8
Version:        0.8.3
Release:        %autorelease
Summary:        Rust crate "bytecheck"
License:        MIT
URL:            https://github.com/rkyv/bytecheck
#!RemoteAsset:  sha256:26333eeac754f0ad8a6bcd0eb0ac012156302e4e16b852b72ee399aea4f12c29
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytecheck-derive-0.8) >= 0.8.3
Requires:       crate(ptr-meta-0.3) >= 0.3.0
Requires:       crate(rancor-0.1) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "bytecheck"

%package     -n %{name}+simdutf8
Summary:        Memory validation framework for Rust - feature "simdutf8" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(simdutf8-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/simdutf8) = %{version}

%description -n %{name}+simdutf8
This metapackage enables feature "simdutf8" for the Rust bytecheck crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+uuid-1
Summary:        Memory validation framework for Rust - feature "uuid-1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-1) >= 1.0.0
Provides:       crate(%{pkgname}/uuid-1) = %{version}

%description -n %{name}+uuid-1
This metapackage enables feature "uuid-1" for the Rust bytecheck crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
