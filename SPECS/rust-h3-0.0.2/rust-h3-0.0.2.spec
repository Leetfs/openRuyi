# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name h3
%global full_version 0.0.2
%global pkgname h3-0.0.2

Name:           rust-h3-0.0.2
Version:        0.0.2
Release:        %autorelease
Summary:        Rust crate "h3"
License:        MIT
URL:            https://github.com/hyperium/h3
#!RemoteAsset:  sha256:6de6ca43eed186fd055214af06967b0a7a68336cefec7e8a4004e96efeaccb9e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(fastrand-1/default) >= 1.9.0
Requires:       crate(futures-util-0.3) >= 0.3.0
Requires:       crate(http-0.2/default) >= 0.2.9
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Requires:       crate(tracing-0.1/default) >= 0.1.37

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "h3"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
