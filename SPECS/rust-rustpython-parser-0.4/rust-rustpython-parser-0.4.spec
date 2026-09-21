# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustpython-parser
%global full_version 0.4.0
%global pkgname rustpython-parser-0.4

Name:           rust-rustpython-parser-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "rustpython-parser"
License:        MIT
URL:            https://github.com/RustPython/Parser
#!RemoteAsset:  sha256:868f724daac0caf9bd36d38caf45819905193a901e8f1c983345a68e18fb2abb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1) >= 1.0.102
Requires:       crate(is-macro-0.3/default) >= 0.3.7
Requires:       crate(itertools-0.11/default) >= 0.11.0
Requires:       crate(lalrpop-util-0.20) >= 0.20.2
Requires:       crate(log-0.4/default) >= 0.4.30
Requires:       crate(num-traits-0.2/default) >= 0.2.19
Requires:       crate(phf-0.11/default) >= 0.11.3
Requires:       crate(phf-codegen-0.11) >= 0.11.3
Requires:       crate(rustc-hash-1/default) >= 1.1.0
Requires:       crate(rustpython-ast-0.4) >= 0.4.0
Requires:       crate(rustpython-parser-core-0.4/default) >= 0.4.0
Requires:       crate(tiny-keccak-2) >= 2.0.2
Requires:       crate(tiny-keccak-2/sha3) >= 2.0.2
Requires:       crate(unic-emoji-char-0.9/default) >= 0.9.0
Requires:       crate(unic-ucd-ident-0.9/default) >= 0.9.0
Requires:       crate(unicode-names2-1/default) >= 1.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/full-lexer) = %{version}

%description
Source code for takopackized Rust crate "rustpython-parser"

%package     -n %{name}+all-nodes-with-ranges
Summary:        Python language parser for Python3 - feature "all-nodes-with-ranges"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustpython-ast-0.4/all-nodes-with-ranges) >= 0.4.0
Provides:       crate(%{pkgname}/all-nodes-with-ranges) = %{version}

%description -n %{name}+all-nodes-with-ranges
This metapackage enables feature "all-nodes-with-ranges" for the Rust rustpython-parser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Python language parser for Python3 - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/location) = %{version}
Requires:       crate(%{pkgname}/malachite-bigint) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rustpython-parser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lalrpop
Summary:        Python language parser for Python3 - feature "lalrpop"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lalrpop-0.20) >= 0.20.0
Provides:       crate(%{pkgname}/lalrpop) = %{version}

%description -n %{name}+lalrpop
This metapackage enables feature "lalrpop" for the Rust rustpython-parser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+location
Summary:        Python language parser for Python3 - feature "location"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustpython-ast-0.4/location) >= 0.4.0
Requires:       crate(rustpython-parser-core-0.4/location) >= 0.4.0
Provides:       crate(%{pkgname}/location) = %{version}

%description -n %{name}+location
This metapackage enables feature "location" for the Rust rustpython-parser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+malachite-bigint
Summary:        Python language parser for Python3 - feature "malachite-bigint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(malachite-bigint-0.2/default) >= 0.2.3
Requires:       crate(rustpython-ast-0.4/malachite-bigint) >= 0.4.0
Provides:       crate(%{pkgname}/malachite-bigint) = %{version}

%description -n %{name}+malachite-bigint
This metapackage enables feature "malachite-bigint" for the Rust rustpython-parser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-bigint
Summary:        Python language parser for Python3 - feature "num-bigint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.4/default) >= 0.4.3
Requires:       crate(rustpython-ast-0.4/num-bigint) >= 0.4.0
Provides:       crate(%{pkgname}/num-bigint) = %{version}

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust rustpython-parser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Python language parser for Python3 - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustpython-parser-core-0.4/serde) >= 0.4.0
Requires:       crate(serde-1/derive) >= 1.0.133
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rustpython-parser crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
