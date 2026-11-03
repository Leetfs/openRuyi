# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xiang W <wangxiang@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fwupd-efi
Version:        1.9
Release:        %autorelease
Summary:        Firmware update EFI binaries
License:        LGPL-2.1-only
URL:            https://github.com/fwupd/fwupd-efi
VCS:            git@github.com:fwupd/fwupd-efi.git
#!RemoteAsset:  sha256:b1a92713659b5ffe6adae7a53adae6f353f07cfcc668736d38d217ec53fa022b
Source0:        https://github.com/fwupd/fwupd-efi/archive/refs/tags/%{version}.tar.gz
BuildSystem:    meson

# binutils still produces broken Optional Header (SizeOfOptionalHeader=0),
# so always use manual symbols for riscv64.
Patch2000:      2000-efi-force-manual-symbols-for-riscv64.patch

BuildOption(conf):  -Defi-libdir=/usr/lib64
BuildOption(conf):  -Defi_sbat_distro_id="%{sbat_distro}"
BuildOption(conf):  -Defi_sbat_distro_summary="%{sbat_distro_summary}"
BuildOption(conf):  -Defi_sbat_distro_pkgname="%{name}"
BuildOption(conf):  -Defi_sbat_distro_version="%{version}"
BuildOption(conf):  -Defi_sbat_distro_url="%{sbat_distro_url}"
BuildOption(conf):  -Dgenpeimg=disabled

BuildRequires:  meson
BuildRequires:  gnu-efi
BuildRequires:  python3-pefile

%description
fwupd is a project to allow updating device firmware, and this package provides
the EFI binary that is used for updating using UpdateCapsule.

%files
%doc README.md AUTHORS
%license COPYING
%{_libexecdir}/fwupd/efi/*.efi
%{_libdir}/pkgconfig/fwupd-efi.pc

%changelog
%autochangelog
