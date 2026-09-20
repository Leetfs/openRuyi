# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name half
%global full_version 1.8.3
%global pkgname half-1

Name:           rust-half-1
Version:        1.8.3
Release:        %autorelease
Summary:        Rust crate "half"
License:        MIT OR Apache-2.0
URL:            https://github.com/starkat99/half-rs
#!RemoteAsset:  sha256:1b43ede17f21864e81be2fa654110bf1e793774238d86ef8555c37e6519c0403
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/use-intrinsics) = %{version}

%description
Source code for takopackized Rust crate "half"

%package     -n %{name}+bytemuck
Summary:        Half-precision floating point f16 and bf16 types for Rust implementing the IEEE 754-2008 standard binary16 and bfloat16 types - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1/derive) >= 1.4.1
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust half crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-traits
Summary:        Half-precision floating point f16 and bf16 types for Rust implementing the IEEE 754-2008 standard binary16 and bfloat16 types - feature "num-traits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2/libm) >= 0.2.14
Provides:       crate(%{pkgname}/num-traits) = %{version}

%description -n %{name}+num-traits
This metapackage enables feature "num-traits" for the Rust half crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Half-precision floating point f16 and bf16 types for Rust implementing the IEEE 754-2008 standard binary16 and bfloat16 types - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serialize) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust half crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serialize" feature.

%package     -n %{name}+zerocopy
Summary:        Half-precision floating point f16 and bf16 types for Rust implementing the IEEE 754-2008 standard binary16 and bfloat16 types - feature "zerocopy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zerocopy-0.6) >= 0.6.0
Provides:       crate(%{pkgname}/zerocopy) = %{version}

%description -n %{name}+zerocopy
This metapackage enables feature "zerocopy" for the Rust half crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
