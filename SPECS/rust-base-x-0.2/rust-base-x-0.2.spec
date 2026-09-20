# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name base-x
%global full_version 0.2.0
%global pkgname base-x-0.2

Name:           rust-base-x-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "base-x"
License:        FIXME
URL:            https://github.com/OrKoN/base-x-rs
#!RemoteAsset:  sha256:fe9ad92e7876f320bf1ba3325acb19d1bfcfdfdf52d15cbe7bd38314cf81854d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "base-x"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
