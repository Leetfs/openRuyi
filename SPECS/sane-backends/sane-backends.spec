# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sane-backends
Version:        1.4.0
Release:        %autorelease
Summary:        Scanner access library, device backends and command line tools
License:        GPL-2.0-or-later AND (GPL-2.0-or-later WITH SANE-exception) AND IJG AND MIT
URL:            https://www.sane-project.org/
VCS:            git:https://gitlab.com/sane-project/backends.git
#!RemoteAsset:  git+https://gitlab.com/sane-project/backends.git#c7e4b5e35e3d614d2b1181d760a717bfc395a203
#!CreateArchive
Source0:        %{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --with-usb

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gettext-tools
BuildRequires:  libtool
BuildRequires:  patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libjpeg)

%description
SANE provides scanner access through a common C interface. Device
backends support local scanners and scanners shared over the network.
The scanimage command acquires images using the same interface.

%package        devel
Summary:        Development files for the SANE scanner interface
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and build metadata for programs that acquire
images from a SANE device.

%install -a
%find_lang %{name}

%prep
%autosetup
# Generate the release build system using the upstream bootstrap script.
./autogen.sh
sed -n '/Copyright (C) 1996 by Scott Laird/,/\*\//p' backend/qcam.h > QCAM-LICENSE.txt
grep -Fq "IN NO EVENT SHALL SCOTT LAIRD" QCAM-LICENSE.txt

%check -a
# Use SANE's virtual test device to capture a PNM image without scanner hardware.
mkdir test-sane-config
printf 'test\n' >test-sane-config/dll.conf
cp backend/test.conf test-sane-config/
SANE_DEBUG_TEST=4 SANE_DEBUG_DLL=3 SANE_CONFIG_DIR="$PWD/test-sane-config" LD_LIBRARY_PATH="%{buildroot}%{_libdir}/sane:%{buildroot}%{_libdir}" \
    timeout -k 5 60 %{buildroot}%{_bindir}/scanimage -d test:0 --format=pnm -x 5 -y 5 >scan.pnm
test "$(head -c 1 scan.pnm)" = P

%files -f %{name}.lang
%license COPYING LICENSE README.djpeg QCAM-LICENSE.txt
%doc %{_docdir}/sane-backends/
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/libsane.so.*
%{_libdir}/sane/
%config(noreplace) %{_sysconfdir}/sane.d/
%{_datadir}/sane/
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*
%{_mandir}/man8/*

%files devel
%{_includedir}/sane/
%{_libdir}/libsane.so
%{_libdir}/pkgconfig/sane-backends.pc

%changelog
%autochangelog
