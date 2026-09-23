# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name discard
%global full_version 1.0.3
%global pkgname discard-1
%global __requires_exclude_from ^%{_datadir}/cargo/registry/.*$

Name:           rust-discard-1
Version:        1.0.3
Release:        %autorelease
Summary:        Rust crate "discard"
License:        MIT
URL:            https://github.com/Pauan/rust-discard
#!RemoteAsset:  sha256:9a9117502da3c5657cb8e2ca7ffcf52d659f00c78c5127d1ebadc2ebe76465be
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "discard"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
