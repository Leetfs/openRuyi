# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uv-small-str
%global full_version 0.0.96
%global pkgname uv-small-str-0.0.96

Name:           rust-uv-small-str-0.0.96
Version:        0.0.96
Release:        %autorelease
Summary:        Rust crate "uv-small-str"
License:        MIT OR Apache-2.0
URL:            https://pypi.org/project/uv/
#!RemoteAsset:  sha256:0038dae6f914c8e8c5c0dbf56f8db9eead510dae668bd3d70f0d4acfef2f4e61
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arcstr-1) >= 1.2.0
Requires:       crate(rkyv-0.8/bytecheck) >= 0.8.14
Requires:       crate(rkyv-0.8/std) >= 0.8.14
Requires:       crate(serde-1/derive) >= 1.0.210
Requires:       crate(serde-1/rc) >= 1.0.210
Requires:       crate(serde-1/std) >= 1.0.210

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "uv-small-str"

%package     -n %{name}+schemars
Summary:        Internal component crate of uv - feature "schemars"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(schemars-1/derive) >= 1.0.0
Requires:       crate(schemars-1/std) >= 1.0.0
Requires:       crate(schemars-1/url2) >= 1.0.0
Provides:       crate(%{pkgname}/schemars) = %{version}

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust uv-small-str crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
