# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ptr_meta
%global full_version 0.3.2
%global pkgname ptr-meta-0.3

Name:           rust-ptr-meta-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "ptr_meta"
License:        MIT
URL:            https://github.com/rkyv/ptr_meta
#!RemoteAsset:  sha256:743da816b98c921cdbe8628ef7381b76f25ecf4da599fc80aca90eae7ef70cc0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "ptr_meta"

%package     -n %{name}+default
Summary:        Radioactive stabilization of the ptr_meta rfc - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ptr_meta crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ptr-meta-derive
Summary:        Radioactive stabilization of the ptr_meta rfc - feature "ptr_meta_derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ptr-meta-derive-0.3) >= 0.3.2
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/ptr-meta-derive) = %{version}

%description -n %{name}+ptr-meta-derive
This metapackage enables feature "ptr_meta_derive" for the Rust ptr_meta crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
