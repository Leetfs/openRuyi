# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustfft
%global full_version 6.4.1
%global pkgname rustfft-6

Name:           rust-rustfft-6
Version:        6.4.1
Release:        %autorelease
Summary:        Rust crate "rustfft"
License:        MIT OR Apache-2.0
URL:            https://github.com/ejmahler/RustFFT
#!RemoteAsset:  sha256:21db5f9893e91f41798c88680037dba611ca6674703c1a18601b01a72c8adb89
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-complex-0.4/default) >= 0.4.6
Requires:       crate(num-integer-0.1/default) >= 0.1.46
Requires:       crate(num-traits-0.2/default) >= 0.2.19
Requires:       crate(primal-check-0.3/default) >= 0.3.4
Requires:       crate(strength-reduce-0.2/default) >= 0.2.4
Requires:       crate(transpose-0.2/default) >= 0.2.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/avx) = %{version}
Provides:       crate(%{pkgname}/neon) = %{version}
Provides:       crate(%{pkgname}/sse) = %{version}
Provides:       crate(%{pkgname}/wasm-simd) = %{version}

%description
Source code for takopackized Rust crate "rustfft"

%package     -n %{name}+default
Summary:        High-performance FFT library written in pure Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/avx) = %{version}
Requires:       crate(%{pkgname}/neon) = %{version}
Requires:       crate(%{pkgname}/sse) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rustfft crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
