# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clang
%global full_version 2.1.0
%global pkgname clang-2

Name:           rust-clang-2
Version:        2.1.0
Release:        %autorelease
Summary:        Rust crate "clang"
License:        Apache-2.0
URL:            https://github.com/KyleMayes/clang-rs
#!RemoteAsset:  sha256:b2ed30b30e1e17966b55ddd0b9dd2758fd824f0a6da6875c8abb17e6aba47c28
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(clang-sys-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.39

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "clang"

%package     -n %{name}+clang-10-0
Summary:        Somewhat idiomatic Rust wrapper for libclang - feature "clang_10_0"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clang-9-0) = %{version}
Requires:       crate(clang-sys-1/clang-10-0) >= 1.0.0
Provides:       crate(%{pkgname}/clang-10-0) = %{version}

%description -n %{name}+clang-10-0
This metapackage enables feature "clang_10_0" for the Rust clang crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clang-3-5
Summary:        Somewhat idiomatic Rust wrapper for libclang - feature "clang_3_5"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clang-sys-1/clang-3-5) >= 1.0.0
Provides:       crate(%{pkgname}/clang-3-5) = %{version}

%description -n %{name}+clang-3-5
This metapackage enables feature "clang_3_5" for the Rust clang crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clang-3-6
Summary:        Somewhat idiomatic Rust wrapper for libclang - feature "clang_3_6"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clang-3-5) = %{version}
Requires:       crate(clang-sys-1/clang-3-6) >= 1.0.0
Provides:       crate(%{pkgname}/clang-3-6) = %{version}

%description -n %{name}+clang-3-6
This metapackage enables feature "clang_3_6" for the Rust clang crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clang-3-7
Summary:        Somewhat idiomatic Rust wrapper for libclang - feature "clang_3_7"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clang-3-6) = %{version}
Requires:       crate(clang-sys-1/clang-3-7) >= 1.0.0
Provides:       crate(%{pkgname}/clang-3-7) = %{version}

%description -n %{name}+clang-3-7
This metapackage enables feature "clang_3_7" for the Rust clang crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clang-3-8
Summary:        Somewhat idiomatic Rust wrapper for libclang - feature "clang_3_8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clang-3-7) = %{version}
Requires:       crate(clang-sys-1/clang-3-8) >= 1.0.0
Provides:       crate(%{pkgname}/clang-3-8) = %{version}

%description -n %{name}+clang-3-8
This metapackage enables feature "clang_3_8" for the Rust clang crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clang-3-9
Summary:        Somewhat idiomatic Rust wrapper for libclang - feature "clang_3_9"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clang-3-8) = %{version}
Requires:       crate(clang-sys-1/clang-3-9) >= 1.0.0
Provides:       crate(%{pkgname}/clang-3-9) = %{version}

%description -n %{name}+clang-3-9
This metapackage enables feature "clang_3_9" for the Rust clang crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clang-4-0
Summary:        Somewhat idiomatic Rust wrapper for libclang - feature "clang_4_0"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clang-3-9) = %{version}
Requires:       crate(clang-sys-1/clang-4-0) >= 1.0.0
Provides:       crate(%{pkgname}/clang-4-0) = %{version}

%description -n %{name}+clang-4-0
This metapackage enables feature "clang_4_0" for the Rust clang crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clang-5-0
Summary:        Somewhat idiomatic Rust wrapper for libclang - feature "clang_5_0"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clang-4-0) = %{version}
Requires:       crate(clang-sys-1/clang-5-0) >= 1.0.0
Provides:       crate(%{pkgname}/clang-5-0) = %{version}

%description -n %{name}+clang-5-0
This metapackage enables feature "clang_5_0" for the Rust clang crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clang-6-0
Summary:        Somewhat idiomatic Rust wrapper for libclang - feature "clang_6_0"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clang-5-0) = %{version}
Requires:       crate(clang-sys-1/clang-6-0) >= 1.0.0
Provides:       crate(%{pkgname}/clang-6-0) = %{version}

%description -n %{name}+clang-6-0
This metapackage enables feature "clang_6_0" for the Rust clang crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clang-7-0
Summary:        Somewhat idiomatic Rust wrapper for libclang - feature "clang_7_0"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clang-6-0) = %{version}
Requires:       crate(clang-sys-1/clang-7-0) >= 1.0.0
Provides:       crate(%{pkgname}/clang-7-0) = %{version}

%description -n %{name}+clang-7-0
This metapackage enables feature "clang_7_0" for the Rust clang crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clang-8-0
Summary:        Somewhat idiomatic Rust wrapper for libclang - feature "clang_8_0"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clang-7-0) = %{version}
Requires:       crate(clang-sys-1/clang-8-0) >= 1.0.0
Provides:       crate(%{pkgname}/clang-8-0) = %{version}

%description -n %{name}+clang-8-0
This metapackage enables feature "clang_8_0" for the Rust clang crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clang-9-0
Summary:        Somewhat idiomatic Rust wrapper for libclang - feature "clang_9_0"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clang-8-0) = %{version}
Requires:       crate(clang-sys-1/clang-9-0) >= 1.0.0
Provides:       crate(%{pkgname}/clang-9-0) = %{version}

%description -n %{name}+clang-9-0
This metapackage enables feature "clang_9_0" for the Rust clang crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime
Summary:        Somewhat idiomatic Rust wrapper for libclang - feature "runtime"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clang-sys-1/runtime) >= 1.0.0
Provides:       crate(%{pkgname}/runtime) = %{version}

%description -n %{name}+runtime
This metapackage enables feature "runtime" for the Rust clang crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+static
Summary:        Somewhat idiomatic Rust wrapper for libclang - feature "static"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clang-sys-1/static) >= 1.0.0
Provides:       crate(%{pkgname}/static) = %{version}

%description -n %{name}+static
This metapackage enables feature "static" for the Rust clang crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
