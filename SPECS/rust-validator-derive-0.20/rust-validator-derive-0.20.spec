# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name validator_derive
%global full_version 0.20.0
%global pkgname validator-derive-0.20

Name:           rust-validator-derive-0.20
Version:        0.20.0
Release:        %autorelease
Summary:        Rust crate "validator_derive"
License:        MIT
URL:            https://github.com/Keats/validator
#!RemoteAsset:  sha256:b7df16e474ef958526d1205f6dda359fdfab79d9aa6d54bafcb92dcd07673dca
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(darling-0.20/default) >= 0.20.11
Requires:       crate(darling-0.20/suggestions) >= 0.20.11
Requires:       crate(once-cell-1/default) >= 1.21.4
Requires:       crate(proc-macro-error2-2/default) >= 2.0.1
Requires:       crate(proc-macro2-1/default) >= 1.0.106
Requires:       crate(quote-1/default) >= 1.0.45
Requires:       crate(syn-2/default) >= 2.0.117

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "validator_derive"

%package     -n %{name}+nightly-features
Summary:        Macros 1.1 implementation of #[derive(Validate)] - feature "nightly_features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proc-macro-error2-2/nightly) >= 2.0.1
Provides:       crate(%{pkgname}/nightly-features) = %{version}

%description -n %{name}+nightly-features
This metapackage enables feature "nightly_features" for the Rust validator_derive crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
