# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name chrono-tz-build
%global full_version 0.0.3
%global pkgname chrono-tz-build-0.0.3

Name:           rust-chrono-tz-build-0.0.3
Version:        0.0.3
Release:        %autorelease
Summary:        Rust crate "chrono-tz-build"
License:        MIT OR Apache-2.0
URL:            FIXME
#!RemoteAsset:  sha256:6f509c3a87b33437b05e2458750a0700e5bdd6956176773e6c7d6dd15a283a0c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(parse-zoneinfo-0.3/default) >= 0.3.0
Requires:       crate(phf-0.11/uncased) >= 0.11.0
Requires:       crate(phf-codegen-0.11) >= 0.11.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "chrono-tz-build"

%package     -n %{name}+regex
Summary:        Internal build script for chrono-tz - feature "regex" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1) >= 1.0.0
Provides:       crate(%{pkgname}/filter-by-regex) = %{version}
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust chrono-tz-build crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "filter-by-regex" feature.

%package     -n %{name}+uncased
Summary:        Internal build script for chrono-tz - feature "uncased" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uncased-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/case-insensitive) = %{version}
Provides:       crate(%{pkgname}/uncased) = %{version}

%description -n %{name}+uncased
This metapackage enables feature "uncased" for the Rust chrono-tz-build crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "case-insensitive" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
