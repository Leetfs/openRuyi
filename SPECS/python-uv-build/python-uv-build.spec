# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname uv-build
%global pypi_name uv_build

Name:           python-%{srcname}
Version:        0.13.4
Release:        %autorelease
Summary:        The uv build backend
License:        MIT OR Apache-2.0
URL:            https://github.com/astral-sh/uv
#!RemoteAsset:  sha256:93399c547230b849cf725775b0c1c990927c02ddea503e7504736c84c54be9d8
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{pypi_name}-%{version}.tar.gz
#!RemoteAsset:  sha256:182d66815490dbb497b456a6fde93c7e66ae7f27a50a2065b3b5a06fbb3a20bd
Source1:        %{url}/archive/refs/tags/%{version}.tar.gz#/uv-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

# TakoPack dependencies.
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(anstream-1/auto) >= 1.0.0
BuildRequires:  crate(anstream-1/wincon) >= 1.0.0
BuildRequires:  crate(anyhow-1/std) >= 1.0.89
BuildRequires:  crate(tracing-0.1/attributes) >= 0.1.40
BuildRequires:  crate(tracing-0.1/std) >= 0.1.40
BuildRequires:  crate(tracing-subscriber-0.3/ansi) >= 0.3.18
BuildRequires:  crate(tracing-subscriber-0.3/env-filter) >= 0.3.18
BuildRequires:  crate(tracing-subscriber-0.3/fmt) >= 0.3.18
BuildRequires:  crate(tracing-subscriber-0.3/smallvec) >= 0.3.18
BuildRequires:  crate(tracing-subscriber-0.3/std) >= 0.3.18
BuildRequires:  crate(tracing-subscriber-0.3/tracing-log) >= 0.3.18
BuildRequires:  crate(uv-build-backend-0.0.96/default) >= 0.0.96
BuildRequires:  crate(uv-logging-0.0.96/default) >= 0.0.96
BuildRequires:  crate(uv-preview-0.0.96/default) >= 0.0.96
BuildRequires:  crate(uv-static-0.0.96/default) >= 0.0.96
BuildRequires:  crate(uv-version-0.13/default) >= 0.13.4
# Manual additions: build tools.
BuildRequires:  rust >= 1.97
BuildRequires:  cargo
BuildRequires:  python3dist(maturin) >= 1
# Offline Cargo resolution.
BuildRequires:  crate(schemars-1/derive) >= 1.0.0
BuildRequires:  crate(uv-fs-0.0.96/clap) >= 0.0.96
# uv-build-backend tests.
BuildRequires:  crate(hex-0.4/std) >= 0.4.3
BuildRequires:  crate(indoc-2) >= 2.0.5
BuildRequires:  crate(insta-1/colors) >= 1.46.0
BuildRequires:  crate(insta-1/filters) >= 1.46.0
BuildRequires:  crate(insta-1/json) >= 1.46.0
BuildRequires:  crate(insta-1/redactions) >= 1.46.0
BuildRequires:  crate(regex-1/perf) >= 1.13.0
BuildRequires:  crate(regex-1/unicode) >= 1.13.0
# uv-pep508 dev-dependencies.
BuildRequires:  crate(temp-env-0.3/async-closure) >= 0.3.6
BuildRequires:  crate(tracing-test-0.2) >= 0.2.5

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
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
cargo test --offline -p uv-build-backend -- --skip tests::built_by_uv_building_tokio_tar
cargo test --offline -p uv-build-backend tests::built_by_uv_building_tokio_tar -- --exact

%files -f %{pyproject_files}
%doc README.md
%license LICENSE-MIT LICENSE-APACHE
%{_bindir}/uv-build

%changelog
%autochangelog
