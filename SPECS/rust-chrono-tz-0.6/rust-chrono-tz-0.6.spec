# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name chrono-tz
%global full_version 0.6.3
%global pkgname chrono-tz-0.6

Name:           rust-chrono-tz-0.6
Version:        0.6.3
Release:        %autorelease
Summary:        Rust crate "chrono-tz"
License:        MIT OR Apache-2.0
URL:            https://github.com/chronotope/chrono-tz
#!RemoteAsset:  sha256:29c39203181991a7dd4343b8005bd804e7a9a37afb8ac070e43771e8c820bbde
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(chrono-0.4) >= 0.4.0
Requires:       crate(chrono-tz-build-0.0.3) >= 0.0.3
Requires:       crate(phf-0.11/uncased) >= 0.11.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "chrono-tz"

%package     -n %{name}+case-insensitive
Summary:        TimeZone implementations for rust-chrono from the IANA database - feature "case-insensitive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/uncased) = %{version}
Requires:       crate(chrono-tz-build-0.0.3) >= 0.0.3
Requires:       crate(chrono-tz-build-0.0.3/case-insensitive) >= 0.0.3
Provides:       crate(%{pkgname}/case-insensitive) = %{version}

%description -n %{name}+case-insensitive
This metapackage enables feature "case-insensitive" for the Rust chrono-tz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+filter-by-regex
Summary:        TimeZone implementations for rust-chrono from the IANA database - feature "filter-by-regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-tz-build-0.0.3) >= 0.0.3
Requires:       crate(chrono-tz-build-0.0.3/filter-by-regex) >= 0.0.3
Provides:       crate(%{pkgname}/filter-by-regex) = %{version}

%description -n %{name}+filter-by-regex
This metapackage enables feature "filter-by-regex" for the Rust chrono-tz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        TimeZone implementations for rust-chrono from the IANA database - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust chrono-tz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uncased
Summary:        TimeZone implementations for rust-chrono from the IANA database - feature "uncased"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uncased-0.9) >= 0.9.0
Provides:       crate(%{pkgname}/uncased) = %{version}

%description -n %{name}+uncased
This metapackage enables feature "uncased" for the Rust chrono-tz crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
