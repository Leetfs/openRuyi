# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pythonize
%global full_version 0.28.0
%global pkgname pythonize-0.28

Name:           rust-pythonize-0.28
Version:        0.28.0
Release:        %autorelease
Summary:        Rust crate "pythonize"
License:        MIT
URL:            https://github.com/davidhewitt/pythonize
#!RemoteAsset:  sha256:0b79f670c9626c8b651c0581011b57b6ba6970bb69faf01a7c4c0cfc81c43f95
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pyo3-0.28) >= 0.28.3
Requires:       crate(serde-1/std) >= 1.0.228

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pythonize"

%package     -n %{name}+arbitrary-precision
Summary:        Serde Serializer & Deserializer from Rust <--> Python, backed by PyO3 - feature "arbitrary_precision"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Requires:       crate(serde-json-1/arbitrary-precision) >= 1.0.149
Requires:       crate(serde-json-1/std) >= 1.0.149
Provides:       crate(%{pkgname}/arbitrary-precision) = %{version}

%description -n %{name}+arbitrary-precision
This metapackage enables feature "arbitrary_precision" for the Rust pythonize crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Serde Serializer & Deserializer from Rust <--> Python, backed by PyO3 - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/std) >= 1.0.149
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust pythonize crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
