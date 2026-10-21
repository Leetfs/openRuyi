# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uv-macros
%global full_version 0.0.96
%global pkgname uv-macros-0.0.96

Name:           rust-uv-macros-0.0.96
Version:        0.0.96
Release:        %autorelease
Summary:        Rust crate "uv-macros"
License:        MIT OR Apache-2.0
URL:            https://pypi.org/project/uv/
#!RemoteAsset:  sha256:8da81f4904e65c2a5f78240cd16dd87e693f27931e2dcaa839811b5a5e563a76
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/proc-macro) >= 1.0.86
Requires:       crate(quote-1/proc-macro) >= 1.0.37
Requires:       crate(syn-3/clone-impls) >= 3.0.0
Requires:       crate(syn-3/derive) >= 3.0.0
Requires:       crate(syn-3/full) >= 3.0.0
Requires:       crate(syn-3/parsing) >= 3.0.0
Requires:       crate(syn-3/printing) >= 3.0.0
Requires:       crate(syn-3/proc-macro) >= 3.0.0
Requires:       crate(textwrap-0.16/smawk) >= 0.16.1
Requires:       crate(textwrap-0.16/unicode-width) >= 0.16.1
Requires:       crate(uv-version-0.13/default) >= 0.13.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "uv-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
