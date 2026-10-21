# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uv-pep508
%global full_version 0.0.96
%global pkgname uv-pep508-0.0.96

Name:           rust-uv-pep508-0.0.96
Version:        0.0.96
Release:        %autorelease
Summary:        Rust crate "uv-pep508"
License:        Apache-2.0 OR BSD-2-Clause
URL:            https://pypi.org/project/uv/
#!RemoteAsset:  sha256:72dc9cb31db1b87ca1b0bab1c5673239fe6112ff6cd79a3ce397a216b8131b41
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arcstr-1) >= 1.2.0
Requires:       crate(astral-version-ranges-0.2) >= 0.2.2
Requires:       crate(boxcar-0.2) >= 0.2.5
Requires:       crate(hashbrown-0.17/equivalent) >= 0.17.0
Requires:       crate(hashbrown-0.17/inline-more) >= 0.17.0
Requires:       crate(indexmap-2/std) >= 2.5.0
Requires:       crate(itertools-0.14/use-std) >= 0.14.0
Requires:       crate(rustc-hash-2/std) >= 2.0.0
Requires:       crate(serde-1/derive) >= 1.0.210
Requires:       crate(serde-1/rc) >= 1.0.210
Requires:       crate(serde-1/std) >= 1.0.210
Requires:       crate(smallvec-1) >= 1.13.2
Requires:       crate(thiserror-2/std) >= 2.0.0
Requires:       crate(unicode-width-0.2) >= 0.2.0
Requires:       crate(url-2/serde) >= 2.5.2
Requires:       crate(url-2/std) >= 2.5.2
Requires:       crate(uv-cache-key-0.0.96/default) >= 0.0.96
Requires:       crate(uv-fs-0.0.96/default) >= 0.0.96
Requires:       crate(uv-fs-0.0.96/serde) >= 0.0.96
Requires:       crate(uv-fs-0.0.96/tokio) >= 0.0.96
Requires:       crate(uv-normalize-0.0.96/default) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/default) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/rkyv) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/tracing) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/version-ranges) >= 0.0.96
Requires:       crate(uv-redacted-0.0.96/default) >= 0.0.96

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/non-pep508-extensions) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/unsafe-url) = %{version}

%description
Source code for takopackized Rust crate "uv-pep508"

%package     -n %{name}+rkyv
Summary:        Internal component crate of uv - feature "rkyv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-0.8/bytecheck) >= 0.8.14
Requires:       crate(rkyv-0.8/std) >= 0.8.14
Provides:       crate(%{pkgname}/rkyv) = %{version}

%description -n %{name}+rkyv
This metapackage enables feature "rkyv" for the Rust uv-pep508 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schemars
Summary:        Internal component crate of uv - feature "schemars"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(schemars-1/derive) >= 1.0.0
Requires:       crate(schemars-1/std) >= 1.0.0
Requires:       crate(schemars-1/url2) >= 1.0.0
Provides:       crate(%{pkgname}/schemars) = %{version}

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust uv-pep508 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Internal component crate of uv - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1/attributes) >= 0.1.40
Requires:       crate(tracing-0.1/std) >= 0.1.40
Requires:       crate(uv-pep440-0.0.96/rkyv) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/tracing) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/version-ranges) >= 0.0.96
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust uv-pep508 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
