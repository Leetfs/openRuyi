# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name geo-types
%global full_version 0.7.0
%global pkgname geo-types-0.7

Name:           rust-geo-types-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "geo-types"
License:        MIT OR Apache-2.0
URL:            https://github.com/georust/geo
#!RemoteAsset:  sha256:a6b362f0f09b4ff7ad8210f806f80ab6d0d895365a6830cb504267aeccfe3f43
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "geo-types"

%package     -n %{name}+approx
Summary:        Geospatial primitive data types - feature "approx"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(approx-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/approx) = %{version}

%description -n %{name}+approx
This metapackage enables feature "approx" for the Rust geo-types crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rstar
Summary:        Geospatial primitive data types - feature "rstar"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rstar-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/rstar) = %{version}

%description -n %{name}+rstar
This metapackage enables feature "rstar" for the Rust geo-types crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Geospatial primitive data types - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust geo-types crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-rstar
Summary:        Geospatial primitive data types - feature "use-rstar"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/approx) = %{version}
Requires:       crate(%{pkgname}/rstar) = %{version}
Provides:       crate(%{pkgname}/use-rstar) = %{version}

%description -n %{name}+use-rstar
This metapackage enables feature "use-rstar" for the Rust geo-types crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
