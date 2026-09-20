# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name enum-ordinalize
%global full_version 4.3.2
%global pkgname enum-ordinalize-4

Name:           rust-enum-ordinalize-4
Version:        4.3.2
Release:        %autorelease
Summary:        Rust crate "enum-ordinalize"
License:        MIT
URL:            https://magiclen.org/enum-ordinalize
#!RemoteAsset:  sha256:4a1091a7bb1f8f2c4b28f1fe2cef4980ca2d410a3d727d67ecc3178c9b0800f0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/nightly-test) = %{version}

%description
Source code for takopackized Rust crate "enum-ordinalize"

%package     -n %{name}+default
Summary:        This library enables enums to not only obtain the ordinal values of their variants but also allows for the construction of enums from an ordinal value - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/traits) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust enum-ordinalize crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        This library enables enums to not only obtain the ordinal values of their variants but also allows for the construction of enums from an ordinal value - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(enum-ordinalize-derive-4) >= 4.3.2
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust enum-ordinalize crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+traits
Summary:        This library enables enums to not only obtain the ordinal values of their variants but also allows for the construction of enums from an ordinal value - feature "traits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(enum-ordinalize-derive-4/traits) >= 4.3.2
Provides:       crate(%{pkgname}/traits) = %{version}

%description -n %{name}+traits
This metapackage enables feature "traits" for the Rust enum-ordinalize crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
