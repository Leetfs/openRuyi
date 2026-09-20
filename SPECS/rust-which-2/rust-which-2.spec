# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name which
%global full_version 2.0.0
%global pkgname which-2

Name:           rust-which-2
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "which"
License:        MIT
URL:            https://github.com/fangyuanziti/which-rs.git
#!RemoteAsset:  sha256:49c4f580e93079b70ac522e7bdebbe1568c8afa7d8d05ee534ee737ca37d2f51
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(failure-0.1/default) >= 0.1.1
Requires:       crate(libc-0.2/default) >= 0.2.10

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Locate installed execuable in cross platforms.
Source code for takopackized Rust crate "which"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
