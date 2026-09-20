# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tiktoken-rs
%global full_version 0.9.1
%global pkgname tiktoken-rs-0.9

Name:           rust-tiktoken-rs-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "tiktoken-rs"
License:        MIT
URL:            https://github.com/zurawiki/tiktoken-rs
#!RemoteAsset:  sha256:3a19830747d9034cd9da43a60eaa8e552dfda7712424aebf187b7a60126bae0d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.102
Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(bstr-1/default) >= 1.12.1
Requires:       crate(fancy-regex-0.13/default) >= 0.13.0
Requires:       crate(lazy-static-1/default) >= 1.5.0
Requires:       crate(regex-1/default) >= 1.12.3
Requires:       crate(rustc-hash-1/default) >= 1.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tiktoken-rs"

%package     -n %{name}+async-openai
Summary:        Encoding and decoding with the tiktoken library in Rust - feature "async-openai"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-openai-0.14/default) >= 0.14.2
Provides:       crate(%{pkgname}/async-openai) = %{version}

%description -n %{name}+async-openai
This metapackage enables feature "async-openai" for the Rust tiktoken-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dhat-heap
Summary:        Encoding and decoding with the tiktoken library in Rust - feature "dhat-heap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dhat-0.3/default) >= 0.3.2
Provides:       crate(%{pkgname}/dhat-heap) = %{version}

%description -n %{name}+dhat-heap
This metapackage enables feature "dhat-heap" for the Rust tiktoken-rs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
