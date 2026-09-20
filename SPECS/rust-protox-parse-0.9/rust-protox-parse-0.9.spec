# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name protox-parse
%global full_version 0.9.0
%global pkgname protox-parse-0.9

Name:           rust-protox-parse-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "protox-parse"
License:        MIT OR Apache-2.0
URL:            https://github.com/andrewhickman/protox
#!RemoteAsset:  sha256:072eee358134396a4643dff81cfff1c255c9fbd3fb296be14bdb6a26f9156366
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(logos-0.15/default) >= 0.15.1
Requires:       crate(miette-7/default) >= 7.6.0
Requires:       crate(prost-types-0.14/default) >= 0.14.3
Requires:       crate(thiserror-2/default) >= 2.0.18

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "protox-parse"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
