# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dropwatch
Version:        1.5.5
Release:        %autorelease
Summary:        Monitor packets dropped by the Linux kernel
License:        GPL-2.0-or-later
URL:            https://github.com/nhorman/dropwatch
#!RemoteAsset:  sha256:73d4bcbbb056b3bd514b7d88ef927ece8aca32c2d50724b37c7d0a0d4d133009
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

# The BFD lookup implementation is a stub; kallsyms provides symbol lookup.
BuildOption(conf):  --without-bfd

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(readline)
BuildRequires:  psmisc

%description
Dropwatch monitors packets dropped by the Linux kernel and identifies the
functions where the drops occur using kernel symbols. It supports summary
and per-packet alerts, software and hardware drop monitoring, and kernel
drop statistics. The dwdump utility captures dropped packets in pcap format.

%conf -p
autoreconf -fiv

%files
%doc README.md
%license COPYING
%{_bindir}/dropwatch
%{_bindir}/dwdump
%{_mandir}/man1/dropwatch.1*
%{_mandir}/man1/dwdump.1*

%changelog
%autochangelog
