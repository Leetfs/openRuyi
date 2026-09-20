# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-dispatcher
%global full_version 0.1.2
%global pkgname async-dispatcher-0.1

Name:           rust-async-dispatcher-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "async-dispatcher"
License:        Apache-2.0
URL:            FIXME
#!RemoteAsset:  sha256:5c8bff43baa5b0ca8f8bcd7f9338f5d30fbd75236a2aa89130a7c5121a06d6ca
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-task-4/default) >= 4.7.0
Requires:       crate(futures-lite-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-dispatcher"

%package     -n %{name}+async-dispatcher-macros
Summary:        Async runtime based on a pluggable dispatcher - feature "async-dispatcher-macros" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-dispatcher-macros-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/async-dispatcher-macros) = %{version}
Provides:       crate(%{pkgname}/macros) = %{version}

%description -n %{name}+async-dispatcher-macros
This metapackage enables feature "async-dispatcher-macros" for the Rust async-dispatcher crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "macros" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
