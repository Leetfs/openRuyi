# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name thread-id
%global full_version 3.2.0
%global pkgname thread-id-3

Name:           rust-thread-id-3
Version:        3.2.0
Release:        %autorelease
Summary:        Rust crate "thread-id"
License:        MIT OR Apache-2.0
URL:            https://github.com/ruuda/thread-id
#!RemoteAsset:  sha256:2af4d6289a69a35c4d3aea737add39685f2784122c28119a7713165a63d68c9d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(kernel32-sys-0.2/default) >= 0.2.1
Requires:       crate(libc-0.2/default) >= 0.2.6
Requires:       crate(redox-syscall-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "thread-id"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
