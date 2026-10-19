# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name munge
%global full_version 0.4.7
%global pkgname munge-0.4

Name:           rust-munge-0.4
Version:        0.4.7
Release:        %autorelease
Summary:        Rust crate "munge"
License:        MIT
URL:            https://github.com/djkoloski/munge
#!RemoteAsset:  sha256:5e17401f259eba956ca16491461b6e8f72913a0a114e39736ce404410f915a0c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(munge-macro-0.4) >= 0.4.7

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "munge"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
