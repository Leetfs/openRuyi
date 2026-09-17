# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name encoding_rs_io
%global full_version 0.1.7
%global pkgname encoding-rs-io-0.1

Name:           rust-encoding-rs-io-0.1
Version:        0.1.7
Release:        %autorelease
Summary:        Rust crate "encoding_rs_io"
License:        MIT OR Apache-2.0
URL:            https://github.com/BurntSushi/encoding_rs_io
#!RemoteAsset:  sha256:1cc3c5651fb62ab8aa3103998dade57efdd028544bd300516baa31840c252a83
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(encoding-rs-0.8/default) >= 0.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "encoding_rs_io"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
