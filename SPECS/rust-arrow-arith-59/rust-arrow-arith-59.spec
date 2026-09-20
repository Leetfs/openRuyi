# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-arith
%global full_version 59.3.0
%global pkgname arrow-arith-59

Name:           rust-arrow-arith-59
Version:        59.3.0
Release:        %autorelease
Summary:        Rust crate "arrow-arith"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:ce2961626677665b2195eb59242af4c7befe7b8737ca2050295389362380104e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-array-59/default) >= 59.3.0
Requires:       crate(arrow-buffer-59/default) >= 59.3.0
Requires:       crate(arrow-data-59/default) >= 59.3.0
Requires:       crate(arrow-schema-59/default) >= 59.3.0
Requires:       crate(chrono-0.4/clock) >= 0.4.40
Requires:       crate(num-traits-0.2/std) >= 0.2.19

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "arrow-arith"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
