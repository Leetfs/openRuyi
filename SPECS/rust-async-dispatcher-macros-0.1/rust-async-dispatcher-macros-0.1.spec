# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-dispatcher-macros
%global full_version 0.1.1
%global pkgname async-dispatcher-macros-0.1

Name:           rust-async-dispatcher-macros-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "async-dispatcher-macros"
License:        Apache-2.0
URL:            FIXME
#!RemoteAsset:  sha256:290f667ea7d3d4d63aa9b0e101218e6af1291e319338988d930c3f7700f8dff8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-dispatcher-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
