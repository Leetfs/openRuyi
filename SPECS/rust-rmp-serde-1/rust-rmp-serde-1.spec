# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rmp-serde
%global full_version 1.3.1
%global pkgname rmp-serde-1

Name:           rust-rmp-serde-1
Version:        1.3.1
Release:        %autorelease
Summary:        Rust crate "rmp-serde"
License:        MIT
URL:            https://github.com/3Hren/msgpack-rust
#!RemoteAsset:  sha256:72f81bee8c8ef9b577d1681a70ebbc962c232461e397b22c208c43c04b67a155
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rmp-0.8/default) >= 0.8.15
Requires:       crate(serde-1/default) >= 1.0.228

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rmp-serde"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
