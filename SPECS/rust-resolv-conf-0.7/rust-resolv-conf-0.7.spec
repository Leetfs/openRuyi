# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name resolv-conf
%global full_version 0.7.0
%global pkgname resolv-conf-0.7

Name:           rust-resolv-conf-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "resolv-conf"
License:        MIT OR Apache-2.0
URL:            http://github.com/tailhook/resolv-conf
#!RemoteAsset:  sha256:52e44394d2086d010551b14b53b1f24e31647570cd1deb0379e2c21b329aba00
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quick-error-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "resolv-conf"

%package     -n %{name}+hostname
Summary:        Resolv.conf file parser - feature "hostname" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hostname-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/hostname) = %{version}
Provides:       crate(%{pkgname}/system) = %{version}

%description -n %{name}+hostname
This metapackage enables feature "hostname" for the Rust resolv-conf crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "system" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
