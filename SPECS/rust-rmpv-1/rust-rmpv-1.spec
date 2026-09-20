# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rmpv
%global full_version 1.3.1
%global pkgname rmpv-1

Name:           rust-rmpv-1
Version:        1.3.1
Release:        %autorelease
Summary:        Rust crate "rmpv"
License:        MIT
URL:            https://github.com/3Hren/msgpack-rust
#!RemoteAsset:  sha256:7a4e1d4b9b938a26d2996af33229f0ca0956c652c1375067f0b45291c1df8417
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rmp-0.8/default) >= 0.8.15

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rmpv"

%package     -n %{name}+serde
Summary:        Decoding/Encoding MessagePack values without schema - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.228
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rmpv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-bytes
Summary:        Decoding/Encoding MessagePack values without schema - feature "serde_bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-bytes-0.11/default) >= 0.11.19
Provides:       crate(%{pkgname}/serde-bytes) = %{version}

%description -n %{name}+serde-bytes
This metapackage enables feature "serde_bytes" for the Rust rmpv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-serde
Summary:        Decoding/Encoding MessagePack values without schema - feature "with-serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-bytes) = %{version}
Provides:       crate(%{pkgname}/with-serde) = %{version}

%description -n %{name}+with-serde
This metapackage enables feature "with-serde" for the Rust rmpv crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
