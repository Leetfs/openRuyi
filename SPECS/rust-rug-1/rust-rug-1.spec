# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rug
%global full_version 1.24.1
%global pkgname rug-1

Name:           rust-rug-1
Version:        1.24.1
Release:        %autorelease
Summary:        Rust crate "rug"
License:        LGPL-3.0+
URL:            https://gitlab.com/tspiteri/rug
#!RemoteAsset:  sha256:a8df4099c6fa90a1a7f5ddc0c7fba50991080fa2084d5a78808a5a3cab406bb9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(az-1/default) >= 1.1.0
Requires:       crate(libc-0.2) >= 0.2.44
Requires:       crate(libm-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/fail-on-warnings) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "rug"

%package     -n %{name}+complex
Summary:        Arbitrary-precision integers, rational, floating-point and complex numbers based on GMP, MPFR and MPC - feature "complex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/float) = %{version}
Requires:       crate(gmp-mpfr-sys-1/mpc) >= 1.6.0
Provides:       crate(%{pkgname}/complex) = %{version}

%description -n %{name}+complex
This metapackage enables feature "complex" for the Rust rug crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Arbitrary-precision integers, rational, floating-point and complex numbers based on GMP, MPFR and MPC - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/complex) = %{version}
Requires:       crate(%{pkgname}/float) = %{version}
Requires:       crate(%{pkgname}/integer) = %{version}
Requires:       crate(%{pkgname}/rand) = %{version}
Requires:       crate(%{pkgname}/rational) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rug crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+float
Summary:        Arbitrary-precision integers, rational, floating-point and complex numbers based on GMP, MPFR and MPC - feature "float"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gmp-mpfr-sys-1/mpfr) >= 1.6.0
Provides:       crate(%{pkgname}/float) = %{version}

%description -n %{name}+float
This metapackage enables feature "float" for the Rust rug crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gmp-mpfr-sys
Summary:        Arbitrary-precision integers, rational, floating-point and complex numbers based on GMP, MPFR and MPC - feature "gmp-mpfr-sys" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gmp-mpfr-sys-1) >= 1.6.0
Provides:       crate(%{pkgname}/gmp-mpfr-sys) = %{version}
Provides:       crate(%{pkgname}/integer) = %{version}
Provides:       crate(%{pkgname}/rand) = %{version}
Provides:       crate(%{pkgname}/rational) = %{version}

%description -n %{name}+gmp-mpfr-sys
This metapackage enables feature "gmp-mpfr-sys" for the Rust rug crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "integer", "rand", and "rational" features.

%package     -n %{name}+num-integer
Summary:        Arbitrary-precision integers, rational, floating-point and complex numbers based on GMP, MPFR and MPC - feature "num-integer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-integer-0.1/i128) >= 0.1.45
Provides:       crate(%{pkgname}/num-integer) = %{version}

%description -n %{name}+num-integer
This metapackage enables feature "num-integer" for the Rust rug crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-traits
Summary:        Arbitrary-precision integers, rational, floating-point and complex numbers based on GMP, MPFR and MPC - feature "num-traits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/num-integer) = %{version}
Requires:       crate(num-traits-0.2/i128) >= 0.2.15
Requires:       crate(num-traits-0.2/std) >= 0.2.15
Provides:       crate(%{pkgname}/num-traits) = %{version}

%description -n %{name}+num-traits
This metapackage enables feature "num-traits" for the Rust rug crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Arbitrary-precision integers, rational, floating-point and complex numbers based on GMP, MPFR and MPC - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(serde-1/default) >= 1.0.25
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rug crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
