# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lexical-util
%global full_version 0.8.5
%global pkgname lexical-util-0.8

Name:           rust-lexical-util-0.8
Version:        0.8.5
Release:        %autorelease
Summary:        Rust crate "lexical-util"
License:        MIT OR Apache-2.0
URL:            https://github.com/Alexhuszagh/rust-lexical
#!RemoteAsset:  sha256:5255b9ff16ff898710eb9eb63cb39248ea8a5bb036bea8085b1a767ff6c4e3fc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(static-assertions-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/compact) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/f128) = %{version}
Provides:       crate(%{pkgname}/f16) = %{version}
Provides:       crate(%{pkgname}/floats) = %{version}
Provides:       crate(%{pkgname}/format) = %{version}
Provides:       crate(%{pkgname}/integers) = %{version}
Provides:       crate(%{pkgname}/lint) = %{version}
Provides:       crate(%{pkgname}/parse) = %{version}
Provides:       crate(%{pkgname}/power-of-two) = %{version}
Provides:       crate(%{pkgname}/radix) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/write) = %{version}

%description
Source code for takopackized Rust crate "lexical-util"

%package     -n %{name}+parse-floats
Summary:        Shared utilities for lexical creates - feature "parse-floats"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/floats) = %{version}
Requires:       crate(%{pkgname}/parse) = %{version}
Provides:       crate(%{pkgname}/parse-floats) = %{version}

%description -n %{name}+parse-floats
This metapackage enables feature "parse-floats" for the Rust lexical-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parse-integers
Summary:        Shared utilities for lexical creates - feature "parse-integers"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/integers) = %{version}
Requires:       crate(%{pkgname}/parse) = %{version}
Provides:       crate(%{pkgname}/parse-integers) = %{version}

%description -n %{name}+parse-integers
This metapackage enables feature "parse-integers" for the Rust lexical-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+write-floats
Summary:        Shared utilities for lexical creates - feature "write-floats"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/floats) = %{version}
Requires:       crate(%{pkgname}/write) = %{version}
Provides:       crate(%{pkgname}/write-floats) = %{version}

%description -n %{name}+write-floats
This metapackage enables feature "write-floats" for the Rust lexical-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+write-integers
Summary:        Shared utilities for lexical creates - feature "write-integers"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/integers) = %{version}
Requires:       crate(%{pkgname}/write) = %{version}
Provides:       crate(%{pkgname}/write-integers) = %{version}

%description -n %{name}+write-integers
This metapackage enables feature "write-integers" for the Rust lexical-util crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
