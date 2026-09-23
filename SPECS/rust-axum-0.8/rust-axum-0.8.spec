# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name axum
%global full_version 0.8.8
%global pkgname axum-0.8

Name:           rust-axum-0.8
Version:        0.8.8
Release:        %autorelease
Summary:        Rust crate "axum"
License:        MIT
URL:            https://github.com/tokio-rs/axum
#!RemoteAsset:  sha256:8b52af3cb4058c895d37317bb27508dccc8e5f2d39454016b297bf4a400597b8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(axum-core-0.5/default) >= 0.5.6
Requires:       crate(bytes-1/default) >= 1.12.0
Requires:       crate(futures-util-0.3/alloc) >= 0.3.32
Requires:       crate(http-1/default) >= 1.4.0
Requires:       crate(http-body-1/default) >= 1.0.1
Requires:       crate(http-body-util-0.1/default) >= 0.1.3
Requires:       crate(itoa-1/default) >= 1.0.18
Requires:       crate(matchit-0.8/default) >= 0.8.4
Requires:       crate(memchr-2/default) >= 2.8.1
Requires:       crate(mime-0.3/default) >= 0.3.17
Requires:       crate(percent-encoding-2/default) >= 2.3.2
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.17
Requires:       crate(serde-core-1/default) >= 1.0.228
Requires:       crate(sync-wrapper-1/default) >= 1.0.2
Requires:       crate(tower-0.5/util) >= 0.5.3
Requires:       crate(tower-layer-0.3/default) >= 0.3.3
Requires:       crate(tower-service-0.3/default) >= 0.3.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/matched-path) = %{version}
Provides:       crate(%{pkgname}/original-uri) = %{version}

%description
Source code for takopackized Rust crate "axum"

%package     -n %{name}+private
Summary:        Web framework that focuses on ergonomics and modularity - feature "__private"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/http1) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(reqwest-0.12/json) >= 0.12.0
Requires:       crate(reqwest-0.12/multipart) >= 0.12.0
Requires:       crate(reqwest-0.12/stream) >= 0.12.0
Provides:       crate(%{pkgname}/private) = %{version}

%description -n %{name}+private
This metapackage enables feature "__private" for the Rust axum crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+private-docs
Summary:        Web framework that focuses on ergonomics and modularity - feature "__private_docs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(axum-core-0.5/private-docs) >= 0.5.6
Requires:       crate(serde-1/default) >= 1.0.211
Requires:       crate(tower-0.5/full) >= 0.5.3
Requires:       crate(tower-0.5/util) >= 0.5.3
Requires:       crate(tower-http-0.6/add-extension) >= 0.6.0
Requires:       crate(tower-http-0.6/auth) >= 0.6.0
Requires:       crate(tower-http-0.6/catch-panic) >= 0.6.0
Requires:       crate(tower-http-0.6/compression-br) >= 0.6.0
Requires:       crate(tower-http-0.6/compression-deflate) >= 0.6.0
Requires:       crate(tower-http-0.6/compression-gzip) >= 0.6.0
Requires:       crate(tower-http-0.6/cors) >= 0.6.0
Requires:       crate(tower-http-0.6/decompression-br) >= 0.6.0
Requires:       crate(tower-http-0.6/decompression-deflate) >= 0.6.0
Requires:       crate(tower-http-0.6/decompression-gzip) >= 0.6.0
Requires:       crate(tower-http-0.6/default) >= 0.6.0
Requires:       crate(tower-http-0.6/follow-redirect) >= 0.6.0
Requires:       crate(tower-http-0.6/fs) >= 0.6.0
Requires:       crate(tower-http-0.6/limit) >= 0.6.0
Requires:       crate(tower-http-0.6/map-request-body) >= 0.6.0
Requires:       crate(tower-http-0.6/map-response-body) >= 0.6.0
Requires:       crate(tower-http-0.6/metrics) >= 0.6.0
Requires:       crate(tower-http-0.6/normalize-path) >= 0.6.0
Requires:       crate(tower-http-0.6/propagate-header) >= 0.6.0
Requires:       crate(tower-http-0.6/redirect) >= 0.6.0
Requires:       crate(tower-http-0.6/request-id) >= 0.6.0
Requires:       crate(tower-http-0.6/sensitive-headers) >= 0.6.0
Requires:       crate(tower-http-0.6/set-header) >= 0.6.0
Requires:       crate(tower-http-0.6/set-status) >= 0.6.0
Requires:       crate(tower-http-0.6/timeout) >= 0.6.0
Requires:       crate(tower-http-0.6/trace) >= 0.6.0
Requires:       crate(tower-http-0.6/util) >= 0.6.0
Requires:       crate(tower-http-0.6/validate-request) >= 0.6.0
Provides:       crate(%{pkgname}/private-docs) = %{version}

%description -n %{name}+private-docs
This metapackage enables feature "__private_docs" for the Rust axum crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Web framework that focuses on ergonomics and modularity - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/form) = %{version}
Requires:       crate(%{pkgname}/http1) = %{version}
Requires:       crate(%{pkgname}/json) = %{version}
Requires:       crate(%{pkgname}/matched-path) = %{version}
Requires:       crate(%{pkgname}/original-uri) = %{version}
Requires:       crate(%{pkgname}/query) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(%{pkgname}/tower-log) = %{version}
Requires:       crate(%{pkgname}/tracing) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust axum crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+form
Summary:        Web framework that focuses on ergonomics and modularity - feature "form" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(form-urlencoded-1/default) >= 1.2.2
Requires:       crate(serde-path-to-error-0.1/default) >= 0.1.20
Requires:       crate(serde-urlencoded-0.7/default) >= 0.7.1
Provides:       crate(%{pkgname}/form) = %{version}
Provides:       crate(%{pkgname}/query) = %{version}

%description -n %{name}+form
This metapackage enables feature "form" for the Rust axum crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "query" feature.

%package     -n %{name}+http1
Summary:        Web framework that focuses on ergonomics and modularity - feature "http1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-1/default) >= 1.10.1
Requires:       crate(hyper-1/http1) >= 1.10.1
Requires:       crate(hyper-util-0.1/http1) >= 0.1.20
Requires:       crate(hyper-util-0.1/server) >= 0.1.20
Requires:       crate(hyper-util-0.1/service) >= 0.1.20
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.20
Provides:       crate(%{pkgname}/http1) = %{version}

%description -n %{name}+http1
This metapackage enables feature "http1" for the Rust axum crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http2
Summary:        Web framework that focuses on ergonomics and modularity - feature "http2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-1/default) >= 1.10.1
Requires:       crate(hyper-1/http2) >= 1.10.1
Requires:       crate(hyper-util-0.1/http2) >= 0.1.20
Requires:       crate(hyper-util-0.1/server) >= 0.1.20
Requires:       crate(hyper-util-0.1/service) >= 0.1.20
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.20
Provides:       crate(%{pkgname}/http2) = %{version}

%description -n %{name}+http2
This metapackage enables feature "http2" for the Rust axum crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Web framework that focuses on ergonomics and modularity - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.150
Requires:       crate(serde-json-1/raw-value) >= 1.0.150
Requires:       crate(serde-path-to-error-0.1/default) >= 0.1.20
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
This metapackage enables feature "json" for the Rust axum crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        Web framework that focuses on ergonomics and modularity - feature "macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(axum-macros-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/macros) = %{version}

%description -n %{name}+macros
This metapackage enables feature "macros" for the Rust axum crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+multipart
Summary:        Web framework that focuses on ergonomics and modularity - feature "multipart"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(multer-3/default) >= 3.0.0
Provides:       crate(%{pkgname}/multipart) = %{version}

%description -n %{name}+multipart
This metapackage enables feature "multipart" for the Rust axum crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Web framework that focuses on ergonomics and modularity - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyper-util-0.1/default) >= 0.1.20
Requires:       crate(hyper-util-0.1/server) >= 0.1.20
Requires:       crate(hyper-util-0.1/service) >= 0.1.20
Requires:       crate(hyper-util-0.1/tokio) >= 0.1.20
Requires:       crate(tokio-1/default) >= 1.53.1
Requires:       crate(tokio-1/macros) >= 1.53.1
Requires:       crate(tokio-1/net) >= 1.53.1
Requires:       crate(tokio-1/rt) >= 1.53.1
Requires:       crate(tokio-1/time) >= 1.53.1
Requires:       crate(tower-0.5/make) >= 0.5.3
Requires:       crate(tower-0.5/util) >= 0.5.3
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust axum crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tower-log
Summary:        Web framework that focuses on ergonomics and modularity - feature "tower-log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tower-0.5/log) >= 0.5.3
Requires:       crate(tower-0.5/util) >= 0.5.3
Provides:       crate(%{pkgname}/tower-log) = %{version}

%description -n %{name}+tower-log
This metapackage enables feature "tower-log" for the Rust axum crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Web framework that focuses on ergonomics and modularity - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(axum-core-0.5/tracing) >= 0.5.6
Requires:       crate(tracing-0.1) >= 0.1.44
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust axum crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ws
Summary:        Web framework that focuses on ergonomics and modularity - feature "ws"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(hyper-1/default) >= 1.10.1
Requires:       crate(sha1-0.10/default) >= 0.10.0
Requires:       crate(tokio-tungstenite-0.28/default) >= 0.28.0
Provides:       crate(%{pkgname}/ws) = %{version}

%description -n %{name}+ws
This metapackage enables feature "ws" for the Rust axum crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
