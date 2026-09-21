# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-build-config
%global full_version 0.21.2
%global pkgname pyo3-build-config-0.21

Name:           rust-pyo3-build-config-0.21
Version:        0.21.2
Release:        %autorelease
Summary:        Rust crate "pyo3-build-config"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:7883df5835fafdad87c0d888b266c8ec0f4c9ca48a5bed6bbb592e8dedee1b50
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1/default) >= 1.0.0
Requires:       crate(target-lexicon-0.12) >= 0.12.0
Requires:       crate(target-lexicon-0.12/default) >= 0.12.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/abi3) = %{version}
Provides:       crate(%{pkgname}/abi3-py310) = %{version}
Provides:       crate(%{pkgname}/abi3-py311) = %{version}
Provides:       crate(%{pkgname}/abi3-py312) = %{version}
Provides:       crate(%{pkgname}/abi3-py37) = %{version}
Provides:       crate(%{pkgname}/abi3-py38) = %{version}
Provides:       crate(%{pkgname}/abi3-py39) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/extension-module) = %{version}
Provides:       crate(%{pkgname}/resolve-config) = %{version}

%description
Source code for takopackized Rust crate "pyo3-build-config"

%package     -n %{name}+python3-dll-a
Summary:        Build configuration for the PyO3 ecosystem - feature "python3-dll-a"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(python3-dll-a-0.2/default) >= 0.2.6
Provides:       crate(%{pkgname}/python3-dll-a) = %{version}

%description -n %{name}+python3-dll-a
This metapackage enables feature "python3-dll-a" for the Rust pyo3-build-config crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
