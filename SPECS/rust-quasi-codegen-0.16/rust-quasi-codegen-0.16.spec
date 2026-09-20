# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quasi_codegen
%global full_version 0.16.0
%global pkgname quasi-codegen-0.16

Name:           rust-quasi-codegen-0.16
Version:        0.16.0
Release:        %autorelease
Summary:        Rust crate "quasi_codegen"
License:        MIT OR Apache-2.0
URL:            https://github.com/serde-rs/quasi
#!RemoteAsset:  sha256:1a3856abd5ec12f873eeac0837cce65ac33814ed4acba287a9e806620763d4b7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aster-0.22) >= 0.22.1

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "quasi_codegen"

%package     -n %{name}+clippy
Summary:        Quasi-quoting macro system - feature "clippy" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clippy-0.0.302/default) >= 0.0.302
Provides:       crate(%{pkgname}/clippy) = %{version}
Provides:       crate(%{pkgname}/unstable-testing) = %{version}

%description -n %{name}+clippy
This metapackage enables feature "clippy" for the Rust quasi_codegen crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable-testing" feature.

%package     -n %{name}+syntex
Summary:        Quasi-quoting macro system - feature "syntex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntex-0.39/default) >= 0.39.0
Provides:       crate(%{pkgname}/syntex) = %{version}

%description -n %{name}+syntex
This metapackage enables feature "syntex" for the Rust quasi_codegen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syntex-errors
Summary:        Quasi-quoting macro system - feature "syntex_errors"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntex-errors-0.39/default) >= 0.39.0
Provides:       crate(%{pkgname}/syntex-errors) = %{version}

%description -n %{name}+syntex-errors
This metapackage enables feature "syntex_errors" for the Rust quasi_codegen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syntex-syntax
Summary:        Quasi-quoting macro system - feature "syntex_syntax"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntex-syntax-0.39/default) >= 0.39.0
Provides:       crate(%{pkgname}/syntex-syntax) = %{version}

%description -n %{name}+syntex-syntax
This metapackage enables feature "syntex_syntax" for the Rust quasi_codegen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-syntex
Summary:        Quasi-quoting macro system - feature "with-syntex" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/syntex) = %{version}
Requires:       crate(%{pkgname}/syntex-errors) = %{version}
Requires:       crate(%{pkgname}/syntex-syntax) = %{version}
Requires:       crate(aster-0.22/with-syntex) >= 0.22.1
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/with-syntex) = %{version}

%description -n %{name}+with-syntex
This metapackage enables feature "with-syntex" for the Rust quasi_codegen crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
