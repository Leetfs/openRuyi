# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name saa
%global full_version 5.5.0
%global pkgname saa-5

Name:           rust-saa-5
Version:        5.5.0
Release:        %autorelease
Summary:        Rust crate "saa"
License:        Apache-2.0
URL:            https://codeberg.org/wvwwvwwv/synchronous-and-asynchronous
#!RemoteAsset:  sha256:16c7f49c9d5caa3bf4b3106900484b447b9253fe99670ceb81cb6cb5027855e1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "saa"

%package     -n %{name}+lock-api
Summary:        Word-sized low-level synchronization primitives providing both asynchronous and synchronous interfaces - feature "lock_api"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lock-api-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/lock-api) = %{version}

%description -n %{name}+lock-api
This metapackage enables feature "lock_api" for the Rust saa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+loom
Summary:        Word-sized low-level synchronization primitives providing both asynchronous and synchronous interfaces - feature "loom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(loom-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/loom) = %{version}

%description -n %{name}+loom
This metapackage enables feature "loom" for the Rust saa crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
