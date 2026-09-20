# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name daachorse
%global full_version 1.0.0
%global pkgname daachorse-1

Name:           rust-daachorse-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "daachorse"
License:        MIT OR Apache-2.0
URL:            https://github.com/daac-tools/daachorse
#!RemoteAsset:  sha256:63b7ef7a4be509357f4804d0a22e830daddb48f19fd604e4ad32ddce04a94c36
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "daachorse"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
