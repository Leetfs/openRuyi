# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name symphonia-format-ogg
%global full_version 0.6.0
%global pkgname symphonia-format-ogg-0.6

Name:           rust-symphonia-format-ogg-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "symphonia-format-ogg"
License:        MPL-2.0
URL:            https://github.com/pdeljanov/Symphonia
#!RemoteAsset:  sha256:b05a67e02b1e4fca1a261ba4fe06910a9357489ad8c36aafdd2960e9c6559433
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(symphonia-common-0.6/default) >= 0.6.0
Requires:       crate(symphonia-core-0.6/default) >= 0.6.0
Requires:       crate(symphonia-metadata-0.6/vorbis) >= 0.6.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "symphonia-format-ogg"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
