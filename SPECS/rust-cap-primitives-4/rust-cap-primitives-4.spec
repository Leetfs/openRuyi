# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cap-primitives
%global full_version 4.0.3
%global pkgname cap-primitives-4

Name:           rust-cap-primitives-4
Version:        4.0.3
Release:        %autorelease
Summary:        Rust crate "cap-primitives"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/cap-std
#!RemoteAsset:  sha256:8b5f74729fd2f44701d1a8eb47e906cdb3ccd9ec0f02baad85a744b791940b18
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ambient-authority-0.0.2/default) >= 0.0.2
Requires:       crate(fs-set-times-0.20/default) >= 0.20.0
Requires:       crate(io-extras-0.19/default) >= 0.19.0
Requires:       crate(io-lifetimes-3) >= 3.0.1
Requires:       crate(ipnet-2/default) >= 2.5.0
Requires:       crate(maybe-owned-0.3/default) >= 0.3.4
Requires:       crate(rustix-1/default) >= 1.0.0
Requires:       crate(rustix-1/fs) >= 1.0.0
Requires:       crate(rustix-1/process) >= 1.0.0
Requires:       crate(rustix-1/termios) >= 1.0.0
Requires:       crate(rustix-1/time) >= 1.0.0
Requires:       crate(rustix-linux-procfs-0.1/default) >= 0.1.1
Requires:       crate(windows-sys-0.60/default) >= 0.60.0
Requires:       crate(windows-sys-0.60/wdk-foundation) >= 0.60.0
Requires:       crate(windows-sys-0.60/wdk-storage-filesystem) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-foundation) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-security) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-storage-filesystem) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-io) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-kernel) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-windowsprogramming) >= 0.60.0
Requires:       crate(winx-0.36/default) >= 0.36.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cap-primitives"

%package     -n %{name}+arbitrary
Summary:        Capability-based primitives - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.0.0
Requires:       crate(arbitrary-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust cap-primitives crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
