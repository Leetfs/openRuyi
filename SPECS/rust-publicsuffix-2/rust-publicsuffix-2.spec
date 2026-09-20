# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name publicsuffix
%global full_version 2.2.3
%global pkgname publicsuffix-2

Name:           rust-publicsuffix-2
Version:        2.2.3
Release:        %autorelease
Summary:        Rust crate "publicsuffix"
License:        MIT OR Apache-2.0
URL:            https://github.com/rushmorem/publicsuffix
#!RemoteAsset:  sha256:96a8c1bda5ae1af7f99a2962e49df150414a43d62404644d98dd5c3a93d07457
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(psl-types-2/default) >= 2.0.11

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "publicsuffix"

%package     -n %{name}+hashbrown
Summary:        Extract root domain and suffix from a domain name - feature "hashbrown"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.12/default) >= 0.12.3
Requires:       crate(hashbrown-0.12/inline-more) >= 0.12.3
Provides:       crate(%{pkgname}/hashbrown) = %{version}

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust publicsuffix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+idna
Summary:        Extract root domain and suffix from a domain name - feature "idna" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(idna-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/idna) = %{version}
Provides:       crate(%{pkgname}/punycode) = %{version}

%description -n %{name}+idna
This metapackage enables feature "idna" for the Rust publicsuffix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "punycode" features.

%package     -n %{name}+unicase
Summary:        Extract root domain and suffix from a domain name - feature "unicase" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicase-2) >= 2.6.0
Provides:       crate(%{pkgname}/anycase) = %{version}
Provides:       crate(%{pkgname}/unicase) = %{version}

%description -n %{name}+unicase
This metapackage enables feature "unicase" for the Rust publicsuffix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "anycase" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
