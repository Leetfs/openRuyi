# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name stdweb-internal-macros
%global full_version 0.2.7
%global pkgname stdweb-internal-macros-0.2
%global __requires_exclude_from ^%{_datadir}/cargo/registry/.*$

Name:           rust-stdweb-internal-macros-0.2
Version:        0.2.7
Release:        %autorelease
Summary:        Rust crate "stdweb-internal-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/koute/stdweb
#!RemoteAsset:  sha256:e68f7d08b76979a43e93fe043b66d2626e35d41d68b0b85519202c6dd8ac59fa
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base-x-0.2/default) >= 0.2.0
Requires:       crate(proc-macro2-0.4/default) >= 0.4.0
Requires:       crate(quote-0.6/default) >= 0.6.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-derive-1/default) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(sha1-0.6/default) >= 0.6.0
Requires:       crate(syn-0.15/clone-impls) >= 0.15.0
Requires:       crate(syn-0.15/full) >= 0.15.0
Requires:       crate(syn-0.15/parsing) >= 0.15.0
Requires:       crate(syn-0.15/printing) >= 0.15.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "stdweb-internal-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
