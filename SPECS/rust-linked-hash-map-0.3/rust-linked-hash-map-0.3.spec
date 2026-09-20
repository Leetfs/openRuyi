# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name linked-hash-map
%global full_version 0.3.0
%global pkgname linked-hash-map-0.3

Name:           rust-linked-hash-map-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "linked-hash-map"
License:        MIT OR Apache-2.0
URL:            https://github.com/contain-rs/linked-hash-map
#!RemoteAsset:  sha256:6d262045c5b87c0861b3f004610afd0e2c851e2908d08b6c870cbb9d5f494ecd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "linked-hash-map"

%package     -n %{name}+clippy
Summary:        HashMap wrapper that holds key-value pairs in insertion order - feature "clippy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clippy-0.0.302/default) >= 0.0.302
Provides:       crate(%{pkgname}/clippy) = %{version}

%description -n %{name}+clippy
This metapackage enables feature "clippy" for the Rust linked-hash-map crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        HashMap wrapper that holds key-value pairs in insertion order - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-0.8/default) >= 0.8.23
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust linked-hash-map crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-impl
Summary:        HashMap wrapper that holds key-value pairs in insertion order - feature "serde_impl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-test) = %{version}
Provides:       crate(%{pkgname}/serde-impl) = %{version}

%description -n %{name}+serde-impl
This metapackage enables feature "serde_impl" for the Rust linked-hash-map crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-test
Summary:        HashMap wrapper that holds key-value pairs in insertion order - feature "serde_test"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-test-0.8/default) >= 0.8.23
Provides:       crate(%{pkgname}/serde-test) = %{version}

%description -n %{name}+serde-test
This metapackage enables feature "serde_test" for the Rust linked-hash-map crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
