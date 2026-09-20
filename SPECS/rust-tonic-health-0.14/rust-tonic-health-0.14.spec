# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tonic-health
%global full_version 0.14.6
%global pkgname tonic-health-0.14

Name:           rust-tonic-health-0.14
Version:        0.14.6
Release:        %autorelease
Summary:        Rust crate "tonic-health"
License:        MIT
URL:            https://github.com/hyperium/tonic
#!RemoteAsset:  sha256:fcfab99db777fba2802f0dfa861d1628d1ae916fb199d29819941f139ae85082
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(prost-0.14/default) >= 0.14.3
Requires:       crate(tokio-1/default) >= 1.52.3
Requires:       crate(tokio-1/sync) >= 1.52.3
Requires:       crate(tokio-stream-0.1/sync) >= 0.1.18
Requires:       crate(tonic-0.14/codegen) >= 0.14.6
Requires:       crate(tonic-prost-0.14) >= 0.14.6

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tonic-health"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
