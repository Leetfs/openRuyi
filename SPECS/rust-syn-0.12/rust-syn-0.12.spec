# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name syn
%global full_version 0.12.0
%global pkgname syn-0.12

Name:           rust-syn-0.12
Version:        0.12.0
Release:        %autorelease
Summary:        Rust crate "syn"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/syn
#!RemoteAsset:  sha256:b186344b4b9c63567a0e29a5b43e2d5ffd02870951722950ab765a93a03433dd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-0.2/default) >= 0.2.0
Requires:       crate(unicode-xid-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/clone-impls) = %{version}
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/extra-traits) = %{version}
Provides:       crate(%{pkgname}/fold) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}
Provides:       crate(%{pkgname}/parsing) = %{version}
Provides:       crate(%{pkgname}/visit) = %{version}
Provides:       crate(%{pkgname}/visit-mut) = %{version}

%description
Source code for takopackized Rust crate "syn"

%package     -n %{name}+default
Summary:        Nom parser for Rust source code - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clone-impls) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/parsing) = %{version}
Requires:       crate(%{pkgname}/printing) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quote
Summary:        Nom parser for Rust source code - feature "quote" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quote-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/printing) = %{version}
Provides:       crate(%{pkgname}/quote) = %{version}

%description -n %{name}+quote
This metapackage enables feature "quote" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "printing" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
