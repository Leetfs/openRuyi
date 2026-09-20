# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name void
%global full_version 1.0.0
%global pkgname void-1

Name:           rust-void-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "void"
License:        MIT
URL:            https://github.com/reem/rust-void.git
#!RemoteAsset:  sha256:9190d4fdcc6b93d290236afff590896050a971233ec853958c0e52d42bdeb72c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "void"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
