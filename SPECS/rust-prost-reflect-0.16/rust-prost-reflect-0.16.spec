# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prost-reflect
%global full_version 0.16.5
%global pkgname prost-reflect-0.16

Name:           rust-prost-reflect-0.16
Version:        0.16.5
Release:        %autorelease
Summary:        Rust crate "prost-reflect"
License:        MIT OR Apache-2.0
URL:            https://github.com/andrewhickman/prost-reflect
#!RemoteAsset:  sha256:01b80ea363c31af2de2b92e3c07ed1156628f7838c4afb4df75ee78a37fedbd1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(prost-0.14/default) >= 0.14.3
Requires:       crate(prost-types-0.14/default) >= 0.14.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "prost-reflect"

%package     -n %{name}+derive
Summary:        Protobuf library extending prost with reflection support and dynamic messages - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prost-reflect-derive-0.16/default) >= 0.16.1
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust prost-reflect crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+miette
Summary:        Protobuf library extending prost with reflection support and dynamic messages - feature "miette"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(miette-7/default) >= 7.6.0
Provides:       crate(%{pkgname}/miette) = %{version}

%description -n %{name}+miette
This metapackage enables feature "miette" for the Rust prost-reflect crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Protobuf library extending prost with reflection support and dynamic messages - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64-0.22/default) >= 0.22.0
Requires:       crate(serde-1/default) >= 1.0.132
Requires:       crate(serde-value-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust prost-reflect crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+text-format
Summary:        Protobuf library extending prost with reflection support and dynamic messages - feature "text-format"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(logos-0.16/default) >= 0.16.1
Provides:       crate(%{pkgname}/text-format) = %{version}

%description -n %{name}+text-format
This metapackage enables feature "text-format" for the Rust prost-reflect crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
