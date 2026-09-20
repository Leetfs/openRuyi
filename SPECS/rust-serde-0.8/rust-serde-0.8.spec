# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde
%global full_version 0.8.23
%global pkgname serde-0.8

Name:           rust-serde-0.8
Version:        0.8.23
Release:        %autorelease
Summary:        Rust crate "serde"
License:        MIT OR Apache-2.0
URL:            https://serde.rs
#!RemoteAsset:  sha256:9dad3f759919b92c3068c696c15c3d17238234498bbdcc80f2c469606f948ac8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/collections) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "serde"

%package     -n %{name}+clippy
Summary:        Generic serialization/deserialization framework - feature "clippy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clippy-0.0.302/default) >= 0.0.302
Provides:       crate(%{pkgname}/clippy) = %{version}

%description -n %{name}+clippy
This metapackage enables feature "clippy" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-testing
Summary:        Generic serialization/deserialization framework - feature "unstable-testing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clippy) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/unstable) = %{version}
Provides:       crate(%{pkgname}/unstable-testing) = %{version}

%description -n %{name}+unstable-testing
This metapackage enables feature "unstable-testing" for the Rust serde crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
