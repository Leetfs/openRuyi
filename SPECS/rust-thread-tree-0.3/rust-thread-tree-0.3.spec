# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name thread-tree
%global full_version 0.3.3
%global pkgname thread-tree-0.3

Name:           rust-thread-tree-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "thread-tree"
License:        MIT OR Apache-2.0
URL:            https://github.com/bluss/thread-tree
#!RemoteAsset:  sha256:ffbd370cb847953a25954d9f63e14824a36113f8c72eecf6eccef5dc4b45d630
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
The tree structure means that there is no contention between workers when delivering jobs.
Source code for takopackized Rust crate "thread-tree"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
