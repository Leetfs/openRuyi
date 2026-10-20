# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: avrovadonz2026 <jinyuan.or@isrc.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Keep pkg-config metadata from participating in solver choice for pkgconfig(libudev).
%global __provides_exclude_from ^%{_libdir}/pkgconfig/libudev\\.pc$
%global __requires_exclude_from ^%{_libdir}/pkgconfig/libudev\\.pc$

Name:           libudev-zero
Version:        1.0.5
Release:        %autorelease
Summary:        Drop-in replacement for libudev
License:        ISC
URL:            https://github.com/illiliti/libudev-zero
#!RemoteAsset:  sha256:bf4372f79ddbe6b0e266a3d2994ffac7018a7edf4f87632aecb5176565d96138
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Ddefault_library=shared

BuildRequires:  meson

# Conflicting libudev.so.1
Conflicts:      systemd-udev

%description
%{name} is a drop-in replacement for libudev intended to work with
different Linux device managers.

%package        devel
Summary:        Development files for %{name}
Conflicts:      pkgconfig(libudev)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains header files and the pkg-config metadata for %{name}.

%files
%doc README.md
%license LICENSE
%{_libdir}/libudev.so.1

%files devel
%{_includedir}/libudev.h
%{_libdir}/libudev.so
%{_libdir}/pkgconfig/libudev.pc

%changelog
%autochangelog
