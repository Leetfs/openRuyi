# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arcstr
%global full_version 1.2.0
%global pkgname arcstr-1

Name:           rust-arcstr-1
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "arcstr"
License:        Apache-2.0 OR MIT OR Zlib
URL:            https://github.com/thomcc/arcstr
#!RemoteAsset:  sha256:03918c3dbd7701a85c6b9887732e2921175f26c350b4563841d0958c21d57e6d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/substr) = %{version}
Provides:       crate(%{pkgname}/substr-usize-indices) = %{version}

%description
Source code for takopackized Rust crate "arcstr"

%package     -n %{name}+serde
Summary:        Better reference-counted string type, with zero-cost (allocation-free) support for string literals, and reference counted substrings - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust arcstr crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
