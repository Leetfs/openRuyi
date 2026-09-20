# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name multer
%global full_version 3.1.0
%global pkgname multer-3

Name:           rust-multer-3
Version:        3.1.0
Release:        %autorelease
Summary:        Rust crate "multer"
License:        MIT
URL:            https://github.com/rwf2/multer
#!RemoteAsset:  sha256:83e87776546dc87511aa5ee218730c92b666d7264ab6ed41f9d215af9cd5224b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(encoding-rs-0.8/default) >= 0.8.20
Requires:       crate(futures-util-0.3) >= 0.3.0
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(httparse-1/default) >= 1.3.0
Requires:       crate(memchr-2/default) >= 2.4.0
Requires:       crate(mime-0.3/default) >= 0.3.10
Requires:       crate(spin-0.9/spin-mutex) >= 0.9.0
Requires:       crate(version-check-0.9) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "multer"

%package     -n %{name}+json
Summary:        Async parser for `multipart/form-data` content-type in Rust - feature "json" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
This metapackage enables feature "json" for the Rust multer crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "all" feature.

%package     -n %{name}+log
Summary:        Async parser for `multipart/form-data` content-type in Rust - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.15
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust multer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Async parser for `multipart/form-data` content-type in Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust multer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Async parser for `multipart/form-data` content-type in Rust - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust multer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Async parser for `multipart/form-data` content-type in Rust - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust multer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-io
Summary:        Async parser for `multipart/form-data` content-type in Rust - feature "tokio-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(%{pkgname}/tokio-util) = %{version}
Provides:       crate(%{pkgname}/tokio-io) = %{version}

%description -n %{name}+tokio-io
This metapackage enables feature "tokio-io" for the Rust multer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-util
Summary:        Async parser for `multipart/form-data` content-type in Rust - feature "tokio-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-util-0.7/default) >= 0.7.0
Requires:       crate(tokio-util-0.7/io) >= 0.7.0
Provides:       crate(%{pkgname}/tokio-util) = %{version}

%description -n %{name}+tokio-util
This metapackage enables feature "tokio-util" for the Rust multer crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
