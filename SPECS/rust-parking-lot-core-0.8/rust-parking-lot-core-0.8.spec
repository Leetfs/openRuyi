# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name parking_lot_core
%global full_version 0.8.6
%global pkgname parking-lot-core-0.8

Name:           rust-parking-lot-core-0.8
Version:        0.8.6
Release:        %autorelease
Summary:        Rust crate "parking_lot_core"
License:        Apache-2.0 OR MIT
URL:            https://github.com/Amanieu/parking_lot
#!RemoteAsset:  sha256:60a2cfe6f0ad2bfc16aefa463b497d5c7a5ecd44a23efa72aa342d90177356dc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(instant-0.1/default) >= 0.1.9
Requires:       crate(libc-0.2/default) >= 0.2.95
Requires:       crate(redox-syscall-0.2/default) >= 0.2.8
Requires:       crate(smallvec-1/default) >= 1.6.1
Requires:       crate(winapi-0.3/default) >= 0.3.9
Requires:       crate(winapi-0.3/errhandlingapi) >= 0.3.9
Requires:       crate(winapi-0.3/handleapi) >= 0.3.9
Requires:       crate(winapi-0.3/minwindef) >= 0.3.9
Requires:       crate(winapi-0.3/ntstatus) >= 0.3.9
Requires:       crate(winapi-0.3/winbase) >= 0.3.9
Requires:       crate(winapi-0.3/winerror) >= 0.3.9
Requires:       crate(winapi-0.3/winnt) >= 0.3.9

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "parking_lot_core"

%package     -n %{name}+backtrace
Summary:        Advanced API for creating custom synchronization primitives - feature "backtrace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(backtrace-0.3/default) >= 0.3.60
Provides:       crate(%{pkgname}/backtrace) = %{version}

%description -n %{name}+backtrace
This metapackage enables feature "backtrace" for the Rust parking_lot_core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deadlock-detection
Summary:        Advanced API for creating custom synchronization primitives - feature "deadlock_detection"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/backtrace) = %{version}
Requires:       crate(%{pkgname}/petgraph) = %{version}
Requires:       crate(%{pkgname}/thread-id) = %{version}
Provides:       crate(%{pkgname}/deadlock-detection) = %{version}

%description -n %{name}+deadlock-detection
This metapackage enables feature "deadlock_detection" for the Rust parking_lot_core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+petgraph
Summary:        Advanced API for creating custom synchronization primitives - feature "petgraph"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(petgraph-0.5/default) >= 0.5.1
Provides:       crate(%{pkgname}/petgraph) = %{version}

%description -n %{name}+petgraph
This metapackage enables feature "petgraph" for the Rust parking_lot_core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thread-id
Summary:        Advanced API for creating custom synchronization primitives - feature "thread-id"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(thread-id-4/default) >= 4.0.0
Provides:       crate(%{pkgname}/thread-id) = %{version}

%description -n %{name}+thread-id
This metapackage enables feature "thread-id" for the Rust parking_lot_core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
