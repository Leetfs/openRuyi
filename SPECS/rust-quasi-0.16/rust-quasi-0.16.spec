# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quasi
%global full_version 0.16.0
%global pkgname quasi-0.16

Name:           rust-quasi-0.16
Version:        0.16.0
Release:        %autorelease
Summary:        Rust crate "quasi"
License:        MIT OR Apache-2.0
URL:            https://github.com/serde-rs/quasi
#!RemoteAsset:  sha256:314e56e9e59af71a5b1f09fab15e8e66ab2ccb786688f8d2e04d98b8d7cbc161
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "quasi"

%package     -n %{name}+clippy
Summary:        Quasi-quoting macro system - feature "clippy" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clippy-0.0.302/default) >= 0.0.302
Provides:       crate(%{pkgname}/clippy) = %{version}
Provides:       crate(%{pkgname}/unstable-testing) = %{version}

%description -n %{name}+clippy
This metapackage enables feature "clippy" for the Rust quasi crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable-testing" feature.

%package     -n %{name}+syntex-errors
Summary:        Quasi-quoting macro system - feature "syntex_errors"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntex-errors-0.39/default) >= 0.39.0
Provides:       crate(%{pkgname}/syntex-errors) = %{version}

%description -n %{name}+syntex-errors
This metapackage enables feature "syntex_errors" for the Rust quasi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syntex-syntax
Summary:        Quasi-quoting macro system - feature "syntex_syntax"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntex-syntax-0.39/default) >= 0.39.0
Provides:       crate(%{pkgname}/syntex-syntax) = %{version}

%description -n %{name}+syntex-syntax
This metapackage enables feature "syntex_syntax" for the Rust quasi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-syntex
Summary:        Quasi-quoting macro system - feature "with-syntex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/syntex-errors) = %{version}
Requires:       crate(%{pkgname}/syntex-syntax) = %{version}
Provides:       crate(%{pkgname}/with-syntex) = %{version}

%description -n %{name}+with-syntex
This metapackage enables feature "with-syntex" for the Rust quasi crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
