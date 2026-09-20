# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name logos-codegen
%global full_version 0.16.1
%global pkgname logos-codegen-0.16

Name:           rust-logos-codegen-0.16
Version:        0.16.1
Release:        %autorelease
Summary:        Rust crate "logos-codegen"
License:        MIT OR Apache-2.0
URL:            https://logos.maciej.codes/
#!RemoteAsset:  sha256:58b3ffaa284e1350d017a57d04ada118c4583cf260c8fb01e0fe28a2e9cf8970
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fnv-1/default) >= 1.0.7
Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(regex-automata-0.4/default) >= 0.4.14
Requires:       crate(regex-syntax-0.8/default) >= 0.8.10
Requires:       crate(syn-2/default) >= 2.0.117
Requires:       crate(syn-2/full) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/forbid-unsafe) = %{version}
Provides:       crate(%{pkgname}/state-machine-codegen) = %{version}

%description
Source code for takopackized Rust crate "logos-codegen"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
