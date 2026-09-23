# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name stdweb-derive
%global full_version 0.5.1
%global pkgname stdweb-derive-0.5
%global __requires_exclude_from ^%{_datadir}/cargo/registry/.*$

Name:           rust-stdweb-derive-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "stdweb-derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/koute/stdweb
#!RemoteAsset:  sha256:0e21ebd9179de08f2300a65454268a17ea3de204627458588c84319c4def3930
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-0.4/default) >= 0.4.0
Requires:       crate(quote-0.6/default) >= 0.6.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-derive-1/default) >= 1.0.0
Requires:       crate(syn-0.15/derive) >= 0.15.0
Requires:       crate(syn-0.15/parsing) >= 0.15.0
Requires:       crate(syn-0.15/printing) >= 0.15.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "stdweb-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
