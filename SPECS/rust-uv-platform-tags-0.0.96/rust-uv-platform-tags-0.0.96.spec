# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uv-platform-tags
%global full_version 0.0.96
%global pkgname uv-platform-tags-0.0.96

Name:           rust-uv-platform-tags-0.0.96
Version:        0.0.96
Release:        %autorelease
Summary:        Rust crate "uv-platform-tags"
License:        MIT OR Apache-2.0
URL:            https://pypi.org/project/uv/
#!RemoteAsset:  sha256:af49d51092abc721444ef17a1e6f933c739ce5191a47820836d5bee81bfef109
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2) >= 2.6.0
Requires:       crate(memchr-2/std) >= 2.7.4
Requires:       crate(rkyv-0.8/bytecheck) >= 0.8.14
Requires:       crate(rkyv-0.8/std) >= 0.8.14
Requires:       crate(rustc-hash-2/std) >= 2.0.0
Requires:       crate(serde-1/derive) >= 1.0.210
Requires:       crate(serde-1/rc) >= 1.0.210
Requires:       crate(serde-1/std) >= 1.0.210
Requires:       crate(thiserror-2/std) >= 2.0.0
Requires:       crate(uv-macros-0.0.96/default) >= 0.0.96
Requires:       crate(uv-small-str-0.0.96/default) >= 0.0.96

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "uv-platform-tags"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
