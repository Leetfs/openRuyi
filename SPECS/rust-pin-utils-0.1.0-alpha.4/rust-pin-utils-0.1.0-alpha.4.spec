# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pin-utils
%global full_version 0.1.0-alpha.4
%global pkgname pin-utils-0.1.0-alpha.4
%global __requires_exclude_from ^%{_datadir}/cargo/registry/.*$

Name:           rust-pin-utils-0.1.0-alpha.4
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "pin-utils"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang-nursery/pin-utils
#!RemoteAsset:  sha256:5894c618ce612a3fa23881b152b608bafb8c56cfc22f434a3ba3120b40f7b587
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{full_version}
Provides:       crate(%{pkgname}/default) = %{full_version}

%description
Source code for takopackized Rust crate "pin-utils"

%install
%rust_install_crate
mv %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version} %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
