# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uv-globfilter
%global full_version 0.0.96
%global pkgname uv-globfilter-0.0.96

Name:           rust-uv-globfilter-0.0.96
Version:        0.0.96
Release:        %autorelease
Summary:        Rust crate "uv-globfilter"
License:        MIT OR Apache-2.0
URL:            https://pypi.org/project/uv/
#!RemoteAsset:  sha256:ef42416174704a2635edd18718fa0299e151945a15bf01ddba54863f54b227ea
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(globset-0.4) >= 0.4.15
Requires:       crate(regex-1/perf-backtrack) >= 1.13.0
Requires:       crate(regex-1/perf-cache) >= 1.13.0
Requires:       crate(regex-1/perf-dfa) >= 1.13.0
Requires:       crate(regex-1/perf-inline) >= 1.13.0
Requires:       crate(regex-1/perf-literal) >= 1.13.0
Requires:       crate(regex-1/std) >= 1.13.0
Requires:       crate(regex-1/unicode-case) >= 1.13.0
Requires:       crate(regex-1/unicode-gencat) >= 1.13.0
Requires:       crate(regex-1/unicode-perl) >= 1.13.0
Requires:       crate(regex-automata-0.4/dfa-build) >= 0.4.8
Requires:       crate(regex-automata-0.4/dfa-search) >= 0.4.8
Requires:       crate(regex-automata-0.4/perf) >= 0.4.8
Requires:       crate(regex-automata-0.4/std) >= 0.4.8
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.8
Requires:       crate(thiserror-2/std) >= 2.0.0
Requires:       crate(tracing-0.1/attributes) >= 0.1.40
Requires:       crate(tracing-0.1/std) >= 0.1.40
Requires:       crate(uv-errors-0.0.96/default) >= 0.0.96
Requires:       crate(walkdir-2) >= 2.5.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "uv-globfilter"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
