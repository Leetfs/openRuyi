# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uv-distribution-filename
%global full_version 0.0.96
%global pkgname uv-distribution-filename-0.0.96

Name:           rust-uv-distribution-filename-0.0.96
Version:        0.0.96
Release:        %autorelease
Summary:        Rust crate "uv-distribution-filename"
License:        MIT OR Apache-2.0
URL:            https://pypi.org/project/uv/
#!RemoteAsset:  sha256:f745b0e4f1883cda0047664e60ba3814f9f224f70cea03929e4694470966e741
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2/std) >= 2.7.4
Requires:       crate(rkyv-0.8/bytecheck) >= 0.8.14
Requires:       crate(rkyv-0.8/smallvec-1) >= 0.8.14
Requires:       crate(rkyv-0.8/std) >= 0.8.14
Requires:       crate(serde-1/derive) >= 1.0.210
Requires:       crate(serde-1/rc) >= 1.0.210
Requires:       crate(serde-1/std) >= 1.0.210
Requires:       crate(smallvec-1) >= 1.13.2
Requires:       crate(thiserror-2/std) >= 2.0.0
Requires:       crate(uv-cache-key-0.0.96/default) >= 0.0.96
Requires:       crate(uv-normalize-0.0.96/default) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/default) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/rkyv) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/tracing) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/version-ranges) >= 0.0.96
Requires:       crate(uv-platform-tags-0.0.96/default) >= 0.0.96
Requires:       crate(uv-small-str-0.0.96/default) >= 0.0.96

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "uv-distribution-filename"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
