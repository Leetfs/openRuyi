# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name malachite-nz
%global full_version 0.4.22
%global pkgname malachite-nz-0.4

Name:           rust-malachite-nz-0.4
Version:        0.4.22
Release:        %autorelease
Summary:        Rust crate "malachite-nz"
License:        LGPL-3.0-only
URL:            https://malachite.rs/
#!RemoteAsset:  sha256:34a79feebb2bc9aa7762047c8e5495269a367da6b5a90a99882a0aeeac1841f7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(itertools-0.11/use-alloc) >= 0.11.0
Requires:       crate(libm-0.2) >= 0.2.16
Requires:       crate(malachite-base-0.4) >= 0.4.22

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/32-bit-limbs) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/float-helpers) = %{version}

%description
Source code for takopackized Rust crate "malachite-nz"

%package     -n %{name}+embed-doc-image
Summary:        Bignum types Natural and Integer, with efficient algorithms partially derived from GMP and FLINT - feature "embed-doc-image" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(embed-doc-image-0.1/default) >= 0.1.4
Provides:       crate(%{pkgname}/doc-images) = %{version}
Provides:       crate(%{pkgname}/embed-doc-image) = %{version}

%description -n %{name}+embed-doc-image
This metapackage enables feature "embed-doc-image" for the Rust malachite-nz crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "doc-images" feature.

%package     -n %{name}+enable-pyo3
Summary:        Bignum types Natural and Integer, with efficient algorithms partially derived from GMP and FLINT - feature "enable_pyo3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pyo3) = %{version}
Requires:       crate(%{pkgname}/pyo3-build-config) = %{version}
Provides:       crate(%{pkgname}/enable-pyo3) = %{version}

%description -n %{name}+enable-pyo3
This metapackage enables feature "enable_pyo3" for the Rust malachite-nz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indoc
Summary:        Bignum types Natural and Integer, with efficient algorithms partially derived from GMP and FLINT - feature "indoc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indoc-2/default) >= 2.0.4
Provides:       crate(%{pkgname}/indoc) = %{version}

%description -n %{name}+indoc
This metapackage enables feature "indoc" for the Rust malachite-nz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num
Summary:        Bignum types Natural and Integer, with efficient algorithms partially derived from GMP and FLINT - feature "num"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-0.4/default) >= 0.4.3
Requires:       crate(num-0.4/serde) >= 0.4.3
Provides:       crate(%{pkgname}/num) = %{version}

%description -n %{name}+num
This metapackage enables feature "num" for the Rust malachite-nz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pyo3
Summary:        Bignum types Natural and Integer, with efficient algorithms partially derived from GMP and FLINT - feature "pyo3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-0.21/default) >= 0.21.2
Provides:       crate(%{pkgname}/pyo3) = %{version}

%description -n %{name}+pyo3
This metapackage enables feature "pyo3" for the Rust malachite-nz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pyo3-build-config
Summary:        Bignum types Natural and Integer, with efficient algorithms partially derived from GMP and FLINT - feature "pyo3-build-config"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-build-config-0.21/default) >= 0.21.2
Requires:       crate(pyo3-build-config-0.21/resolve-config) >= 0.21.2
Provides:       crate(%{pkgname}/pyo3-build-config) = %{version}

%description -n %{name}+pyo3-build-config
This metapackage enables feature "pyo3-build-config" for the Rust malachite-nz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+random
Summary:        Bignum types Natural and Integer, with efficient algorithms partially derived from GMP and FLINT - feature "random"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(malachite-base-0.4/random) >= 0.4.22
Provides:       crate(%{pkgname}/random) = %{version}

%description -n %{name}+random
This metapackage enables feature "random" for the Rust malachite-nz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rug
Summary:        Bignum types Natural and Integer, with efficient algorithms partially derived from GMP and FLINT - feature "rug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rug-1/integer) >= 1.24.1
Requires:       crate(rug-1/serde) >= 1.24.1
Provides:       crate(%{pkgname}/rug) = %{version}

%description -n %{name}+rug
This metapackage enables feature "rug" for the Rust malachite-nz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Bignum types Natural and Integer, with efficient algorithms partially derived from GMP and FLINT - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.188
Requires:       crate(serde-1/derive) >= 1.0.188
Provides:       crate(%{pkgname}/enable-serde) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust malachite-nz crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "enable_serde" feature.

%package     -n %{name}+serde-json
Summary:        Bignum types Natural and Integer, with efficient algorithms partially derived from GMP and FLINT - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.105
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust malachite-nz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+test-build
Summary:        Bignum types Natural and Integer, with efficient algorithms partially derived from GMP and FLINT - feature "test_build" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/indoc) = %{version}
Requires:       crate(%{pkgname}/num) = %{version}
Requires:       crate(%{pkgname}/pyo3) = %{version}
Requires:       crate(%{pkgname}/pyo3-build-config) = %{version}
Requires:       crate(%{pkgname}/random) = %{version}
Requires:       crate(%{pkgname}/rug) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Requires:       crate(malachite-base-0.4/test-build) >= 0.4.22
Provides:       crate(%{pkgname}/bin-build) = %{version}
Provides:       crate(%{pkgname}/test-build) = %{version}

%description -n %{name}+test-build
This metapackage enables feature "test_build" for the Rust malachite-nz crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bin_build" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
