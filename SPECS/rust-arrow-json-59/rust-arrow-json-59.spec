# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-json
%global full_version 59.3.0
%global pkgname arrow-json-59

Name:           rust-arrow-json-59
Version:        59.3.0
Release:        %autorelease
Summary:        Rust crate "arrow-json"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:a2f57d7a81969f24ccf80809587b76c09897e6f829d2d65a5976bfb3218851f1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-array-59/default) >= 59.3.0
Requires:       crate(arrow-buffer-59/default) >= 59.3.0
Requires:       crate(arrow-cast-59/default) >= 59.3.0
Requires:       crate(arrow-ord-59/default) >= 59.3.0
Requires:       crate(arrow-schema-59/default) >= 59.3.0
Requires:       crate(arrow-select-59/default) >= 59.3.0
Requires:       crate(chrono-0.4/clock) >= 0.4.40
Requires:       crate(half-2) >= 2.1.0
Requires:       crate(indexmap-2/std) >= 2.0.0
Requires:       crate(itoa-1/default) >= 1.0.0
Requires:       crate(lexical-core-1) >= 1.0.0
Requires:       crate(memchr-2/default) >= 2.7.4
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Requires:       crate(ryu-1/default) >= 1.0.0
Requires:       crate(serde-core-1) >= 1.0.0
Requires:       crate(serde-json-1/std) >= 1.0.0
Requires:       crate(simdutf8-0.1) >= 0.1.5

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "arrow-json"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
