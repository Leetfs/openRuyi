# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-openssl
%global full_version 0.6.5
%global pkgname tokio-openssl-0.6

Name:           rust-tokio-openssl-0.6
Version:        0.6.5
Release:        %autorelease
Summary:        Rust crate "tokio-openssl"
License:        MIT OR Apache-2.0
URL:            https://github.com/tokio-rs/tokio-openssl
#!RemoteAsset:  sha256:59df6849caa43bb7567f9a36f863c447d95a11d5903c9cc334ba32576a27eadd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(openssl-0.10/default) >= 0.10.81
Requires:       crate(openssl-sys-0.9/default) >= 0.9.117
Requires:       crate(tokio-1/default) >= 1.52.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tokio-openssl"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
