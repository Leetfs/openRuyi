# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uv-redacted
%global full_version 0.0.96
%global pkgname uv-redacted-0.0.96

Name:           rust-uv-redacted-0.0.96
Version:        0.0.96
Release:        %autorelease
Summary:        Rust crate "uv-redacted"
License:        MIT OR Apache-2.0
URL:            https://pypi.org/project/uv/
#!RemoteAsset:  sha256:18de554c63e573a7ecd6f30c512c616c9844b7180325d5e3ce7f3a449eb6165c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ref-cast-1) >= 1.0.24
Requires:       crate(serde-1/derive) >= 1.0.210
Requires:       crate(serde-1/rc) >= 1.0.210
Requires:       crate(serde-1/std) >= 1.0.210
Requires:       crate(thiserror-2/std) >= 2.0.0
Requires:       crate(url-2/serde) >= 2.5.2
Requires:       crate(url-2/std) >= 2.5.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "uv-redacted"

%package     -n %{name}+schemars
Summary:        Internal component crate of uv - feature "schemars"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(schemars-1/derive) >= 1.0.0
Requires:       crate(schemars-1/std) >= 1.0.0
Requires:       crate(schemars-1/url2) >= 1.0.0
Provides:       crate(%{pkgname}/schemars) = %{version}

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust uv-redacted crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
