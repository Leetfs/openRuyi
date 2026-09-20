# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pin-project-internal
%global full_version 1.1.13
%global pkgname pin-project-internal-1

Name:           rust-pin-project-internal-1
Version:        1.1.13
Release:        %autorelease
Summary:        Rust crate "pin-project-internal"
License:        Apache-2.0 OR MIT
URL:            https://github.com/taiki-e/pin-project
#!RemoteAsset:  sha256:c96395f0a926bc13b1c17622aaddda1ecb55d49c8f1bf9777e4d877800a43f8b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.60
Requires:       crate(quote-1/default) >= 1.0.25
Requires:       crate(syn-2/clone-impls) >= 2.0.1
Requires:       crate(syn-2/full) >= 2.0.1
Requires:       crate(syn-2/parsing) >= 2.0.1
Requires:       crate(syn-2/printing) >= 2.0.1
Requires:       crate(syn-2/proc-macro) >= 2.0.1
Requires:       crate(syn-2/visit-mut) >= 2.0.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pin-project-internal"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
