# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name malachite-base
%global full_version 0.4.22
%global pkgname malachite-base-0.4

Name:           rust-malachite-base-0.4
Version:        0.4.22
Release:        %autorelease
Summary:        Rust crate "malachite-base"
License:        LGPL-3.0-only
URL:            https://malachite.rs/
#!RemoteAsset:  sha256:5ea0ed76adf7defc1a92240b5c36d5368cfe9251640dcce5bd2d0b7c1fd87aeb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hashbrown-0.14/ahash) >= 0.14.5
Requires:       crate(hashbrown-0.14/inline-more) >= 0.14.5
Requires:       crate(itertools-0.11/use-alloc) >= 0.11.0
Requires:       crate(libm-0.2) >= 0.2.16
Requires:       crate(ryu-1) >= 1.0.23

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "malachite-base"

%package     -n %{name}+bin-build
Summary:        Collection of utilities, including new arithmetic traits and iterators that generate all values of a type - feature "bin_build"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/test-build) = %{version}
Requires:       crate(%{pkgname}/walkdir) = %{version}
Provides:       crate(%{pkgname}/bin-build) = %{version}

%description -n %{name}+bin-build
This metapackage enables feature "bin_build" for the Rust malachite-base crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clap
Summary:        Collection of utilities, including new arithmetic traits and iterators that generate all values of a type - feature "clap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-2/default) >= 2.33.1
Provides:       crate(%{pkgname}/clap) = %{version}

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust malachite-base crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Collection of utilities, including new arithmetic traits and iterators that generate all values of a type - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.2/js) >= 0.2.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust malachite-base crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnuplot
Summary:        Collection of utilities, including new arithmetic traits and iterators that generate all values of a type - feature "gnuplot"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gnuplot-0.0.39/default) >= 0.0.39
Provides:       crate(%{pkgname}/gnuplot) = %{version}

%description -n %{name}+gnuplot
This metapackage enables feature "gnuplot" for the Rust malachite-base crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Collection of utilities, including new arithmetic traits and iterators that generate all values of a type - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.8) >= 0.8.5
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust malachite-base crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-chacha
Summary:        Collection of utilities, including new arithmetic traits and iterators that generate all values of a type - feature "rand_chacha"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-chacha-0.3) >= 0.3.1
Provides:       crate(%{pkgname}/rand-chacha) = %{version}

%description -n %{name}+rand-chacha
This metapackage enables feature "rand_chacha" for the Rust malachite-base crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+random
Summary:        Collection of utilities, including new arithmetic traits and iterators that generate all values of a type - feature "random"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/getrandom) = %{version}
Requires:       crate(%{pkgname}/rand) = %{version}
Requires:       crate(%{pkgname}/rand-chacha) = %{version}
Requires:       crate(%{pkgname}/sha3) = %{version}
Provides:       crate(%{pkgname}/random) = %{version}

%description -n %{name}+random
This metapackage enables feature "random" for the Rust malachite-base crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha3
Summary:        Collection of utilities, including new arithmetic traits and iterators that generate all values of a type - feature "sha3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha3-0.10) >= 0.10.8
Provides:       crate(%{pkgname}/sha3) = %{version}

%description -n %{name}+sha3
This metapackage enables feature "sha3" for the Rust malachite-base crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+test-build
Summary:        Collection of utilities, including new arithmetic traits and iterators that generate all values of a type - feature "test_build"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clap) = %{version}
Requires:       crate(%{pkgname}/gnuplot) = %{version}
Requires:       crate(%{pkgname}/random) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Requires:       crate(itertools-0.11/use-alloc) >= 0.11.0
Requires:       crate(itertools-0.11/use-std) >= 0.11.0
Provides:       crate(%{pkgname}/test-build) = %{version}

%description -n %{name}+test-build
This metapackage enables feature "test_build" for the Rust malachite-base crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Collection of utilities, including new arithmetic traits and iterators that generate all values of a type - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/default) >= 0.3.28
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust malachite-base crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+walkdir
Summary:        Collection of utilities, including new arithmetic traits and iterators that generate all values of a type - feature "walkdir"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(walkdir-2/default) >= 2.3.3
Provides:       crate(%{pkgname}/walkdir) = %{version}

%description -n %{name}+walkdir
This metapackage enables feature "walkdir" for the Rust malachite-base crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
