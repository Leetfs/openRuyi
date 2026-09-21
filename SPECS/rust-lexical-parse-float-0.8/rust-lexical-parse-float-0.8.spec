# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lexical-parse-float
%global full_version 0.8.5
%global pkgname lexical-parse-float-0.8

Name:           rust-lexical-parse-float-0.8
Version:        0.8.5
Release:        %autorelease
Summary:        Rust crate "lexical-parse-float"
License:        MIT OR Apache-2.0
URL:            https://github.com/Alexhuszagh/rust-lexical
#!RemoteAsset:  sha256:683b3a5ebd0130b8fb52ba0bdc718cc56815b6a097e28ae5a6997d0ad17dc05f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lexical-parse-integer-0.8) >= 0.8.5
Requires:       crate(lexical-util-0.8/parse-floats) >= 0.8.5
Requires:       crate(static-assertions-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "lexical-parse-float"

%package     -n %{name}+compact
Summary:        Efficient parsing of floats from strings - feature "compact"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-parse-integer-0.8/compact) >= 0.8.5
Requires:       crate(lexical-util-0.8/compact) >= 0.8.5
Requires:       crate(lexical-util-0.8/parse-floats) >= 0.8.5
Provides:       crate(%{pkgname}/compact) = %{version}

%description -n %{name}+compact
This metapackage enables feature "compact" for the Rust lexical-parse-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+f128
Summary:        Efficient parsing of floats from strings - feature "f128"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-0.8/f128) >= 0.8.5
Requires:       crate(lexical-util-0.8/parse-floats) >= 0.8.5
Provides:       crate(%{pkgname}/f128) = %{version}

%description -n %{name}+f128
This metapackage enables feature "f128" for the Rust lexical-parse-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+f16
Summary:        Efficient parsing of floats from strings - feature "f16"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-0.8/f16) >= 0.8.5
Requires:       crate(lexical-util-0.8/parse-floats) >= 0.8.5
Provides:       crate(%{pkgname}/f16) = %{version}

%description -n %{name}+f16
This metapackage enables feature "f16" for the Rust lexical-parse-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+format
Summary:        Efficient parsing of floats from strings - feature "format"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-parse-integer-0.8/format) >= 0.8.5
Requires:       crate(lexical-util-0.8/format) >= 0.8.5
Requires:       crate(lexical-util-0.8/parse-floats) >= 0.8.5
Provides:       crate(%{pkgname}/format) = %{version}

%description -n %{name}+format
This metapackage enables feature "format" for the Rust lexical-parse-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lint
Summary:        Efficient parsing of floats from strings - feature "lint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-parse-integer-0.8/lint) >= 0.8.5
Requires:       crate(lexical-util-0.8/lint) >= 0.8.5
Requires:       crate(lexical-util-0.8/parse-floats) >= 0.8.5
Provides:       crate(%{pkgname}/lint) = %{version}

%description -n %{name}+lint
This metapackage enables feature "lint" for the Rust lexical-parse-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly
Summary:        Efficient parsing of floats from strings - feature "nightly"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-parse-integer-0.8/nightly) >= 0.8.5
Provides:       crate(%{pkgname}/nightly) = %{version}

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust lexical-parse-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+power-of-two
Summary:        Efficient parsing of floats from strings - feature "power-of-two"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-parse-integer-0.8/power-of-two) >= 0.8.5
Requires:       crate(lexical-util-0.8/parse-floats) >= 0.8.5
Requires:       crate(lexical-util-0.8/power-of-two) >= 0.8.5
Provides:       crate(%{pkgname}/power-of-two) = %{version}

%description -n %{name}+power-of-two
This metapackage enables feature "power-of-two" for the Rust lexical-parse-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+radix
Summary:        Efficient parsing of floats from strings - feature "radix"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/power-of-two) = %{version}
Requires:       crate(lexical-parse-integer-0.8/radix) >= 0.8.5
Requires:       crate(lexical-util-0.8/parse-floats) >= 0.8.5
Requires:       crate(lexical-util-0.8/radix) >= 0.8.5
Provides:       crate(%{pkgname}/radix) = %{version}

%description -n %{name}+radix
This metapackage enables feature "radix" for the Rust lexical-parse-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+safe
Summary:        Efficient parsing of floats from strings - feature "safe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-parse-integer-0.8/safe) >= 0.8.5
Provides:       crate(%{pkgname}/safe) = %{version}

%description -n %{name}+safe
This metapackage enables feature "safe" for the Rust lexical-parse-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Efficient parsing of floats from strings - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-parse-integer-0.8/std) >= 0.8.5
Requires:       crate(lexical-util-0.8/parse-floats) >= 0.8.5
Requires:       crate(lexical-util-0.8/std) >= 0.8.5
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust lexical-parse-float crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
