# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dot-parser-macros
%global full_version 0.5.1
%global pkgname dot-parser-macros-0.5

Name:           rust-dot-parser-macros-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "dot-parser-macros"
License:        GPL-2.0-or-later
URL:            https://codeberg.org/bromind/dot-parser.git
#!RemoteAsset:  sha256:b5f46b58a6249ec5f7102770351aeca8eef2a3093872bb8eec1eb9e0b432d260
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dot-parser-0.5/default) >= 0.5.1
Requires:       crate(dot-parser-0.5/to-tokens) >= 0.5.1
Requires:       crate(litrs-0.4/default) >= 0.4.1
Requires:       crate(proc-macro2-1/default) >= 1.0.88
Requires:       crate(quote-1/default) >= 1.0.37

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dot-parser-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
