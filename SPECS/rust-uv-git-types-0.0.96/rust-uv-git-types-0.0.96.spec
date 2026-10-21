# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uv-git-types
%global full_version 0.0.96
%global pkgname uv-git-types-0.0.96

Name:           rust-uv-git-types-0.0.96
Version:        0.0.96
Release:        %autorelease
Summary:        Rust crate "uv-git-types"
License:        MIT OR Apache-2.0
URL:            https://pypi.org/project/uv/
#!RemoteAsset:  sha256:e0437f5a70c0d86e3ec087da8ee639690001656a0d8602fa0590a5f5c7a7cb23
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(percent-encoding-2/std) >= 2.3.1
Requires:       crate(serde-1/derive) >= 1.0.210
Requires:       crate(serde-1/rc) >= 1.0.210
Requires:       crate(serde-1/std) >= 1.0.210
Requires:       crate(thiserror-2/std) >= 2.0.0
Requires:       crate(tracing-0.1/attributes) >= 0.1.40
Requires:       crate(tracing-0.1/std) >= 0.1.40
Requires:       crate(uv-cache-key-0.0.96/default) >= 0.0.96
Requires:       crate(uv-redacted-0.0.96/default) >= 0.0.96
Requires:       crate(uv-static-0.0.96/default) >= 0.0.96

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "uv-git-types"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
