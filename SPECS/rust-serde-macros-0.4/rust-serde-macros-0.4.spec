# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_macros
%global full_version 0.4.0
%global pkgname serde-macros-0.4

Name:           rust-serde-macros-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "serde_macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/erickt/rust-serde
#!RemoteAsset:  sha256:4bfd1cd9bd36101ff422614c6083ba9174b8b455b94653ab7166a52845d41a80
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-codegen-0.7/nightly) >= 0.7.15

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "serde_macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
