# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name petgraph
%global full_version 0.4.5
%global pkgname petgraph-0.4

Name:           rust-petgraph-0.4
Version:        0.4.5
Release:        %autorelease
Summary:        Rust crate "petgraph"
License:        MIT OR Apache-2.0
URL:            https://github.com/bluss/petgraph
#!RemoteAsset:  sha256:14c6ae5ccb73b438781abc93d35615019b1ad6e24b44116377fb819cfd7587de
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fixedbitset-0.1/default) >= 0.1.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/generate) = %{version}
Provides:       crate(%{pkgname}/stable-graph) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Provides graph types and graph algorithms.
Source code for takopackized Rust crate "petgraph"

%package     -n %{name}+all
Summary:        Graph data structure library - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/graphmap) = %{version}
Requires:       crate(%{pkgname}/quickcheck) = %{version}
Requires:       crate(%{pkgname}/stable-graph) = %{version}
Requires:       crate(%{pkgname}/unstable) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
Provides graph types and graph algorithms.
This metapackage enables feature "all" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Graph data structure library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/graphmap) = %{version}
Requires:       crate(%{pkgname}/stable-graph) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
Provides graph types and graph algorithms.
This metapackage enables feature "default" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ordermap
Summary:        Graph data structure library - feature "ordermap" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ordermap-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/graphmap) = %{version}
Provides:       crate(%{pkgname}/ordermap) = %{version}

%description -n %{name}+ordermap
Provides graph types and graph algorithms.
This metapackage enables feature "ordermap" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "graphmap" feature.

%package     -n %{name}+quickcheck
Summary:        Graph data structure library - feature "quickcheck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quickcheck-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/quickcheck) = %{version}

%description -n %{name}+quickcheck
Provides graph types and graph algorithms.
This metapackage enables feature "quickcheck" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
