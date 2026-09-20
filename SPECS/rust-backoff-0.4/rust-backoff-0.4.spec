# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name backoff
%global full_version 0.4.0
%global pkgname backoff-0.4

Name:           rust-backoff-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "backoff"
License:        MIT OR Apache-2.0
URL:            https://github.com/ihrwein/backoff
#!RemoteAsset:  sha256:b62ddb9cb1ec0a098ad4bbf9344d0713fa193ae1a80af55febcff2627b6a00c1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(getrandom-0.2/default) >= 0.2.17
Requires:       crate(instant-0.1/default) >= 0.1.13
Requires:       crate(rand-0.8/default) >= 0.8.5

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "backoff"

%package     -n %{name}+async-std
Summary:        Retry operations with exponential backoff policy - feature "async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-std-1) = %{version}
Requires:       crate(%{pkgname}/futures) = %{version}
Provides:       crate(%{pkgname}/async-std) = %{version}

%description -n %{name}+async-std
This metapackage enables feature "async-std" for the Rust backoff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-std-1
Summary:        Retry operations with exponential backoff policy - feature "async_std_1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-std-1/default) >= 1.9.0
Provides:       crate(%{pkgname}/async-std-1) = %{version}

%description -n %{name}+async-std-1
This metapackage enables feature "async_std_1" for the Rust backoff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Retry operations with exponential backoff policy - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-core) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust backoff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-core
Summary:        Retry operations with exponential backoff policy - feature "futures-core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3) >= 0.3.32
Provides:       crate(%{pkgname}/futures-core) = %{version}

%description -n %{name}+futures-core
This metapackage enables feature "futures-core" for the Rust backoff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pin-project-lite
Summary:        Retry operations with exponential backoff policy - feature "pin-project-lite"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17
Provides:       crate(%{pkgname}/pin-project-lite) = %{version}

%description -n %{name}+pin-project-lite
This metapackage enables feature "pin-project-lite" for the Rust backoff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Retry operations with exponential backoff policy - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures) = %{version}
Requires:       crate(%{pkgname}/tokio-1) = %{version}
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust backoff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-1
Summary:        Retry operations with exponential backoff policy - feature "tokio_1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.52.3
Requires:       crate(tokio-1/time) >= 1.52.3
Provides:       crate(%{pkgname}/tokio-1) = %{version}

%description -n %{name}+tokio-1
This metapackage enables feature "tokio_1" for the Rust backoff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-bindgen
Summary:        Retry operations with exponential backoff policy - feature "wasm-bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.2/js) >= 0.2.17
Requires:       crate(instant-0.1/wasm-bindgen) >= 0.1.13
Provides:       crate(%{pkgname}/wasm-bindgen) = %{version}

%description -n %{name}+wasm-bindgen
This metapackage enables feature "wasm-bindgen" for the Rust backoff crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
