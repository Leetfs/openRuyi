# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unic-char-range
%global full_version 0.9.0
%global pkgname unic-char-range-0.9

Name:           rust-unic-char-range-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "unic-char-range"
License:        MIT OR Apache-2.0
URL:            https://github.com/open-i18n/rust-unic/
#!RemoteAsset:  sha256:0398022d5f700414f6b899e10b8348231abf9173fa93144cbc1a43b9793c1fbc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/exact-size-is-empty) = %{version}
Provides:       crate(%{pkgname}/fused) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/trusted-len) = %{version}

%description
Source code for takopackized Rust crate "unic-char-range"

%package     -n %{name}+rayon
Summary:        UNIC — Unicode Character Tools — Character Range and Iteration - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust unic-char-range crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable
Summary:        UNIC — Unicode Character Tools — Character Range and Iteration - feature "unstable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/exact-size-is-empty) = %{version}
Requires:       crate(%{pkgname}/fused) = %{version}
Requires:       crate(%{pkgname}/trusted-len) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description -n %{name}+unstable
This metapackage enables feature "unstable" for the Rust unic-char-range crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
