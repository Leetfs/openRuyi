# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name reqwest-eventsource
%global full_version 0.6.0
%global pkgname reqwest-eventsource-0.6

Name:           rust-reqwest-eventsource-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "reqwest-eventsource"
License:        MIT OR Apache-2.0
URL:            https://github.com/jpopesculian/reqwest-eventsource
#!RemoteAsset:  sha256:632c55746dbb44275691640e7b40c907c16a2dc1a5842aa98aaec90da6ec6bde
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(eventsource-stream-0.2/default) >= 0.2.3
Requires:       crate(futures-core-0.3/default) >= 0.3.32
Requires:       crate(futures-timer-3/default) >= 3.0.3
Requires:       crate(mime-0.3/default) >= 0.3.17
Requires:       crate(nom-7/default) >= 7.1.3
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17
Requires:       crate(reqwest-0.12/stream) >= 0.12.28
Requires:       crate(thiserror-1/default) >= 1.0.69

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "reqwest-eventsource"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
