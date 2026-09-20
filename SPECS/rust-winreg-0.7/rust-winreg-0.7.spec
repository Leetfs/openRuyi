# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name winreg
%global full_version 0.7.0
%global pkgname winreg-0.7

Name:           rust-winreg-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "winreg"
License:        MIT
URL:            https://github.com/gentoo90/winreg-rs
#!RemoteAsset:  sha256:0120db82e8a1e0b9fb3345a539c478767c0048d842860994d96113d5b667bd69
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/handleapi) >= 0.3.0
Requires:       crate(winapi-0.3/impl-debug) >= 0.3.0
Requires:       crate(winapi-0.3/impl-default) >= 0.3.0
Requires:       crate(winapi-0.3/minwinbase) >= 0.3.0
Requires:       crate(winapi-0.3/minwindef) >= 0.3.0
Requires:       crate(winapi-0.3/timezoneapi) >= 0.3.0
Requires:       crate(winapi-0.3/winerror) >= 0.3.0
Requires:       crate(winapi-0.3/winnt) >= 0.3.0
Requires:       crate(winapi-0.3/winreg) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "winreg"

%package     -n %{name}+chrono
Summary:        Rust bindings to MS Windows Registry API - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/default) >= 0.4.6
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust winreg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Rust bindings to MS Windows Registry API - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust winreg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serialization-serde
Summary:        Rust bindings to MS Windows Registry API - feature "serialization-serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/transactions) = %{version}
Provides:       crate(%{pkgname}/serialization-serde) = %{version}

%description -n %{name}+serialization-serde
This metapackage enables feature "serialization-serde" for the Rust winreg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+transactions
Summary:        Rust bindings to MS Windows Registry API - feature "transactions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(winapi-0.3/handleapi) >= 0.3.0
Requires:       crate(winapi-0.3/impl-debug) >= 0.3.0
Requires:       crate(winapi-0.3/impl-default) >= 0.3.0
Requires:       crate(winapi-0.3/ktmw32) >= 0.3.0
Requires:       crate(winapi-0.3/minwinbase) >= 0.3.0
Requires:       crate(winapi-0.3/minwindef) >= 0.3.0
Requires:       crate(winapi-0.3/timezoneapi) >= 0.3.0
Requires:       crate(winapi-0.3/winerror) >= 0.3.0
Requires:       crate(winapi-0.3/winnt) >= 0.3.0
Requires:       crate(winapi-0.3/winreg) >= 0.3.0
Provides:       crate(%{pkgname}/transactions) = %{version}

%description -n %{name}+transactions
This metapackage enables feature "transactions" for the Rust winreg crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
