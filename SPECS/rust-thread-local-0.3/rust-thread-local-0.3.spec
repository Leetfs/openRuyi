# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name thread_local
%global full_version 0.3.2
%global pkgname thread-local-0.3

Name:           rust-thread-local-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "thread_local"
License:        Apache-2.0 OR MIT
URL:            https://github.com/Amanieu/thread_local-rs
#!RemoteAsset:  sha256:7793b722f0f77ce716e7f1acf416359ca32ff24d04ffbac4269f44a4a83be05d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(thread-id-3/default) >= 3.0.0
Requires:       crate(unreachable-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "thread_local"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
