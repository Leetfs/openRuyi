# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wincolor
%global full_version 0.1.1
%global pkgname wincolor-0.1

Name:           rust-wincolor-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "wincolor"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/ripgrep/tree/master/wincolor
#!RemoteAsset:  sha256:c5010d99d659a6df48d6094844ecde4afc68d3cb3dff752e5983b5f1124e0529
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(kernel32-sys-0.2/default) >= 0.2.2
Requires:       crate(winapi-0.2/default) >= 0.2.8

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wincolor"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
