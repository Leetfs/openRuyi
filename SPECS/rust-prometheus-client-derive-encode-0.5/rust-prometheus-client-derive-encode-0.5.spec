# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prometheus-client-derive-encode
%global full_version 0.5.0
%global pkgname prometheus-client-derive-encode-0.5

Name:           rust-prometheus-client-derive-encode-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "prometheus-client-derive-encode"
License:        Apache-2.0 OR MIT
URL:            https://github.com/prometheus/client_rust
#!RemoteAsset:  sha256:9adf1691c04c0a5ff46ff8f262b58beb07b0dbb61f96f9f54f6cbd82106ed87f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/default) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "prometheus-client-derive-encode"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
