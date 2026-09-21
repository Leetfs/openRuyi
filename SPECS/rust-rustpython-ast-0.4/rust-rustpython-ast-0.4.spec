# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustpython-ast
%global full_version 0.4.0
%global pkgname rustpython-ast-0.4

Name:           rust-rustpython-ast-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "rustpython-ast"
License:        MIT
URL:            https://github.com/RustPython/Parser
#!RemoteAsset:  sha256:4cdaf8ee5c1473b993b398c174641d3aa9da847af36e8d5eb8291930b72f31a5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(is-macro-0.3/default) >= 0.3.7
Requires:       crate(rustpython-parser-core-0.4/default) >= 0.4.0
Requires:       crate(static-assertions-1/default) >= 1.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/all-nodes-with-ranges) = %{version}
Provides:       crate(%{pkgname}/constant-optimization) = %{version}
Provides:       crate(%{pkgname}/fold) = %{version}
Provides:       crate(%{pkgname}/visitor) = %{version}

%description
Source code for takopackized Rust crate "rustpython-ast"

%package     -n %{name}+default
Summary:        AST definitions for RustPython - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/location) = %{version}
Requires:       crate(%{pkgname}/malachite-bigint) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rustpython-ast crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+location
Summary:        AST definitions for RustPython - feature "location"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fold) = %{version}
Requires:       crate(rustpython-parser-core-0.4/location) >= 0.4.0
Provides:       crate(%{pkgname}/location) = %{version}

%description -n %{name}+location
This metapackage enables feature "location" for the Rust rustpython-ast crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+malachite-bigint
Summary:        AST definitions for RustPython - feature "malachite-bigint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(malachite-bigint-0.2/default) >= 0.2.3
Provides:       crate(%{pkgname}/malachite-bigint) = %{version}

%description -n %{name}+malachite-bigint
This metapackage enables feature "malachite-bigint" for the Rust rustpython-ast crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-bigint
Summary:        AST definitions for RustPython - feature "num-bigint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.4/default) >= 0.4.3
Provides:       crate(%{pkgname}/num-bigint) = %{version}

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust rustpython-ast crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustpython-literal
Summary:        AST definitions for RustPython - feature "rustpython-literal" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustpython-literal-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/rustpython-literal) = %{version}
Provides:       crate(%{pkgname}/unparse) = %{version}

%description -n %{name}+rustpython-literal
This metapackage enables feature "rustpython-literal" for the Rust rustpython-ast crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unparse" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
