# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name astral-mail-headers
%global full_version 0.0.1
%global pkgname astral-mail-headers-0.0.1

Name:           rust-astral-mail-headers-0.0.1
Version:        0.0.1
Release:        %autorelease
Summary:        Rust crate "astral-mail-headers"
License:        MIT OR Apache-2.0
URL:            https://github.com/astral-sh/astral-mail-headers
#!RemoteAsset:  sha256:dc019ecca82cfc91ffa31ab4ffe705aaa706399840a7152926b7eee736da410a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.22/alloc) >= 0.22.1
Requires:       crate(encoding-rs-0.8/alloc) >= 0.8.35
Requires:       crate(memchr-2/std) >= 2.7.4
Requires:       crate(simdutf8-0.1/aarch64-neon) >= 0.1.5
Requires:       crate(simdutf8-0.1/std) >= 0.1.5

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "astral-mail-headers"

%package     -n %{name}+benchmark-jemalloc
Summary:        High-performance email header parser designed for Python packaging - feature "benchmark-jemalloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tikv-jemallocator-0.6/background-threads-runtime-support) >= 0.6.0
Provides:       crate(%{pkgname}/benchmark-jemalloc) = %{version}

%description -n %{name}+benchmark-jemalloc
This metapackage enables feature "benchmark-jemalloc" for the Rust astral-mail-headers crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
