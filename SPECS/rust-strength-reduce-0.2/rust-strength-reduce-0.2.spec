# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name strength_reduce
%global full_version 0.2.4
%global pkgname strength-reduce-0.2

Name:           rust-strength-reduce-0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Rust crate "strength_reduce"
License:        MIT OR Apache-2.0
URL:            http://github.com/ejmahler/strength_reduce
#!RemoteAsset:  sha256:fe895eb47f22e2ddd4dabc02bce419d2e643c8e3b585c78158b349195bc24d82
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "strength_reduce"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
