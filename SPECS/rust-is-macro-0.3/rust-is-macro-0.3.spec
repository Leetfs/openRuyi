# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name is-macro
%global full_version 0.3.7
%global pkgname is-macro-0.3

Name:           rust-is-macro-0.3
Version:        0.3.7
Release:        %autorelease
Summary:        Rust crate "is-macro"
License:        Apache-2.0
URL:            https://github.com/dudykr/ddbase.git
#!RemoteAsset:  sha256:1d57a3e447e24c22647738e4607f1df1e0ec6f72e16182c4cd199f647cdfb0e4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/default) >= 2.0.117
Requires:       crate(syn-2/derive) >= 2.0.117
Requires:       crate(syn-2/extra-traits) >= 2.0.117
Requires:       crate(syn-2/fold) >= 2.0.117
Requires:       crate(syn-2/full) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "is-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
