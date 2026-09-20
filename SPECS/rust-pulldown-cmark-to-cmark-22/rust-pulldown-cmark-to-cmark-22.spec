# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pulldown-cmark-to-cmark
%global full_version 22.0.0
%global pkgname pulldown-cmark-to-cmark-22

Name:           rust-pulldown-cmark-to-cmark-22
Version:        22.0.0
Release:        %autorelease
Summary:        Rust crate "pulldown-cmark-to-cmark"
License:        Apache-2.0
URL:            https://github.com/Byron/pulldown-cmark-to-cmark
#!RemoteAsset:  sha256:50793def1b900256624a709439404384204a5dc3a6ec580281bfaac35e882e90
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pulldown-cmark-0.13) >= 0.13.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pulldown-cmark-to-cmark"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
