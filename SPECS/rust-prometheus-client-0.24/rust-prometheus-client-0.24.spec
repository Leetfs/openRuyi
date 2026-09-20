# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prometheus-client
%global full_version 0.24.0
%global pkgname prometheus-client-0.24

Name:           rust-prometheus-client-0.24
Version:        0.24.0
Release:        %autorelease
Summary:        Rust crate "prometheus-client"
License:        Apache-2.0 OR MIT
URL:            https://github.com/prometheus/client_rust
#!RemoteAsset:  sha256:e4500adecd7af8e0e9f4dbce15cfee07ce913fbf6ad605cc468b83f2d531ee94
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dtoa-1/default) >= 1.0.11
Requires:       crate(itoa-1/default) >= 1.0.17
Requires:       crate(parking-lot-0.12/default) >= 0.12.5
Requires:       crate(prometheus-client-derive-encode-0.5/default) >= 0.5.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "prometheus-client"

%package     -n %{name}+protobuf
Summary:        Open Metrics client library allowing users to natively instrument applications - feature "protobuf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prost-0.12/default) >= 0.12.0
Requires:       crate(prost-build-0.12/default) >= 0.12.0
Requires:       crate(prost-types-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/protobuf) = %{version}

%description -n %{name}+protobuf
This metapackage enables feature "protobuf" for the Rust prometheus-client crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
