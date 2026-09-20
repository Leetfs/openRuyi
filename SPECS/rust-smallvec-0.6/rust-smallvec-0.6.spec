# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name smallvec
%global full_version 0.6.0
%global pkgname smallvec-0.6

Name:           rust-smallvec-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "smallvec"
License:        MPL-2.0
URL:            https://github.com/servo/rust-smallvec
#!RemoteAsset:  sha256:44db0ecb22921ef790d17ae13a3f6d15784183ff5f2a01aa32098c7498d2b4b9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "smallvec"

%package     -n %{name}+serde
Summary:        'Small vector' optimization: store up to a small number of items on the stack - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust smallvec crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
