# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zerocopy
%global full_version 0.6.6
%global pkgname zerocopy-0.6

Name:           rust-zerocopy-0.6
Version:        0.6.6
Release:        %autorelease
Summary:        Rust crate "zerocopy"
License:        BSD-2-Clause
URL:            https://github.com/google/zerocopy
#!RemoteAsset:  sha256:854e949ac82d619ee9a14c66a1b674ac730422372ccb759ce0c39cabcf2bf8e6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1) >= 1.3.0
Requires:       crate(zerocopy-derive-0.6/default) >= 0.6.6

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/simd) = %{version}
Provides:       crate(%{pkgname}/simd-nightly) = %{version}

%description
Source code for takopackized Rust crate "zerocopy"

%package     -n %{name}+internal-use-only-features-that-work-on-stable
Summary:        Utilities for zero-copy parsing and serialization - feature "__internal_use_only_features_that_work_on_stable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/simd) = %{version}
Provides:       crate(%{pkgname}/internal-use-only-features-that-work-on-stable) = %{version}

%description -n %{name}+internal-use-only-features-that-work-on-stable
This metapackage enables feature "__internal_use_only_features_that_work_on_stable" for the Rust zerocopy crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
