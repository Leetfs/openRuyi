# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rend
%global full_version 0.5.4
%global pkgname rend-0.5

Name:           rust-rend-0.5
Version:        0.5.4
Release:        %autorelease
Summary:        Rust crate "rend"
License:        MIT
URL:            https://github.com/djkoloski/rend
#!RemoteAsset:  sha256:663ba70707f96e871406fe10d68128412e619b06d1d47cb91c3a4c6501176240
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rend"

%package     -n %{name}+bytecheck
Summary:        Cross-platform, endian-aware primitives for Rust - feature "bytecheck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytecheck-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/bytecheck) = %{version}

%description -n %{name}+bytecheck
This metapackage enables feature "bytecheck" for the Rust rend crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck-1
Summary:        Cross-platform, endian-aware primitives for Rust - feature "bytemuck-1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1) >= 1.0.0
Provides:       crate(%{pkgname}/bytemuck-1) = %{version}

%description -n %{name}+bytemuck-1
This metapackage enables feature "bytemuck-1" for the Rust rend crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zerocopy-0-8
Summary:        Cross-platform, endian-aware primitives for Rust - feature "zerocopy-0_8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zerocopy-0.8) >= 0.8.0
Requires:       crate(zerocopy-derive-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/zerocopy-0-8) = %{version}

%description -n %{name}+zerocopy-0-8
This metapackage enables feature "zerocopy-0_8" for the Rust rend crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
