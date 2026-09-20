# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name riptoken
%global full_version 0.3.0
%global pkgname riptoken-0.3

Name:           rust-riptoken-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "riptoken"
License:        MIT
URL:            https://github.com/daechoi/riptoken
#!RemoteAsset:  sha256:196b37c4dd48f99b51e8aeaa3d0c343df62c7bb5b66cd6735aa072524fbe8665
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fancy-regex-0.17/default) >= 0.17.0
Requires:       crate(rayon-1/default) >= 1.12.0
Requires:       crate(regex-1) >= 1.12.3
Requires:       crate(regex-1/default) >= 1.12.3
Requires:       crate(regex-automata-0.4) >= 0.4.14
Requires:       crate(regex-automata-0.4/default) >= 0.4.14
Requires:       crate(rustc-hash-2/default) >= 2.1.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/precompiled-dfa) = %{version}

%description
Source code for takopackized Rust crate "riptoken"

%package     -n %{name}+python
Summary:        Fast BPE tokenizer for LLMs — a faster, drop-in compatible reimplementation of tiktoken - feature "python"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-0.27/extension-module) >= 0.27.2
Requires:       crate(pyo3-0.27/macros) >= 0.27.2
Provides:       crate(%{pkgname}/python) = %{version}

%description -n %{name}+python
This metapackage enables feature "python" for the Rust riptoken crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
