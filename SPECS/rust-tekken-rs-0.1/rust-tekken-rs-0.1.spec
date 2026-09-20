# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tekken-rs
%global full_version 0.1.1
%global pkgname tekken-rs-0.1

Name:           rust-tekken-rs-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "tekken-rs"
License:        Apache-2.0
URL:            https://github.com/jorge-menjivar/tekken-rs
#!RemoteAsset:  sha256:49623843103837f53f7ebe8cfafc19ccff28ff0e15e7c4b9f6ad21e36fbfde3a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.102
Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(env-logger-0.11/default) >= 0.11.10
Requires:       crate(hound-3/default) >= 3.5.1
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(ndarray-0.16/default) >= 0.16.1
Requires:       crate(regex-1/default) >= 1.12.3
Requires:       crate(rubato-0.16/default) >= 0.16.2
Requires:       crate(rustc-hash-1/default) >= 1.1.0
Requires:       crate(rustfft-6/default) >= 6.4.1
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-json-1/default) >= 1.0.149
Requires:       crate(thiserror-2/default) >= 2.0.18
Requires:       crate(tiktoken-rs-0.7/default) >= 0.7.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tekken-rs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
