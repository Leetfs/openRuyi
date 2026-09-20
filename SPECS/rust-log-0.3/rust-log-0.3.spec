# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name log
%global full_version 0.3.6
%global pkgname log-0.3

Name:           rust-log-0.3
Version:        0.3.6
Release:        %autorelease
Summary:        Rust crate "log"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/log
#!RemoteAsset:  sha256:ab83497bf8bf4ed2a74259c1c802351fcd67a65baa86394b6ba73c36f4838054
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/max-level-debug) = %{version}
Provides:       crate(%{pkgname}/max-level-error) = %{version}
Provides:       crate(%{pkgname}/max-level-info) = %{version}
Provides:       crate(%{pkgname}/max-level-off) = %{version}
Provides:       crate(%{pkgname}/max-level-trace) = %{version}
Provides:       crate(%{pkgname}/max-level-warn) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/release-max-level-debug) = %{version}
Provides:       crate(%{pkgname}/release-max-level-error) = %{version}
Provides:       crate(%{pkgname}/release-max-level-info) = %{version}
Provides:       crate(%{pkgname}/release-max-level-off) = %{version}
Provides:       crate(%{pkgname}/release-max-level-trace) = %{version}
Provides:       crate(%{pkgname}/release-max-level-warn) = %{version}
Provides:       crate(%{pkgname}/use-std) = %{version}

%description
Source code for takopackized Rust crate "log"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
