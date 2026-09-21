# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustpython-parser-core
%global full_version 0.4.0
%global pkgname rustpython-parser-core-0.4

Name:           rust-rustpython-parser-core-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "rustpython-parser-core"
License:        MIT
URL:            https://github.com/RustPython/Parser
#!RemoteAsset:  sha256:b4b6c12fa273825edc7bccd9a734f0ad5ba4b8a2f4da5ff7efe946f066d0f4ad
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(is-macro-0.3/default) >= 0.3.7
Requires:       crate(memchr-2/default) >= 2.8.1
Requires:       crate(rustpython-parser-vendored-0.4/default) >= 0.4.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/location) = %{version}

%description
Source code for takopackized Rust crate "rustpython-parser-core"

%package     -n %{name}+serde
Summary:        RustPython parser data types - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.133
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rustpython-parser-core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
