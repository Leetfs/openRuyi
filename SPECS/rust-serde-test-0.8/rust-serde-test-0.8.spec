# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_test
%global full_version 0.8.23
%global pkgname serde-test-0.8

Name:           rust-serde-test-0.8
Version:        0.8.23
Release:        %autorelease
Summary:        Rust crate "serde_test"
License:        MIT OR Apache-2.0
URL:            https://serde.rs
#!RemoteAsset:  sha256:110b3dbdf8607ec493c22d5d947753282f3bae73c0f56d322af1e8c78e4c23d5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-0.8/default) >= 0.8.23

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "serde_test"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
