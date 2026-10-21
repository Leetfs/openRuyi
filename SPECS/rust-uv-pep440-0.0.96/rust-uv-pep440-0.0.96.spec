# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uv-pep440
%global full_version 0.0.96
%global pkgname uv-pep440-0.0.96

Name:           rust-uv-pep440-0.0.96
Version:        0.0.96
Release:        %autorelease
Summary:        Rust crate "uv-pep440"
License:        Apache-2.0 OR BSD-2-Clause
URL:            https://pypi.org/project/uv/
#!RemoteAsset:  sha256:f2dd9ee813b0a1605cd8b0df07383b5acc58d4f82c15832d1bffffe146eb2073
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1/derive) >= 1.0.210
Requires:       crate(serde-1/rc) >= 1.0.210
Requires:       crate(serde-1/std) >= 1.0.210
Requires:       crate(unicode-width-0.2) >= 0.2.0
Requires:       crate(unscanny-0.1) >= 0.1.0
Requires:       crate(uv-cache-key-0.0.96/default) >= 0.0.96

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}

%description
Source code for takopackized Rust crate "uv-pep440"

%package     -n %{name}+rkyv
Summary:        Internal component crate of uv - feature "rkyv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-0.8/bytecheck) >= 0.8.14
Requires:       crate(rkyv-0.8/std) >= 0.8.14
Provides:       crate(%{pkgname}/rkyv) = %{version}

%description -n %{name}+rkyv
This metapackage enables feature "rkyv" for the Rust uv-pep440 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Internal component crate of uv - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1/attributes) >= 0.1.40
Requires:       crate(tracing-0.1/std) >= 0.1.40
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust uv-pep440 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+version-ranges
Summary:        Internal component crate of uv - feature "version-ranges"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(astral-version-ranges-0.2) >= 0.2.2
Provides:       crate(%{pkgname}/version-ranges) = %{version}

%description -n %{name}+version-ranges
This metapackage enables feature "version-ranges" for the Rust uv-pep440 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
