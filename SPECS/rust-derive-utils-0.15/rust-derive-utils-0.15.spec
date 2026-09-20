# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name derive_utils
%global full_version 0.15.1
%global pkgname derive-utils-0.15

Name:           rust-derive-utils-0.15
Version:        0.15.1
Release:        %autorelease
Summary:        Rust crate "derive_utils"
License:        Apache-2.0 OR MIT
URL:            https://github.com/taiki-e/derive_utils
#!RemoteAsset:  sha256:362f47930db19fe7735f527e6595e4900316b893ebf6d48ad3d31be928d57dd6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/clone-impls) >= 2.0.117
Requires:       crate(syn-2/full) >= 2.0.117
Requires:       crate(syn-2/parsing) >= 2.0.117
Requires:       crate(syn-2/printing) >= 2.0.117
Requires:       crate(syn-2/proc-macro) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "derive_utils"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
