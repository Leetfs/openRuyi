# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cap-std
%global full_version 4.0.3
%global pkgname cap-std-4

Name:           rust-cap-std-4
Version:        4.0.3
Release:        %autorelease
Summary:        Rust crate "cap-std"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/cap-std
#!RemoteAsset:  sha256:c1ec78e242cfa2cfe276807ac2ecc00315a6c97786977414bcd1c3963b6c91b8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cap-primitives-4/default) >= 4.0.3
Requires:       crate(io-extras-0.19/default) >= 0.19.0
Requires:       crate(io-lifetimes-3) >= 3.0.1
Requires:       crate(rustix-1/default) >= 1.0.0
Requires:       crate(rustix-1/fs) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cap-std"

%package     -n %{name}+arf-strings
Summary:        Capability-based version of the Rust standard library - feature "arf_strings"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fs-utf8) = %{version}
Requires:       crate(arf-strings-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/arf-strings) = %{version}

%description -n %{name}+arf-strings
This metapackage enables feature "arf_strings" for the Rust cap-std crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+camino
Summary:        Capability-based version of the Rust standard library - feature "camino" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(camino-1/default) >= 1.0.5
Provides:       crate(%{pkgname}/camino) = %{version}
Provides:       crate(%{pkgname}/fs-utf8) = %{version}

%description -n %{name}+camino
This metapackage enables feature "camino" for the Rust cap-std crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "fs_utf8" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
