# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tempdir
%global full_version 0.3.0
%global pkgname tempdir-0.3

Name:           rust-tempdir-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "tempdir"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/tempdir
#!RemoteAsset:  sha256:347ab2bfa411b170b49c4209a2f0366bdbc90bb199f7c4d479639ad54c019b90
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tempdir"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
