# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name asynchronous-codec
%global full_version 0.7.0
%global pkgname asynchronous-codec-0.7

Name:           rust-asynchronous-codec-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "asynchronous-codec"
License:        MIT
URL:            https://github.com/mxinden/asynchronous-codec
#!RemoteAsset:  sha256:a860072022177f903e59730004fb5dc13db9275b79bb2aef7ba8ce831956c233
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.12.0
Requires:       crate(futures-sink-0.3/default) >= 0.3.32
Requires:       crate(futures-util-0.3/default) >= 0.3.32
Requires:       crate(futures-util-0.3/io) >= 0.3.32
Requires:       crate(memchr-2/default) >= 2.8.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "asynchronous-codec"

%package     -n %{name}+cbor
Summary:        Utilities for encoding and decoding frames using `async/await` - feature "cbor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-cbor) = %{version}
Provides:       crate(%{pkgname}/cbor) = %{version}

%description -n %{name}+cbor
This metapackage enables feature "cbor" for the Rust asynchronous-codec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Utilities for encoding and decoding frames using `async/await` - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
This metapackage enables feature "json" for the Rust asynchronous-codec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Utilities for encoding and decoding frames using `async/await` - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust asynchronous-codec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-cbor
Summary:        Utilities for encoding and decoding frames using `async/await` - feature "serde_cbor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-cbor-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}/serde-cbor) = %{version}

%description -n %{name}+serde-cbor
This metapackage enables feature "serde_cbor" for the Rust asynchronous-codec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Utilities for encoding and decoding frames using `async/await` - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust asynchronous-codec crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
