# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global source_version 2.3.4

Name:           libdovi
Version:        3.4.0
Release:        %autorelease
Summary:        Dolby Vision metadata parsing and writing library
License:        MIT
URL:            https://github.com/quietvoid/dovi_tool
#!RemoteAsset:  sha256:15b5cb68b3598e51ca968316443c9fb9597b6230e9d692cb4e641d54505a97ec
Source0:        https://github.com/quietvoid/dovi_tool/archive/refs/tags/%{source_version}.tar.gz
BuildSystem:    rust

BuildRequires:  cargo-c
BuildRequires:  rust >= 1.88.0
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(anyhow-1/default) >= 1.0.103
BuildRequires:  crate(bitvec-1/default) >= 1.1.1
BuildRequires:  crate(bitvec-helpers-4/bitstream-io) >= 4.0.2
BuildRequires:  crate(crc-3/default) >= 3.4.0
BuildRequires:  crate(criterion-0.8/default) >= 0.8.2
BuildRequires:  crate(libc-0.2/default)
BuildRequires:  crate(roxmltree-0.21/default) >= 0.21.1
BuildRequires:  crate(serde-1/default) >= 1.0.228
BuildRequires:  crate(serde-1/derive) >= 1.0.228
BuildRequires:  crate(serde-json-1/default) >= 1.0.150
BuildRequires:  crate(serde-json-1/preserve-order) >= 1.0.150
BuildRequires:  crate(tinyvec-1/default) >= 1.12.0
BuildRequires:  crate(tinyvec-1/rustc-1-55) >= 1.12.0
BuildRequires:  crate(tinyvec-1/serde) >= 1.12.0

%description
libdovi provides a C API for reading, editing, and writing Dolby Vision
metadata. It supports RPU metadata in HEVC and AV1 streams, profile
conversion, and metadata generation from XML and JSON descriptions.

%package devel
Summary:        Development files for libdovi
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers, pkg-config metadata, and examples for developing applications
that use the libdovi C API.

%prep -a
rm -f dolby_vision/Cargo.lock

%build
cd dolby_vision
cargo cbuild --offline --release --library-type cdylib --features xml

%install
cd dolby_vision
cargo cinstall --offline --release --library-type cdylib --features xml \
    --prefix %{_prefix} --libdir %{_libdir} --destdir %{buildroot}

%check -p
cd dolby_vision
export RUST_TEST_FLAGS=--all-features

%check -a
cd examples
%{__cc} %{build_cflags} capi_rpu_file.c \
    -I%{buildroot}%{_includedir} -L%{buildroot}%{_libdir} \
    %{build_ldflags} -ldovi -o ../../capi_rpu_file
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ../../capi_rpu_file

%files
%doc dolby_vision/README.md dolby_vision/CHANGELOG.md
%license LICENSE
%{_libdir}/libdovi.so.*

%files devel
%doc dolby_vision/examples
%{_includedir}/libdovi/
%{_libdir}/libdovi.so
%{_libdir}/pkgconfig/dovi.pc

%changelog
%autochangelog
