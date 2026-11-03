# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jiter
%global full_version 0.18.0
%global pkgname jiter-0.18

Name:           rust-jiter-0.18
Version:        0.18.0
Release:        %autorelease
Summary:        Rust crate "jiter"
License:        MIT
URL:            https://github.com/pydantic/jiter/
#!RemoteAsset:  sha256:49e31424b61d85292bd805dbf643c3ccc44f5f3871fb751209b889ee70585029
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitvec-1/default) >= 1.0.1
Requires:       crate(lexical-parse-float-1/default) >= 1.0.5
Requires:       crate(lexical-parse-float-1/format) >= 1.0.5
Requires:       crate(num-traits-0.2/default) >= 0.2.16
Requires:       crate(smallvec-1/const-new) >= 1.11.0
Requires:       crate(smallvec-1/default) >= 1.11.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "jiter"

%package     -n %{name}+num-bigint
Summary:        Fast Iterable JSON parser - feature "num-bigint" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.4/default) >= 0.4.4
Requires:       crate(pyo3-0.30/num-bigint) >= 0.30.1
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/num-bigint) = %{version}

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust jiter crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+python
Summary:        Fast Iterable JSON parser - feature "python"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ahash-0.8/default) >= 0.8.0
Requires:       crate(pyo3-0.30/default) >= 0.30.1
Requires:       crate(pyo3-build-config-0.30/default) >= 0.30.1
Provides:       crate(%{pkgname}/python) = %{version}

%description -n %{name}+python
This metapackage enables feature "python" for the Rust jiter crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Fast Iterable JSON parser - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.147
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust jiter crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
