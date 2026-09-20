# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name term
%global full_version 0.5.1
%global pkgname term-0.5

Name:           rust-term-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "term"
License:        MIT OR Apache-2.0
URL:            https://github.com/Stebalien/term
#!RemoteAsset:  sha256:5e6b677dd1e8214ea1ef4297f85dbcbed8e8cdddb561040cc998ca2551c37561
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1/default) >= 1.2.1
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/fileapi) >= 0.3.0
Requires:       crate(winapi-0.3/handleapi) >= 0.3.0
Requires:       crate(winapi-0.3/wincon) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "term"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
