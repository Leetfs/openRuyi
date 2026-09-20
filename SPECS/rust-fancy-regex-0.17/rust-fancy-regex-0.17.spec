# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fancy-regex
%global full_version 0.17.0
%global pkgname fancy-regex-0.17

Name:           rust-fancy-regex-0.17
Version:        0.17.0
Release:        %autorelease
Summary:        Rust crate "fancy-regex"
License:        MIT
URL:            https://github.com/fancy-regex/fancy-regex
#!RemoteAsset:  sha256:72cf461f865c862bb7dc573f643dd6a2b6842f7c30b07882b56bd148cc2761b8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bit-set-0.8) >= 0.8.0
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.14
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.14
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.14
Requires:       crate(regex-automata-0.4/meta) >= 0.4.14
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.14
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.14
Requires:       crate(regex-syntax-0.8) >= 0.8.10

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/track-caller) = %{version}

%description
Source code for takopackized Rust crate "fancy-regex"

%package     -n %{name}+default
Summary:        Regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/perf) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/unicode) = %{version}
Requires:       crate(%{pkgname}/variable-lookbehinds) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf
Summary:        Regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "perf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.14
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.14
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.14
Requires:       crate(regex-automata-0.4/meta) >= 0.4.14
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.14
Requires:       crate(regex-automata-0.4/perf) >= 0.4.14
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.14
Provides:       crate(%{pkgname}/perf) = %{version}

%description -n %{name}+perf
This metapackage enables feature "perf" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bit-set-0.8/std) >= 0.8.0
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.14
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.14
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.14
Requires:       crate(regex-automata-0.4/meta) >= 0.4.14
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.14
Requires:       crate(regex-automata-0.4/std) >= 0.4.14
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.14
Requires:       crate(regex-syntax-0.8/std) >= 0.8.10
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "unicode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.14
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.14
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.14
Requires:       crate(regex-automata-0.4/meta) >= 0.4.14
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.14
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.14
Requires:       crate(regex-automata-0.4/unicode) >= 0.4.14
Requires:       crate(regex-syntax-0.8/unicode) >= 0.8.10
Provides:       crate(%{pkgname}/unicode) = %{version}

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+variable-lookbehinds
Summary:        Regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "variable-lookbehinds"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-automata-0.4/alloc) >= 0.4.14
Requires:       crate(regex-automata-0.4/dfa) >= 0.4.14
Requires:       crate(regex-automata-0.4/dfa-search) >= 0.4.14
Requires:       crate(regex-automata-0.4/hybrid) >= 0.4.14
Requires:       crate(regex-automata-0.4/meta) >= 0.4.14
Requires:       crate(regex-automata-0.4/nfa) >= 0.4.14
Requires:       crate(regex-automata-0.4/syntax) >= 0.4.14
Provides:       crate(%{pkgname}/variable-lookbehinds) = %{version}

%description -n %{name}+variable-lookbehinds
This metapackage enables feature "variable-lookbehinds" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
