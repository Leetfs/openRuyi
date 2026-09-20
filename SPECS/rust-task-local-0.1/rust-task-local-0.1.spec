# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name task-local
%global full_version 0.1.1
%global pkgname task-local-0.1

Name:           rust-task-local-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "task-local"
License:        MIT OR Apache-2.0
URL:            https://github.com/BugenZhao/task-local
#!RemoteAsset:  sha256:2972044a9e5e448a506a7ff6f0d03b566d8ef4cd6918a58fc59835a0f8666626
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "task-local"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
