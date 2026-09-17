# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pcre2
%global full_version 0.2.11
%global pkgname pcre2-0.2

Name:           rust-pcre2-0.2
Version:        0.2.11
Release:        %autorelease
Summary:        Rust crate "pcre2"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/rust-pcre2
#!RemoteAsset:  sha256:9e970b0fcce0c7ee6ef662744ff711f21ccd6f11b7cf03cd187a80e89797fc67
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.146
Requires:       crate(log-0.4/default) >= 0.4.19
Requires:       crate(pcre2-sys-0.2/default) >= 0.2.10

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pcre2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
