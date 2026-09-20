# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-convert
%global full_version 1.0.0
%global pkgname async-convert-1

Name:           rust-async-convert-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "async-convert"
License:        MIT OR Apache-2.0
URL:            https://github.com/yoshuawuyts/async-convert
#!RemoteAsset:  sha256:6d416feee97712e43152cd42874de162b8f9b77295b1c85e5d92725cc8310bae
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-trait-0.1/default) >= 0.1.52

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-convert"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
