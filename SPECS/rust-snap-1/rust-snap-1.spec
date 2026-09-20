# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name snap
%global full_version 1.1.2
%global pkgname snap-1

Name:           rust-snap-1
Version:        1.1.2
Release:        %autorelease
Summary:        Rust crate "snap"
License:        BSD-3-Clause
URL:            https://github.com/BurntSushi/rust-snappy
#!RemoteAsset:  sha256:199905e6153d6405f9728fe44daace35f8f837bbf830bb6e85fbd5828709a886
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Includes streaming compression and decompression.
Source code for takopackized Rust crate "snap"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
