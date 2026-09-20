# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name heapsize
%global full_version 0.4.0
%global pkgname heapsize-0.4

Name:           rust-heapsize-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "heapsize"
License:        MPL-2.0
URL:            https://github.com/servo/heapsize
#!RemoteAsset:  sha256:4c7593b1522161003928c959c20a2ca421c68e940d63d75573316a009e48a6d4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(kernel32-sys-0.2/default) >= 0.2.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/flexible-tests) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "heapsize"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
