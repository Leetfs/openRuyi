# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name opencv-binding-generator
%global full_version 0.103.0
%global pkgname opencv-binding-generator-0.103

Name:           rust-opencv-binding-generator-0.103
Version:        0.103.0
Release:        %autorelease
Summary:        Rust crate "opencv-binding-generator"
License:        MIT
URL:            https://github.com/twistedfall/opencv-rust
#!RemoteAsset:  sha256:310ef27c6e0c01710b3242a87b22f0673059c5a749db8b9df6bda4b20053f2d5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(clang-2/clang-9-0) >= 2.0.0
Requires:       crate(clang-2/default) >= 2.0.0
Requires:       crate(clang-sys-1/clang-9-0) >= 1.0.0
Requires:       crate(clang-sys-1/default) >= 1.0.0
Requires:       crate(dunce-1/default) >= 1.0.0
Requires:       crate(percent-encoding-2) >= 2.0.0
Requires:       crate(regex-1/default) >= 1.0.0
Requires:       crate(semver-1/default) >= 1.0.0
Requires:       crate(shlex-2) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "opencv-binding-generator"

%package     -n %{name}+clang-runtime
Summary:        Binding generator for opencv crate - feature "clang-runtime"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clang-2/clang-9-0) >= 2.0.0
Requires:       crate(clang-2/runtime) >= 2.0.0
Requires:       crate(clang-sys-1/clang-9-0) >= 1.0.0
Requires:       crate(clang-sys-1/runtime) >= 1.0.0
Provides:       crate(%{pkgname}/clang-runtime) = %{version}

%description -n %{name}+clang-runtime
This metapackage enables feature "clang-runtime" for the Rust opencv-binding-generator crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
