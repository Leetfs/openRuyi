# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name thread-id
%global full_version 4.2.2
%global pkgname thread-id-4

Name:           rust-thread-id-4
Version:        4.2.2
Release:        %autorelease
Summary:        Rust crate "thread-id"
License:        MIT OR Apache-2.0
URL:            https://github.com/ruuda/thread-id
#!RemoteAsset:  sha256:cfe8f25bbdd100db7e1d34acf7fd2dc59c4bf8f7483f505eaa7d4f12f76cc0ea
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.147
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/processthreadsapi) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "thread-id"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
