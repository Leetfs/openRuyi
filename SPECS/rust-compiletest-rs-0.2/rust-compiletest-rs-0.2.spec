# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name compiletest_rs
%global full_version 0.2.10
%global pkgname compiletest-rs-0.2

Name:           rust-compiletest-rs-0.2
Version:        0.2.10
Release:        %autorelease
Summary:        Rust crate "compiletest_rs"
License:        Apache-2.0 OR MIT
URL:            https://github.com/laumann/compiletest-rs
#!RemoteAsset:  sha256:2741d378feb7a434dba54228c89a70b4e427fee521de67cdda3750b8a0265f5a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.3/default) >= 0.3.5
Requires:       crate(rustc-serialize-0.3/default) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "compiletest_rs"

%package     -n %{name}+tempdir
Summary:        Compiletest utility from the Rust compiler as a standalone testing harness - feature "tempdir" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tempdir-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/tempdir) = %{version}
Provides:       crate(%{pkgname}/tmp) = %{version}

%description -n %{name}+tempdir
This metapackage enables feature "tempdir" for the Rust compiletest_rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "tmp" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
