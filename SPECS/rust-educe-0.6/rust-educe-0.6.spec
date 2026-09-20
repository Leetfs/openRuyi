# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name educe
%global full_version 0.6.0
%global pkgname educe-0.6

Name:           rust-educe-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "educe"
License:        MIT
URL:            https://magiclen.org/educe
#!RemoteAsset:  sha256:1d7bc049e1bd8cdeb31b68bbd586a9464ecf9f3944af3958a7a9d0f8b9799417
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(enum-ordinalize-4/derive) >= 4.3.2
Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/default) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/clone) = %{version}
Provides:       crate(%{pkgname}/copy) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/deref) = %{version}
Provides:       crate(%{pkgname}/derefmut) = %{version}
Provides:       crate(%{pkgname}/eq) = %{version}
Provides:       crate(%{pkgname}/hash) = %{version}
Provides:       crate(%{pkgname}/into) = %{version}
Provides:       crate(%{pkgname}/ord) = %{version}
Provides:       crate(%{pkgname}/partialeq) = %{version}
Provides:       crate(%{pkgname}/partialord) = %{version}

%description
Source code for takopackized Rust crate "educe"

%package     -n %{name}+default
Summary:        This crate offers procedural macros designed to facilitate the swift implementation of Rust's built-in traits - feature "Default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clone) = %{version}
Requires:       crate(%{pkgname}/copy) = %{version}
Requires:       crate(%{pkgname}/debug) = %{version}
Requires:       crate(%{pkgname}/deref) = %{version}
Requires:       crate(%{pkgname}/derefmut) = %{version}
Requires:       crate(%{pkgname}/eq) = %{version}
Requires:       crate(%{pkgname}/hash) = %{version}
Requires:       crate(%{pkgname}/into) = %{version}
Requires:       crate(%{pkgname}/ord) = %{version}
Requires:       crate(%{pkgname}/partialeq) = %{version}
Requires:       crate(%{pkgname}/partialord) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "Default" for the Rust educe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        This crate offers procedural macros designed to facilitate the swift implementation of Rust's built-in traits - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-2/full) >= 2.0.117
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust educe crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
