# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name idna
%global full_version 0.4.0
%global pkgname idna-0.4

Name:           rust-idna-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "idna"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/rust-url/
#!RemoteAsset:  sha256:7d20d6b07bfbc108882d88ed8e37d39636dcc260e15e30c45e6ba089610b917c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-bidi-0.3/hardcoded-data) >= 0.3.10
Requires:       crate(unicode-normalization-0.1) >= 0.1.22

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}

%description
Source code for takopackized Rust crate "idna"

%package     -n %{name}+std
Summary:        IDNA (Internationalizing Domain Names in Applications) and Punycode - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(unicode-bidi-0.3/hardcoded-data) >= 0.3.10
Requires:       crate(unicode-bidi-0.3/std) >= 0.3.10
Requires:       crate(unicode-normalization-0.1/std) >= 0.1.22
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust idna crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
