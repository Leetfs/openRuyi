# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gnuplot
%global full_version 0.0.39
%global pkgname gnuplot-0.0.39

Name:           rust-gnuplot-0.0.39
Version:        0.0.39
Release:        %autorelease
Summary:        Rust crate "gnuplot"
License:        LGPL-3.0
URL:            https://github.com/SiegeLord/RustGnuplot
#!RemoteAsset:  sha256:2529467b8aef62bdf0c97dc984ca33244b84f8b5eb9517328f24bbb9afa0fb31
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1/default) >= 1.4.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gnuplot"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
