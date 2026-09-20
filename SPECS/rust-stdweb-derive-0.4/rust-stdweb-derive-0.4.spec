# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name stdweb-derive
%global full_version 0.4.0
%global pkgname stdweb-derive-0.4

Name:           rust-stdweb-derive-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "stdweb-derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/koute/stdweb
#!RemoteAsset:  sha256:6aa46e9b38ea028a8a327ae6db35a486ace3eb834f5600bb3b6a71c0b6b1bd4b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-0.4/default) >= 0.4.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-derive-1/default) >= 1.0.0
Requires:       crate(syn-0.12/derive) >= 0.12.0
Requires:       crate(syn-0.12/parsing) >= 0.12.0
Requires:       crate(syn-0.12/printing) >= 0.12.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "stdweb-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
