# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dot-parser
%global full_version 0.5.1
%global pkgname dot-parser-0.5

Name:           rust-dot-parser-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "dot-parser"
License:        GPL-2.0-or-later
URL:            https://codeberg.org/bromind/dot-parser.git
#!RemoteAsset:  sha256:6cce83b336cd8d9b2718f4e8228a185de6e7a1cfe34f237e8c4acaf1c4141630
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(either-1/default) >= 1.13.0
Requires:       crate(pest-2/default) >= 2.7.14
Requires:       crate(pest-derive-2/default) >= 2.7.14

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/display) = %{version}

%description
Source code for takopackized Rust crate "dot-parser"

%package     -n %{name}+to-tokens
Summary:        Parser for the DOT/Graphviz graph description language, as well as useful functions to transform those graphs - feature "to_tokens"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proc-macro2-1/default) >= 1.0.88
Requires:       crate(quote-1/default) >= 1.0.37
Provides:       crate(%{pkgname}/to-tokens) = %{version}

%description -n %{name}+to-tokens
This metapackage enables feature "to_tokens" for the Rust dot-parser crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
