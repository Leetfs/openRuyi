# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gmp-mpfr-sys
%global full_version 1.7.1
%global pkgname gmp-mpfr-sys-1

Name:           rust-gmp-mpfr-sys-1
Version:        1.7.1
Release:        %autorelease
Summary:        Rust crate "gmp-mpfr-sys"
License:        LGPL-3.0+
URL:            https://gitlab.com/tspiteri/gmp-mpfr-sys
#!RemoteAsset:  sha256:7db155b537cb791b133341f99f68371d86ee7fa4c79aacfbc376d72d23c70531
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2) >= 0.2.127

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/c-no-tests) = %{version}
Provides:       crate(%{pkgname}/cnodelete) = %{version}
Provides:       crate(%{pkgname}/fail-on-warnings) = %{version}
Provides:       crate(%{pkgname}/force-cross) = %{version}
Provides:       crate(%{pkgname}/mpc) = %{version}
Provides:       crate(%{pkgname}/mpfr) = %{version}
Provides:       crate(%{pkgname}/use-system-libs) = %{version}

%description
Source code for takopackized Rust crate "gmp-mpfr-sys"

%package     -n %{name}+default
Summary:        Rust FFI bindings for GMP, MPFR and MPC - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/mpc) = %{version}
Requires:       crate(%{pkgname}/mpfr) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust gmp-mpfr-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
