# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name malachite
%global full_version 0.4.22
%global pkgname malachite-0.4

Name:           rust-malachite-0.4
Version:        0.4.22
Release:        %autorelease
Summary:        Rust crate "malachite"
License:        LGPL-3.0-only
URL:            https://malachite.rs/
#!RemoteAsset:  sha256:2fbdf9cb251732db30a7200ebb6ae5d22fe8e11397364416617d2c2cf0c51cb5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(malachite-base-0.4) >= 0.4.22

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "malachite"

%package     -n %{name}+32-bit-limbs
Summary:        Arbitrary-precision arithmetic, with efficient algorithms partially derived from GMP, FLINT, and MPFR - feature "32_bit_limbs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(malachite-float-0.4/32-bit-limbs) >= 0.4.22
Requires:       crate(malachite-nz-0.4/32-bit-limbs) >= 0.4.22
Requires:       crate(malachite-q-0.4/32-bit-limbs) >= 0.4.22
Provides:       crate(%{pkgname}/32-bit-limbs) = %{version}

%description -n %{name}+32-bit-limbs
This metapackage enables feature "32_bit_limbs" for the Rust malachite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Arbitrary-precision arithmetic, with efficient algorithms partially derived from GMP, FLINT, and MPFR - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/naturals-and-integers) = %{version}
Requires:       crate(%{pkgname}/rationals) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust malachite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+embed-doc-image
Summary:        Arbitrary-precision arithmetic, with efficient algorithms partially derived from GMP, FLINT, and MPFR - feature "embed-doc-image"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(embed-doc-image-0.1/default) >= 0.1.4
Provides:       crate(%{pkgname}/embed-doc-image) = %{version}

%description -n %{name}+embed-doc-image
This metapackage enables feature "embed-doc-image" for the Rust malachite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+enable-pyo3
Summary:        Arbitrary-precision arithmetic, with efficient algorithms partially derived from GMP, FLINT, and MPFR - feature "enable_pyo3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(malachite-nz-0.4/enable-pyo3) >= 0.4.22
Provides:       crate(%{pkgname}/enable-pyo3) = %{version}

%description -n %{name}+enable-pyo3
This metapackage enables feature "enable_pyo3" for the Rust malachite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+enable-serde
Summary:        Arbitrary-precision arithmetic, with efficient algorithms partially derived from GMP, FLINT, and MPFR - feature "enable_serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(malachite-float-0.4/enable-serde) >= 0.4.22
Requires:       crate(malachite-nz-0.4/enable-serde) >= 0.4.22
Requires:       crate(malachite-q-0.4/enable-serde) >= 0.4.22
Provides:       crate(%{pkgname}/enable-serde) = %{version}

%description -n %{name}+enable-serde
This metapackage enables feature "enable_serde" for the Rust malachite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+malachite-float
Summary:        Arbitrary-precision arithmetic, with efficient algorithms partially derived from GMP, FLINT, and MPFR - feature "malachite-float" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(malachite-float-0.4) >= 0.4.22
Provides:       crate(%{pkgname}/floats) = %{version}
Provides:       crate(%{pkgname}/malachite-float) = %{version}

%description -n %{name}+malachite-float
This metapackage enables feature "malachite-float" for the Rust malachite crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "floats" feature.

%package     -n %{name}+malachite-nz
Summary:        Arbitrary-precision arithmetic, with efficient algorithms partially derived from GMP, FLINT, and MPFR - feature "malachite-nz" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(malachite-nz-0.4) >= 0.4.22
Provides:       crate(%{pkgname}/malachite-nz) = %{version}
Provides:       crate(%{pkgname}/naturals-and-integers) = %{version}

%description -n %{name}+malachite-nz
This metapackage enables feature "malachite-nz" for the Rust malachite crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "naturals_and_integers" feature.

%package     -n %{name}+malachite-q
Summary:        Arbitrary-precision arithmetic, with efficient algorithms partially derived from GMP, FLINT, and MPFR - feature "malachite-q" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(malachite-q-0.4) >= 0.4.22
Provides:       crate(%{pkgname}/malachite-q) = %{version}
Provides:       crate(%{pkgname}/rationals) = %{version}

%description -n %{name}+malachite-q
This metapackage enables feature "malachite-q" for the Rust malachite crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rationals" feature.

%package     -n %{name}+random
Summary:        Arbitrary-precision arithmetic, with efficient algorithms partially derived from GMP, FLINT, and MPFR - feature "random"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(malachite-base-0.4/random) >= 0.4.22
Requires:       crate(malachite-float-0.4/random) >= 0.4.22
Requires:       crate(malachite-nz-0.4/random) >= 0.4.22
Requires:       crate(malachite-q-0.4/random) >= 0.4.22
Provides:       crate(%{pkgname}/random) = %{version}

%description -n %{name}+random
This metapackage enables feature "random" for the Rust malachite crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Arbitrary-precision arithmetic, with efficient algorithms partially derived from GMP, FLINT, and MPFR - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.188
Requires:       crate(serde-1/derive) >= 1.0.188
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust malachite crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
