# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro2
%global full_version 0.2.0
%global pkgname proc-macro2-0.2

Name:           rust-proc-macro2-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "proc-macro2"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/proc-macro2
#!RemoteAsset:  sha256:b48db3af21624df4894fcd6c2e09f38b43f9fede17b9619b19e030916a3a31b3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-xid-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Comes with an option, off by default, to also reimplement itself in terms of the upstream unstable API.
Source code for takopackized Rust crate "proc-macro2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
