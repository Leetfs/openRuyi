# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name heapless
%global full_version 0.5.0
%global pkgname heapless-0.5

Name:           rust-heapless-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "heapless"
License:        MIT OR Apache-2.0
URL:            https://github.com/japaric/heapless
#!RemoteAsset:  sha256:c6c7ce2e47016f34d17acbf2fe5f9e0337ea59d2ab8ceecd9405b2336ffaca9b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(as-slice-0.1/default) >= 0.1.0
Requires:       crate(generic-array-0.13/default) >= 0.13.0
Requires:       crate(hash32-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "heapless"

%package     -n %{name}+serde
Summary:        `static` friendly data structures that don't require dynamic memory allocation - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust heapless crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
