# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name logos-derive
%global full_version 0.16.1
%global pkgname logos-derive-0.16

Name:           rust-logos-derive-0.16
Version:        0.16.1
Release:        %autorelease
Summary:        Rust crate "logos-derive"
License:        MIT OR Apache-2.0
URL:            https://logos.maciej.codes/
#!RemoteAsset:  sha256:52d3a9855747c17eaf4383823f135220716ab49bea5fbea7dd42cc9a92f8aa31
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(logos-codegen-0.16/default) >= 0.16.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "logos-derive"

%package     -n %{name}+debug
Summary:        Create ridiculously fast Lexers - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(logos-codegen-0.16/debug) >= 0.16.1
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust logos-derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+forbid-unsafe
Summary:        Create ridiculously fast Lexers - feature "forbid_unsafe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(logos-codegen-0.16/forbid-unsafe) >= 0.16.1
Provides:       crate(%{pkgname}/forbid-unsafe) = %{version}

%description -n %{name}+forbid-unsafe
This metapackage enables feature "forbid_unsafe" for the Rust logos-derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+state-machine-codegen
Summary:        Create ridiculously fast Lexers - feature "state_machine_codegen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(logos-codegen-0.16/state-machine-codegen) >= 0.16.1
Provides:       crate(%{pkgname}/state-machine-codegen) = %{version}

%description -n %{name}+state-machine-codegen
This metapackage enables feature "state_machine_codegen" for the Rust logos-derive crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
