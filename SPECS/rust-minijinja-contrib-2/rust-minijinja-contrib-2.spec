# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name minijinja-contrib
%global full_version 2.24.0
%global pkgname minijinja-contrib-2

Name:           rust-minijinja-contrib-2
Version:        2.24.0
Release:        %autorelease
Summary:        Rust crate "minijinja-contrib"
License:        Apache-2.0
URL:            https://github.com/mitsuhiko/minijinja
#!RemoteAsset:  sha256:bd3e5f077bc2379f0f7d911e7cfdd921114ed99fc884533dca502944cb355b11
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(minijinja-2) >= 2.24.0
Requires:       crate(serde-1/default) >= 1.0.228

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/html-entities) = %{version}
Provides:       crate(%{pkgname}/rand) = %{version}

%description
Source code for takopackized Rust crate "minijinja-contrib"

%package     -n %{name}+pycompat
Summary:        Extra utilities for MiniJinja - feature "pycompat"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(minijinja-2/builtins) >= 2.24.0
Provides:       crate(%{pkgname}/pycompat) = %{version}

%description -n %{name}+pycompat
This metapackage enables feature "pycompat" for the Rust minijinja-contrib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+textwrap
Summary:        Extra utilities for MiniJinja - feature "textwrap" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(textwrap-0.16/smawk) >= 0.16.2
Provides:       crate(%{pkgname}/textwrap) = %{version}
Provides:       crate(%{pkgname}/wordwrap) = %{version}

%description -n %{name}+textwrap
This metapackage enables feature "textwrap" for the Rust minijinja-contrib crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "wordwrap" feature.

%package     -n %{name}+time
Summary:        Extra utilities for MiniJinja - feature "time" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/default) >= 0.3.35
Requires:       crate(time-0.3/formatting) >= 0.3.35
Requires:       crate(time-0.3/parsing) >= 0.3.35
Requires:       crate(time-0.3/serde) >= 0.3.35
Provides:       crate(%{pkgname}/datetime) = %{version}
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust minijinja-contrib crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "datetime" feature.

%package     -n %{name}+time-tz
Summary:        Extra utilities for MiniJinja - feature "time-tz" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-tz-2/db) >= 2.0.0
Requires:       crate(time-tz-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/time-tz) = %{version}
Provides:       crate(%{pkgname}/timezone) = %{version}

%description -n %{name}+time-tz
This metapackage enables feature "time-tz" for the Rust minijinja-contrib crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "timezone" feature.

%package     -n %{name}+unicode-categories
Summary:        Extra utilities for MiniJinja - feature "unicode_categories" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-categories-0.1/default) >= 0.1.1
Provides:       crate(%{pkgname}/unicode-categories) = %{version}
Provides:       crate(%{pkgname}/wordcount) = %{version}

%description -n %{name}+unicode-categories
This metapackage enables feature "unicode_categories" for the Rust minijinja-contrib crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "wordcount" feature.

%package     -n %{name}+unicode-wordwrap
Summary:        Extra utilities for MiniJinja - feature "unicode_wordwrap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/wordwrap) = %{version}
Requires:       crate(textwrap-0.16/smawk) >= 0.16.2
Requires:       crate(textwrap-0.16/unicode-linebreak) >= 0.16.2
Requires:       crate(textwrap-0.16/unicode-width) >= 0.16.2
Provides:       crate(%{pkgname}/unicode-wordwrap) = %{version}

%description -n %{name}+unicode-wordwrap
This metapackage enables feature "unicode_wordwrap" for the Rust minijinja-contrib crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
