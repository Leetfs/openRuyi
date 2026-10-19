# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname uv-build
%global pypi_name uv_build

Name:           python-%{srcname}
Version:        0.12.24
Release:        %autorelease
Summary:        The uv build backend
License:        MIT OR Apache-2.0
URL:            https://github.com/astral-sh/uv
#!RemoteAsset:  sha256:7f67b18a83af209b66b1ec3d6ed565406dab2ebfee7bbe3598b541e7d39a5e5a
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{pypi_name}-%{version}.tar.gz
#!RemoteAsset:  sha256:7653be670f1c601326eae28af88f2cfd15d10539689d1b34887b43eda0a02ea7
Source1:        %{url}/archive/refs/tags/%{version}.tar.gz#/uv-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  rust >= 1.97
BuildRequires:  cargo
BuildRequires:  rust-rpm-macros
BuildRequires:  python3dist(maturin)
BuildRequires:  crate(anstream-1/auto) >= 1.0.0
BuildRequires:  crate(anstream-1/wincon) >= 1.0.0
BuildRequires:  crate(anyhow-1/std) >= 1.0.89
BuildRequires:  crate(arcstr-1) >= 1.2.0
BuildRequires:  crate(arrayvec-0.7) >= 0.7.6
BuildRequires:  crate(astral-async-zip-0.0.21/deflate) >= 0.0.21
BuildRequires:  crate(astral-tokio-tar-0.7) >= 0.7.0
BuildRequires:  crate(astral-version-ranges-0.2) >= 0.2.2
BuildRequires:  crate(backon-1) >= 1.3.0
BuildRequires:  crate(base64-0.22/std) >= 0.22.1
BuildRequires:  crate(bitflags-2) >= 2.6.0
BuildRequires:  crate(boxcar-0.2) >= 0.2.5
BuildRequires:  crate(clap-4/derive) >= 4.5.17
BuildRequires:  crate(clap-4/suggestions) >= 4.5.17
BuildRequires:  crate(csv-1) >= 1.3.0
BuildRequires:  crate(dunce-1) >= 1.0.5
BuildRequires:  crate(either-1/std) >= 1.13.0
BuildRequires:  crate(encoding-rs-io-0.1) >= 0.1.7
BuildRequires:  crate(enumflags2-0.7) >= 0.7.12
BuildRequires:  crate(flate2-1/zlib-rs) >= 1.0.33
BuildRequires:  crate(fs-err-3/tokio) >= 3.2.2
BuildRequires:  crate(futures-lite-2/std) >= 2.6.1
BuildRequires:  crate(globset-0.4) >= 0.4.15
BuildRequires:  crate(hashbrown-0.17/equivalent) >= 0.17.0
BuildRequires:  crate(hex-0.4/std) >= 0.4.3
BuildRequires:  crate(indexmap-2/serde) >= 2.5.0
BuildRequires:  crate(indoc-2) >= 2.0.5
BuildRequires:  crate(insta-1/colors) >= 1.46.0
BuildRequires:  crate(insta-1/filters) >= 1.46.0
BuildRequires:  crate(insta-1/redactions) >= 1.46.0
BuildRequires:  crate(itertools-0.14/use-std) >= 0.14.0
BuildRequires:  crate(jiff-0.2/serde) >= 0.2.0
BuildRequires:  crate(jiff-0.2/tz-fat) >= 0.2.0
BuildRequires:  crate(jiff-0.2/tz-system) >= 0.2.0
BuildRequires:  crate(jiff-0.2/tzdb-bundle-platform) >= 0.2.0
BuildRequires:  crate(junction-2) >= 2.0.0
BuildRequires:  crate(linux-raw-sys-0.12/ioctl) >= 0.12.1
BuildRequires:  crate(mailparse-0.16) >= 0.16.0
BuildRequires:  crate(memchr-2/std) >= 2.7.4
BuildRequires:  crate(owo-colors-4) >= 4.1.0
BuildRequires:  crate(path-slash-0.2) >= 0.2.1
BuildRequires:  crate(percent-encoding-2/std) >= 2.3.1
BuildRequires:  crate(petgraph-0.8/std) >= 0.8.0
BuildRequires:  crate(proc-macro2-1/proc-macro) >= 1.0.86
BuildRequires:  crate(quote-1/proc-macro) >= 1.0.37
BuildRequires:  crate(ref-cast-1) >= 1.0.24
BuildRequires:  crate(reflink-copy-0.1) >= 0.1.19
BuildRequires:  crate(regex-1/perf) >= 1.13.0
BuildRequires:  crate(regex-1/std) >= 1.13.0
BuildRequires:  crate(regex-1/unicode) >= 1.13.0
BuildRequires:  crate(regex-automata-0.4/dfa-build) >= 0.4.8
BuildRequires:  crate(regex-automata-0.4/perf) >= 0.4.8
BuildRequires:  crate(regex-automata-0.4/std) >= 0.4.8
BuildRequires:  crate(regex-automata-0.4/syntax) >= 0.4.8
BuildRequires:  crate(rkyv-0.8/bytecheck) >= 0.8.14
BuildRequires:  crate(rkyv-0.8/smallvec-1) >= 0.8.14
BuildRequires:  crate(rkyv-0.8/std) >= 0.8.14
BuildRequires:  crate(rustc-hash-2/std) >= 2.0.0
BuildRequires:  crate(rustix-1/std) >= 1.0.0
BuildRequires:  crate(rustix-1/system) >= 1.0.0
BuildRequires:  crate(same-file-1) >= 1.0.6
BuildRequires:  crate(schemars-1/derive) >= 1.0.0
BuildRequires:  crate(seahash-4) >= 4.1.0
BuildRequires:  crate(self-replace-1) >= 1.5.0
BuildRequires:  crate(serde-1/derive) >= 1.0.210
BuildRequires:  crate(serde-1/rc) >= 1.0.210
BuildRequires:  crate(serde-1/std) >= 1.0.210
BuildRequires:  crate(serde-json-1/std) >= 1.0.128
BuildRequires:  crate(serde-untagged-0.1) >= 0.1.6
BuildRequires:  crate(sha2-0.11) >= 0.11.0
BuildRequires:  crate(smallvec-1) >= 1.13.2
BuildRequires:  crate(spdx-0.13) >= 0.13.0
BuildRequires:  crate(syn-3/printing) >= 3.0.0
BuildRequires:  crate(syn-3/proc-macro) >= 3.0.0
BuildRequires:  crate(tar-codec-0.0.14) >= 0.0.14
BuildRequires:  crate(temp-env-0.3/async-closure) >= 0.3.6
BuildRequires:  crate(tempfile-3/getrandom) >= 3.14.0
BuildRequires:  crate(terminal-size-0.4) >= 0.4.2
BuildRequires:  crate(textwrap-0.16/smawk) >= 0.16.1
BuildRequires:  crate(textwrap-0.16/unicode-width) >= 0.16.1
BuildRequires:  crate(thiserror-2/std) >= 2.0.0
BuildRequires:  crate(tokio-1/macros) >= 1.40.0
BuildRequires:  crate(tokio-1/net) >= 1.40.0
BuildRequires:  crate(tokio-1/process) >= 1.40.0
BuildRequires:  crate(tokio-1/signal) >= 1.40.0
BuildRequires:  crate(toml-1/display) >= 1.1.0
BuildRequires:  crate(toml-1/fast-hash) >= 1.1.0
BuildRequires:  crate(toml-1/parse) >= 1.1.0
BuildRequires:  crate(toml-1/serde) >= 1.1.0
BuildRequires:  crate(toml-edit-0.25/display) >= 0.25.8
BuildRequires:  crate(toml-edit-0.25/parse) >= 0.25.8
BuildRequires:  crate(toml-edit-0.25/serde) >= 0.25.8
BuildRequires:  crate(tracing-0.1/attributes) >= 0.1.40
BuildRequires:  crate(tracing-0.1/std) >= 0.1.40
BuildRequires:  crate(tracing-subscriber-0.3/ansi) >= 0.3.18
BuildRequires:  crate(tracing-subscriber-0.3/env-filter) >= 0.3.18
BuildRequires:  crate(tracing-subscriber-0.3/smallvec) >= 0.3.18
BuildRequires:  crate(tracing-subscriber-0.3/tracing-log) >= 0.3.18
BuildRequires:  crate(tracing-test-0.2) >= 0.2.5
BuildRequires:  crate(unicode-width-0.2) >= 0.2.0
BuildRequires:  crate(unscanny-0.1) >= 0.1.0
BuildRequires:  crate(url-2/serde) >= 2.5.2
BuildRequires:  crate(url-2/std) >= 2.5.2
BuildRequires:  crate(walkdir-2) >= 2.5.0
BuildRequires:  crate(windows-0.61) >= 0.61.0

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This package is a slimmed down version of uv containing only the build backend. See
documentation.

%prep -a
%rust_setup_registry
rm -f Cargo.lock
# The sdist omits a fixture required by the upstream backend tests.
tar -xf %{SOURCE1} --strip-components=1 uv-%{version}/test/packages/built-by-uv

%generate_buildrequires
%pyproject_buildrequires

%check -a
# The two backend variants share inline snapshot locations and need separate processes.
cargo test --offline -p uv-build-backend -- --skip tests::built_by_uv_building_tar_codec
cargo test --offline -p uv-build-backend tests::built_by_uv_building_tar_codec -- --exact

%files -f %{pyproject_files}
%doc README.md
%license LICENSE-MIT LICENSE-APACHE
%{_bindir}/uv-build

%changelog
%autochangelog
