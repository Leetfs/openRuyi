# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wkb
%global full_version 0.9.2
%global pkgname wkb-0.9

Name:           rust-wkb-0.9
Version:        0.9.2
Release:        %autorelease
Summary:        Rust crate "wkb"
License:        MIT OR Apache-2.0
URL:            https://github.com/georust/wkb
#!RemoteAsset:  sha256:a120b336c7ad17749026d50427c23d838ecb50cd64aaea6254b5030152f890a9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1/default) >= 1.0.0
Requires:       crate(geo-traits-0.3/default) >= 0.3.0
Requires:       crate(num-enum-0.7/default) >= 0.7.0
Requires:       crate(thiserror-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wkb"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
