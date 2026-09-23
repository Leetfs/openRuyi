# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futures-util-preview
%global full_version 0.3.0-alpha.15
%global pkgname futures-util-preview-0.3.0-alpha.15
%global __requires_exclude_from ^%{_datadir}/cargo/registry/.*$

Name:           rust-futures-util-preview-0.3.0-alpha.15
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "futures-util-preview"
License:        MIT OR Apache-2.0
URL:            https://rust-lang-nursery.github.io/futures-rs
#!RemoteAsset:  sha256:ca958da50f4073c475d9f7ec6ce405451e06707bfd69686e83abd76cb4e1e7fb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-channel-preview-0.3.0-alpha.15) >= 0.3.0-alpha.15
Requires:       crate(futures-core-preview-0.3.0-alpha.15) >= 0.3.0-alpha.15
Requires:       crate(futures-io-preview-0.3.0-alpha.15) >= 0.3.0-alpha.15
Requires:       crate(futures-sink-preview-0.3.0-alpha.15) >= 0.3.0-alpha.15
Requires:       crate(pin-utils-0.1.0-alpha.4/default) >= 0.1.0-alpha.4

Provides:       crate(%{pkgname}) = %{full_version}
Provides:       crate(%{pkgname}/bench) = %{full_version}
Provides:       crate(%{pkgname}/never-type) = %{full_version}

%description
Source code for takopackized Rust crate "futures-util-preview"

%package     -n %{name}+alloc
Summary:        Common utilities and extension traits for the futures-rs library - feature "alloc"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(futures-core-preview-0.3.0-alpha.15/alloc) >= 0.3.0-alpha.15
Requires:       crate(futures-sink-preview-0.3.0-alpha.15/alloc) >= 0.3.0-alpha.15
Provides:       crate(%{pkgname}/alloc) = %{full_version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust futures-util-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-await
Summary:        Common utilities and extension traits for the futures-rs library - feature "async-await"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(%{pkgname}/futures-select-macro-preview) = %{full_version}
Requires:       crate(%{pkgname}/proc-macro-hack) = %{full_version}
Requires:       crate(%{pkgname}/proc-macro-nested) = %{full_version}
Requires:       crate(%{pkgname}/rand) = %{full_version}
Requires:       crate(%{pkgname}/rand-core) = %{full_version}
Requires:       crate(%{pkgname}/std) = %{full_version}
Provides:       crate(%{pkgname}/async-await) = %{full_version}

%description -n %{name}+async-await
This metapackage enables feature "async-await" for the Rust futures-util-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cfg-target-has-atomic
Summary:        Common utilities and extension traits for the futures-rs library - feature "cfg-target-has-atomic"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(futures-core-preview-0.3.0-alpha.15/cfg-target-has-atomic) >= 0.3.0-alpha.15
Provides:       crate(%{pkgname}/cfg-target-has-atomic) = %{full_version}

%description -n %{name}+cfg-target-has-atomic
This metapackage enables feature "cfg-target-has-atomic" for the Rust futures-util-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compat
Summary:        Common utilities and extension traits for the futures-rs library - feature "compat"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(%{pkgname}/futures-01) = %{full_version}
Requires:       crate(%{pkgname}/std) = %{full_version}
Provides:       crate(%{pkgname}/compat) = %{full_version}

%description -n %{name}+compat
This metapackage enables feature "compat" for the Rust futures-util-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-select-macro-preview
Summary:        Common utilities and extension traits for the futures-rs library - feature "futures-select-macro-preview"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(futures-select-macro-preview-0.3.0-alpha.15) >= 0.3.0-alpha.15
Provides:       crate(%{pkgname}/futures-select-macro-preview) = %{full_version}

%description -n %{name}+futures-select-macro-preview
This metapackage enables feature "futures-select-macro-preview" for the Rust futures-util-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-01
Summary:        Common utilities and extension traits for the futures-rs library - feature "futures_01"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(futures-0.1/default) >= 0.1.25
Provides:       crate(%{pkgname}/futures-01) = %{full_version}

%description -n %{name}+futures-01
This metapackage enables feature "futures_01" for the Rust futures-util-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+io-compat
Summary:        Common utilities and extension traits for the futures-rs library - feature "io-compat"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(%{pkgname}/compat) = %{full_version}
Requires:       crate(%{pkgname}/tokio-io) = %{full_version}
Provides:       crate(%{pkgname}/io-compat) = %{full_version}

%description -n %{name}+io-compat
This metapackage enables feature "io-compat" for the Rust futures-util-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+memchr
Summary:        Common utilities and extension traits for the futures-rs library - feature "memchr"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(memchr-2/default) >= 2.2.0
Provides:       crate(%{pkgname}/memchr) = %{full_version}

%description -n %{name}+memchr
This metapackage enables feature "memchr" for the Rust futures-util-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly
Summary:        Common utilities and extension traits for the futures-rs library - feature "nightly"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(futures-core-preview-0.3.0-alpha.15/nightly) >= 0.3.0-alpha.15
Requires:       crate(futures-sink-preview-0.3.0-alpha.15/nightly) >= 0.3.0-alpha.15
Provides:       crate(%{pkgname}/nightly) = %{full_version}

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust futures-util-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro-hack
Summary:        Common utilities and extension traits for the futures-rs library - feature "proc-macro-hack"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(proc-macro-hack-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/proc-macro-hack) = %{full_version}

%description -n %{name}+proc-macro-hack
This metapackage enables feature "proc-macro-hack" for the Rust futures-util-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro-nested
Summary:        Common utilities and extension traits for the futures-rs library - feature "proc-macro-nested"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(proc-macro-nested-0.1/default) >= 0.1.2
Provides:       crate(%{pkgname}/proc-macro-nested) = %{full_version}

%description -n %{name}+proc-macro-nested
This metapackage enables feature "proc-macro-nested" for the Rust futures-util-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Common utilities and extension traits for the futures-rs library - feature "rand"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(rand-0.6/default) >= 0.6.4
Provides:       crate(%{pkgname}/rand) = %{full_version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust futures-util-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Common utilities and extension traits for the futures-rs library - feature "rand_core"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(rand-core-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/rand-core) = %{full_version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust futures-util-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+slab
Summary:        Common utilities and extension traits for the futures-rs library - feature "slab"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(slab-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/slab) = %{full_version}

%description -n %{name}+slab
This metapackage enables feature "slab" for the Rust futures-util-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Common utilities and extension traits for the futures-rs library - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(%{pkgname}/alloc) = %{full_version}
Requires:       crate(%{pkgname}/memchr) = %{full_version}
Requires:       crate(%{pkgname}/slab) = %{full_version}
Requires:       crate(futures-core-preview-0.3.0-alpha.15/std) >= 0.3.0-alpha.15
Requires:       crate(futures-io-preview-0.3.0-alpha.15/std) >= 0.3.0-alpha.15
Requires:       crate(futures-sink-preview-0.3.0-alpha.15/std) >= 0.3.0-alpha.15
Provides:       crate(%{pkgname}/default) = %{full_version}
Provides:       crate(%{pkgname}/std) = %{full_version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust futures-util-preview crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+tokio-io
Summary:        Common utilities and extension traits for the futures-rs library - feature "tokio-io"
Requires:       crate(%{pkgname}) = %{full_version}
Requires:       crate(tokio-io-0.1/default) >= 0.1.9
Provides:       crate(%{pkgname}/tokio-io) = %{full_version}

%description -n %{name}+tokio-io
This metapackage enables feature "tokio-io" for the Rust futures-util-preview crate, by pulling in any additional dependencies needed by that feature.

%install
%rust_install_crate
mv %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version} %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
