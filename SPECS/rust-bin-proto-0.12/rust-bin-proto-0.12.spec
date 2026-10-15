# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bin-proto
%global full_version 0.12.5
%global pkgname bin-proto-0.12

Name:           rust-bin-proto-0.12
Version:        0.12.5
Release:        %autorelease
Summary:        Rust crate "bin-proto"
License:        MIT
URL:            https://github.com/wojciech-graj/bin-proto
#!RemoteAsset:  sha256:903e1e50903f91d32e7be235a526e6146a5cd2a17c5f5014ea6cea33e29d04da
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitstream-io-4) >= 4.6.0
Requires:       crate(core2-0.4) >= 0.4.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/prepend-tags) = %{version}

%description
Source code for takopackized Rust crate "bin-proto"

%package     -n %{name}+alloc
Summary:        Conversion to/from binary for arbitrary types - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitstream-io-4/alloc) >= 4.6.0
Requires:       crate(core2-0.4/alloc) >= 0.4.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust bin-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Conversion to/from binary for arbitrary types - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust bin-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Conversion to/from binary for arbitrary types - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bin-proto-derive-0.12/default) >= 0.12.1
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust bin-proto crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Conversion to/from binary for arbitrary types - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(bitstream-io-4/std) >= 4.6.0
Requires:       crate(core2-0.4/std) >= 0.4.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust bin-proto crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
