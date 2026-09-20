# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name stdweb
%global full_version 0.4.0
%global pkgname stdweb-0.4

Name:           rust-stdweb-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "stdweb"
License:        MIT OR Apache-2.0
URL:            https://github.com/koute/stdweb
#!RemoteAsset:  sha256:06e24f4ba24441d90410eaebc8f07781d3ceb098007c071afe6d86e59f255db5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(stdweb-derive-0.4/default) >= 0.4.0
Requires:       crate(stdweb-internal-macros-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/experimental-features-which-may-break-on-minor-version-bumps) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/web-test) = %{version}

%description
Source code for takopackized Rust crate "stdweb"

%package     -n %{name}+default
Summary:        Standard library for the client-side Web - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust stdweb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Standard library for the client-side Web - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.1/default) >= 0.1.18
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust stdweb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Standard library for the client-side Web - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust stdweb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Standard library for the client-side Web - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust stdweb crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
