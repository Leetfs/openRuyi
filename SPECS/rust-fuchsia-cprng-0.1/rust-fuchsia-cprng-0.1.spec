# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fuchsia-cprng
%global full_version 0.1.0
%global pkgname fuchsia-cprng-0.1

Name:           rust-fuchsia-cprng-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "fuchsia-cprng"
License:        FIXME
URL:            https://fuchsia.googlesource.com/garnet
#!RemoteAsset:  sha256:81f7f8eb465745ea9b02e2704612a9946a59fa40572086c6fd49d6ddcf30bf31
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fuchsia-cprng"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
