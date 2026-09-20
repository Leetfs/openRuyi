# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name env_logger
%global full_version 0.3.0
%global pkgname env-logger-0.3

Name:           rust-env-logger-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "env_logger"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/log
#!RemoteAsset:  sha256:4abfefaaa4fc67e4cdec29b240562f7d8eb1bc1e792a593b5d21e8aba31db2d2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.3/default) >= 0.3.0
Requires:       crate(regex-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "env_logger"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
