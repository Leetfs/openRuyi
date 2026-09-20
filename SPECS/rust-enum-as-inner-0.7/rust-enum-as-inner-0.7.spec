# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name enum-as-inner
%global full_version 0.7.0
%global pkgname enum-as-inner-0.7

Name:           rust-enum-as-inner-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "enum-as-inner"
License:        MIT OR Apache-2.0
URL:            https://github.com/bluejekyll/enum-as-inner
#!RemoteAsset:  sha256:0359ee92f81184d7985519e474bda2a5738476334edd3746c9b1265c067afe70
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/default) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "enum-as-inner"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
