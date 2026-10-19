# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tar-framing
%global full_version 0.0.14
%global pkgname tar-framing-0.0.14

Name:           rust-tar-framing-0.0.14
Version:        0.0.14
Release:        %autorelease
Summary:        Rust crate "tar-framing"
License:        MIT OR Apache-2.0
URL:            https://github.com/astral-sh/tar-codec
#!RemoteAsset:  sha256:783223a7a6590be4227cb821e7ce80372575511f67c824921aba0752d8ad5573
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(tokio-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tar-framing"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
