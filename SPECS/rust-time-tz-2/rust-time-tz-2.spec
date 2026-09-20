# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name time-tz
%global full_version 2.0.0
%global pkgname time-tz-2

Name:           rust-time-tz-2
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "time-tz"
License:        BSD-3-Clause
URL:            https://github.com/Yuri6037/time-tz
#!RemoteAsset:  sha256:733bc522e97980eb421cbf381160ff225bd14262a48a739110f6653c6258d625
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(parse-zoneinfo-0.3) >= 0.3.0
Requires:       crate(phf-0.11/default) >= 0.11.1
Requires:       crate(phf-codegen-0.11) >= 0.11.1
Requires:       crate(serde-1) >= 1.0.136
Requires:       crate(serde-1/derive) >= 1.0.136
Requires:       crate(serde-xml-rs-0.5) >= 0.5.1
Requires:       crate(time-0.3/default) >= 0.3.7
Requires:       crate(time-0.3/macros) >= 0.3.7
Requires:       crate(time-0.3/wasm-bindgen) >= 0.3.7
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.87

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/db) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "time-tz"

%package     -n %{name}+js-sys
Summary:        Tz database (IANA) for the time Rust crate - feature "js-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(js-sys-0.3/default) >= 0.3.64
Provides:       crate(%{pkgname}/js-sys) = %{version}

%description -n %{name}+js-sys
This metapackage enables feature "js-sys" for the Rust time-tz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nom
Summary:        Tz database (IANA) for the time Rust crate - feature "nom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nom-7/default) >= 7.1.0
Provides:       crate(%{pkgname}/nom) = %{version}

%description -n %{name}+nom
This metapackage enables feature "nom" for the Rust time-tz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+posix-tz
Summary:        Tz database (IANA) for the time Rust crate - feature "posix-tz"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/db) = %{version}
Requires:       crate(%{pkgname}/nom) = %{version}
Requires:       crate(%{pkgname}/thiserror) = %{version}
Provides:       crate(%{pkgname}/posix-tz) = %{version}

%description -n %{name}+posix-tz
This metapackage enables feature "posix-tz" for the Rust time-tz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+system
Summary:        Tz database (IANA) for the time Rust crate - feature "system"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/db) = %{version}
Requires:       crate(%{pkgname}/js-sys) = %{version}
Requires:       crate(%{pkgname}/thiserror) = %{version}
Requires:       crate(%{pkgname}/windows-sys) = %{version}
Provides:       crate(%{pkgname}/system) = %{version}

%description -n %{name}+system
This metapackage enables feature "system" for the Rust time-tz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thiserror
Summary:        Tz database (IANA) for the time Rust crate - feature "thiserror"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(thiserror-1/default) >= 1.0.30
Provides:       crate(%{pkgname}/thiserror) = %{version}

%description -n %{name}+thiserror
This metapackage enables feature "thiserror" for the Rust time-tz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+windows-sys
Summary:        Tz database (IANA) for the time Rust crate - feature "windows-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-sys-0.32/default) >= 0.32.0
Requires:       crate(windows-sys-0.32/win32-foundation) >= 0.32.0
Requires:       crate(windows-sys-0.32/win32-system-time) >= 0.32.0
Provides:       crate(%{pkgname}/windows-sys) = %{version}

%description -n %{name}+windows-sys
This metapackage enables feature "windows-sys" for the Rust time-tz crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
