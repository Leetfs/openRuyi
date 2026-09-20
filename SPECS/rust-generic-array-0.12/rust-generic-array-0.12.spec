# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name generic-array
%global full_version 0.12.0
%global pkgname generic-array-0.12

Name:           rust-generic-array-0.12
Version:        0.12.0
Release:        %autorelease
Summary:        Rust crate "generic-array"
License:        MIT
URL:            https://github.com/fizyk20/generic-array.git
#!RemoteAsset:  sha256:3c0f28c2f5bfb5960175af447a2da7c18900693738343dc896ffbcabd9839592
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(typenum-1/default) >= 1.10.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "generic-array"

%package     -n %{name}+serde
Summary:        Generic types implementing functionality of arrays - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
