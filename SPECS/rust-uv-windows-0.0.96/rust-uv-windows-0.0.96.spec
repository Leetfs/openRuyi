# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uv-windows
%global full_version 0.0.96
%global pkgname uv-windows-0.0.96

Name:           rust-uv-windows-0.0.96
Version:        0.0.96
Release:        %autorelease
Summary:        Rust crate "uv-windows"
License:        MIT OR Apache-2.0
URL:            https://pypi.org/project/uv/
#!RemoteAsset:  sha256:d0f7000ad6b7f5631d9650ddd939d496271e8fa17ecaca711555eec23ab6cc3c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-0.61/std) >= 0.61.0
Requires:       crate(windows-0.61/win32-devices-deviceanddriverinstallation) >= 0.61.0
Requires:       crate(windows-0.61/win32-foundation) >= 0.61.0
Requires:       crate(windows-0.61/win32-globalization) >= 0.61.0
Requires:       crate(windows-0.61/win32-security) >= 0.61.0
Requires:       crate(windows-0.61/win32-storage-filesystem) >= 0.61.0
Requires:       crate(windows-0.61/win32-system-console) >= 0.61.0
Requires:       crate(windows-0.61/win32-system-diagnostics-debug) >= 0.61.0
Requires:       crate(windows-0.61/win32-system-environment) >= 0.61.0
Requires:       crate(windows-0.61/win32-system-io) >= 0.61.0
Requires:       crate(windows-0.61/win32-system-ioctl) >= 0.61.0
Requires:       crate(windows-0.61/win32-system-jobobjects) >= 0.61.0
Requires:       crate(windows-0.61/win32-system-kernel) >= 0.61.0
Requires:       crate(windows-0.61/win32-system-libraryloader) >= 0.61.0
Requires:       crate(windows-0.61/win32-system-registry) >= 0.61.0
Requires:       crate(windows-0.61/win32-system-threading) >= 0.61.0
Requires:       crate(windows-0.61/win32-ui-windowsandmessaging) >= 0.61.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "uv-windows"

%package     -n %{name}+std
Summary:        Windows-specific utilities for uv - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrayvec-0.7) >= 0.7.6
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust uv-windows crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
