# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tar-codec
%global full_version 0.0.14
%global pkgname tar-codec-0.0.14

Name:           rust-tar-codec-0.0.14
Version:        0.0.14
Release:        %autorelease
Summary:        Rust crate "tar-codec"
License:        MIT OR Apache-2.0
URL:            https://github.com/astral-sh/tar-codec
#!RemoteAsset:  sha256:7ea42eb144d30fcbf32c26dfea8959175bb8335bfb7b18d20c6ed32edecf0551
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(archive-trait-0.0.14/default) >= 0.0.14
Requires:       crate(tar-framing-0.0.14/default) >= 0.0.14
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/io-util) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tar-codec"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
