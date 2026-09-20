# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name write16
%global full_version 1.0.0
%global pkgname write16-1

Name:           rust-write16-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "write16"
License:        Apache-2.0 OR MIT
URL:            https://docs.rs/write16/
#!RemoteAsset:  sha256:d1890f4022759daae28ed4fe62859b1236caebfc61ede2f63ed4e695f3f6d936
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "write16"

%package     -n %{name}+arrayvec
Summary:        UTF-16 analog of the Write trait - feature "arrayvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrayvec-0.7/default) >= 0.7.2
Provides:       crate(%{pkgname}/arrayvec) = %{version}

%description -n %{name}+arrayvec
This metapackage enables feature "arrayvec" for the Rust write16 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec
Summary:        UTF-16 analog of the Write trait - feature "smallvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smallvec-1/default) >= 1.9.0
Provides:       crate(%{pkgname}/smallvec) = %{version}

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust write16 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
