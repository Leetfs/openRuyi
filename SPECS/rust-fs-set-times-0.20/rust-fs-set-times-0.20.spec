# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fs-set-times
%global full_version 0.20.3
%global pkgname fs-set-times-0.20

Name:           rust-fs-set-times-0.20
Version:        0.20.3
Release:        %autorelease
Summary:        Rust crate "fs-set-times"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/fs-set-times
#!RemoteAsset:  sha256:94e7099f6313ecacbe1256e8ff9d617b75d1bcb16a6fddef94866d225a01a14a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(io-lifetimes-2) >= 2.0.0
Requires:       crate(rustix-1/default) >= 1.0.0
Requires:       crate(rustix-1/fs) >= 1.0.0
Requires:       crate(rustix-1/time) >= 1.0.0
Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-storage-filesystem) >= 0.52.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fs-set-times"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
