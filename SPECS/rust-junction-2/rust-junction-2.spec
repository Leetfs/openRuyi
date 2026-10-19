# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name junction
%global full_version 2.1.0
%global pkgname junction-2

Name:           rust-junction-2
Version:        2.1.0
Release:        %autorelease
Summary:        Rust crate "junction"
License:        MIT
URL:            https://github.com/tesuji/junction
#!RemoteAsset:  sha256:cde48f36530cbd91b65f050101e6c056d6eb743cea2a8f0f19beef69c6742ff8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(scopeguard-1) >= 1.0.0
Requires:       crate(windows-sys-0.59/win32-foundation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-security) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-storage-filesystem) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-io) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-ioctl) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-systemservices) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-threading) >= 0.59.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/unstable-admin) = %{version}

%description
Source code for takopackized Rust crate "junction"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
