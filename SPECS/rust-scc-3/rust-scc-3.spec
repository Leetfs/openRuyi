# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name scc
%global full_version 3.6.9
%global pkgname scc-3

Name:           rust-scc-3
Version:        3.6.9
Release:        %autorelease
Summary:        Rust crate "scc"
License:        Apache-2.0
URL:            https://codeberg.org/wvwwvwwv/scalable-concurrent-containers/
#!RemoteAsset:  sha256:45bb5ce9efd4a6e7b0f86c2697fe4c1d78d1f4e6d988c54b752d577cafe22fe8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(saa-5/default) >= 5.5.0
Requires:       crate(sdd-4/default) >= 4.7.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "scc"

%package     -n %{name}+equivalent
Summary:        Collection of high-performance asynchronous/concurrent containers with both asynchronous and synchronous interfaces - feature "equivalent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(equivalent-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/equivalent) = %{version}

%description -n %{name}+equivalent
This metapackage enables feature "equivalent" for the Rust scc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+loom
Summary:        Collection of high-performance asynchronous/concurrent containers with both asynchronous and synchronous interfaces - feature "loom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(loom-0.7/checkpoint) >= 0.7.0
Requires:       crate(loom-0.7/default) >= 0.7.0
Requires:       crate(saa-5/loom) >= 5.5.0
Requires:       crate(sdd-4/loom) >= 4.7.3
Provides:       crate(%{pkgname}/loom) = %{version}

%description -n %{name}+loom
This metapackage enables feature "loom" for the Rust scc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Collection of high-performance asynchronous/concurrent containers with both asynchronous and synchronous interfaces - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust scc crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
