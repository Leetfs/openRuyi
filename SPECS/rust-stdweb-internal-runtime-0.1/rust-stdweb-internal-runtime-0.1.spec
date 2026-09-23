# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name stdweb-internal-runtime
%global full_version 0.1.0
%global pkgname stdweb-internal-runtime-0.1
%global __requires_exclude_from ^%{_datadir}/cargo/registry/.*$

Name:           rust-stdweb-internal-runtime-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "stdweb-internal-runtime"
License:        MIT OR Apache-2.0
URL:            https://github.com/koute/stdweb
#!RemoteAsset:  sha256:0e93e3ace205c4c1926b882cf8d8209e86acd445fda5fcf850455c3d178651c7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "stdweb-internal-runtime"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
