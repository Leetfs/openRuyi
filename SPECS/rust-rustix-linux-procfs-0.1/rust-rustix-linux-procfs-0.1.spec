# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustix-linux-procfs
%global full_version 0.1.1
%global pkgname rustix-linux-procfs-0.1

Name:           rust-rustix-linux-procfs-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "rustix-linux-procfs"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/sunfishcode/rustix-linux-procfs
#!RemoteAsset:  sha256:2fc84bf7e9aa16c4f2c758f27412dc9841341e16aa682d9c7ac308fe3ee12056
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1/default) >= 1.5.2
Requires:       crate(rustix-1/alloc) >= 1.0.0
Requires:       crate(rustix-1/fs) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "rustix-linux-procfs"

%package     -n %{name}+std
Summary:        Utilities for opening Linux procfs files and directories - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustix-1/alloc) >= 1.0.0
Requires:       crate(rustix-1/fs) >= 1.0.0
Requires:       crate(rustix-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rustix-linux-procfs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
