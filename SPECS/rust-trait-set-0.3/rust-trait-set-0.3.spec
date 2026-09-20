# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name trait-set
%global full_version 0.3.0
%global pkgname trait-set-0.3

Name:           rust-trait-set-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "trait-set"
License:        MIT
URL:            https://github.com/popzxc/trait-set
#!RemoteAsset:  sha256:b79e2e9c9ab44c6d7c20d5976961b47e8f49ac199154daa514b77cd1ab536625
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-1/default) >= 1.0.109

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "trait-set"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
