# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name miette
%global full_version 7.6.0
%global pkgname miette-7

Name:           rust-miette-7
Version:        7.6.0
Release:        %autorelease
Summary:        Rust crate "miette"
License:        Apache-2.0
URL:            https://github.com/zkat/miette
#!RemoteAsset:  sha256:5f98efec8807c63c752b5bd61f862c165c115b0a35685bdcfd9238c7aeb592b7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.4
Requires:       crate(unicode-width-0.1/default) >= 0.1.14

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/no-format-args-capture) = %{version}

%description
Source code for takopackized Rust crate "miette"

%package     -n %{name}+derive
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(miette-derive-7/default) >= 7.6.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+fancy
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "fancy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fancy-no-backtrace) = %{version}
Requires:       crate(backtrace-0.3/default) >= 0.3.69
Requires:       crate(backtrace-ext-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/fancy) = %{version}

%description -n %{name}+fancy
This metapackage enables feature "fancy" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fancy-base
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "fancy-base" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(owo-colors-4/default) >= 4.0.0
Requires:       crate(textwrap-0.16/unicode-linebreak) >= 0.16.0
Requires:       crate(textwrap-0.16/unicode-width) >= 0.16.0
Provides:       crate(%{pkgname}/fancy-base) = %{version}
Provides:       crate(%{pkgname}/fancy-no-syscall) = %{version}

%description -n %{name}+fancy-base
This metapackage enables feature "fancy-base" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "fancy-no-syscall" feature.

%package     -n %{name}+fancy-no-backtrace
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "fancy-no-backtrace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fancy-base) = %{version}
Requires:       crate(supports-color-3/default) >= 3.0.0
Requires:       crate(supports-hyperlinks-3/default) >= 3.0.0
Requires:       crate(supports-unicode-3/default) >= 3.0.0
Requires:       crate(terminal-size-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/fancy-no-backtrace) = %{version}

%description -n %{name}+fancy-no-backtrace
This metapackage enables feature "fancy-no-backtrace" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.196
Requires:       crate(serde-1/derive) >= 1.0.196
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syntect-highlighter
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers - feature "syntect-highlighter"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fancy-no-backtrace) = %{version}
Requires:       crate(syntect-5/default) >= 5.1.0
Provides:       crate(%{pkgname}/syntect-highlighter) = %{version}

%description -n %{name}+syntect-highlighter
This metapackage enables feature "syntect-highlighter" for the Rust miette crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
