# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cblas-sys
%global full_version 0.1.4
%global pkgname cblas-sys-0.1

Name:           rust-cblas-sys-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "cblas-sys"
License:        Apache-2.0 OR MIT
URL:            https://github.com/blas-lapack-rs/cblas-sys
#!RemoteAsset:  sha256:b6feecd82cce51b0204cf063f0041d69f24ce83f680d87514b004248e7b0fa65
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cblas-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
