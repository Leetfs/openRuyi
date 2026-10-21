# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uv-cache-key
%global full_version 0.0.96
%global pkgname uv-cache-key-0.0.96

Name:           rust-uv-cache-key-0.0.96
Version:        0.0.96
Release:        %autorelease
Summary:        Rust crate "uv-cache-key"
License:        MIT OR Apache-2.0
URL:            https://pypi.org/project/uv/
#!RemoteAsset:  sha256:be89ae6d1288b6d8395136f3588e4c2bd1b83eeb86ba9aaec36cb1f307ea156a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hex-0.4/std) >= 0.4.3
Requires:       crate(memchr-2/std) >= 2.7.4
Requires:       crate(percent-encoding-2/std) >= 2.3.1
Requires:       crate(seahash-4) >= 4.1.0
Requires:       crate(uv-redacted-0.0.96/default) >= 0.0.96

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "uv-cache-key"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
