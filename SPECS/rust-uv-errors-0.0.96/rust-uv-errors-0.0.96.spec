# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uv-errors
%global full_version 0.0.96
%global pkgname uv-errors-0.0.96

Name:           rust-uv-errors-0.0.96
Version:        0.0.96
Release:        %autorelease
Summary:        Rust crate "uv-errors"
License:        MIT OR Apache-2.0
URL:            https://pypi.org/project/uv/
#!RemoteAsset:  sha256:088e3b416018c7da35369fdbb55f0a1232dfc38d3dc1a859852d77753e5b958d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstream-1/auto) >= 1.0.0
Requires:       crate(anstream-1/wincon) >= 1.0.0
Requires:       crate(owo-colors-4) >= 4.1.0
Requires:       crate(terminal-size-0.4) >= 0.4.2
Requires:       crate(textwrap-0.16/smawk) >= 0.16.1
Requires:       crate(textwrap-0.16/unicode-width) >= 0.16.1
Requires:       crate(uv-static-0.0.96/default) >= 0.0.96

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "uv-errors"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
