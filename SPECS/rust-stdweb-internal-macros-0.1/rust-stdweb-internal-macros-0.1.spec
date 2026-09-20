# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name stdweb-internal-macros
%global full_version 0.1.0
%global pkgname stdweb-internal-macros-0.1

Name:           rust-stdweb-internal-macros-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "stdweb-internal-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/koute/stdweb
#!RemoteAsset:  sha256:b0bb3289dfd46bba44d80ed47a9b3d4c43bf6c1d7931b29e2fa86bd6697ccf59
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base-x-0.2/default) >= 0.2.0
Requires:       crate(quote-0.4/default) >= 0.4.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-derive-1/default) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(syn-0.12/clone-impls) >= 0.12.0
Requires:       crate(syn-0.12/full) >= 0.12.0
Requires:       crate(syn-0.12/parsing) >= 0.12.0
Requires:       crate(syn-0.12/printing) >= 0.12.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "stdweb-internal-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
