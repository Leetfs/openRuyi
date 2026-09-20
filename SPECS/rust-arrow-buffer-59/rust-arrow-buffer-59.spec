# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-buffer
%global full_version 59.3.0
%global pkgname arrow-buffer-59

Name:           rust-arrow-buffer-59
Version:        59.3.0
Release:        %autorelease
Summary:        Rust crate "arrow-buffer"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:097d193003ce7995d5d087089069ec2a6e0187faf5a6f8c9f38af2645d987182
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.4.0
Requires:       crate(half-2) >= 2.1.0
Requires:       crate(num-bigint-0.5/std) >= 0.5.0
Requires:       crate(num-traits-0.2/std) >= 0.2.19

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/pool) = %{version}

%description
Source code for takopackized Rust crate "arrow-buffer"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
