# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zerocopy-derive
%global full_version 0.6.6
%global pkgname zerocopy-derive-0.6

Name:           rust-zerocopy-derive-0.6
Version:        0.6.6
Release:        %autorelease
Summary:        Rust crate "zerocopy-derive"
License:        BSD-2-Clause
URL:            https://github.com/google/zerocopy
#!RemoteAsset:  sha256:125139de3f6b9d625c39e2efdd73d41bdac468ccd556556440e322be0e1bbd91
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.1
Requires:       crate(quote-1/default) >= 1.0.10
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/visit) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "zerocopy-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
