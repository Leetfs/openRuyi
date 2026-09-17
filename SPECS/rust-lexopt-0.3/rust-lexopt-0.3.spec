# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lexopt
%global full_version 0.3.2
%global pkgname lexopt-0.3

Name:           rust-lexopt-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "lexopt"
License:        MIT
URL:            https://github.com/blyxxyz/lexopt
#!RemoteAsset:  sha256:803ec87c9cfb29b9d2633f20cba1f488db3fd53f2158b1024cbefb47ba05d413
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "lexopt"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
