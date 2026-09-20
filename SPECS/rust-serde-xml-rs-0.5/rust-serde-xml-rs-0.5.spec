# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde-xml-rs
%global full_version 0.5.1
%global pkgname serde-xml-rs-0.5

Name:           rust-serde-xml-rs-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "serde-xml-rs"
License:        MIT
URL:            https://github.com/RReverser/serde-xml-rs
#!RemoteAsset:  sha256:65162e9059be2f6a3421ebbb4fef3e74b7d9e7c60c50a0e292c6239f19f1edfa
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(xml-rs-0.8/default) >= 0.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "serde-xml-rs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
