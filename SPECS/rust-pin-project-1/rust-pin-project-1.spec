# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pin-project
%global full_version 1.1.13
%global pkgname pin-project-1

Name:           rust-pin-project-1
Version:        1.1.13
Release:        %autorelease
Summary:        Rust crate "pin-project"
License:        Apache-2.0 OR MIT
URL:            https://github.com/taiki-e/pin-project
#!RemoteAsset:  sha256:2466b2336ed02bcdca6b294417127b90ec92038d1d5c4fbeac971a922e0e0924
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pin-project-internal-1/default) >= 1.1.13

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pin-project"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
