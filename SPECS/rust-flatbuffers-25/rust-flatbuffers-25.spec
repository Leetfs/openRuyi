# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name flatbuffers
%global full_version 25.12.19
%global pkgname flatbuffers-25

Name:           rust-flatbuffers-25
Version:        25.12.19
Release:        %autorelease
Summary:        Rust crate "flatbuffers"
License:        Apache-2.0
URL:            https://google.github.io/flatbuffers/
#!RemoteAsset:  sha256:35f6839d7b3b98adde531effaf34f0c2badc6f4735d26fe74709d8e513a96ef3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.8.0
Requires:       crate(rustc-version-0.4) >= 0.4.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "flatbuffers"

%package     -n %{name}+serde
Summary:        Official FlatBuffers Rust runtime library - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serialize) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust flatbuffers crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serialize" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
