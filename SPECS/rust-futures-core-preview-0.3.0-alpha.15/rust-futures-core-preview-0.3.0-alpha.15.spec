# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futures-core-preview
%global full_version 0.3.0-alpha.15
%global pkgname futures-core-preview-0.3.0-alpha.15
%global __requires_exclude_from ^%{_datadir}/cargo/registry/.*$

Name:           rust-futures-core-preview-0.3.0-alpha.15
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "futures-core-preview"
License:        MIT OR Apache-2.0
URL:            https://rust-lang-nursery.github.io/futures-rs
#!RemoteAsset:  sha256:10a3833d58fd08b3a40203613ed3a93c8bc0bc0181af5dd6422a0e08df1bfa68
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{full_version}
Provides:       crate(%{pkgname}/alloc) = %{full_version}
Provides:       crate(%{pkgname}/cfg-target-has-atomic) = %{full_version}
Provides:       crate(%{pkgname}/default) = %{full_version}
Provides:       crate(%{pkgname}/nightly) = %{full_version}
Provides:       crate(%{pkgname}/std) = %{full_version}

%description
Source code for takopackized Rust crate "futures-core-preview"

%install
%rust_install_crate
mv %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version} %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
