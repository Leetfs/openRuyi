# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name astral-tokio-tar
%global full_version 0.7.0
%global pkgname astral-tokio-tar-0.7

Name:           rust-astral-tokio-tar-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "astral-tokio-tar"
License:        MIT OR Apache-2.0
URL:            https://github.com/astral-sh/tokio-tar
#!RemoteAsset:  sha256:6f2e989b33246fe9240d39accf4dd9a01e0b6c1f3ce9dd095e0a47fa02505523
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-core-0.3/default) >= 0.3.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(portable-atomic-1/default) >= 1.0.0
Requires:       crate(rustc-hash-2/default) >= 2.1.0
Requires:       crate(rustix-1/default) >= 1.0.0
Requires:       crate(rustix-1/fs) >= 1.0.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/fs) >= 1.0.0
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-1/rt) >= 1.0.0
Requires:       crate(tokio-stream-0.1/default) >= 0.1.0
Requires:       crate(zerocopy-0.8/default) >= 0.8.52
Requires:       crate(zerocopy-0.8/derive) >= 0.8.52

Provides:       crate(%{pkgname}) = %{version}

%description
This library does not currently handle compression, but it is abstract over all I/O readers and writers. Additionally, great lengths are taken to ensure that the entire contents are never required to be entirely resident in memory all at once.
Source code for takopackized Rust crate "astral-tokio-tar"

%package     -n %{name}+xattr
Summary:        An async TAR file reader and writer - feature "xattr" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(xattr-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/xattr) = %{version}

%description -n %{name}+xattr
This library does not currently handle compression, but it is abstract over all I/O readers and writers. Additionally, great lengths are taken to ensure that the entire contents are never required to be entirely resident in memory all at once.
This metapackage enables feature "xattr" for the Rust astral-tokio-tar crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
