# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name parking_lot
%global full_version 0.11.2
%global pkgname parking-lot-0.11

Name:           rust-parking-lot-0.11
Version:        0.11.2
Release:        %autorelease
Summary:        Rust crate "parking_lot"
License:        Apache-2.0 OR MIT
URL:            https://github.com/Amanieu/parking_lot
#!RemoteAsset:  sha256:7d17b78036a60663b797adeaee46f5c9dfebb86948d1255007a1d6be0271ff99
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(instant-0.1/default) >= 0.1.9
Requires:       crate(lock-api-0.4/default) >= 0.4.5
Requires:       crate(parking-lot-core-0.8/default) >= 0.8.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/send-guard) = %{version}

%description
Source code for takopackized Rust crate "parking_lot"

%package     -n %{name}+arc-lock
Summary:        More compact and efficient implementations of the standard synchronization primitives - feature "arc_lock"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lock-api-0.4/arc-lock) >= 0.4.5
Provides:       crate(%{pkgname}/arc-lock) = %{version}

%description -n %{name}+arc-lock
This metapackage enables feature "arc_lock" for the Rust parking_lot crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deadlock-detection
Summary:        More compact and efficient implementations of the standard synchronization primitives - feature "deadlock_detection"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(parking-lot-core-0.8/deadlock-detection) >= 0.8.4
Provides:       crate(%{pkgname}/deadlock-detection) = %{version}

%description -n %{name}+deadlock-detection
This metapackage enables feature "deadlock_detection" for the Rust parking_lot crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly
Summary:        More compact and efficient implementations of the standard synchronization primitives - feature "nightly"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lock-api-0.4/nightly) >= 0.4.5
Requires:       crate(parking-lot-core-0.8/nightly) >= 0.8.4
Provides:       crate(%{pkgname}/nightly) = %{version}

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust parking_lot crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+owning-ref
Summary:        More compact and efficient implementations of the standard synchronization primitives - feature "owning_ref"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lock-api-0.4/owning-ref) >= 0.4.5
Provides:       crate(%{pkgname}/owning-ref) = %{version}

%description -n %{name}+owning-ref
This metapackage enables feature "owning_ref" for the Rust parking_lot crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        More compact and efficient implementations of the standard synchronization primitives - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lock-api-0.4/serde) >= 0.4.5
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust parking_lot crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stdweb
Summary:        More compact and efficient implementations of the standard synchronization primitives - feature "stdweb"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(instant-0.1/stdweb) >= 0.1.9
Provides:       crate(%{pkgname}/stdweb) = %{version}

%description -n %{name}+stdweb
This metapackage enables feature "stdweb" for the Rust parking_lot crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen
Summary:        More compact and efficient implementations of the standard synchronization primitives - feature "wasm-bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(instant-0.1/wasm-bindgen) >= 0.1.9
Provides:       crate(%{pkgname}/wasm-bindgen) = %{version}

%description -n %{name}+wasm-bindgen
This metapackage enables feature "wasm-bindgen" for the Rust parking_lot crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
