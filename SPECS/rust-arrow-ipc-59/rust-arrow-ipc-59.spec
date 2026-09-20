# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-ipc
%global full_version 59.2.0
%global pkgname arrow-ipc-59

Name:           rust-arrow-ipc-59
Version:        59.2.0
Release:        %autorelease
Summary:        Rust crate "arrow-ipc"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:149437b14371f5b9ec60f5ddc751483ae99d7a7072653c0075e5e469156eea7b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-array-59/default) >= 59.2.0
Requires:       crate(arrow-buffer-59/default) >= 59.2.0
Requires:       crate(arrow-data-59/default) >= 59.2.0
Requires:       crate(arrow-schema-59/default) >= 59.2.0
Requires:       crate(arrow-select-59/default) >= 59.2.0
Requires:       crate(flatbuffers-25) >= 25.2.10

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "arrow-ipc"

%package     -n %{name}+lz4-flex
Summary:        Support for the Arrow IPC format - feature "lz4_flex" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lz4-flex-0.14/frame) >= 0.14.0
Requires:       crate(lz4-flex-0.14/std) >= 0.14.0
Provides:       crate(%{pkgname}/lz4) = %{version}
Provides:       crate(%{pkgname}/lz4-flex) = %{version}

%description -n %{name}+lz4-flex
This metapackage enables feature "lz4_flex" for the Rust arrow-ipc crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "lz4" feature.

%package     -n %{name}+zstd
Summary:        Support for the Arrow IPC format - feature "zstd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-0.13) >= 0.13.0
Provides:       crate(%{pkgname}/zstd) = %{version}

%description -n %{name}+zstd
This metapackage enables feature "zstd" for the Rust arrow-ipc crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
