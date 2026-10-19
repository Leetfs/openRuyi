# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name winx
%global full_version 0.36.4
%global pkgname winx-0.36

Name:           rust-winx-0.36
Version:        0.36.4
Release:        %autorelease
Summary:        Rust crate "winx"
License:        Apache-2.0 WITH LLVM-exception
URL:            https://github.com/sunfishcode/winx
#!RemoteAsset:  sha256:3f3fd376f71958b862e7afb20cfe5a22830e1963462f3a17f49d82a6c1d1f42d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.4.0
Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-storage-filesystem) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-io) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-ioctl) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-libraryloader) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-performance) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-systemservices) >= 0.52.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "winx"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
