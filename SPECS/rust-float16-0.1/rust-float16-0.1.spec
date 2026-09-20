# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name float16
%global full_version 0.1.0
%global pkgname float16-0.1

Name:           rust-float16-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "float16"
License:        MIT OR Apache-2.0
URL:            https://github.com/Alexhuszagh/float16
#!RemoteAsset:  sha256:79f2b972fb53f36f200fbc4a2eefc036c2b56a28aaca9cd0f9dc19bc44acfac2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(rustc-version-0.2) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "float16"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
