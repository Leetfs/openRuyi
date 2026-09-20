# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rstar
%global full_version 0.8.0
%global pkgname rstar-0.8

Name:           rust-rstar-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "rstar"
License:        MIT OR Apache-2.0
URL:            https://github.com/Stoeoef/rstar
#!RemoteAsset:  sha256:7b305196ce78c78c37c47890cfde452a14f8a5e7d5516314e69b062b5ed132c2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heapless-0.5/default) >= 0.5.0
Requires:       crate(num-traits-0.2/default) >= 0.2.0
Requires:       crate(pdqselect-0.1/default) >= 0.1.0
Requires:       crate(smallvec-1/default) >= 1.4.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rstar"

%package     -n %{name}+serde
Summary:        R*-tree library for the rust ecosystem - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rstar crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
