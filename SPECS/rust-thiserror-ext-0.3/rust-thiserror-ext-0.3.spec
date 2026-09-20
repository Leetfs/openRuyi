# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name thiserror-ext
%global full_version 0.3.0
%global pkgname thiserror-ext-0.3

Name:           rust-thiserror-ext-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "thiserror-ext"
License:        Apache-2.0
URL:            https://github.com/risingwavelabs/thiserror-ext
#!RemoteAsset:  sha256:5fb7e61141f4141832ca9aad63c3c90023843f944a1975460abdacc64d03f534
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(thiserror-2/default) >= 2.0.18
Requires:       crate(thiserror-ext-derive-0.3/default) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "thiserror-ext"

%package     -n %{name}+backtrace
Summary:        Useful extension utilities for `thiserror` - feature "backtrace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(thiserror-ext-derive-0.3/backtrace) >= 0.3.0
Provides:       crate(%{pkgname}/backtrace) = %{version}

%description -n %{name}+backtrace
This metapackage enables feature "backtrace" for the Rust thiserror-ext crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
