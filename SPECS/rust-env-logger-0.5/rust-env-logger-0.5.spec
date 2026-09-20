# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name env_logger
%global full_version 0.5.0
%global pkgname env-logger-0.5

Name:           rust-env-logger-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "env_logger"
License:        MIT OR Apache-2.0
URL:            https://github.com/sebasmagri/env_logger/
#!RemoteAsset:  sha256:72fe4d3b255c5266b62e5bfdf5982650cdd8c707fb91225f4cc28ff981997057
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(chrono-0.4/default) >= 0.4.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(log-0.4/std) >= 0.4.0
Requires:       crate(termcolor-0.3/default) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "env_logger"

%package     -n %{name}+regex
Summary:        Logging implementation for `log` which is configured via an environment variable - feature "regex" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust env_logger crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
