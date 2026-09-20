# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name asynk-strim-attr
%global full_version 0.1.0
%global pkgname asynk-strim-attr-0.1

Name:           rust-asynk-strim-attr-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "asynk-strim-attr"
License:        MIT OR Apache-2.0
URL:            https://github.com/BugenZhao/asynk-strim-attr
#!RemoteAsset:  sha256:b6ccb67be092524ce594e599332719f1cd6d64dcaed8d46f1e8726d466c10bcb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(asynk-strim-0.1/default) >= 0.1.5
Requires:       crate(asynk-strim-attr-macro-0.1/default) >= 0.1.0
Requires:       crate(futures-core-0.3) >= 0.3.32

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "asynk-strim-attr"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
