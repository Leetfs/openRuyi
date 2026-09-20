# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name eventsource-stream
%global full_version 0.2.3
%global pkgname eventsource-stream-0.2

Name:           rust-eventsource-stream-0.2
Version:        0.2.3
Release:        %autorelease
Summary:        Rust crate "eventsource-stream"
License:        MIT OR Apache-2.0
URL:            https://github.com/jpopesculian/eventsource-stream
#!RemoteAsset:  sha256:74fef4569247a5f429d9156b9d0a2599914385dd189c539334c625d8099d90ab
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-core-0.3) >= 0.3.32
Requires:       crate(nom-7) >= 7.1.3
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "eventsource-stream"

%package     -n %{name}+std
Summary:        Basic building block for building an Eventsource from a Stream of bytes - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3/std) >= 0.3.32
Requires:       crate(nom-7/std) >= 7.1.3
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust eventsource-stream crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
