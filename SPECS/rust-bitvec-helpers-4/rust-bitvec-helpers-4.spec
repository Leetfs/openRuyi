# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bitvec_helpers
%global full_version 4.0.2
%global pkgname bitvec-helpers-4

Name:           rust-bitvec-helpers-4
Version:        4.0.2
Release:        %autorelease
Summary:        Rust crate "bitvec_helpers"
License:        MIT
URL:            https://github.com/quietvoid/bitvec_helpers
#!RemoteAsset:  sha256:52e5938870db620c26a8f329f5735aa3450cedd30f4a4bb98475b1b076d8edae
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "bitvec_helpers"

%package     -n %{name}+bitstream-io
Summary:        BitVec based bitstream reader and writer - feature "bitstream-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitstream-io-4/default) >= 4.10.0
Provides:       crate(%{pkgname}/bitstream-io) = %{version}

%description -n %{name}+bitstream-io
This metapackage enables feature "bitstream-io" for the Rust bitvec_helpers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitvec
Summary:        BitVec based bitstream reader and writer - feature "bitvec" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anyhow-1/default) >= 1.0.102
Requires:       crate(bitvec-1/default) >= 1.0.1
Requires:       crate(funty-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/bitvec) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+bitvec
This metapackage enables feature "bitvec" for the Rust bitvec_helpers crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
