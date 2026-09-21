# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name malachite-bigint
%global full_version 0.2.3
%global pkgname malachite-bigint-0.2

Name:           rust-malachite-bigint-0.2
Version:        0.2.3
Release:        %autorelease
Summary:        Rust crate "malachite-bigint"
License:        LGPL-3.0-only
URL:            https://github.com/RustPython/malachite-bigint
#!RemoteAsset:  sha256:d149aaa2965d70381709d9df4c7ee1fc0de1c614a4efc2ee356f5e43d68749f8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(derive-more-1/default) >= 1.0.0
Requires:       crate(derive-more-1/display) >= 1.0.0
Requires:       crate(derive-more-1/from) >= 1.0.0
Requires:       crate(derive-more-1/into) >= 1.0.0
Requires:       crate(malachite-0.4/default) >= 0.4.22
Requires:       crate(num-integer-0.1/i128) >= 0.1.46
Requires:       crate(num-traits-0.2/i128) >= 0.2.19
Requires:       crate(paste-1/default) >= 1.0.15

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "malachite-bigint"

%package     -n %{name}+num-bigint
Summary:        Drop-in num-bigint replacement based on malachite - feature "num-bigint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/num-bigint) = %{version}

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust malachite-bigint crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
