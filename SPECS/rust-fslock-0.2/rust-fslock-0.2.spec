# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fslock
%global full_version 0.2.1
%global pkgname fslock-0.2

Name:           rust-fslock-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "fslock"
License:        MIT
URL:            https://github.com/brunoczim/fslock
#!RemoteAsset:  sha256:04412b8935272e3a9bae6f48c7bfff74c2911f60525404edfdd28e49884c3bfb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2) >= 0.2.66
Requires:       crate(winapi-0.3/default) >= 0.3.8
Requires:       crate(winapi-0.3/errhandlingapi) >= 0.3.8
Requires:       crate(winapi-0.3/fileapi) >= 0.3.8
Requires:       crate(winapi-0.3/handleapi) >= 0.3.8
Requires:       crate(winapi-0.3/minwinbase) >= 0.3.8
Requires:       crate(winapi-0.3/minwindef) >= 0.3.8
Requires:       crate(winapi-0.3/processthreadsapi) >= 0.3.8
Requires:       crate(winapi-0.3/synchapi) >= 0.3.8
Requires:       crate(winapi-0.3/winbase) >= 0.3.8
Requires:       crate(winapi-0.3/winerror) >= 0.3.8
Requires:       crate(winapi-0.3/winnt) >= 0.3.8

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "fslock"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
