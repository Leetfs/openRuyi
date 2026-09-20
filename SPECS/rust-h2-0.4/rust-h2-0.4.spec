# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name h2
%global full_version 0.4.15
%global pkgname h2-0.4

Name:           rust-h2-0.4
Version:        0.4.15
Release:        %autorelease
Summary:        Rust crate "h2"
License:        MIT
URL:            https://github.com/hyperium/h2
#!RemoteAsset:  sha256:6cb093c84e8bd9b188d4c4a8cb6579fc016968d14c99882163cd3ff402a4f155
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(atomic-waker-1/default) >= 1.1.2
Requires:       crate(bytes-1/default) >= 1.12.0
Requires:       crate(fnv-1/default) >= 1.0.7
Requires:       crate(futures-core-0.3) >= 0.3.32
Requires:       crate(futures-sink-0.3) >= 0.3.32
Requires:       crate(http-1/default) >= 1.4.0
Requires:       crate(indexmap-2/default) >= 2.13.0
Requires:       crate(indexmap-2/std) >= 2.13.0
Requires:       crate(slab-0.4/default) >= 0.4.12
Requires:       crate(tokio-1/default) >= 1.52.3
Requires:       crate(tokio-1/io-util) >= 1.52.3
Requires:       crate(tokio-util-0.7/codec) >= 0.7.18
Requires:       crate(tokio-util-0.7/default) >= 0.7.18
Requires:       crate(tokio-util-0.7/io) >= 0.7.18
Requires:       crate(tracing-0.1/std) >= 0.1.44

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/stream) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "h2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
