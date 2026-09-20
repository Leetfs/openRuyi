# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-data
%global full_version 59.3.0
%global pkgname arrow-data-59

Name:           rust-arrow-data-59
Version:        59.3.0
Release:        %autorelease
Summary:        Rust crate "arrow-data"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:9ba2f832eaeca24b8f26143dba750e42ee4ab51cf7d65e701ca9607cfda9f358
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-buffer-59/default) >= 59.3.0
Requires:       crate(arrow-schema-59/default) >= 59.3.0
Requires:       crate(half-2) >= 2.1.0
Requires:       crate(num-integer-0.1/std) >= 0.1.46
Requires:       crate(num-traits-0.2/std) >= 0.2.19

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/force-validate) = %{version}

%description
Source code for takopackized Rust crate "arrow-data"

%package     -n %{name}+ffi
Summary:        Array data abstractions for Apache Arrow - feature "ffi"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-schema-59/ffi) >= 59.3.0
Provides:       crate(%{pkgname}/ffi) = %{version}

%description -n %{name}+ffi
This metapackage enables feature "ffi" for the Rust arrow-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pool
Summary:        Array data abstractions for Apache Arrow - feature "pool"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-buffer-59/pool) >= 59.3.0
Provides:       crate(%{pkgname}/pool) = %{version}

%description -n %{name}+pool
This metapackage enables feature "pool" for the Rust arrow-data crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
