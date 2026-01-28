# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           wayland-utils
Version:        1.2.0
Release:        %autorelease
Summary:        Wayland diagnostic utilities
License:        MIT
URL:            https://wayland.freedesktop.org/
VCS:            git:https://gitlab.freedesktop.org/wayland/wayland-utils
#!RemoteAsset
Source:         https://gitlab.freedesktop.org/wayland/wayland-utils/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://gitlab.freedesktop.org/wayland/wayland-utils/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz.sig
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  pkgconfig(libdrm) >= 2.4.109
BuildRequires:  pkgconfig(wayland-client) >= 1.20.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-scanner)

%description
A collection of wayland utilities, presently just wayland-info.

wayland-info displays information about the protocols supported by a
Wayland compositor, and a subset of Wayland protocols it knows about,
namely Linux DMABUF, presentation time, tablet and XDG output
protocols.

%files
%{_bindir}/wayland*
%{_mandir}/man1/wayl*
%license COPYING

%changelog
%{?autochangelog}
