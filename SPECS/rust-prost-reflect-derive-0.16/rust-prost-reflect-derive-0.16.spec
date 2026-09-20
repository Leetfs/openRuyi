# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prost-reflect-derive
%global full_version 0.16.1
%global pkgname prost-reflect-derive-0.16

Name:           rust-prost-reflect-derive-0.16
Version:        0.16.1
Release:        %autorelease
Summary:        Rust crate "prost-reflect-derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/andrewhickman/prost-reflect
#!RemoteAsset:  sha256:30320eb03b43b7dfcaf9b361f808a4f1adad1e718ad219df1d7e4283e34e73f5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.36
Requires:       crate(quote-1/default) >= 1.0.14
Requires:       crate(syn-2/default) >= 2.0.32

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "prost-reflect-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
