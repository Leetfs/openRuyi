# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name parquet
%global full_version 59.2.0
%global pkgname parquet-59

Name:           rust-parquet-59
Version:        59.2.0
Release:        %autorelease
Summary:        Rust crate "parquet"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:7065842956a20c2a536924ce8e4d9955f7422451511b9eb7500d7bfe5077e59c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ahash-0.8/compile-time-rng) >= 0.8.12
Requires:       crate(ahash-0.8/runtime-rng) >= 0.8.12
Requires:       crate(bytes-1/std) >= 1.12.0
Requires:       crate(chrono-0.4/clock) >= 0.4.44
Requires:       crate(half-2/num-traits) >= 2.7.1
Requires:       crate(hashbrown-0.17) >= 0.17.1
Requires:       crate(num-bigint-0.5) >= 0.5.1
Requires:       crate(num-integer-0.1/std) >= 0.1.46
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Requires:       crate(seq-macro-0.3) >= 0.3.6
Requires:       crate(twox-hash-2/xxhash64) >= 2.1.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/test-common) = %{version}

%description
Source code for takopackized Rust crate "parquet"

%package     -n %{name}+arrow
Summary:        Apache Parquet implementation in Rust - feature "arrow"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arrow-array) = %{version}
Requires:       crate(%{pkgname}/arrow-buffer) = %{version}
Requires:       crate(%{pkgname}/arrow-data) = %{version}
Requires:       crate(%{pkgname}/arrow-ipc) = %{version}
Requires:       crate(%{pkgname}/arrow-schema) = %{version}
Requires:       crate(%{pkgname}/arrow-select) = %{version}
Requires:       crate(%{pkgname}/base64) = %{version}
Provides:       crate(%{pkgname}/arrow) = %{version}

%description -n %{name}+arrow
This metapackage enables feature "arrow" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arrow-array
Summary:        Apache Parquet implementation in Rust - feature "arrow-array"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-array-59/default) >= 59.2.0
Provides:       crate(%{pkgname}/arrow-array) = %{version}

%description -n %{name}+arrow-array
This metapackage enables feature "arrow-array" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arrow-buffer
Summary:        Apache Parquet implementation in Rust - feature "arrow-buffer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-buffer-59/default) >= 59.2.0
Provides:       crate(%{pkgname}/arrow-buffer) = %{version}

%description -n %{name}+arrow-buffer
This metapackage enables feature "arrow-buffer" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arrow-csv
Summary:        Apache Parquet implementation in Rust - feature "arrow-csv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-csv-59/default) >= 59.2.0
Provides:       crate(%{pkgname}/arrow-csv) = %{version}

%description -n %{name}+arrow-csv
This metapackage enables feature "arrow-csv" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arrow-data
Summary:        Apache Parquet implementation in Rust - feature "arrow-data"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-data-59/default) >= 59.2.0
Provides:       crate(%{pkgname}/arrow-data) = %{version}

%description -n %{name}+arrow-data
This metapackage enables feature "arrow-data" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arrow-ipc
Summary:        Apache Parquet implementation in Rust - feature "arrow-ipc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-ipc-59/default) >= 59.2.0
Provides:       crate(%{pkgname}/arrow-ipc) = %{version}

%description -n %{name}+arrow-ipc
This metapackage enables feature "arrow-ipc" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arrow-schema
Summary:        Apache Parquet implementation in Rust - feature "arrow-schema"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-schema-59/default) >= 59.2.0
Provides:       crate(%{pkgname}/arrow-schema) = %{version}

%description -n %{name}+arrow-schema
This metapackage enables feature "arrow-schema" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arrow-select
Summary:        Apache Parquet implementation in Rust - feature "arrow-select"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-select-59/default) >= 59.2.0
Provides:       crate(%{pkgname}/arrow-select) = %{version}

%description -n %{name}+arrow-select
This metapackage enables feature "arrow-select" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arrow-canonical-extension-types
Summary:        Apache Parquet implementation in Rust - feature "arrow_canonical_extension_types"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-schema-59/canonical-extension-types) >= 59.2.0
Provides:       crate(%{pkgname}/arrow-canonical-extension-types) = %{version}

%description -n %{name}+arrow-canonical-extension-types
This metapackage enables feature "arrow_canonical_extension_types" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async
Summary:        Apache Parquet implementation in Rust - feature "async"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Provides:       crate(%{pkgname}/async) = %{version}

%description -n %{name}+async
This metapackage enables feature "async" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+base64
Summary:        Apache Parquet implementation in Rust - feature "base64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64-0.23/std) >= 0.23.1
Provides:       crate(%{pkgname}/base64) = %{version}

%description -n %{name}+base64
This metapackage enables feature "base64" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+brotli
Summary:        Apache Parquet implementation in Rust - feature "brotli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(brotli-8/std) >= 8.0.4
Provides:       crate(%{pkgname}/brotli) = %{version}

%description -n %{name}+brotli
This metapackage enables feature "brotli" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clap
Summary:        Apache Parquet implementation in Rust - feature "clap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/derive) >= 4.1.0
Requires:       crate(clap-4/env) >= 4.1.0
Requires:       crate(clap-4/error-context) >= 4.1.0
Requires:       crate(clap-4/help) >= 4.1.0
Requires:       crate(clap-4/std) >= 4.1.0
Requires:       crate(clap-4/usage) >= 4.1.0
Provides:       crate(%{pkgname}/clap) = %{version}

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cli
Summary:        Apache Parquet implementation in Rust - feature "cli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arrow-csv) = %{version}
Requires:       crate(%{pkgname}/base64) = %{version}
Requires:       crate(%{pkgname}/clap) = %{version}
Requires:       crate(%{pkgname}/json) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/cli) = %{version}

%description -n %{name}+cli
This metapackage enables feature "cli" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crc
Summary:        Apache Parquet implementation in Rust - feature "crc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crc32fast-1) >= 1.4.2
Provides:       crate(%{pkgname}/crc) = %{version}

%description -n %{name}+crc
This metapackage enables feature "crc" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Apache Parquet implementation in Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arrow) = %{version}
Requires:       crate(%{pkgname}/base64) = %{version}
Requires:       crate(%{pkgname}/brotli) = %{version}
Requires:       crate(%{pkgname}/flate2-zlib-rs) = %{version}
Requires:       crate(%{pkgname}/lz4) = %{version}
Requires:       crate(%{pkgname}/simdutf8) = %{version}
Requires:       crate(%{pkgname}/snap) = %{version}
Requires:       crate(%{pkgname}/zstd) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+encryption
Summary:        Apache Parquet implementation in Rust - feature "encryption"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ring-0.17/std) >= 0.17.0
Requires:       crate(ring-0.17/wasm32-unknown-unknown-js) >= 0.17.0
Provides:       crate(%{pkgname}/encryption) = %{version}

%description -n %{name}+encryption
This metapackage enables feature "encryption" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flate2
Summary:        Apache Parquet implementation in Rust - feature "flate2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1) >= 1.1.9
Provides:       crate(%{pkgname}/flate2) = %{version}

%description -n %{name}+flate2
This metapackage enables feature "flate2" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+flate2-rust-backend
Summary:        Apache Parquet implementation in Rust - feature "flate2-rust_backend" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/rust-backend) >= 1.1.9
Provides:       crate(%{pkgname}/flate2-rust-backend) = %{version}
Provides:       crate(%{pkgname}/flate2-rust-backened) = %{version}

%description -n %{name}+flate2-rust-backend
This metapackage enables feature "flate2-rust_backend" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "flate2-rust_backened" feature.

%package     -n %{name}+flate2-zlib-rs
Summary:        Apache Parquet implementation in Rust - feature "flate2-zlib-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/zlib-rs) >= 1.1.9
Provides:       crate(%{pkgname}/flate2-zlib-rs) = %{version}

%description -n %{name}+flate2-zlib-rs
This metapackage enables feature "flate2-zlib-rs" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Apache Parquet implementation in Rust - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.3/std) >= 0.3.0
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json
Summary:        Apache Parquet implementation in Rust - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/base64) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
This metapackage enables feature "json" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lz4-flex
Summary:        Apache Parquet implementation in Rust - feature "lz4_flex" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lz4-flex-0.14/frame) >= 0.14.0
Requires:       crate(lz4-flex-0.14/std) >= 0.14.0
Provides:       crate(%{pkgname}/lz4) = %{version}
Provides:       crate(%{pkgname}/lz4-flex) = %{version}

%description -n %{name}+lz4-flex
This metapackage enables feature "lz4_flex" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "lz4" feature.

%package     -n %{name}+object-store
Summary:        Apache Parquet implementation in Rust - feature "object_store"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(object-store-0.13/tokio) >= 0.13.2
Provides:       crate(%{pkgname}/object-store) = %{version}

%description -n %{name}+object-store
This metapackage enables feature "object_store" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parquet-geospatial
Summary:        Apache Parquet implementation in Rust - feature "parquet-geospatial" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(parquet-geospatial-59/default) >= 59.2.0
Provides:       crate(%{pkgname}/geospatial) = %{version}
Provides:       crate(%{pkgname}/parquet-geospatial) = %{version}

%description -n %{name}+parquet-geospatial
This metapackage enables feature "parquet-geospatial" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "geospatial" feature.

%package     -n %{name}+parquet-variant
Summary:        Apache Parquet implementation in Rust - feature "parquet-variant"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(parquet-variant-59/default) >= 59.2.0
Provides:       crate(%{pkgname}/parquet-variant) = %{version}

%description -n %{name}+parquet-variant
This metapackage enables feature "parquet-variant" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parquet-variant-compute
Summary:        Apache Parquet implementation in Rust - feature "parquet-variant-compute"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(parquet-variant-compute-59/default) >= 59.2.0
Provides:       crate(%{pkgname}/parquet-variant-compute) = %{version}

%description -n %{name}+parquet-variant-compute
This metapackage enables feature "parquet-variant-compute" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parquet-variant-json
Summary:        Apache Parquet implementation in Rust - feature "parquet-variant-json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(parquet-variant-json-59/default) >= 59.2.0
Provides:       crate(%{pkgname}/parquet-variant-json) = %{version}

%description -n %{name}+parquet-variant-json
This metapackage enables feature "parquet-variant-json" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Apache Parquet implementation in Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Apache Parquet implementation in Rust - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/std) >= 1.0.149
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+simdutf8
Summary:        Apache Parquet implementation in Rust - feature "simdutf8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(simdutf8-0.1) >= 0.1.5
Provides:       crate(%{pkgname}/simdutf8) = %{version}

%description -n %{name}+simdutf8
This metapackage enables feature "simdutf8" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+snap
Summary:        Apache Parquet implementation in Rust - feature "snap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(snap-1) >= 1.1.2
Provides:       crate(%{pkgname}/snap) = %{version}

%description -n %{name}+snap
This metapackage enables feature "snap" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Apache Parquet implementation in Rust - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-1/macros) >= 1.0.0
Requires:       crate(tokio-1/rt) >= 1.0.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+variant-experimental
Summary:        Apache Parquet implementation in Rust - feature "variant_experimental" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arrow) = %{version}
Requires:       crate(%{pkgname}/parquet-variant) = %{version}
Requires:       crate(%{pkgname}/parquet-variant-compute) = %{version}
Requires:       crate(%{pkgname}/parquet-variant-json) = %{version}
Provides:       crate(%{pkgname}/experimental) = %{version}
Provides:       crate(%{pkgname}/variant-experimental) = %{version}

%description -n %{name}+variant-experimental
This metapackage enables feature "variant_experimental" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "experimental" feature.

%package     -n %{name}+zstd
Summary:        Apache Parquet implementation in Rust - feature "zstd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-0.13) >= 0.13.3
Provides:       crate(%{pkgname}/zstd) = %{version}

%description -n %{name}+zstd
This metapackage enables feature "zstd" for the Rust parquet crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
