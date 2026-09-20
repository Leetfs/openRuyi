# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name petgraph
%global full_version 0.8.3
%global pkgname petgraph-0.8

Name:           rust-petgraph-0.8
Version:        0.8.3
Release:        %autorelease
Summary:        Rust crate "petgraph"
License:        MIT OR Apache-2.0
URL:            https://github.com/petgraph/petgraph
#!RemoteAsset:  sha256:8701b58ea97060d5e5b155d383a69952a60943f0e6dfe30b04c287beb0b27455
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fixedbitset-0.5) >= 0.5.7
Requires:       crate(hashbrown-0.15/default-hasher) >= 0.15.5
Requires:       crate(hashbrown-0.15/inline-more) >= 0.15.5
Requires:       crate(indexmap-2) >= 2.13.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/generate) = %{version}
Provides:       crate(%{pkgname}/graphmap) = %{version}
Provides:       crate(%{pkgname}/matrix-graph) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Provides graph types and graph algorithms.
Source code for takopackized Rust crate "petgraph"

%package     -n %{name}+all
Summary:        Graph data structure library - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dot-parser) = %{version}
Requires:       crate(%{pkgname}/graphmap) = %{version}
Requires:       crate(%{pkgname}/matrix-graph) = %{version}
Requires:       crate(%{pkgname}/quickcheck) = %{version}
Requires:       crate(%{pkgname}/rayon) = %{version}
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
Requires:       crate(%{pkgname}/matrix-graph) = %{version}
Requires:       crate(%{pkgname}/stable-graph) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
Provides graph types and graph algorithms.
This metapackage enables feature "default" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dot-parser
Summary:        Graph data structure library - feature "dot_parser"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(dot-parser-0.5/default) >= 0.5.1
Requires:       crate(dot-parser-macros-0.5/default) >= 0.5.1
Provides:       crate(%{pkgname}/dot-parser) = %{version}

%description -n %{name}+dot-parser
Provides graph types and graph algorithms.
This metapackage enables feature "dot_parser" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quickcheck
Summary:        Graph data structure library - feature "quickcheck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/graphmap) = %{version}
Requires:       crate(%{pkgname}/stable-graph) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(quickcheck-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/quickcheck) = %{version}

%description -n %{name}+quickcheck
Provides graph types and graph algorithms.
This metapackage enables feature "quickcheck" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Graph data structure library - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(hashbrown-0.15/default-hasher) >= 0.15.5
Requires:       crate(hashbrown-0.15/inline-more) >= 0.15.5
Requires:       crate(hashbrown-0.15/rayon) >= 0.15.5
Requires:       crate(indexmap-2/rayon) >= 2.13.0
Requires:       crate(rayon-1/default) >= 1.5.3
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
Provides graph types and graph algorithms.
This metapackage enables feature "rayon" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Graph data structure library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
Provides graph types and graph algorithms.
This metapackage enables feature "serde" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-1
Summary:        Graph data structure library - feature "serde-1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-derive) = %{version}
Provides:       crate(%{pkgname}/serde-1) = %{version}

%description -n %{name}+serde-1
Provides graph types and graph algorithms.
This metapackage enables feature "serde-1" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-derive
Summary:        Graph data structure library - feature "serde_derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-derive-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde-derive) = %{version}

%description -n %{name}+serde-derive
Provides graph types and graph algorithms.
This metapackage enables feature "serde_derive" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stable-graph
Summary:        Graph data structure library - feature "stable_graph"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/stable-graph) = %{version}

%description -n %{name}+stable-graph
Provides graph types and graph algorithms.
This metapackage enables feature "stable_graph" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Graph data structure library - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/std) >= 2.13.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
Provides graph types and graph algorithms.
This metapackage enables feature "std" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
