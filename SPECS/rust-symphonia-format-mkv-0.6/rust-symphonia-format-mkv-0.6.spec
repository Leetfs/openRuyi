# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name symphonia-format-mkv
%global full_version 0.6.0
%global pkgname symphonia-format-mkv-0.6

Name:           rust-symphonia-format-mkv-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "symphonia-format-mkv"
License:        MPL-2.0
URL:            https://github.com/pdeljanov/Symphonia
#!RemoteAsset:  sha256:fb17713e134f5ad316c2690fa3104590ccc85842cdbcf82c3cd1a845cb08aa74
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lazy-static-1/default) >= 1.5.0
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(symphonia-common-0.6/default) >= 0.6.0
Requires:       crate(symphonia-core-0.6/default) >= 0.6.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "symphonia-format-mkv"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
