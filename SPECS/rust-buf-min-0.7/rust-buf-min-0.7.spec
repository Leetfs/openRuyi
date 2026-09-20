# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name buf-min
%global full_version 0.7.1
%global pkgname buf-min-0.7

Name:           rust-buf-min-0.7
Version:        0.7.1
Release:        %autorelease
Summary:        Rust crate "buf-min"
License:        MIT OR Apache-2.0
URL:            https://github.com/botika/buf-min
#!RemoteAsset:  sha256:22d5698cf6842742ed64805705798f8b351fff53fa546fd45c52184bee58dc90
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "buf-min"

%package     -n %{name}+bytes
Summary:        Minimal utf-8 safe buffer traits - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1/default) >= 1.3.0
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust buf-min crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ntex-bytes
Summary:        Minimal utf-8 safe buffer traits - feature "ntex-bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ntex-bytes-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/ntex-bytes) = %{version}

%description -n %{name}+ntex-bytes
This metapackage enables feature "ntex-bytes" for the Rust buf-min crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
