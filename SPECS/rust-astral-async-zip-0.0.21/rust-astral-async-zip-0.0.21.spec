# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name astral_async_zip
%global full_version 0.0.21
%global pkgname astral-async-zip-0.0.21

Name:           rust-astral-async-zip-0.0.21
Version:        0.0.21
Release:        %autorelease
Summary:        Rust crate "astral_async_zip"
License:        MIT
URL:            https://github.com/astral-sh/rs-async-zip
#!RemoteAsset:  sha256:13f4a9bc6289d907c8e883d25026a54751d686da9926af271d0fc4cbe58a7f4d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crc32fast-1/default) >= 1.0.0
Requires:       crate(futures-lite-2/std) >= 2.1.0
Requires:       crate(pin-project-1/default) >= 1.0.0
Requires:       crate(thiserror-2/default) >= 2.0.18

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "astral_async_zip"

%package     -n %{name}+async-compression
Summary:        Asynchronous ZIP archive reading/writing crate - feature "async-compression"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-compression-0.4/futures-io) >= 0.4.2
Provides:       crate(%{pkgname}/async-compression) = %{version}

%description -n %{name}+async-compression
This metapackage enables feature "async-compression" for the Rust astral_async_zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bzip2
Summary:        Asynchronous ZIP archive reading/writing crate - feature "bzip2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-compression-0.4/bzip2) >= 0.4.2
Requires:       crate(async-compression-0.4/futures-io) >= 0.4.2
Provides:       crate(%{pkgname}/bzip2) = %{version}

%description -n %{name}+bzip2
This metapackage enables feature "bzip2" for the Rust astral_async_zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate
Summary:        Asynchronous ZIP archive reading/writing crate - feature "deflate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-compression-0.4/deflate) >= 0.4.2
Requires:       crate(async-compression-0.4/futures-io) >= 0.4.2
Provides:       crate(%{pkgname}/deflate) = %{version}

%description -n %{name}+deflate
This metapackage enables feature "deflate" for the Rust astral_async_zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate64
Summary:        Asynchronous ZIP archive reading/writing crate - feature "deflate64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-compression-0.4/deflate64) >= 0.4.2
Requires:       crate(async-compression-0.4/futures-io) >= 0.4.2
Provides:       crate(%{pkgname}/deflate64) = %{version}

%description -n %{name}+deflate64
This metapackage enables feature "deflate64" for the Rust astral_async_zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        Asynchronous ZIP archive reading/writing crate - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bzip2) = %{version}
Requires:       crate(%{pkgname}/deflate) = %{version}
Requires:       crate(%{pkgname}/deflate64) = %{version}
Requires:       crate(%{pkgname}/jiff) = %{version}
Requires:       crate(%{pkgname}/lzma) = %{version}
Requires:       crate(%{pkgname}/tokio-fs) = %{version}
Requires:       crate(%{pkgname}/xz) = %{version}
Requires:       crate(%{pkgname}/zstd) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust astral_async_zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full-wasm
Summary:        Asynchronous ZIP archive reading/writing crate - feature "full-wasm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate) = %{version}
Requires:       crate(%{pkgname}/jiff) = %{version}
Requires:       crate(%{pkgname}/zstd) = %{version}
Provides:       crate(%{pkgname}/full-wasm) = %{version}

%description -n %{name}+full-wasm
This metapackage enables feature "full-wasm" for the Rust astral_async_zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jiff
Summary:        Asynchronous ZIP archive reading/writing crate - feature "jiff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(jiff-0.2/std) >= 0.2.0
Provides:       crate(%{pkgname}/jiff) = %{version}

%description -n %{name}+jiff
This metapackage enables feature "jiff" for the Rust astral_async_zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lzma
Summary:        Asynchronous ZIP archive reading/writing crate - feature "lzma"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-compression-0.4/futures-io) >= 0.4.2
Requires:       crate(async-compression-0.4/lzma) >= 0.4.2
Provides:       crate(%{pkgname}/lzma) = %{version}

%description -n %{name}+lzma
This metapackage enables feature "lzma" for the Rust astral_async_zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Asynchronous ZIP archive reading/writing crate - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tokio-util) = %{version}
Requires:       crate(tokio-1) >= 1.0.0
Requires:       crate(tokio-1/io-util) >= 1.0.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust astral_async_zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-fs
Summary:        Asynchronous ZIP archive reading/writing crate - feature "tokio-fs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/fs) >= 1.0.0
Provides:       crate(%{pkgname}/tokio-fs) = %{version}

%description -n %{name}+tokio-fs
This metapackage enables feature "tokio-fs" for the Rust astral_async_zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-util
Summary:        Asynchronous ZIP archive reading/writing crate - feature "tokio-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-util-0.7/compat) >= 0.7.0
Requires:       crate(tokio-util-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/tokio-util) = %{version}

%description -n %{name}+tokio-util
This metapackage enables feature "tokio-util" for the Rust astral_async_zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xz
Summary:        Asynchronous ZIP archive reading/writing crate - feature "xz"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-compression-0.4/futures-io) >= 0.4.2
Requires:       crate(async-compression-0.4/xz) >= 0.4.2
Provides:       crate(%{pkgname}/xz) = %{version}

%description -n %{name}+xz
This metapackage enables feature "xz" for the Rust astral_async_zip crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstd
Summary:        Asynchronous ZIP archive reading/writing crate - feature "zstd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-compression-0.4/futures-io) >= 0.4.2
Requires:       crate(async-compression-0.4/zstd) >= 0.4.2
Provides:       crate(%{pkgname}/zstd) = %{version}

%description -n %{name}+zstd
This metapackage enables feature "zstd" for the Rust astral_async_zip crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
