# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tool-parser
%global full_version 1.2.0
%global pkgname tool-parser-1

Name:           rust-tool-parser-1
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "tool-parser"
License:        Apache-2.0
URL:            https://github.com/lightseekorg/smg
#!RemoteAsset:  sha256:7bdcf0aa96d42cfc2ecc8e7b3c10598b9c1a6052f996b5ab574dec72f483d87c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-trait-0.1/default) >= 0.1.89
Requires:       crate(num-traits-0.2/default) >= 0.2.19
Requires:       crate(openai-protocol-1/default) >= 1.6.0
Requires:       crate(parking-lot-0.12/default) >= 0.12.5
Requires:       crate(regex-1/default) >= 1.12.3
Requires:       crate(rustpython-parser-0.4/default) >= 0.4.0
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-json-1/default) >= 1.0.150
Requires:       crate(serde-json-1/preserve-order) >= 1.0.150
Requires:       crate(thiserror-2/default) >= 2.0.18
Requires:       crate(tokio-1/default) >= 1.53.1
Requires:       crate(tokio-1/macros) >= 1.53.1
Requires:       crate(tokio-1/rt-multi-thread) >= 1.53.1
Requires:       crate(tokio-1/sync) >= 1.53.1
Requires:       crate(tracing-0.1/default) >= 0.1.44

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tool-parser"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
