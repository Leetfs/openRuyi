# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-array
%global full_version 59.3.0
%global pkgname arrow-array-59

Name:           rust-arrow-array-59
Version:        59.3.0
Release:        %autorelease
Summary:        Rust crate "arrow-array"
License:        Apache-2.0 AND MIT
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:1e5f6adeffdf587d7a31db5d2266189624b526730cd3627f9ff9fedae97ad584
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ahash-0.8/compile-time-rng) >= 0.8.0
Requires:       crate(ahash-0.8/runtime-rng) >= 0.8.0
Requires:       crate(arrow-buffer-59/default) >= 59.3.0
Requires:       crate(arrow-data-59/default) >= 59.3.0
Requires:       crate(arrow-schema-59/default) >= 59.3.0
Requires:       crate(chrono-0.4/clock) >= 0.4.40
Requires:       crate(half-2/num-traits) >= 2.1.0
Requires:       crate(hashbrown-0.17) >= 0.17.0
Requires:       crate(num-complex-0.4/std) >= 0.4.6
Requires:       crate(num-integer-0.1/std) >= 0.1.46
Requires:       crate(num-traits-0.2/std) >= 0.2.19

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/force-validate) = %{version}

%description
Source code for takopackized Rust crate "arrow-array"

%package     -n %{name}+async
Summary:        Array abstractions for Apache Arrow - feature "async"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/async) = %{version}

%description -n %{name}+async
This metapackage enables feature "async" for the Rust arrow-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono-tz
Summary:        Array abstractions for Apache Arrow - feature "chrono-tz"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-tz-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/chrono-tz) = %{version}

%description -n %{name}+chrono-tz
This metapackage enables feature "chrono-tz" for the Rust arrow-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ffi
Summary:        Array abstractions for Apache Arrow - feature "ffi"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-data-59/ffi) >= 59.3.0
Requires:       crate(arrow-schema-59/ffi) >= 59.3.0
Requires:       crate(libc-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/ffi) = %{version}

%description -n %{name}+ffi
This metapackage enables feature "ffi" for the Rust arrow-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pool
Summary:        Array abstractions for Apache Arrow - feature "pool"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-buffer-59/pool) >= 59.3.0
Requires:       crate(arrow-data-59/pool) >= 59.3.0
Provides:       crate(%{pkgname}/pool) = %{version}

%description -n %{name}+pool
This metapackage enables feature "pool" for the Rust arrow-array crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
