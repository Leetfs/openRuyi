# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name protox
%global full_version 0.9.1
%global pkgname protox-0.9

Name:           rust-protox-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "protox"
License:        MIT OR Apache-2.0
URL:            https://github.com/andrewhickman/protox
#!RemoteAsset:  sha256:4f25a07a73c6717f0b9bbbd685918f5df9815f7efba450b83d9c9dea41f0e3a1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.12.0
Requires:       crate(miette-7/default) >= 7.6.0
Requires:       crate(prost-0.14/default) >= 0.14.3
Requires:       crate(prost-reflect-0.16/default) >= 0.16.5
Requires:       crate(prost-reflect-0.16/miette) >= 0.16.5
Requires:       crate(prost-reflect-0.16/text-format) >= 0.16.5
Requires:       crate(prost-types-0.14/default) >= 0.14.3
Requires:       crate(protox-parse-0.9/default) >= 0.9.0
Requires:       crate(thiserror-2/default) >= 2.0.18

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "protox"

%package     -n %{name}+bin
Summary:        The protobuf compiler - feature "bin"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/default) >= 4.5.4
Requires:       crate(clap-4/derive) >= 4.5.4
Requires:       crate(miette-7/fancy) >= 7.6.0
Provides:       crate(%{pkgname}/bin) = %{version}

%description -n %{name}+bin
This metapackage enables feature "bin" for the Rust protox crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
