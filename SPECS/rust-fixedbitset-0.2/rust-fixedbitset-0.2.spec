# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fixedbitset
%global full_version 0.2.0
%global pkgname fixedbitset-0.2

Name:           rust-fixedbitset-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "fixedbitset"
License:        MIT OR Apache-2.0
URL:            https://github.com/bluss/fixedbitset
#!RemoteAsset:  sha256:37ab347416e802de484e4d03c7316c48f1ecb56574dfd4a46a80f173ce1de04d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "fixedbitset"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
