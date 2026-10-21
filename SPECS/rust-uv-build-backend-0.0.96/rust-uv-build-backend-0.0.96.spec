# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uv-build-backend
%global full_version 0.0.96
%global pkgname uv-build-backend-0.0.96

Name:           rust-uv-build-backend-0.0.96
Version:        0.0.96
Release:        %autorelease
Summary:        Rust crate "uv-build-backend"
License:        MIT OR Apache-2.0
URL:            https://pypi.org/project/uv/
#!RemoteAsset:  sha256:7bcc77308081471d53204517c77a0781504e4c5a1a9078c20343de036cecd342
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(astral-async-zip-0.0.22/deflate) >= 0.0.22
Requires:       crate(astral-tokio-tar-0.7) >= 0.7.0
Requires:       crate(astral-version-ranges-0.2) >= 0.2.2
Requires:       crate(base64-0.22/std) >= 0.22.1
Requires:       crate(csv-1) >= 1.3.0
Requires:       crate(flate2-1/zlib-rs) >= 1.0.33
Requires:       crate(fs-err-3/tokio) >= 3.2.2
Requires:       crate(futures-lite-2/std) >= 2.6.1
Requires:       crate(globset-0.4) >= 0.4.15
Requires:       crate(indexmap-2/std) >= 2.5.0
Requires:       crate(itertools-0.14/use-std) >= 0.14.0
Requires:       crate(rustc-hash-2/std) >= 2.0.0
Requires:       crate(serde-1/derive) >= 1.0.210
Requires:       crate(serde-1/rc) >= 1.0.210
Requires:       crate(serde-1/std) >= 1.0.210
Requires:       crate(serde-json-1/std) >= 1.0.128
Requires:       crate(sha2-0.11) >= 0.11.0
Requires:       crate(spdx-0.13) >= 0.13.0
Requires:       crate(tar-codec-0.0.15) >= 0.0.15
Requires:       crate(tempfile-3/getrandom) >= 3.14.0
Requires:       crate(thiserror-2/std) >= 2.0.0
Requires:       crate(tokio-1/fs) >= 1.40.0
Requires:       crate(tokio-1/io-util) >= 1.40.0
Requires:       crate(tokio-1/macros) >= 1.40.0
Requires:       crate(tokio-1/net) >= 1.40.0
Requires:       crate(tokio-1/process) >= 1.40.0
Requires:       crate(tokio-1/rt) >= 1.40.0
Requires:       crate(tokio-1/signal) >= 1.40.0
Requires:       crate(tokio-1/sync) >= 1.40.0
Requires:       crate(tokio-1/time) >= 1.40.0
Requires:       crate(toml-1/display) >= 1.1.0
Requires:       crate(toml-1/fast-hash) >= 1.1.0
Requires:       crate(toml-1/parse) >= 1.1.0
Requires:       crate(toml-1/serde) >= 1.1.0
Requires:       crate(toml-1/std) >= 1.1.0
Requires:       crate(tracing-0.1/attributes) >= 0.1.40
Requires:       crate(tracing-0.1/std) >= 0.1.40
Requires:       crate(uv-distribution-filename-0.0.96/default) >= 0.0.96
Requires:       crate(uv-errors-0.0.96/default) >= 0.0.96
Requires:       crate(uv-fs-0.0.96/default) >= 0.0.96
Requires:       crate(uv-fs-0.0.96/serde) >= 0.0.96
Requires:       crate(uv-fs-0.0.96/tokio) >= 0.0.96
Requires:       crate(uv-globfilter-0.0.96/default) >= 0.0.96
Requires:       crate(uv-macros-0.0.96/default) >= 0.0.96
Requires:       crate(uv-normalize-0.0.96/default) >= 0.0.96
Requires:       crate(uv-options-metadata-0.0.96/default) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/default) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/rkyv) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/tracing) >= 0.0.96
Requires:       crate(uv-pep440-0.0.96/version-ranges) >= 0.0.96
Requires:       crate(uv-pep508-0.0.96/default) >= 0.0.96
Requires:       crate(uv-pep508-0.0.96/non-pep508-extensions) >= 0.0.96
Requires:       crate(uv-platform-tags-0.0.96/default) >= 0.0.96
Requires:       crate(uv-preview-0.0.96/default) >= 0.0.96
Requires:       crate(uv-pypi-types-0.0.96/default) >= 0.0.96
Requires:       crate(uv-static-0.0.96/default) >= 0.0.96
Requires:       crate(uv-toml-0.0.96/default) >= 0.0.96
Requires:       crate(uv-version-0.13/default) >= 0.13.4
Requires:       crate(uv-warnings-0.0.96/default) >= 0.0.96
Requires:       crate(walkdir-2) >= 2.5.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "uv-build-backend"

%package     -n %{name}+schemars
Summary:        Internal component crate of uv - feature "schemars"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(schemars-1/derive) >= 1.0.0
Requires:       crate(schemars-1/std) >= 1.0.0
Requires:       crate(schemars-1/url2) >= 1.0.0
Requires:       crate(uv-pypi-types-0.0.96/schemars) >= 0.0.96
Provides:       crate(%{pkgname}/schemars) = %{version}

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust uv-build-backend crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
