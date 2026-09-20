# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_codegen
%global full_version 0.7.15
%global pkgname serde-codegen-0.7

Name:           rust-serde-codegen-0.7
Version:        0.7.15
Release:        %autorelease
Summary:        Rust crate "serde_codegen"
License:        MIT OR Apache-2.0
URL:            https://github.com/serde-rs/serde
#!RemoteAsset:  sha256:973836af70870533bc6a332488ded6aef80a5ff507b663e8b4e1ef44580ea8fd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aster-0.22) >= 0.22.1
Requires:       crate(quasi-0.16) >= 0.16.0
Requires:       crate(serde-codegen-internals-0.4) >= 0.4.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "serde_codegen"

%package     -n %{name}+clippy
Summary:        Macros to auto-generate implementations for the serde framework - feature "clippy" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clippy-0.0.302/default) >= 0.0.302
Provides:       crate(%{pkgname}/clippy) = %{version}
Provides:       crate(%{pkgname}/nightly-testing) = %{version}

%description -n %{name}+clippy
This metapackage enables feature "clippy" for the Rust serde_codegen crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "nightly-testing" feature.

%package     -n %{name}+quasi-codegen
Summary:        Macros to auto-generate implementations for the serde framework - feature "quasi_codegen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quasi-codegen-0.16/default) >= 0.16.0
Provides:       crate(%{pkgname}/quasi-codegen) = %{version}

%description -n %{name}+quasi-codegen
This metapackage enables feature "quasi_codegen" for the Rust serde_codegen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quasi-macros
Summary:        Macros to auto-generate implementations for the serde framework - feature "quasi_macros" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quasi-macros-0.16/default) >= 0.16.0
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/quasi-macros) = %{version}

%description -n %{name}+quasi-macros
This metapackage enables feature "quasi_macros" for the Rust serde_codegen crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "nightly" feature.

%package     -n %{name}+syntex
Summary:        Macros to auto-generate implementations for the serde framework - feature "syntex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntex-0.39/default) >= 0.39.0
Provides:       crate(%{pkgname}/syntex) = %{version}

%description -n %{name}+syntex
This metapackage enables feature "syntex" for the Rust serde_codegen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syntex-syntax
Summary:        Macros to auto-generate implementations for the serde framework - feature "syntex_syntax"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntex-syntax-0.39/default) >= 0.39.0
Provides:       crate(%{pkgname}/syntex-syntax) = %{version}

%description -n %{name}+syntex-syntax
This metapackage enables feature "syntex_syntax" for the Rust serde_codegen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-syntex
Summary:        Macros to auto-generate implementations for the serde framework - feature "with-syntex" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/quasi-codegen) = %{version}
Requires:       crate(%{pkgname}/syntex) = %{version}
Requires:       crate(%{pkgname}/syntex-syntax) = %{version}
Requires:       crate(quasi-0.16/with-syntex) >= 0.16.0
Requires:       crate(quasi-codegen-0.16/with-syntex) >= 0.16.0
Requires:       crate(serde-codegen-internals-0.4/with-syntex) >= 0.4.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/with-syntex) = %{version}

%description -n %{name}+with-syntex
This metapackage enables feature "with-syntex" for the Rust serde_codegen crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
