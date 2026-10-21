# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uv-logging
%global full_version 0.0.96
%global pkgname uv-logging-0.0.96

Name:           rust-uv-logging-0.0.96
Version:        0.0.96
Release:        %autorelease
Summary:        Rust crate "uv-logging"
License:        MIT OR Apache-2.0
URL:            https://pypi.org/project/uv/
#!RemoteAsset:  sha256:7e297242c62e8cd7fcd0b9801410cd53ee5960bff73f2a7498df32996f4e8326
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstream-1/auto) >= 1.0.0
Requires:       crate(anstream-1/wincon) >= 1.0.0
Requires:       crate(owo-colors-4) >= 4.1.0
Requires:       crate(tracing-0.1/attributes) >= 0.1.40
Requires:       crate(tracing-0.1/std) >= 0.1.40
Requires:       crate(tracing-subscriber-0.3/ansi) >= 0.3.18
Requires:       crate(tracing-subscriber-0.3/fmt) >= 0.3.18
Requires:       crate(tracing-subscriber-0.3/smallvec) >= 0.3.18
Requires:       crate(tracing-subscriber-0.3/std) >= 0.3.18
Requires:       crate(tracing-subscriber-0.3/tracing-log) >= 0.3.18

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "uv-logging"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
