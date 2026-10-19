# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rkyv
%global full_version 0.8.18
%global pkgname rkyv-0.8

Name:           rust-rkyv-0.8
Version:        0.8.18
Release:        %autorelease
Summary:        Rust crate "rkyv"
License:        MIT
URL:            https://github.com/rkyv/rkyv
#!RemoteAsset:  sha256:d9776093b7ca170454ab1406954f7b7d97a57c51dc6c0642957fb2ef25c2d399
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(munge-0.4) >= 0.4.0
Requires:       crate(ptr-meta-0.3) >= 0.3.0
Requires:       crate(rancor-0.1) >= 0.1.0
Requires:       crate(rend-0.5) >= 0.5.0
Requires:       crate(rkyv-derive-0.8) >= 0.8.18

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/aligned) = %{version}
Provides:       crate(%{pkgname}/big-endian) = %{version}
Provides:       crate(%{pkgname}/little-endian) = %{version}
Provides:       crate(%{pkgname}/pointer-width-16) = %{version}
Provides:       crate(%{pkgname}/pointer-width-32) = %{version}
Provides:       crate(%{pkgname}/pointer-width-64) = %{version}
Provides:       crate(%{pkgname}/unaligned) = %{version}

%description
Source code for takopackized Rust crate "rkyv"

%package     -n %{name}+alloc
Summary:        Zero-copy deserialization framework for Rust - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.17) >= 0.17.0
Requires:       crate(rancor-0.1/alloc) >= 0.1.0
Requires:       crate(tinyvec-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arrayvec-0-7
Summary:        Zero-copy deserialization framework for Rust - feature "arrayvec-0_7"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrayvec-0.7) >= 0.7.0
Provides:       crate(%{pkgname}/arrayvec-0-7) = %{version}

%description -n %{name}+arrayvec-0-7
This metapackage enables feature "arrayvec-0_7" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytecheck
Summary:        Zero-copy deserialization framework for Rust - feature "bytecheck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytecheck-0.8/simdutf8) >= 0.8.0
Requires:       crate(rend-0.5/bytecheck) >= 0.5.0
Requires:       crate(rkyv-derive-0.8/bytecheck) >= 0.8.18
Provides:       crate(%{pkgname}/bytecheck) = %{version}

%description -n %{name}+bytecheck
This metapackage enables feature "bytecheck" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes-1
Summary:        Zero-copy deserialization framework for Rust - feature "bytes-1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1) >= 1.0.0
Provides:       crate(%{pkgname}/bytes-1) = %{version}

%description -n %{name}+bytes-1
This metapackage enables feature "bytes-1" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Zero-copy deserialization framework for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bytecheck) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown-0-14
Summary:        Zero-copy deserialization framework for Rust - feature "hashbrown-0_14"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.14) >= 0.14.0
Provides:       crate(%{pkgname}/hashbrown-0-14) = %{version}

%description -n %{name}+hashbrown-0-14
This metapackage enables feature "hashbrown-0_14" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown-0-15
Summary:        Zero-copy deserialization framework for Rust - feature "hashbrown-0_15"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.15) >= 0.15.0
Provides:       crate(%{pkgname}/hashbrown-0-15) = %{version}

%description -n %{name}+hashbrown-0-15
This metapackage enables feature "hashbrown-0_15" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown-0-16
Summary:        Zero-copy deserialization framework for Rust - feature "hashbrown-0_16"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.16) >= 0.16.0
Provides:       crate(%{pkgname}/hashbrown-0-16) = %{version}

%description -n %{name}+hashbrown-0-16
This metapackage enables feature "hashbrown-0_16" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown-0-17
Summary:        Zero-copy deserialization framework for Rust - feature "hashbrown-0_17"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.17) >= 0.17.0
Provides:       crate(%{pkgname}/hashbrown-0-17) = %{version}

%description -n %{name}+hashbrown-0-17
This metapackage enables feature "hashbrown-0_17" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap-2
Summary:        Zero-copy deserialization framework for Rust - feature "indexmap-2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(indexmap-2) >= 2.0.0
Provides:       crate(%{pkgname}/indexmap-2) = %{version}

%description -n %{name}+indexmap-2
This metapackage enables feature "indexmap-2" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec-1
Summary:        Zero-copy deserialization framework for Rust - feature "smallvec-1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smallvec-1) >= 1.0.0
Provides:       crate(%{pkgname}/smallvec-1) = %{version}

%description -n %{name}+smallvec-1
This metapackage enables feature "smallvec-1" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smol-str-0-2
Summary:        Zero-copy deserialization framework for Rust - feature "smol_str-0_2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smol-str-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/smol-str-0-2) = %{version}

%description -n %{name}+smol-str-0-2
This metapackage enables feature "smol_str-0_2" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smol-str-0-3
Summary:        Zero-copy deserialization framework for Rust - feature "smol_str-0_3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smol-str-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/smol-str-0-3) = %{version}

%description -n %{name}+smol-str-0-3
This metapackage enables feature "smol_str-0_3" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Zero-copy deserialization framework for Rust - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(bytes-1/std) >= 1.0.0
Requires:       crate(indexmap-2/std) >= 2.0.0
Requires:       crate(ptr-meta-0.3/std) >= 0.3.0
Requires:       crate(uuid-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thin-vec-0-2
Summary:        Zero-copy deserialization framework for Rust - feature "thin-vec-0_2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(thin-vec-0.2) >= 0.2.12
Provides:       crate(%{pkgname}/thin-vec-0-2) = %{version}

%description -n %{name}+thin-vec-0-2
This metapackage enables feature "thin-vec-0_2" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tinyvec-1
Summary:        Zero-copy deserialization framework for Rust - feature "tinyvec-1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tinyvec-1) >= 1.0.0
Provides:       crate(%{pkgname}/tinyvec-1) = %{version}

%description -n %{name}+tinyvec-1
This metapackage enables feature "tinyvec-1" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+triomphe-0-1
Summary:        Zero-copy deserialization framework for Rust - feature "triomphe-0_1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(triomphe-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/triomphe-0-1) = %{version}

%description -n %{name}+triomphe-0-1
This metapackage enables feature "triomphe-0_1" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid-1
Summary:        Zero-copy deserialization framework for Rust - feature "uuid-1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytecheck-0.8/simdutf8) >= 0.8.0
Requires:       crate(bytecheck-0.8/uuid-1) >= 0.8.0
Requires:       crate(uuid-1) >= 1.0.0
Provides:       crate(%{pkgname}/uuid-1) = %{version}

%description -n %{name}+uuid-1
This metapackage enables feature "uuid-1" for the Rust rkyv crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
