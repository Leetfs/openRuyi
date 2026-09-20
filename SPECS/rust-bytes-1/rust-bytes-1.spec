# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bytes
%global full_version 1.12.0
%global pkgname bytes-1

Name:           rust-bytes-1
Version:        1.12.0
Release:        %autorelease
Summary:        Rust crate "bytes"
License:        MIT
URL:            https://github.com/tokio-rs/bytes
#!RemoteAsset:  sha256:8ae3f5d315924270530207e2a68396c3cc547f6dca3fbdca317cfb1a51edb593
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "bytes"

%package     -n %{name}+extra-platforms
Summary:        Types and traits for working with bytes - feature "extra-platforms"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(portable-atomic-1/require-cas) >= 1.3.0
Provides:       crate(%{pkgname}/extra-platforms) = %{version}

%description -n %{name}+extra-platforms
This metapackage enables feature "extra-platforms" for the Rust bytes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Types and traits for working with bytes - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.228
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bytes crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
