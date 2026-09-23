# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name win_uds
%global full_version 0.2.2
%global pkgname win-uds-0.2

Name:           rust-win-uds-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "win_uds"
License:        Unlicense
URL:            https://github.com/kouhe3/win_uds
#!RemoteAsset:  sha256:7dd30a1a28a3799479cbf4e17284a220ea9ff6bad098a9d0224543a5d1efe1da
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(socket2-0.6/default) >= 0.6.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "win_uds"

%package     -n %{name}+async
Summary:        Windows Unix Domain Socket - feature "async"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-io-2/default) >= 2.6.0
Requires:       crate(futures-io-0.3/default) >= 0.3.32
Provides:       crate(%{pkgname}/async) = %{version}

%description -n %{name}+async
This metapackage enables feature "async" for the Rust win_uds crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
