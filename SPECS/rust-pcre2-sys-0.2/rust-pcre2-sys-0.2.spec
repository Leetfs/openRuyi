# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pcre2-sys
%global full_version 0.2.10
%global pkgname pcre2-sys-0.2

Name:           rust-pcre2-sys-0.2
Version:        0.2.10
Release:        %autorelease
Summary:        Rust crate "pcre2-sys"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/rust-pcre2
#!RemoteAsset:  sha256:18b9073c1a2549bd409bf4a32c94d903bb1a09bf845bc306ae148897fa0760a4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.73
Requires:       crate(cc-1/parallel) >= 1.0.73
Requires:       crate(libc-0.2/default) >= 0.2.146
Requires:       crate(pkg-config-0.3) >= 0.3.27

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pcre2-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
