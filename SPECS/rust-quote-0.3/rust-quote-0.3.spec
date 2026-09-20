# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quote
%global full_version 0.3.15
%global pkgname quote-0.3

Name:           rust-quote-0.3
Version:        0.3.15
Release:        %autorelease
Summary:        Rust crate "quote"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/quote
#!RemoteAsset:  sha256:7a6e920b65c65f10b2ae65c831a81a073a89edd28c7cce89475bff467ab4167a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "quote"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
