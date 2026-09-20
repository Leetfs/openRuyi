# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name memchr
%global full_version 0.1.9
%global pkgname memchr-0.1

Name:           rust-memchr-0.1
Version:        0.1.9
Release:        %autorelease
Summary:        Rust crate "memchr"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/rust-memchr
#!RemoteAsset:  sha256:3d6a28668369c3a29b9993a59a8f65947b74e19a7914cb925273dbd97077c69f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "memchr"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
