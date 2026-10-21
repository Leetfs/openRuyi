# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uv-fs
%global full_version 0.0.96
%global pkgname uv-fs-0.0.96

Name:           rust-uv-fs-0.0.96
Version:        0.0.96
Release:        %autorelease
Summary:        Rust crate "uv-fs"
License:        MIT OR Apache-2.0
URL:            https://pypi.org/project/uv/
#!RemoteAsset:  sha256:ed1e769fe1955e92ea6ac674807a58956e622ffca4c280b849f0e4dd7d74bb24
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(backon-1/std) >= 1.3.0
Requires:       crate(backon-1/std-blocking-sleep) >= 1.3.0
Requires:       crate(backon-1/tokio-sleep) >= 1.3.0
Requires:       crate(dunce-1) >= 1.0.5
Requires:       crate(either-1/std) >= 1.13.0
Requires:       crate(encoding-rs-io-0.1) >= 0.1.7
Requires:       crate(fs-err-3/tokio) >= 3.2.2
Requires:       crate(junction-2/unstable-admin) >= 2.0.0
Requires:       crate(libc-0.2/std) >= 0.2.0
Requires:       crate(linux-raw-sys-0.12/ioctl) >= 0.12.1
Requires:       crate(path-slash-0.2) >= 0.2.1
Requires:       crate(percent-encoding-2/std) >= 2.3.1
Requires:       crate(reflink-copy-0.1) >= 0.1.19
Requires:       crate(rustc-hash-2/std) >= 2.0.0
Requires:       crate(rustix-1/fs) >= 1.0.0
Requires:       crate(rustix-1/std) >= 1.0.0
Requires:       crate(rustix-1/system) >= 1.0.0
Requires:       crate(same-file-1) >= 1.0.6
Requires:       crate(self-replace-1) >= 1.5.0
Requires:       crate(tempfile-3/getrandom) >= 3.14.0
Requires:       crate(thiserror-2/std) >= 2.0.0
Requires:       crate(tracing-0.1/attributes) >= 0.1.40
Requires:       crate(tracing-0.1/std) >= 0.1.40
Requires:       crate(uv-static-0.0.96/default) >= 0.0.96
Requires:       crate(uv-warnings-0.0.96/default) >= 0.0.96
Requires:       crate(uv-windows-0.0.96/default) >= 0.0.96
Requires:       crate(walkdir-2) >= 2.5.0
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
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "uv-fs"

%package     -n %{name}+clap
Summary:        Internal component crate of uv - feature "clap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/color) >= 4.5.17
Requires:       crate(clap-4/derive) >= 4.5.17
Requires:       crate(clap-4/env) >= 4.5.17
Requires:       crate(clap-4/error-context) >= 4.5.17
Requires:       crate(clap-4/help) >= 4.5.17
Requires:       crate(clap-4/std) >= 4.5.17
Requires:       crate(clap-4/string) >= 4.5.17
Requires:       crate(clap-4/suggestions) >= 4.5.17
Requires:       crate(clap-4/usage) >= 4.5.17
Requires:       crate(clap-4/wrap-help) >= 4.5.17
Provides:       crate(%{pkgname}/clap) = %{version}

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust uv-fs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schemars
Summary:        Internal component crate of uv - feature "schemars"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(schemars-1/derive) >= 1.0.0
Requires:       crate(schemars-1/std) >= 1.0.0
Requires:       crate(schemars-1/url2) >= 1.0.0
Provides:       crate(%{pkgname}/schemars) = %{version}

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust uv-fs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Internal component crate of uv - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.210
Requires:       crate(serde-1/rc) >= 1.0.210
Requires:       crate(serde-1/std) >= 1.0.210
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust uv-fs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Internal component crate of uv - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fs-err-3/tokio) >= 3.2.2
Requires:       crate(tokio-1/fs) >= 1.40.0
Requires:       crate(tokio-1/io-util) >= 1.40.0
Requires:       crate(tokio-1/macros) >= 1.40.0
Requires:       crate(tokio-1/net) >= 1.40.0
Requires:       crate(tokio-1/process) >= 1.40.0
Requires:       crate(tokio-1/rt) >= 1.40.0
Requires:       crate(tokio-1/signal) >= 1.40.0
Requires:       crate(tokio-1/sync) >= 1.40.0
Requires:       crate(tokio-1/time) >= 1.40.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust uv-fs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
