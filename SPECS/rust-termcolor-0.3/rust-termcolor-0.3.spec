# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name termcolor
%global full_version 0.3.0
%global pkgname termcolor-0.3

Name:           rust-termcolor-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "termcolor"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/ripgrep/tree/master/termcolor
#!RemoteAsset:  sha256:387efd1898a671474f094752a6ea597cb499d2e10bfbc9d81986567bc906efdf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(wincolor-0.1/default) >= 0.1.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "termcolor"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
