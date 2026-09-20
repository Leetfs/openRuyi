# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hound
%global full_version 3.5.1
%global pkgname hound-3

Name:           rust-hound-3
Version:        3.5.1
Release:        %autorelease
Summary:        Rust crate "hound"
License:        Apache-2.0
URL:            https://github.com/ruuda/hound
#!RemoteAsset:  sha256:62adaabb884c94955b19907d60019f4e145d091c75345379e70d1ee696f7854f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "hound"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
