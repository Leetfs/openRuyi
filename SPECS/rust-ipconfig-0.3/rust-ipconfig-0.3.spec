# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ipconfig
%global full_version 0.3.0
%global pkgname ipconfig-0.3

Name:           rust-ipconfig-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "ipconfig"
License:        MIT OR Apache-2.0
URL:            https://github.com/liranringel/ipconfig
#!RemoteAsset:  sha256:723519edce41262b05d4143ceb95050e4c614f483e78e9fd9e39a8275a84ad98
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(socket2-0.4/default) >= 0.4.0
Requires:       crate(widestring-0.5/default) >= 0.5.0
Requires:       crate(winapi-0.3/default) >= 0.3.4
Requires:       crate(winreg-0.7/default) >= 0.7.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ipconfig"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
