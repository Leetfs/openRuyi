# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name symphonia-bundle-mp3
%global full_version 0.6.0
%global pkgname symphonia-bundle-mp3-0.6

Name:           rust-symphonia-bundle-mp3-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "symphonia-bundle-mp3"
License:        MPL-2.0
URL:            https://github.com/pdeljanov/Symphonia
#!RemoteAsset:  sha256:350f1f2f2e19ad4dd315db94304d1eb361b29af070681f94e51b8fdaad769546
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lazy-static-1/default) >= 1.5.0
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(symphonia-core-0.6/default) >= 0.6.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/mp1) = %{version}
Provides:       crate(%{pkgname}/mp2) = %{version}
Provides:       crate(%{pkgname}/mp3) = %{version}

%description
Source code for takopackized Rust crate "symphonia-bundle-mp3"

%package     -n %{name}+default
Summary:        Pure Rust MP1, MP2, and MP3 demuxer and decoder (a part of project Symphonia) - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/mp1) = %{version}
Requires:       crate(%{pkgname}/mp2) = %{version}
Requires:       crate(%{pkgname}/mp3) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust symphonia-bundle-mp3 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
