# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name thiserror-ext-derive
%global full_version 0.3.0
%global pkgname thiserror-ext-derive-0.3

Name:           rust-thiserror-ext-derive-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "thiserror-ext-derive"
License:        Apache-2.0
URL:            https://github.com/risingwavelabs/thiserror-ext
#!RemoteAsset:  sha256:2b5042dd3b562d1d57711be902006a0003fa2781b81d5b2bec07416be31586ff
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(either-1/default) >= 1.15.0
Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/default) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/backtrace) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "thiserror-ext-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
