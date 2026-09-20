# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global git_tag v0.0.11
%global git_commit 76e849426cc092f84509e31a17027755f67d662a
%global crate_name oss-harmony
%global full_version 0.0.11
%global pkgname oss-harmony-0.0.11

Name:           rust-oss-harmony-0.0.11
Version:        0.0.11
Release:        %autorelease
Summary:        Rust crate "oss-harmony"
License:        Apache-2.0
URL:            https://github.com/oss-harmony/harmony
#!RemoteAsset:  sha256:b48928a222b66a5eb66d6480edc332586b75034423ac669f4c097bdfd549ff2d
Source:         https://github.com/oss-harmony/harmony/archive/refs/tags/%{git_tag}.tar.gz#/%{crate_name}-%{git_tag}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates
BuildOption(prep):  -n harmony-0.0.11

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.102
Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(bstr-1/default) >= 1.12.1
Requires:       crate(fancy-regex-0.13/default) >= 0.13.0
Requires:       crate(rustc-hash-1/default) >= 1.1.0
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-json-1/default) >= 1.0.149
Requires:       crate(serde-json-1/preserve-order) >= 1.0.149
Requires:       crate(serde-with-3/default) >= 3.18.0
Requires:       crate(sha2-0.10/default) >= 0.10.9
Requires:       crate(thiserror-2/default) >= 2.0.18
Requires:       crate(zstd-0.13/default) >= 0.13.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "oss-harmony"

%package     -n %{name}+pyo3
Summary:        Response format library for the gpt-oss open-weight model series (fork of openai-harmony) - feature "pyo3" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-0.25/abi3-py38) >= 0.25.0
Requires:       crate(pyo3-0.25/default) >= 0.25.0
Requires:       crate(pyo3-0.25/extension-module) >= 0.25.0
Provides:       crate(%{pkgname}/pyo3) = %{version}
Provides:       crate(%{pkgname}/python-binding) = %{version}

%description -n %{name}+pyo3
This metapackage enables feature "pyo3" for the Rust oss-harmony crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "python-binding" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
