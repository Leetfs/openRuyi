# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_default
%global full_version 0.2.0
%global pkgname serde-default-0.2

Name:           rust-serde-default-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "serde_default"
License:        MIT
URL:            https://github.com/TedDriggs/serde_default
#!RemoteAsset:  sha256:486b028b311aaaea83e0ba65a3e6e3cbef381e74e9d0bd6263faefd1fb503c1d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(darling-0.20/default) >= 0.20.11
Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/default) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "serde_default"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
