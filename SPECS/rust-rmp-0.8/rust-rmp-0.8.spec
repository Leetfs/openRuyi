# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rmp
%global full_version 0.8.15
%global pkgname rmp-0.8

Name:           rust-rmp-0.8
Version:        0.8.15
Release:        %autorelease
Summary:        Rust crate "rmp"
License:        MIT
URL:            https://github.com/3Hren/msgpack-rust
#!RemoteAsset:  sha256:4ba8be72d372b2c9b35542551678538b562e7cf86c3315773cae48dfbfe7790c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2) >= 0.2.19

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "rmp"

%package     -n %{name}+std
Summary:        Pure Rust MessagePack serialization implementation - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rmp crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
