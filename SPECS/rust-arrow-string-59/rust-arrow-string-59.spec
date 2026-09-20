# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-string
%global full_version 59.3.0
%global pkgname arrow-string-59

Name:           rust-arrow-string-59
Version:        59.3.0
Release:        %autorelease
Summary:        Rust crate "arrow-string"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:2e0813f3c35c1cfea65e14c20a953440f7783c088b7ad2d0db162ccdeefcec14
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-array-59/default) >= 59.3.0
Requires:       crate(arrow-buffer-59/default) >= 59.3.0
Requires:       crate(arrow-data-59/default) >= 59.3.0
Requires:       crate(arrow-schema-59/default) >= 59.3.0
Requires:       crate(arrow-select-59/default) >= 59.3.0
Requires:       crate(memchr-2/default) >= 2.7.4
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Requires:       crate(regex-1/perf) >= 1.7.0
Requires:       crate(regex-1/std) >= 1.7.0
Requires:       crate(regex-1/unicode) >= 1.7.0
Requires:       crate(regex-syntax-0.8/unicode) >= 0.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "arrow-string"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
