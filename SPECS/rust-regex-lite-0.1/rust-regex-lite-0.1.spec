# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name regex-lite
%global full_version 0.1.9
%global pkgname regex-lite-0.1

Name:           rust-regex-lite-0.1
Version:        0.1.9
Release:        %autorelease
Summary:        Rust crate "regex-lite"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/regex/tree/master/regex-lite
#!RemoteAsset:  sha256:cab834c73d247e67f4fae452806d17d3c7501756d98c8808d7c9c7aa7d18f973
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/string) = %{version}

%description
Source code for takopackized Rust crate "regex-lite"

%package     -n %{name}+default
Summary:        Lightweight regex engine that optimizes for binary size and compilation time - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/string) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust regex-lite crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
