# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sha3
%global full_version 0.10.8
%global pkgname sha3-0.10

Name:           rust-sha3-0.10
Version:        0.10.8
Release:        %autorelease
Summary:        Rust crate "sha3"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/hashes
#!RemoteAsset:  sha256:75872d278a8f37ef87fa0ddbda7802605cb18344497949862c0d4dcb291eba60
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(digest-0.10/default) >= 0.10.4
Requires:       crate(keccak-0.1/default) >= 0.1.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/reset) = %{version}

%description
Source code for takopackized Rust crate "sha3"

%package     -n %{name}+asm
Summary:        Pure Rust implementation of SHA-3, a family of Keccak-based hash functions including the SHAKE family of eXtendable-Output Functions (XOFs), as well as the accelerated variant TurboSHAKE - feature "asm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(keccak-0.1/asm) >= 0.1.4
Provides:       crate(%{pkgname}/asm) = %{version}

%description -n %{name}+asm
This metapackage enables feature "asm" for the Rust sha3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+oid
Summary:        Pure Rust implementation of SHA-3, a family of Keccak-based hash functions including the SHAKE family of eXtendable-Output Functions (XOFs), as well as the accelerated variant TurboSHAKE - feature "oid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.10/oid) >= 0.10.4
Provides:       crate(%{pkgname}/oid) = %{version}

%description -n %{name}+oid
This metapackage enables feature "oid" for the Rust sha3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of SHA-3, a family of Keccak-based hash functions including the SHAKE family of eXtendable-Output Functions (XOFs), as well as the accelerated variant TurboSHAKE - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.10/std) >= 0.10.4
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust sha3 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
