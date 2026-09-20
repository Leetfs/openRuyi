# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-csv
%global full_version 59.2.0
%global pkgname arrow-csv-59

Name:           rust-arrow-csv-59
Version:        59.2.0
Release:        %autorelease
Summary:        Rust crate "arrow-csv"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:25011b52b346407d497ef0030e12b45e4f2d0cc279efc09c4f3d09106db30e36
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-array-59/default) >= 59.2.0
Requires:       crate(arrow-cast-59/default) >= 59.2.0
Requires:       crate(arrow-schema-59/default) >= 59.2.0
Requires:       crate(chrono-0.4/clock) >= 0.4.40
Requires:       crate(csv-1) >= 1.1.0
Requires:       crate(csv-core-0.1/default) >= 0.1.0
Requires:       crate(regex-1/perf) >= 1.7.0
Requires:       crate(regex-1/std) >= 1.7.0
Requires:       crate(regex-1/unicode) >= 1.7.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "arrow-csv"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
