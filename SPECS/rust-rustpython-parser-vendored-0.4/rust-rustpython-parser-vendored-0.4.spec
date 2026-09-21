# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustpython-parser-vendored
%global full_version 0.4.0
%global pkgname rustpython-parser-vendored-0.4

Name:           rust-rustpython-parser-vendored-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "rustpython-parser-vendored"
License:        MIT
URL:            https://github.com/RustPython/Parser
#!RemoteAsset:  sha256:04fcea49a4630a3a5d940f4d514dc4f575ed63c14c3e3ed07146634aed7f67a6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2/default) >= 2.8.1
Requires:       crate(once-cell-1/default) >= 1.21.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/location) = %{version}

%description
Source code for takopackized Rust crate "rustpython-parser-vendored"

%package     -n %{name}+serde
Summary:        RustPython parser vendored third-party crates - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.133
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rustpython-parser-vendored crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
