# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name embed-doc-image
%global full_version 0.1.4
%global pkgname embed-doc-image-0.1

Name:           rust-embed-doc-image-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "embed-doc-image"
License:        MIT
URL:            https://github.com/Andlon/embed-doc-image
#!RemoteAsset:  sha256:af36f591236d9d822425cb6896595658fa558fcebf5ee8accac1d4b92c47166e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.13/default) >= 0.13.0
Requires:       crate(proc-macro2-1/default) >= 1.0.27
Requires:       crate(quote-1/default) >= 1.0.9
Requires:       crate(syn-1/full) >= 1.0.72
Requires:       crate(syn-1/parsing) >= 1.0.72
Requires:       crate(syn-1/printing) >= 1.0.72
Requires:       crate(syn-1/proc-macro) >= 1.0.72

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "embed-doc-image"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
