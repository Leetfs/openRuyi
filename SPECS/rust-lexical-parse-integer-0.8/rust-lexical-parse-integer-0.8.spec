# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lexical-parse-integer
%global full_version 0.8.6
%global pkgname lexical-parse-integer-0.8

Name:           rust-lexical-parse-integer-0.8
Version:        0.8.6
Release:        %autorelease
Summary:        Rust crate "lexical-parse-integer"
License:        MIT OR Apache-2.0
URL:            https://github.com/Alexhuszagh/rust-lexical
#!RemoteAsset:  sha256:6d0994485ed0c312f6d965766754ea177d07f9c00c9b82a5ee62ed5b47945ee9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lexical-util-0.8/parse-integers) >= 0.8.5
Requires:       crate(static-assertions-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/safe) = %{version}

%description
Source code for takopackized Rust crate "lexical-parse-integer"

%package     -n %{name}+compact
Summary:        Efficient parsing of integers from strings - feature "compact"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-0.8/compact) >= 0.8.5
Requires:       crate(lexical-util-0.8/parse-integers) >= 0.8.5
Provides:       crate(%{pkgname}/compact) = %{version}

%description -n %{name}+compact
This metapackage enables feature "compact" for the Rust lexical-parse-integer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+format
Summary:        Efficient parsing of integers from strings - feature "format"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-0.8/format) >= 0.8.5
Requires:       crate(lexical-util-0.8/parse-integers) >= 0.8.5
Provides:       crate(%{pkgname}/format) = %{version}

%description -n %{name}+format
This metapackage enables feature "format" for the Rust lexical-parse-integer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lint
Summary:        Efficient parsing of integers from strings - feature "lint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-0.8/lint) >= 0.8.5
Requires:       crate(lexical-util-0.8/parse-integers) >= 0.8.5
Provides:       crate(%{pkgname}/lint) = %{version}

%description -n %{name}+lint
This metapackage enables feature "lint" for the Rust lexical-parse-integer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+power-of-two
Summary:        Efficient parsing of integers from strings - feature "power-of-two"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-0.8/parse-integers) >= 0.8.5
Requires:       crate(lexical-util-0.8/power-of-two) >= 0.8.5
Provides:       crate(%{pkgname}/power-of-two) = %{version}

%description -n %{name}+power-of-two
This metapackage enables feature "power-of-two" for the Rust lexical-parse-integer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+radix
Summary:        Efficient parsing of integers from strings - feature "radix"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/power-of-two) = %{version}
Requires:       crate(lexical-util-0.8/parse-integers) >= 0.8.5
Requires:       crate(lexical-util-0.8/radix) >= 0.8.5
Provides:       crate(%{pkgname}/radix) = %{version}

%description -n %{name}+radix
This metapackage enables feature "radix" for the Rust lexical-parse-integer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Efficient parsing of integers from strings - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-0.8/parse-integers) >= 0.8.5
Requires:       crate(lexical-util-0.8/std) >= 0.8.5
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust lexical-parse-integer crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
