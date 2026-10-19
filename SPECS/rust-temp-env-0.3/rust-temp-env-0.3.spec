# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name temp-env
%global full_version 0.3.6
%global pkgname temp-env-0.3

Name:           rust-temp-env-0.3
Version:        0.3.6
Release:        %autorelease
Summary:        Rust crate "temp-env"
License:        MIT OR Apache-2.0
URL:            https://github.com/vmx/temp-env
#!RemoteAsset:  sha256:96374855068f47402c3121c6eed88d29cb1de8f3ab27090e273e420bdabcf050
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(parking-lot-0.12/default) >= 0.12.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "temp-env"

%package     -n %{name}+async-closure
Summary:        Set environment variables temporarily - feature "async_closure"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.3/default) >= 0.3.21
Provides:       crate(%{pkgname}/async-closure) = %{version}

%description -n %{name}+async-closure
This metapackage enables feature "async_closure" for the Rust temp-env crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
