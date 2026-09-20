# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fastokens
%global full_version 0.2.1
%global pkgname fastokens-0.2

Name:           rust-fastokens-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "fastokens"
License:        Apache-2.0
URL:            https://github.com/Atero-ai/fastokens
#!RemoteAsset:  sha256:8728655e193e0d08d7a95d63cf1fdb9b768d282cab0a112ecb006615bae9f067
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(daachorse-1/default) >= 1.0.0
Requires:       crate(fancy-regex-0.17/default) >= 0.17.0
Requires:       crate(icu-normalizer-2/default) >= 2.1.1
Requires:       crate(memchr-2/default) >= 2.8.0
Requires:       crate(pcre2-0.2/default) >= 0.2.11
Requires:       crate(rayon-1/default) >= 1.12.0
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-json-1/default) >= 1.0.149
Requires:       crate(strum-0.27/default) >= 0.27.2
Requires:       crate(strum-0.27/derive) >= 0.27.2
Requires:       crate(thiserror-2/default) >= 2.0.18

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "fastokens"

%package     -n %{name}+hf-hub
Summary:        Fast Tokenizer - feature "hf-hub" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hf-hub-0.4/rustls-tls) >= 0.4.3
Requires:       crate(hf-hub-0.4/ureq) >= 0.4.3
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/hf-hub) = %{version}

%description -n %{name}+hf-hub
This metapackage enables feature "hf-hub" for the Rust fastokens crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
