# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sdd
%global full_version 4.7.3
%global pkgname sdd-4

Name:           rust-sdd-4
Version:        4.7.3
Release:        %autorelease
Summary:        Rust crate "sdd"
License:        Apache-2.0
URL:            https://codeberg.org/wvwwvwwv/scalable-delayed-dealloc
#!RemoteAsset:  sha256:b21a75f5913ab130e4b369fb8693be25f29b983e2ecad4279df9bfa5dd8aaf3e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sdd"

%package     -n %{name}+loom
Summary:        Scalable lock-free delayed memory reclaimer - feature "loom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(loom-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/loom) = %{version}

%description -n %{name}+loom
This metapackage enables feature "loom" for the Rust sdd crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
