# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name malachite-q
%global full_version 0.4.22
%global pkgname malachite-q-0.4

Name:           rust-malachite-q-0.4
Version:        0.4.22
Release:        %autorelease
Summary:        Rust crate "malachite-q"
License:        LGPL-3.0-only
URL:            https://malachite.rs/
#!RemoteAsset:  sha256:50f235d5747b1256b47620f5640c2a17a88c7569eebdf27cd9cb130e1a619191
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(itertools-0.11/use-alloc) >= 0.11.0
Requires:       crate(malachite-base-0.4) >= 0.4.22
Requires:       crate(malachite-nz-0.4) >= 0.4.22

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "malachite-q"

%package     -n %{name}+32-bit-limbs
Summary:        Arbitrary-precision type Rational, with efficient algorithms partially derived from GMP and FLINT - feature "32_bit_limbs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(malachite-nz-0.4/32-bit-limbs) >= 0.4.22
Provides:       crate(%{pkgname}/32-bit-limbs) = %{version}

%description -n %{name}+32-bit-limbs
This metapackage enables feature "32_bit_limbs" for the Rust malachite-q crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+enable-serde
Summary:        Arbitrary-precision type Rational, with efficient algorithms partially derived from GMP and FLINT - feature "enable_serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(malachite-nz-0.4/enable-serde) >= 0.4.22
Provides:       crate(%{pkgname}/enable-serde) = %{version}

%description -n %{name}+enable-serde
This metapackage enables feature "enable_serde" for the Rust malachite-q crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num
Summary:        Arbitrary-precision type Rational, with efficient algorithms partially derived from GMP and FLINT - feature "num"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-0.4/default) >= 0.4.3
Requires:       crate(num-0.4/serde) >= 0.4.3
Provides:       crate(%{pkgname}/num) = %{version}

%description -n %{name}+num
This metapackage enables feature "num" for the Rust malachite-q crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+random
Summary:        Arbitrary-precision type Rational, with efficient algorithms partially derived from GMP and FLINT - feature "random"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(malachite-base-0.4/random) >= 0.4.22
Requires:       crate(malachite-nz-0.4/random) >= 0.4.22
Provides:       crate(%{pkgname}/random) = %{version}

%description -n %{name}+random
This metapackage enables feature "random" for the Rust malachite-q crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rug
Summary:        Arbitrary-precision type Rational, with efficient algorithms partially derived from GMP and FLINT - feature "rug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rug-1/rational) >= 1.24.1
Requires:       crate(rug-1/serde) >= 1.24.1
Provides:       crate(%{pkgname}/rug) = %{version}

%description -n %{name}+rug
This metapackage enables feature "rug" for the Rust malachite-q crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Arbitrary-precision type Rational, with efficient algorithms partially derived from GMP and FLINT - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.188
Requires:       crate(serde-1/derive) >= 1.0.188
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust malachite-q crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Arbitrary-precision type Rational, with efficient algorithms partially derived from GMP and FLINT - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.105
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust malachite-q crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+test-build
Summary:        Arbitrary-precision type Rational, with efficient algorithms partially derived from GMP and FLINT - feature "test_build" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/num) = %{version}
Requires:       crate(%{pkgname}/random) = %{version}
Requires:       crate(%{pkgname}/rug) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Requires:       crate(malachite-base-0.4/test-build) >= 0.4.22
Requires:       crate(malachite-nz-0.4/test-build) >= 0.4.22
Provides:       crate(%{pkgname}/bin-build) = %{version}
Provides:       crate(%{pkgname}/test-build) = %{version}

%description -n %{name}+test-build
This metapackage enables feature "test_build" for the Rust malachite-q crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bin_build" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
