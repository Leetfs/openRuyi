# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bin-proto-derive
%global full_version 0.12.1
%global pkgname bin-proto-derive-0.12

Name:           rust-bin-proto-derive-0.12
Version:        0.12.1
Release:        %autorelease
Summary:        Rust crate "bin-proto-derive"
License:        MIT
URL:            https://github.com/wojciech-graj/bin-proto
#!RemoteAsset:  sha256:5d10aefb1f658b852ec73510524abee7644e3b2b8552dba503722a7f5b944290
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.32
Requires:       crate(syn-2/full) >= 2.0.32

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "bin-proto-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
