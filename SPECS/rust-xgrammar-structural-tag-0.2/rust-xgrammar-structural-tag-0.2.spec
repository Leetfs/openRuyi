# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xgrammar-structural-tag
%global full_version 0.2.0+xgrammar.0.2.4.dd729e7
%global pkgname xgrammar-structural-tag-0.2

Name:           rust-xgrammar-structural-tag-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "xgrammar-structural-tag"
License:        Apache-2.0
URL:            https://github.com/Inferact/xgrammar-structural-tag
#!RemoteAsset:  sha256:d4d24c842efc3c24e9756aa426d530cbdac0980e49af223cb384e276e981ca0a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(auto-impl-1/default) >= 1.3.0
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-json-1/default) >= 1.0.149
Requires:       crate(serde-json-1/preserve-order) >= 1.0.149
Requires:       crate(strum-0.27/default) >= 0.27.2
Requires:       crate(strum-0.27/derive) >= 0.27.2
Requires:       crate(thiserror-2/default) >= 2.0.18

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "xgrammar-structural-tag"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
