# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name symphonia-metadata
%global full_version 0.6.0
%global pkgname symphonia-metadata-0.6

Name:           rust-symphonia-metadata-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "symphonia-metadata"
License:        MPL-2.0
URL:            https://github.com/pdeljanov/Symphonia
#!RemoteAsset:  sha256:a31acf5cd623398a6208e2225d18f4b20f761c55098a796a5247ad516a4a8681
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lazy-static-1/default) >= 1.5.0
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(regex-lite-0.1/default) >= 0.1.9
Requires:       crate(smallvec-1/default) >= 1.15.1
Requires:       crate(symphonia-core-0.6/default) >= 0.6.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/ape) = %{version}
Provides:       crate(%{pkgname}/flac) = %{version}
Provides:       crate(%{pkgname}/id3v1) = %{version}
Provides:       crate(%{pkgname}/id3v2) = %{version}
Provides:       crate(%{pkgname}/riff-id3) = %{version}
Provides:       crate(%{pkgname}/riff-info) = %{version}
Provides:       crate(%{pkgname}/vorbis) = %{version}

%description
Source code for takopackized Rust crate "symphonia-metadata"

%package     -n %{name}+default
Summary:        Project Symphonia multimedia tag and metadata readers - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ape) = %{version}
Requires:       crate(%{pkgname}/id3v1) = %{version}
Requires:       crate(%{pkgname}/id3v2) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust symphonia-metadata crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+riff
Summary:        Project Symphonia multimedia tag and metadata readers - feature "riff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/riff-id3) = %{version}
Requires:       crate(%{pkgname}/riff-info) = %{version}
Provides:       crate(%{pkgname}/riff) = %{version}

%description -n %{name}+riff
This metapackage enables feature "riff" for the Rust symphonia-metadata crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
