# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name asynk-strim-attr-macro
%global full_version 0.1.0
%global pkgname asynk-strim-attr-macro-0.1

Name:           rust-asynk-strim-attr-macro-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "asynk-strim-attr-macro"
License:        MIT OR Apache-2.0
URL:            https://github.com/BugenZhao/asynk-strim-attr
#!RemoteAsset:  sha256:34e40a2181bb16fb68e25c49c8b3e25bbb9a808bf8f9f83bc596ac4ad70c86a1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro-crate-3) >= 3.5.0
Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/clone-impls) >= 2.0.117
Requires:       crate(syn-2/full) >= 2.0.117
Requires:       crate(syn-2/parsing) >= 2.0.117
Requires:       crate(syn-2/printing) >= 2.0.117
Requires:       crate(syn-2/proc-macro) >= 2.0.117
Requires:       crate(syn-2/visit-mut) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "asynk-strim-attr-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
