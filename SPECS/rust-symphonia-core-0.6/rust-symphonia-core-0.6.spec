# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name symphonia-core
%global full_version 0.6.0
%global pkgname symphonia-core-0.6

Name:           rust-symphonia-core-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "symphonia-core"
License:        MPL-2.0
URL:            https://github.com/pdeljanov/Symphonia
#!RemoteAsset:  sha256:95ec293b5f288383b72a7bffcade6b2860b642cf66f28b3bd5967349a49938b1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.11.0
Requires:       crate(bytemuck-1/default) >= 1.25.0
Requires:       crate(lazy-static-1/default) >= 1.5.0
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(num-complex-0.4/default) >= 0.4.6
Requires:       crate(smallvec-1/default) >= 1.15.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/exp-subtitle-codecs) = %{version}
Provides:       crate(%{pkgname}/exp-video-codecs) = %{version}

%description
Source code for takopackized Rust crate "symphonia-core"

%package     -n %{name}+opt-simd
Summary:        Project Symphonia shared structs, traits, and features - feature "opt-simd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/opt-simd-avx) = %{version}
Requires:       crate(%{pkgname}/opt-simd-neon) = %{version}
Requires:       crate(%{pkgname}/opt-simd-sse) = %{version}
Provides:       crate(%{pkgname}/opt-simd) = %{version}

%description -n %{name}+opt-simd
This metapackage enables feature "opt-simd" for the Rust symphonia-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+opt-simd-avx
Summary:        Project Symphonia shared structs, traits, and features - feature "opt-simd-avx"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustfft-6/avx) >= 6.1.0
Provides:       crate(%{pkgname}/opt-simd-avx) = %{version}

%description -n %{name}+opt-simd-avx
This metapackage enables feature "opt-simd-avx" for the Rust symphonia-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+opt-simd-neon
Summary:        Project Symphonia shared structs, traits, and features - feature "opt-simd-neon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustfft-6/neon) >= 6.1.0
Provides:       crate(%{pkgname}/opt-simd-neon) = %{version}

%description -n %{name}+opt-simd-neon
This metapackage enables feature "opt-simd-neon" for the Rust symphonia-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+opt-simd-sse
Summary:        Project Symphonia shared structs, traits, and features - feature "opt-simd-sse"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustfft-6/sse) >= 6.1.0
Provides:       crate(%{pkgname}/opt-simd-sse) = %{version}

%description -n %{name}+opt-simd-sse
This metapackage enables feature "opt-simd-sse" for the Rust symphonia-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustfft
Summary:        Project Symphonia shared structs, traits, and features - feature "rustfft"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustfft-6) >= 6.1.0
Provides:       crate(%{pkgname}/rustfft) = %{version}

%description -n %{name}+rustfft
This metapackage enables feature "rustfft" for the Rust symphonia-core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
