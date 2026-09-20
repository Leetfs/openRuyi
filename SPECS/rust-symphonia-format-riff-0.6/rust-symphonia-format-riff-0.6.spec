# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name symphonia-format-riff
%global full_version 0.6.0
%global pkgname symphonia-format-riff-0.6

Name:           rust-symphonia-format-riff-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "symphonia-format-riff"
License:        MPL-2.0
URL:            https://github.com/pdeljanov/Symphonia
#!RemoteAsset:  sha256:17424452a777666d3eaf09a5c651029b15b6a333812fcc5b5474f2a3f0cff3f0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(extended-0.1/default) >= 0.1.0
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(symphonia-core-0.6/default) >= 0.6.0
Requires:       crate(symphonia-metadata-0.6) >= 0.6.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "symphonia-format-riff"

%package     -n %{name}+aiff
Summary:        Pure Rust RIFF demuxer (a part of project Symphonia) - feature "aiff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-metadata-0.6/riff-id3) >= 0.6.0
Provides:       crate(%{pkgname}/aiff) = %{version}

%description -n %{name}+aiff
This metapackage enables feature "aiff" for the Rust symphonia-format-riff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust RIFF demuxer (a part of project Symphonia) - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aiff) = %{version}
Requires:       crate(%{pkgname}/wav) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust symphonia-format-riff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wav
Summary:        Pure Rust RIFF demuxer (a part of project Symphonia) - feature "wav"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symphonia-metadata-0.6/riff-info) >= 0.6.0
Provides:       crate(%{pkgname}/wav) = %{version}

%description -n %{name}+wav
This metapackage enables feature "wav" for the Rust symphonia-format-riff crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
