# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name realfft
%global full_version 3.5.0
%global pkgname realfft-3

Name:           rust-realfft-3
Version:        3.5.0
Release:        %autorelease
Summary:        Rust crate "realfft"
License:        MIT
URL:            https://github.com/HEnquist/realfft
#!RemoteAsset:  sha256:f821338fddb99d089116342c46e9f1fbf3828dba077674613e734e01d6ea8677
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustfft-6) >= 6.4.1

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "realfft"

%package     -n %{name}+avx
Summary:        Real-to-complex forward FFT and complex-to-real inverse FFT for Rust - feature "avx"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustfft-6/avx) >= 6.4.1
Provides:       crate(%{pkgname}/avx) = %{version}

%description -n %{name}+avx
This metapackage enables feature "avx" for the Rust realfft crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Real-to-complex forward FFT and complex-to-real inverse FFT for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustfft-6/default) >= 6.4.1
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust realfft crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+neon
Summary:        Real-to-complex forward FFT and complex-to-real inverse FFT for Rust - feature "neon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustfft-6/neon) >= 6.4.1
Provides:       crate(%{pkgname}/neon) = %{version}

%description -n %{name}+neon
This metapackage enables feature "neon" for the Rust realfft crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sse
Summary:        Real-to-complex forward FFT and complex-to-real inverse FFT for Rust - feature "sse"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustfft-6/sse) >= 6.4.1
Provides:       crate(%{pkgname}/sse) = %{version}

%description -n %{name}+sse
This metapackage enables feature "sse" for the Rust realfft crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-simd
Summary:        Real-to-complex forward FFT and complex-to-real inverse FFT for Rust - feature "wasm_simd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustfft-6/wasm-simd) >= 6.4.1
Provides:       crate(%{pkgname}/wasm-simd) = %{version}

%description -n %{name}+wasm-simd
This metapackage enables feature "wasm_simd" for the Rust realfft crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
