# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name card-validate
%global full_version 2.4.0
%global pkgname card-validate-2

Name:           rust-card-validate-2
Version:        2.4.0
Release:        %autorelease
Summary:        Rust crate "card-validate"
License:        MIT
URL:            https://github.com/valeriansaliou/rs-card-validate
#!RemoteAsset:  sha256:655fa70596e2a38372c0c0c4449ec0166ad9cc43d91558bbecc1a6f38bf9eb91
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lazy-static-1/default) >= 1.0.0
Requires:       crate(regex-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "card-validate"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
