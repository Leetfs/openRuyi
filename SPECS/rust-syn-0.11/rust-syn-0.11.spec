# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name syn
%global full_version 0.11.11
%global pkgname syn-0.11

Name:           rust-syn-0.11
Version:        0.11.11
Release:        %autorelease
Summary:        Rust crate "syn"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/syn
#!RemoteAsset:  sha256:d3b891b9015c88c576343b9b3e41c2c11a51c219ef067b264bd9c8aa9b441dad
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/aster) = %{version}
Provides:       crate(%{pkgname}/fold) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}
Provides:       crate(%{pkgname}/visit) = %{version}

%description
Source code for takopackized Rust crate "syn"

%package     -n %{name}+default
Summary:        Nom parser for Rust source code - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/parsing) = %{version}
Requires:       crate(%{pkgname}/printing) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parsing
Summary:        Nom parser for Rust source code - feature "parsing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/synom) = %{version}
Requires:       crate(%{pkgname}/unicode-xid) = %{version}
Provides:       crate(%{pkgname}/parsing) = %{version}

%description -n %{name}+parsing
This metapackage enables feature "parsing" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quote
Summary:        Nom parser for Rust source code - feature "quote" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quote-0.3/default) >= 0.3.7
Provides:       crate(%{pkgname}/printing) = %{version}
Provides:       crate(%{pkgname}/quote) = %{version}

%description -n %{name}+quote
This metapackage enables feature "quote" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "printing" feature.

%package     -n %{name}+synom
Summary:        Nom parser for Rust source code - feature "synom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(synom-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}/synom) = %{version}

%description -n %{name}+synom
This metapackage enables feature "synom" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-xid
Summary:        Nom parser for Rust source code - feature "unicode-xid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-xid-0.0.4/default) >= 0.0.4
Provides:       crate(%{pkgname}/unicode-xid) = %{version}

%description -n %{name}+unicode-xid
This metapackage enables feature "unicode-xid" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
