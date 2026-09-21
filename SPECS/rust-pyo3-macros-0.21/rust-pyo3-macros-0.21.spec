# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-macros
%global full_version 0.21.2
%global pkgname pyo3-macros-0.21

Name:           rust-pyo3-macros-0.21
Version:        0.21.2
Release:        %autorelease
Summary:        Rust crate "pyo3-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:77b34069fc0682e11b31dbd10321cbf94808394c56fd996796ce45217dfac53c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1) >= 1.0.0
Requires:       crate(pyo3-macros-backend-0.21/default) >= 0.21.2
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/experimental-declarative-modules) = %{version}
Provides:       crate(%{pkgname}/multiple-pymethods) = %{version}

%description
Source code for takopackized Rust crate "pyo3-macros"

%package     -n %{name}+experimental-async
Summary:        Proc macros for PyO3 package - feature "experimental-async"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-macros-backend-0.21/experimental-async) >= 0.21.2
Provides:       crate(%{pkgname}/experimental-async) = %{version}

%description -n %{name}+experimental-async
This metapackage enables feature "experimental-async" for the Rust pyo3-macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
