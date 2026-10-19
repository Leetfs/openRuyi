# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rancor
%global full_version 0.1.3
%global pkgname rancor-0.1

Name:           rust-rancor-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "rancor"
License:        MIT
URL:            https://github.com/rkyv/rancor
#!RemoteAsset:  sha256:9b534442d0fcdb55d66f373d9cac6d33b6293a2335bc2136dbd06ce0e87d2572
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ptr-meta-0.3/derive) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rancor"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
