# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-attributes
%global full_version 1.1.2
%global pkgname async-attributes-1

Name:           rust-async-attributes-1
Version:        1.1.2
Release:        %autorelease
Summary:        Rust crate "async-attributes"
License:        MIT OR Apache-2.0
URL:            https://github.com/async-rs/async-attributes
#!RemoteAsset:  sha256:a3203e79f4dd9bdda415ed03cf14dae5a2bf775c683a00f94e9cd1faf0f596e5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-1/default) >= 1.0.0
Requires:       crate(syn-1/full) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-attributes"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
