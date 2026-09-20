# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name asynk-strim
%global full_version 0.1.5
%global pkgname asynk-strim-0.1

Name:           rust-asynk-strim-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "asynk-strim"
License:        MIT OR Apache-2.0
URL:            https://github.com/aumetra/asynk-strim.git
#!RemoteAsset:  sha256:52697735bdaac441a29391a9e97102c74c6ef0f9b60a40cf109b1b404e29d2f6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-core-0.3) >= 0.3.32
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "asynk-strim"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
