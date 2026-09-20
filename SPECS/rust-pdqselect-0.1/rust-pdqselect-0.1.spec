# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pdqselect
%global full_version 0.1.0
%global pkgname pdqselect-0.1

Name:           rust-pdqselect-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "pdqselect"
License:        Apache-2.0 OR MIT
URL:            FIXME
#!RemoteAsset:  sha256:4ec91767ecc0a0bbe558ce8c9da33c068066c57ecc8bb8477ef8c1ad3ef77c27
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pdqselect"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
