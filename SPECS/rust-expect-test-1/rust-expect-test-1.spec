# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name expect-test
%global full_version 1.5.1
%global pkgname expect-test-1

Name:           rust-expect-test-1
Version:        1.5.1
Release:        %autorelease
Summary:        Rust crate "expect-test"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-analyzer/expect-test
#!RemoteAsset:  sha256:63af43ff4431e848fb47472a920f14fa71c24de13255a5692e93d4e90302acb0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dissimilar-1/default) >= 1.0.0
Requires:       crate(once-cell-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "expect-test"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
