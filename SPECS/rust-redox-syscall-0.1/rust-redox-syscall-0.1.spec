# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name redox_syscall
%global full_version 0.1.0
%global pkgname redox-syscall-0.1

Name:           rust-redox-syscall-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "redox_syscall"
License:        MIT
URL:            FIXME
#!RemoteAsset:  sha256:35a48131ab10dbeb17202bd1dcb9c9798963a58a50c9ec31640f237358832094
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "redox_syscall"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
