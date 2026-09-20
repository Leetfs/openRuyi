# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name symphonia-codec-pcm
%global full_version 0.6.0
%global pkgname symphonia-codec-pcm-0.6

Name:           rust-symphonia-codec-pcm-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "symphonia-codec-pcm"
License:        MPL-2.0
URL:            https://github.com/pdeljanov/Symphonia
#!RemoteAsset:  sha256:50baee168f0e9dcf6ba7fc06e8b57eb62072a4490cc7cf13af77e72baae5d328
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(symphonia-core-0.6/default) >= 0.6.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "symphonia-codec-pcm"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
