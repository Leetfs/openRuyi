# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dogged
%global full_version 0.2.0
%global pkgname dogged-0.2

Name:           rust-dogged-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "dogged"
License:        Apache-2.0 OR MIT
URL:            https://github.com/nikomatsakis/dogged
#!RemoteAsset:  sha256:2638df109789fe360f0d9998c5438dd19a36678aaf845e46f285b688b1a1657a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dogged"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
