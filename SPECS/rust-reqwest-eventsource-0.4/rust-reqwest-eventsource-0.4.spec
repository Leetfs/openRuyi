# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name reqwest-eventsource
%global full_version 0.4.0
%global pkgname reqwest-eventsource-0.4

Name:           rust-reqwest-eventsource-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "reqwest-eventsource"
License:        MIT OR Apache-2.0
URL:            https://github.com/jpopesculian/reqwest-eventsource
#!RemoteAsset:  sha256:8f03f570355882dd8d15acc3a313841e6e90eddbc76a93c748fd82cc13ba9f51
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(eventsource-stream-0.2/default) >= 0.2.3
Requires:       crate(futures-core-0.3/default) >= 0.3.5
Requires:       crate(futures-timer-3/default) >= 3.0.2
Requires:       crate(mime-0.3/default) >= 0.3.16
Requires:       crate(nom-7/default) >= 7.1.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.8
Requires:       crate(reqwest-0.11/stream) >= 0.11.0
Requires:       crate(thiserror-1/default) >= 1.0.30

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "reqwest-eventsource"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
