# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name openai-protocol
%global full_version 1.6.0
%global pkgname openai-protocol-1

Name:           rust-openai-protocol-1
Version:        1.6.0
Release:        %autorelease
Summary:        Rust crate "openai-protocol"
License:        Apache-2.0
URL:            https://github.com/lightseekorg/smg
#!RemoteAsset:  sha256:7b8d41ed865b7a26b6b2d2a519b774460e5ddc50eeeb4ac2a2409c8817ec2de9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.13.0
Requires:       crate(chrono-0.4/default) >= 0.4.44
Requires:       crate(rand-0.9/default) >= 0.9.5
Requires:       crate(schemars-0.8/default) >= 0.8.22
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-json-1/default) >= 1.0.150
Requires:       crate(serde-json-1/preserve-order) >= 1.0.150
Requires:       crate(serde-with-3/default) >= 3.20.0
Requires:       crate(serde-with-3/macros) >= 3.20.0
Requires:       crate(tokio-1/default) >= 1.53.1
Requires:       crate(tracing-0.1/default) >= 0.1.44
Requires:       crate(url-2/default) >= 2.5.8
Requires:       crate(validator-0.20/default) >= 0.20.0
Requires:       crate(validator-0.20/derive) >= 0.20.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "openai-protocol"

%package     -n %{name}+axum
Summary:        OpenAI-compatible API protocol definitions and types - feature "axum"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(axum-0.8/default) >= 0.8.6
Provides:       crate(%{pkgname}/axum) = %{version}

%description -n %{name}+axum
This metapackage enables feature "axum" for the Rust openai-protocol crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
