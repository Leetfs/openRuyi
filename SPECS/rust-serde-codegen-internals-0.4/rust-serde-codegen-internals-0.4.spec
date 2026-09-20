# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_codegen_internals
%global full_version 0.4.0
%global pkgname serde-codegen-internals-0.4

Name:           rust-serde-codegen-internals-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "serde_codegen_internals"
License:        MIT OR Apache-2.0
URL:            https://github.com/serde-rs/serde
#!RemoteAsset:  sha256:eed6f11ba7400225025b44c77b4eca1655958aac6c586c5ec9c76fd5597ef849
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Unstable.
Source code for takopackized Rust crate "serde_codegen_internals"

%package     -n %{name}+clippy
Summary:        AST representation used by Serde codegen - feature "clippy" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clippy-0.0.302/default) >= 0.0.302
Provides:       crate(%{pkgname}/clippy) = %{version}
Provides:       crate(%{pkgname}/nightly-testing) = %{version}

%description -n %{name}+clippy
Unstable.
This metapackage enables feature "clippy" for the Rust serde_codegen_internals crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "nightly-testing" feature.

%package     -n %{name}+syntex-errors
Summary:        AST representation used by Serde codegen - feature "syntex_errors"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntex-errors-0.39/default) >= 0.39.0
Provides:       crate(%{pkgname}/syntex-errors) = %{version}

%description -n %{name}+syntex-errors
Unstable.
This metapackage enables feature "syntex_errors" for the Rust serde_codegen_internals crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syntex-syntax
Summary:        AST representation used by Serde codegen - feature "syntex_syntax"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntex-syntax-0.39/default) >= 0.39.0
Provides:       crate(%{pkgname}/syntex-syntax) = %{version}

%description -n %{name}+syntex-syntax
Unstable.
This metapackage enables feature "syntex_syntax" for the Rust serde_codegen_internals crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-syntex
Summary:        AST representation used by Serde codegen - feature "with-syntex" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/syntex-errors) = %{version}
Requires:       crate(%{pkgname}/syntex-syntax) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/with-syntex) = %{version}

%description -n %{name}+with-syntex
Unstable.
This metapackage enables feature "with-syntex" for the Rust serde_codegen_internals crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
