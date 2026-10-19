# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name maybe-owned
%global full_version 0.3.4
%global pkgname maybe-owned-0.3

Name:           rust-maybe-owned-0.3
Version:        0.3.4
Release:        %autorelease
Summary:        Rust crate "maybe-owned"
License:        MIT OR Apache-2.0
URL:            https://github.com/rustonaut/maybe-owned
#!RemoteAsset:  sha256:4facc753ae494aeb6e3c22f839b158aebd4f9270f55cd3c79906c45476c47ab4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "maybe-owned"

%package     -n %{name}+serde
Summary:        Provides a `MaybeOwned` (and `MaybeOwnedMut`) type similar to std's `Cow` but it implements `From<T>` and `From<&'a T>` and does not require `ToOwned` - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust maybe-owned crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
