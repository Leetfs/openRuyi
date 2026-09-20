# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name auto_enums
%global full_version 0.8.9
%global pkgname auto-enums-0.8

Name:           rust-auto-enums-0.8
Version:        0.8.9
Release:        %autorelease
Summary:        Rust crate "auto_enums"
License:        Apache-2.0 OR MIT
URL:            https://github.com/taiki-e/auto_enums
#!RemoteAsset:  sha256:2e4487600931c9a89f8db7ffbdf3fbdd45bb7bd85e26861f659a463cd0dff966
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(derive-utils-0.15/default) >= 0.15.1
Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/clone-impls) >= 2.0.117
Requires:       crate(syn-2/full) >= 2.0.117
Requires:       crate(syn-2/parsing) >= 2.0.117
Requires:       crate(syn-2/printing) >= 2.0.117
Requires:       crate(syn-2/proc-macro) >= 2.0.117
Requires:       crate(syn-2/visit-mut) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/convert) = %{version}
Provides:       crate(%{pkgname}/coroutine-trait) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/fmt) = %{version}
Provides:       crate(%{pkgname}/fn-traits) = %{version}
Provides:       crate(%{pkgname}/futures01) = %{version}
Provides:       crate(%{pkgname}/futures03) = %{version}
Provides:       crate(%{pkgname}/generator-trait) = %{version}
Provides:       crate(%{pkgname}/http-body1) = %{version}
Provides:       crate(%{pkgname}/ops) = %{version}
Provides:       crate(%{pkgname}/rayon) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/tokio01) = %{version}
Provides:       crate(%{pkgname}/tokio02) = %{version}
Provides:       crate(%{pkgname}/tokio03) = %{version}
Provides:       crate(%{pkgname}/tokio1) = %{version}
Provides:       crate(%{pkgname}/transpose-methods) = %{version}
Provides:       crate(%{pkgname}/trusted-len) = %{version}
Provides:       crate(%{pkgname}/type-analysis) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "auto_enums"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
