# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rlimit
%global full_version 0.11.0
%global pkgname rlimit-0.11

Name:           rust-rlimit-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "rlimit"
License:        MIT
URL:            https://github.com/Nugine/rlimit/
#!RemoteAsset:  sha256:f35ee2729c56bb610f6dba436bf78135f728b7373bdffae2ec815b2d3eb98cc3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.183

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rlimit"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
