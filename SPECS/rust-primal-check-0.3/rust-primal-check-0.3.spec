# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name primal-check
%global full_version 0.3.4
%global pkgname primal-check-0.3

Name:           rust-primal-check-0.3
Version:        0.3.4
Release:        %autorelease
Summary:        Rust crate "primal-check"
License:        MIT OR Apache-2.0
URL:            https://github.com/huonw/primal
#!RemoteAsset:  sha256:dc0d895b311e3af9902528fbb8f928688abbd95872819320517cc24ca6b2bd08
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-integer-0.1/default) >= 0.1.46

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "primal-check"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
