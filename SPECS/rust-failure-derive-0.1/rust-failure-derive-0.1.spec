# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name failure_derive
%global full_version 0.1.1
%global pkgname failure-derive-0.1

Name:           rust-failure-derive-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "failure_derive"
License:        MIT OR Apache-2.0
URL:            https://boats.gitlab.io/failure
#!RemoteAsset:  sha256:c7cdda555bb90c9bb67a3b670a0f42de8e73f5981524123ad8578aafec8ddb8b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-0.3/default) >= 0.3.15
Requires:       crate(syn-0.11/default) >= 0.11.11
Requires:       crate(synstructure-0.6/default) >= 0.6.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "failure_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
