# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aster
%global full_version 0.22.1
%global pkgname aster-0.22

Name:           rust-aster-0.22
Version:        0.22.1
Release:        %autorelease
Summary:        Rust crate "aster"
License:        MIT OR Apache-2.0
URL:            https://github.com/serde-rs/aster
#!RemoteAsset:  sha256:3c2e21e476ef6522e1762461ddbd1eba4d049c9a86619ccd03226b09f3d0741e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "aster"

%package     -n %{name}+clippy
Summary:        Libsyntax ast builder - feature "clippy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clippy-0.0.302/default) >= 0.0.302
Provides:       crate(%{pkgname}/clippy) = %{version}

%description -n %{name}+clippy
This metapackage enables feature "clippy" for the Rust aster crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compiletest-rs
Summary:        Libsyntax ast builder - feature "compiletest_rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(compiletest-rs-0.2/default) >= 0.2.10
Provides:       crate(%{pkgname}/compiletest-rs) = %{version}

%description -n %{name}+compiletest-rs
This metapackage enables feature "compiletest_rs" for the Rust aster crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syntex-syntax
Summary:        Libsyntax ast builder - feature "syntex_syntax" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntex-syntax-0.39/default) >= 0.39.0
Provides:       crate(%{pkgname}/syntex-syntax) = %{version}
Provides:       crate(%{pkgname}/with-syntex) = %{version}

%description -n %{name}+syntex-syntax
This metapackage enables feature "syntex_syntax" for the Rust aster crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-syntex" feature.

%package     -n %{name}+unstable-testing
Summary:        Libsyntax ast builder - feature "unstable-testing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clippy) = %{version}
Requires:       crate(%{pkgname}/compiletest-rs) = %{version}
Provides:       crate(%{pkgname}/unstable-testing) = %{version}

%description -n %{name}+unstable-testing
This metapackage enables feature "unstable-testing" for the Rust aster crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
