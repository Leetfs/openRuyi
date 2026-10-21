# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name archive-trait
%global full_version 0.0.15
%global pkgname archive-trait-0.0.15

Name:           rust-archive-trait-0.0.15
Version:        0.0.15
Release:        %autorelease
Summary:        Rust crate "archive-trait"
License:        MIT OR Apache-2.0
URL:            https://github.com/astral-sh/astral-codec
#!RemoteAsset:  sha256:999bf88cc483664cab77700ca2fdfb0415a73412abe284ef5bc2319d00938e00
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cap-std-4/default) >= 4.0.2
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/fs) >= 1.0.0
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-1/rt) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Requires:       crate(walkdir-2/default) >= 2.5.0
Requires:       crate(windows-sys-0.60/default) >= 0.60.2
Requires:       crate(windows-sys-0.60/win32-storage-filesystem) >= 0.60.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "archive-trait"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
