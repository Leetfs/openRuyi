# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro2
%global full_version 0.4.0
%global pkgname proc-macro2-0.4

Name:           rust-proc-macro2-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "proc-macro2"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/proc-macro2
#!RemoteAsset:  sha256:5992baf49fc653894c8f854f72b161c1b3e525bfa3d1b3ea85a93623ba933d13
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-xid-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/proc-macro) = %{version}

%description
Comes with an option, off by default, to also reimplement itself in terms of the upstream unstable API.
Source code for takopackized Rust crate "proc-macro2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
