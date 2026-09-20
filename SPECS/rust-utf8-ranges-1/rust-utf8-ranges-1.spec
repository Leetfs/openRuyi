# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name utf8-ranges
%global full_version 1.0.0
%global pkgname utf8-ranges-1

Name:           rust-utf8-ranges-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "utf8-ranges"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/utf8-ranges
#!RemoteAsset:  sha256:662fab6525a98beff2921d7f61a39e7d59e0b425ebc7d0d9e66d316e55124122
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "utf8-ranges"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
