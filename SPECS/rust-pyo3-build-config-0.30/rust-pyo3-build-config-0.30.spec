# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-build-config
%global full_version 0.30.1
%global pkgname pyo3-build-config-0.30

Name:           rust-pyo3-build-config-0.30
Version:        0.30.1
Release:        %autorelease
Summary:        Rust crate "pyo3-build-config"
License:        MIT OR Apache-2.0
URL:            https://pyo3.rs/
#!RemoteAsset:  sha256:70130e2b6dd1ee589a8788026a429561ca5c40fa7a2fa7914c2282eddae24700
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(target-lexicon-0.13/default) >= 0.13.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/extension-module) = %{version}
Provides:       crate(%{pkgname}/generate-import-lib) = %{version}
Provides:       crate(%{pkgname}/resolve-config) = %{version}

%description
Source code for takopackized Rust crate "pyo3-build-config"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
