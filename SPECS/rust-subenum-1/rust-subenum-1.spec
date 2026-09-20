# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name subenum
%global full_version 1.1.3
%global pkgname subenum-1

Name:           rust-subenum-1
Version:        1.1.3
Release:        %autorelease
Summary:        Rust crate "subenum"
License:        MIT OR Apache-2.0
URL:            https://github.com/paholg/subenum
#!RemoteAsset:  sha256:ec3d08fe7078c57309d5c3d938e50eba95ba1d33b9c3a101a8465fc6861a5416
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/default) >= 2.0.117
Requires:       crate(syn-2/extra-traits) >= 2.0.117
Requires:       crate(syn-2/full) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/error-trait) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "subenum"

%package     -n %{name}+default
Summary:        Proc-macro to create subsets of enums, that can be converted   to and from - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/error-trait) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust subenum crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
