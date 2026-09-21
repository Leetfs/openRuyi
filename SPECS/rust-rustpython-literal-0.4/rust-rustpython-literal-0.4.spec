# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustpython-literal
%global full_version 0.4.0
%global pkgname rustpython-literal-0.4

Name:           rust-rustpython-literal-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "rustpython-literal"
License:        MIT
URL:            https://github.com/RustPython/Parser
#!RemoteAsset:  sha256:a8304be3cae00232a1721a911033e55877ca3810215f66798e964a2d8d22281d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hexf-parse-0.2/default) >= 0.2.1
Requires:       crate(is-macro-0.3/default) >= 0.3.0
Requires:       crate(lexical-parse-float-0.8/default) >= 0.8.0
Requires:       crate(lexical-parse-float-0.8/format) >= 0.8.0
Requires:       crate(num-traits-0.2/default) >= 0.2.0
Requires:       crate(unic-ucd-category-0.9/default) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rustpython-literal"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
