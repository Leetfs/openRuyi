# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-openai
%global full_version 0.14.3
%global pkgname async-openai-0.14

Name:           rust-async-openai-0.14
Version:        0.14.3
Release:        %autorelease
Summary:        Rust crate "async-openai"
License:        MIT
URL:            https://github.com/64bit/async-openai
#!RemoteAsset:  sha256:7e1df052c2bd7b241fc828bc2fda74ce9a7ef05e0a593c37275aaaba52caf49d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-convert-1/default) >= 1.0.0
Requires:       crate(backoff-0.4/default) >= 0.4.0
Requires:       crate(backoff-0.4/tokio) >= 0.4.0
Requires:       crate(base64-0.21/default) >= 0.21.0
Requires:       crate(derive-builder-0.12/default) >= 0.12.0
Requires:       crate(futures-0.3/default) >= 0.3.26
Requires:       crate(rand-0.8/default) >= 0.8.5
Requires:       crate(reqwest-0.11/json) >= 0.11.14
Requires:       crate(reqwest-0.11/multipart) >= 0.11.14
Requires:       crate(reqwest-0.11/stream) >= 0.11.14
Requires:       crate(reqwest-eventsource-0.4/default) >= 0.4.0
Requires:       crate(serde-1/default) >= 1.0.152
Requires:       crate(serde-1/derive) >= 1.0.152
Requires:       crate(serde-1/rc) >= 1.0.152
Requires:       crate(serde-json-1/default) >= 1.0.93
Requires:       crate(thiserror-1/default) >= 1.0.38
Requires:       crate(tokio-1/default) >= 1.25.0
Requires:       crate(tokio-1/fs) >= 1.25.0
Requires:       crate(tokio-1/macros) >= 1.25.0
Requires:       crate(tokio-stream-0.1/default) >= 0.1.11
Requires:       crate(tokio-util-0.7/codec) >= 0.7.7
Requires:       crate(tokio-util-0.7/default) >= 0.7.7
Requires:       crate(tokio-util-0.7/io-util) >= 0.7.7
Requires:       crate(tracing-0.1/default) >= 0.1.37

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "async-openai"

%package     -n %{name}+native-tls
Summary:        Async bindings for OpenAI REST API based on OpenAPI spec - feature "native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.11/json) >= 0.11.14
Requires:       crate(reqwest-0.11/multipart) >= 0.11.14
Requires:       crate(reqwest-0.11/native-tls) >= 0.11.14
Requires:       crate(reqwest-0.11/stream) >= 0.11.14
Provides:       crate(%{pkgname}/native-tls) = %{version}

%description -n %{name}+native-tls
This metapackage enables feature "native-tls" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls-vendored
Summary:        Async bindings for OpenAI REST API based on OpenAPI spec - feature "native-tls-vendored"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.11/json) >= 0.11.14
Requires:       crate(reqwest-0.11/multipart) >= 0.11.14
Requires:       crate(reqwest-0.11/native-tls-vendored) >= 0.11.14
Requires:       crate(reqwest-0.11/stream) >= 0.11.14
Provides:       crate(%{pkgname}/native-tls-vendored) = %{version}

%description -n %{name}+native-tls-vendored
This metapackage enables feature "native-tls-vendored" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustls
Summary:        Async bindings for OpenAI REST API based on OpenAPI spec - feature "rustls" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.11/json) >= 0.11.14
Requires:       crate(reqwest-0.11/multipart) >= 0.11.14
Requires:       crate(reqwest-0.11/rustls-tls-native-roots) >= 0.11.14
Requires:       crate(reqwest-0.11/stream) >= 0.11.14
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rustls) = %{version}

%description -n %{name}+rustls
This metapackage enables feature "rustls" for the Rust async-openai crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
