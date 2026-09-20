# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name v_htmlescape
%global full_version 0.15.8
%global pkgname v-htmlescape-0.15

Name:           rust-v-htmlescape-0.15
Version:        0.15.8
Release:        %autorelease
Summary:        Rust crate "v_htmlescape"
License:        MIT OR Apache-2.0
URL:            https://github.com/botika/v_escape
#!RemoteAsset:  sha256:4e8257fbc510f0a46eb602c10215901938b5c2a7d5e70fc11483b1d3c9b5b18c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "v_htmlescape"

%package     -n %{name}+buf-min
Summary:        Simd optimized HTML escaping code - feature "buf-min" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(buf-min-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/buf-min) = %{version}
Provides:       crate(%{pkgname}/bytes-buf) = %{version}

%description -n %{name}+buf-min
This metapackage enables feature "buf-min" for the Rust v_htmlescape crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bytes-buf" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
