# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name memchr
%global full_version 1.0.0
%global pkgname memchr-1

Name:           rust-memchr-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "memchr"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/rust-memchr
#!RemoteAsset:  sha256:7492849298f0731c393b1f34ce03a7c84c00bead2e7057db9342907c8fdcae28
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.18

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "memchr"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
