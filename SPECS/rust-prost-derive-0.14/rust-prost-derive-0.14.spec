# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prost-derive
%global full_version 0.14.3
%global pkgname prost-derive-0.14

Name:           rust-prost-derive-0.14
Version:        0.14.3
Release:        %autorelease
Summary:        Rust crate "prost-derive"
License:        Apache-2.0
URL:            https://github.com/tokio-rs/prost
#!RemoteAsset:  sha256:27c6023962132f4b30eb4c172c91ce92d933da334c59c23cddee82358ddafb0b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.102
Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/default) >= 2.0.117
Requires:       crate(syn-2/extra-traits) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "prost-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
