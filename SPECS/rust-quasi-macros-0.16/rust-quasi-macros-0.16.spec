# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quasi_macros
%global full_version 0.16.0
%global pkgname quasi-macros-0.16

Name:           rust-quasi-macros-0.16
Version:        0.16.0
Release:        %autorelease
Summary:        Rust crate "quasi_macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/serde-rs/quasi
#!RemoteAsset:  sha256:9b530b7ff57b6a38e4d53909c64657f40e0eef6a8fea1f0943d76160c277c9c5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quasi-codegen-0.16) >= 0.16.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "quasi_macros"

%package     -n %{name}+clippy
Summary:        Quasi-quoting macro system - feature "clippy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clippy-0.0.302/default) >= 0.0.302
Provides:       crate(%{pkgname}/clippy) = %{version}

%description -n %{name}+clippy
This metapackage enables feature "clippy" for the Rust quasi_macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-testing
Summary:        Quasi-quoting macro system - feature "unstable-testing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clippy) = %{version}
Requires:       crate(quasi-codegen-0.16/unstable-testing) >= 0.16.0
Provides:       crate(%{pkgname}/unstable-testing) = %{version}

%description -n %{name}+unstable-testing
This metapackage enables feature "unstable-testing" for the Rust quasi_macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
