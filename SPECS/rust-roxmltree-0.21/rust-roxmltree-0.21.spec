# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name roxmltree
%global full_version 0.21.1
%global pkgname roxmltree-0.21

Name:           rust-roxmltree-0.21
Version:        0.21.1
Release:        %autorelease
Summary:        Rust crate "roxmltree"
License:        MIT OR Apache-2.0
URL:            https://github.com/RazrFalcon/roxmltree
#!RemoteAsset:  sha256:f1964b10c76125c36f8afe190065a4bf9a87bf324842c05701330bba9f1cacbb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/positions) = %{version}

%description
Source code for takopackized Rust crate "roxmltree"

%package     -n %{name}+default
Summary:        Represent an XML as a read-only tree - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/positions) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust roxmltree crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Represent an XML as a read-only tree - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memchr-2/std) >= 2.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust roxmltree crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
