# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uv-pypi-types
%global full_version 0.0.96
%global pkgname uv-pypi-types-0.0.96

Name:           rust-uv-pypi-types-0.0.96
Version:        0.0.96
Release:        %autorelease
Summary:        Rust crate "uv-pypi-types"
License:        MIT OR Apache-2.0
URL:            https://pypi.org/project/uv/
#!RemoteAsset:  sha256:43d4e858d64705908e3e0a8b3037ff9ab111786f4bb13ee6db78765e79fc318a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(astral-mail-headers-0.0.1) >= 0.0.1
Requires:       crate(hashbrown-0.17/equivalent) >= 0.17.0
Requires:       crate(hashbrown-0.17/inline-more) >= 0.17.0
Requires:       crate(indexmap-2/serde) >= 2.5.0
Requires:       crate(indexmap-2/std) >= 2.5.0
Requires:       crate(itertools-0.14/use-std) >= 0.14.0
Requires:       crate(jiff-0.2/perf-inline) >= 0.2.0
Requires:       crate(jiff-0.2/serde) >= 0.2.0
Requires:       crate(jiff-0.2/std) >= 0.2.0
Requires:       crate(jiff-0.2/tz-fat) >= 0.2.0
Requires:       crate(petgraph-0.8/std) >= 0.8.0
Requires:       crate(regex-1/perf-backtrack) >= 1.13.0
Requires:       crate(regex-1/perf-cache) >= 1.13.0
Requires:       crate(regex-1/perf-dfa) >= 1.13.0
Requires:       crate(regex-1/perf-inline) >= 1.13.0
Requires:       crate(regex-1/perf-literal) >= 1.13.0
Requires:       crate(regex-1/std) >= 1.13.0
Requires:       crate(regex-1/unicode-case) >= 1.13.0
Requires:       crate(regex-1/unicode-gencat) >= 1.13.0
Requires:       crate(regex-1/unicode-perl) >= 1.13.0
Requires:       crate(rkyv-0.8/bytecheck) >= 0.8.14
Requires:       crate(rkyv-0.8/std) >= 0.8.14
Requires:       crate(rustc-hash-2/std) >= 2.0.0
Requires:       crate(serde-1/derive) >= 1.0.210
Requires:       crate(serde-1/rc) >= 1.0.210
Requires:       crate(serde-1/std) >= 1.0.210
Requires:       crate(serde-json-1/std) >= 1.0.128
Requires:       crate(thiserror-2/std) >= 2.0.0
Requires:       crate(toml-edit-0.25/display) >= 0.25.8
Requires:       crate(toml-edit-0.25/parse) >= 0.25.8
Requires:       crate(toml-edit-0.25/serde) >= 0.25.8
Requires:       crate(tracing-0.1/attributes) >= 0.1.40
Requires:       crate(tracing-0.1/std) >= 0.1.40
Requires:       crate(uv-cache-key-0.0.96/default) >= 0.0.96
Requires:       crate(uv-distribution-filename-0.0.96/default) >= 0.0.96
Requires:       crate(uv-git-types-0.0.96/default) >= 0.0.96
Requires:       crate(uv-macros-0.0.96/default) >= 0.0.96
Requires:       crate(uv-normalize-0.0.96/default) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/default) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/rkyv) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/tracing) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/version-ranges) >= 0.0.96
Requires:       crate(uv-pep508-0.0.96/default) >= 0.0.96
Requires:       crate(uv-pep508-0.0.96/non-pep508-extensions) >= 0.0.96
Requires:       crate(uv-pep508-0.0.96/rkyv) >= 0.0.96
Requires:       crate(uv-redacted-0.0.96/default) >= 0.0.96
Requires:       crate(uv-small-str-0.0.96/default) >= 0.0.96

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "uv-pypi-types"

%package     -n %{name}+schemars
Summary:        Internal component crate of uv - feature "schemars"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(schemars-1/derive) >= 1.0.0
Requires:       crate(schemars-1/std) >= 1.0.0
Requires:       crate(schemars-1/url2) >= 1.0.0
Requires:       crate(uv-normalize-0.0.96/schemars) >= 0.0.96
Provides:       crate(%{pkgname}/schemars) = %{version}

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust uv-pypi-types crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
