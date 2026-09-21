# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name redox_syscall
%global full_version 0.2.16
%global pkgname redox-syscall-0.2

Name:           rust-redox-syscall-0.2
Version:        0.2.16
Release:        %autorelease
Summary:        Rust crate "redox_syscall"
License:        MIT
URL:            https://gitlab.redox-os.org/redox-os/syscall
#!RemoteAsset:  sha256:fb5a58c1855b4b6819d59012155603f0b22ad30cad752600aadfcb695265519a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "redox_syscall"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
