# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hostname
%global full_version 0.3.0
%global pkgname hostname-0.3

Name:           rust-hostname-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "hostname"
License:        MIT
URL:            https://github.com/svartalf/hostname
#!RemoteAsset:  sha256:01b1af8d6d068ba9de1c39c6ff0d879aed20f74873d4d3929a4535000bb07886
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(match-cfg-0.1/default) >= 0.1.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/sysinfoapi) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/set) = %{version}

%description
Source code for takopackized Rust crate "hostname"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
